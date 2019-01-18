from quickweb import controller
import json

# https://apidocs.cloudfoundry.org/6.10.0/info/get_info.html


info_dict = {
  "name": "vcap",
  "build": "2222",
  "support": "http://support.cloudfoundry.com",
  "version": 2,
  "description": "Cloud Foundry sponsored by Pivotal",
  "authorization_endpoint": "http://localhost:8080/uaa",
  "token_endpoint": "http://localhost:8080/uaa",
  "min_cli_version": None,
  "min_recommended_cli_version": None,
  "api_version": "2.128.0",
  "app_ssh_endpoint": "ssh.system.domain.example.com:2222",
  "app_ssh_host_key_fingerprint": "47:0d:d1:c8:c3:3d:0a:36:d1:49:2f:f2:90:27:31:d0",
  "app_ssh_oauth_client": None,
  "routing_endpoint": "http://localhost:3000",
  "logging_endpoint": "ws://loggregator.vcap.me:80"
}

class Controller(object):

    @controller.publish
    def index(self):
        return json.dumps(info_dict)
