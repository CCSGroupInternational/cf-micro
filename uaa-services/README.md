# User Account and Authentication
The UAA services provide authentication, authorization and account management services for the cf-micro platform.

## Use cases
An auditor, developer or manager wants to perform an activity on a micro-cf instance using the CF command line interface.

### Command Line Login (Integrated Identity Repository)
1. Authentication

    a) The `cf login` command is executed

    b) CF CLI sends an `HTTP(S) "GET /login; Accept=application/json"` request to the _authorization_endpoint_

    c) The UAA `/login` service responds with a JSON describing the fields required for the authentication token grant:
    ```json
    {
        "prompts": {
            "username": ["text", "Email"], 
            "password": ["password", "Password"]
            }
    }
    ```
    d) The CF CLI requests or retrieves the fields from the command line and submits a token grant request: `HTTP(S) "PUT /oauth/token"`

    e) The UAA `/oauth/token` service validates the submitted credentials, if valid it returns a signed JSON Web Token, this JSON includes the list of privileges authorizations/scopes that are granted to the user, example:
    ```json
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
    ```

    f) Subsequent `cf commands` result in HTTP(S) requests submitted to the API endpoint, such requests must include a valid token header. The command is accepted if the scope and authorities are sufficient for the operation execution.


References:

- https://docs.cloudfoundry.org/uaa/uaa-overview.html

- https://github.com/cloudfoundry/uaa
