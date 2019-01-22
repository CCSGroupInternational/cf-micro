import json
from quickweb import controller

SPACE_DICT = \
{
  "total_results": 0,
  "total_pages": 0,
  "prev_url": None,
  "next_url": None,
  "resources": []
}

ORG_DICT = \
{
  "total_results": 1,
  "total_pages": 1,
  "prev_url": None,
  "next_url": None,
  "resources": [
    {
      "metadata": {
        "guid": "a7aff246-5f5b-4cf8-87d8-f316053e4a20",
        "url": "/v2/organizations/a7aff246-5f5b-4cf8-87d8-f316053e4a20",
        "created_at": "2016-06-08T16:41:33Z",
        "updated_at": "2016-06-08T16:41:26Z"
      },
      "entity": {
        "name": "the-system_domain-org-name",
        "billing_enabled": False,
        "quota_definition_guid": "dcb680a9-b190-4838-a3d2-b84aa17517a6",
        "status": "active",
        "quota_definition_url": "/v2/quota_definitions/dcb680a9-b190-4838-a3d2-b84aa17517a6",
        "spaces_url": "/v2/organizations/a7aff246-5f5b-4cf8-87d8-f316053e4a20/spaces",
        "domains_url": "/v2/organizations/a7aff246-5f5b-4cf8-87d8-f316053e4a20/domains",
        "private_domains_url": "/v2/organizations/a7aff246-5f5b-4cf8-87d8-f316053e4a20/private_domains",
        "users_url": "/v2/organizations/a7aff246-5f5b-4cf8-87d8-f316053e4a20/users",
        "managers_url": "/v2/organizations/a7aff246-5f5b-4cf8-87d8-f316053e4a20/managers",
        "billing_managers_url": "/v2/organizations/a7aff246-5f5b-4cf8-87d8-f316053e4a20/billing_managers",
        "auditors_url": "/v2/organizations/a7aff246-5f5b-4cf8-87d8-f316053e4a20/auditors",
        "app_events_url": "/v2/organizations/a7aff246-5f5b-4cf8-87d8-f316053e4a20/app_events",
        "space_quota_definitions_url": "/v2/organizations/a7aff246-5f5b-4cf8-87d8-f316053e4a20/space_quota_definitions"
      }
    }
  ]
}

class Controller(object):

    @controller.publish
    def default(self, *args, **kwargs):
        if len(args) == 2:
            org_gid, org_resource = args
            return json.dumps(SPACE_DICT)
            print("ARGS", org_gid, org_resource)
        order_by = kwargs.get('order-by')
        return json.dumps(ORG_DICT)
