#!/bin/sh -eu

CF_CLI_VERSION=6.42.0
RQLITE_VERSION=4.4.0

mkdir -p "${CFM_ETC_DIR}"
mkdir -p "${CFM_BIN_DIR}"

echo Downloading binaries...

rm -f "${CFM_BIN_DIR}/*.tgz"

wget "https://packages.cloudfoundry.org/stable?release=linux64-binary&version=$CF_CLI_VERSION" -O "${CFM_BIN_DIR}/cf.tgz"
tar -C "${CFM_BIN_DIR}" -xf "${CFM_BIN_DIR}"/cf.tgz cf
chmod 755 "${CFM_BIN_DIR}"/*

RQLITE_FILE=rqlite-v${RQLITE_VERSION}-linux-amd64.tar.gz
wget "https://github.com/rqlite/rqlite/releases/download/v${RQLITE_VERSION}/${RQLITE_FILE}" -O "${CFM_BIN_DIR}/rqlite.tgz"
tar -C "${CFM_BIN_DIR}" --strip-components 1 --wildcards -xf "${CFM_BIN_DIR}"/rqlite.tgz "*/rqlite*"

rm -f "${CFM_BIN_DIR}/*.tgz"