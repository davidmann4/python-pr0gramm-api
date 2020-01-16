import requests


class Api:
    def __init__(self):
        self.server = "https://pr0gramm.com/api/"

        # flags: SFW = 1, NSFW = 2, NSFL = 4
        self.flags = 0b001

    def enable_sfw(self):
        self.flags |= 0b001

    def disable_sfw(self):
        self.flags &= 0b110

    def enable_nsfw(self):
        self.flags |= 0b010

    def disable_nsfw(self):
        self.flags &= 0b101

    def enable_nsfl(self):
        self.flags |= 0b100

    def disable_nsfl(self):
        self.flags &= 0b011

    def items(self, query, older=None, promoted=False):
        # build params
        params = {
            'flags': self.flags,
            'tags': query,
            'promoted': 1 if promoted else 0
        }

        # add older param if given
        if older is not None:
            params['older'] = older

        # build URL
        url = self.server + 'items/get'

        # send request
        response = requests.get(url, params)
        response.raise_for_status()

        # return items
        return response.json()["items"]

    def info(self, post_id: int):
        # build params
        params = {
            'itemId': post_id
        }

        # build URL
        url = self.server + 'items/info'

        # send request
        response = requests.get(url, params)
        response.raise_for_status()

        return response.json()
