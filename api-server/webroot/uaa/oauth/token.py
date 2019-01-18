from quickweb import controller
import jose.jws
import json

class Controller(object):

    @controller.publish

    def default(self, *args, **kwargs):
        grant_type = kwargs.get('grant_type')
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
        print(jose.jws.sign(GR, key="cli"))
        payload= \
        {   "access_token": jose.jws.sign(GR, key='cli'),
            "token_type":"bearer",
        }
        if grant_type == 'password':
            username = kwargs.get("username")
            password = kwargs.get("password")
            print(json.dumps(payload))
            return json.dumps(payload)
