#!/bin/sh -eu

export API_ENDPOINT=api.example.com:8443
export MCF_BIN_DIR=$HOME/micro-cf/bin
export MCF_ETC_DIR=$HOME/micro-cf/etc
export MCF_SSL_CONF_DIR=$HOME/micro-cf/etc/ssl
export MCF_API_INFO_FILE=$HOME/micro-cf/etc/api-info.http
export PATH=$PATH:$MCF_BIN_DIR

mkdir -p ${MCF_ETC_DIR}

