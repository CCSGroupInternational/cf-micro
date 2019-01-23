#!/bin/sh -eu


# RQLITE config
export RQLITE_ENDPOINT=rqlite.example.com:4001
export RQLITE_BACKEND_FIRST_IP=127.0.30.1
export RQLITE_BACKEND_PORT=4848
export RQLITE_CLUSTER_FIRST_IP=127.0.40.1
export RQLITE_CLUSTER_PORT=4949

# API config
export API_ENDPOINT=api.example.com:8443

# UAA config
export UAA_ENDPOINT=uaa.example.com:8443
export UAA_BACKEND_FIRST_IP=127.0.20.1
export UAA_BACKEND_PORT=8000

# cf-micro global config
export MCF_BIN_DIR=$HOME/cf-micro/bin
export MCF_ETC_DIR=$HOME/cf-micro/etc
export MCF_SSL_CONF_DIR=$HOME/cf-micro/etc/ssl
export MCF_API_INFO_FILE=$HOME/cf-micro/etc/api-info.http
export PATH=$PATH:$MCF_BIN_DIR
