import json
import requests

class Api:
    def __init__(self):
        self.server = "http://pr0gramm.com/api/"
        self.flags = 0

    def enableNSFW(self):
        self.flags += 2
                
    def disableNSFW(self):
        self.flags -= 2
        
    def enableSFW(self):
        self.flags += 1
        
    def disableSFW(self):
        self.flags -= 1

    def search(self, q):
        # Set up the arguments for the REST call.
        args = ({
            #'older': 104574,
            'flags': self.flags,
            'promoted': 1,
            'tags': q
        })
        
        # Make the request and verify success.
        url = self.server + 'items/get'
        response = requests.get(url, params= args)
        response.raise_for_status()
        return response.json()["items"]

    def info(self, id):
        args = ({
             'itemId': id
        })
        
        url = self.server + 'items/info'
        response = requests.get(url, params= args)
        response.raise_for_status()
        return response.json()
