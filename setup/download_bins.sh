#!/bin/sh
CF_CLI_VERSION=6.42.0

mkdir -p ~/micro-cf/bin
rm -f ~/micro-cf/bin/*.tgz

echo Downloading binaries...
wget "https://packages.cloudfoundry.org/stable?release=linux64-binary&version=$CF_CLI_VERSION" -O ~/micro-cf/bin/cf.tgz
tar -C ~/micro-cf/bin/ -xvf ~/micro-cf/bin/cf.tgz cf
rm -f ~/micro-cf/bin/bin/*.tgz
chmod 755 ~/micro-cf/bin/*
export PATH=$PATH:~/micro-cf/bin
echo
echo Please make sure you set the path on your ~/.bashrc file:
echo    export PATH=\$PATH:~/micro-cf/bin
echo
cf -v