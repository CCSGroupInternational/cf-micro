import jose.jws
import json
import os
import cherrypy
import pyrqlite.dbapi2 as dbapi2
from passlib.hash import pbkdf2_sha256
from quickweb import controller

class Controller(object):


    def __init__(self):
        self.hostname, self.port = os.getenv("RQLITE_ENDPOINT").split(":")

    @controller.publish
    def default(self, *args, **kwargs):
        grant_type = kwargs.get('grant_type')
        if grant_type == 'password':
            password_is_valid = False
            connection = dbapi2.connect(self.hostname, self.port)
            username = kwargs.get("username")
            password = kwargs.get("password")
            try:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT password FROM USERS WHERE username='{}'" .format(username)
                    )
                    result = cursor.fetchone()
                    hashed_password = result['password']
                    password_is_valid = pbkdf2_sha256.verify(password, hashed_password)
            finally:
                connection.close()
            if password_is_valid is True:
                return self.generate_token()
        raise cherrypy.HTTPError(403, message="Access Denied") 









    def generate_token(self):
        GR=\
        {   "jti":"dada01e968804f6fbd073274d431bdee",
            "sub":"admin",
            "authorities": [
                    "clients.read","clients.secret",
                    "clients.write","uaa.admin",
                    "clients.admin",
                    "scim.write",
                    "scim.read"
                ],
            "scope": [
                "clients.read",
                "clients.secret",
                "clients.write",
                "uaa.admin",
                "clients.admin",
                "scim.write",
                "scim.read"
                ],
            "client_id": "admin",
            "cid":"admin",
            "azp":"admin",
            "grant_type":"client_credentials",
            "rev_sig":"bdcc960",
            "iat":1547554827,
            "exp":1547598027,
            "iss":"http://localhost:8080/uaa/oauth/token",
            "zid":"uaa",
            "aud":["scim","clients","uaa","admin"]
            }
        payload= \
        {   "access_token": jose.jws.sign(GR, key='cli'),
            "token_type":"bearer",
        }
        return json.dumps(payload)

