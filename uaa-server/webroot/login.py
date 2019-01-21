from quickweb import controller
import json

class Controller(object):

    @controller.publish
    def default(self, *args):
        PROMPT_JSON = {
            "prompts":  {
                "username":["text","Email"],
                "password":["password","Password"]
            }
        }
        return json.dumps(PROMPT_JSON)
