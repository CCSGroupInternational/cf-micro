#!/bin/sh -eu

mkdir -p "${CFM_SSL_CONF_DIR}"

openssl req -x509 -newkey rsa:4096 -sha256 -days 3650 -nodes \
    -keyout ${CFM_SSL_CONF_DIR}/example.key \
    -out ${CFM_SSL_CONF_DIR}/example.crt \
    -subj /CN=example.com \
    -addext subjectAltName=DNS:*.example.com,DNS:*.example.net,IP:10.0.0.1

cat ${CFM_SSL_CONF_DIR}/example.crt \
    ${CFM_SSL_CONF_DIR}/example.key \
    > ${CFM_SSL_CONF_DIR}/example.pem