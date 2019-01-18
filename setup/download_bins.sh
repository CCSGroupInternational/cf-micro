#!/bin/sh -eu

CF_CLI_VERSION=6.42.0

mkdir -p "${MCF_BIN_DIR}"

echo Downloading binaries...
wget "https://packages.cloudfoundry.org/stable?release=linux64-binary&version=$CF_CLI_VERSION" -O "${MCF_BIN_DIR}/cf.tgz"
tar -C "${MCF_BIN_DIR}" -xf "${MCF_BIN_DIR}"/cf.tgz cf
rm -f "${MCF_BIN_DIR}/*.tgz"
chmod 755 "${MCF_BIN_DIR}"/*


cf -v