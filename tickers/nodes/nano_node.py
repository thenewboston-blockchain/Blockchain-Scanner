import json
from functools import partial

import requests


class NanoNode:
    def __init__(self, connection_string):
        self.rpc_client = partial(requests.post, connection_string)

    def post(self, method, params=None):
        if not params:
            params = dict()
        headers = {'content-type': 'application/json'}
        payload = {
            "action": method,
            **params,
            "jsonrpc": "2.0",
            "id": 0,
        }
        response = self.rpc_client(data=json.dumps(payload), headers=headers).json()
        return response

    def get_block_info(self, _hash):
        return self.post('block_info', dict(json_block=True, hash=_hash))
