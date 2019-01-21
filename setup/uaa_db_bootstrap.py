#!/usr/bin/python

import os
import hashlib
import uuid
import pyrqlite.dbapi2 as dbapi2
import string
import random
from os.path import join
from passlib.hash import pbkdf2_sha256


SQL_FILENAME = join('setup', 'sql', 'create_tables_uaa.sql')

def password_generator(size=8, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for i in range(size))

hostname, port = os.getenv("RQLITE_ENDPOINT").split(":")

# Connect to the database
connection = dbapi2.connect( host=hostname, port=port)

random_pass = password_generator()

with open(SQL_FILENAME)as sqlfile:
    create_tables_sql = sqlfile.read()

ADMIN_SQL= \
"""
INSERT INTO USERS(username, password) VALUES('admin','%s')
"""
try:
    with connection.cursor() as cursor:
        cursor.execute(create_tables_sql)

    with connection.cursor() as cursor:
        row_count = cursor.execute(ADMIN_SQL % pbkdf2_sha256.hash(random_pass))
    print("Admin password is: %s" % random_pass)
finally:
    connection.close()