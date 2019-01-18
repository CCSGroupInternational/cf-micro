#!/bin/sh -eu


cat > ${MCF_API_INFO_FILE} << _EOF_ 
HTTP/1.0 200 Found
Cache-Control: no-cache
Connection: close
Content-Type: text/json

{
  "name": "vcap",
  "build": "2222",
  "support": "https://github.com/CCSGroupInternational/micro-cf/issues",
  "version": 2,
  "description": "CloudFoundry Compatible Micro Framework ",
  "authorization_endpoint": "http://localhost:8080/uaa",
  "token_endpoint": "http://localhost:8080/uaa",
  "min_cli_version": null,
  "min_recommended_cli_version": null,
  "api_version": "2.128.0",
  "app_ssh_endpoint": "ssh.system.domain.example.com:2222",
  "app_ssh_host_key_fingerprint": "47:0d:d1:c8:c3:3d:0a:36:d1:49:2f:f2:90:27:31:d0",
  "app_ssh_oauth_client": null,
  "routing_endpoint": "http://localhost:3000",
  "logging_endpoint": "ws://loggregator.vcap.me:80"
}
_EOF_
echo ok