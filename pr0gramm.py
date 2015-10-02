import json
import requests

class Api:
    def __init__(self):
        self.server = "http://pr0gramm.com/api/"


    def search(self, q):
        # Set up the arguments for the REST call.
        args = ({
            'older': 104574,
            'flags': 1,
            'promoted': 1,
            'tags': q
        })
        # Make the request and verify success.
        url = self.server + 'items/get'
        response = requests.get(url, params= args)
        response.raise_for_status()
        return response.json()["items"]

