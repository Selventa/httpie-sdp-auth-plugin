'''
SDP API authentication plugin for HTTPie.
'''
from httpie.plugins import AuthPlugin
from urllib.parse   import urlparse, urlunparse
from time           import time

import hmac

class SDPAuth:
    def __init__(self, api_key, private_key):
        self.api_key = api_key
        self.private_key  = private_key

    def __call__(self, r):
        hash_url = self.extend(r.url, {
            'ts': str(int(time())),
            'apikey': self.api_key
        })

        auth_url = self.extend(hash_url, {
            'hash': hmac.new(bytes(self.private_key.encode('utf-8')),
                             bytes(hash_url.encode('utf-8'))).hexdigest()
        })
        r.url = auth_url
        return r

    def extend(self, url, params=None):
        '''
        Return a url extended with name/value parameters added to the
        query string.

        Arguments:

            url    -- a URL to to parse into its components
            params -- a dict of name/value parameters to add
        '''
        if not params:
            params = {}

        u = urlparse(url)
        p = lambda name_val: name_val[0] + '=' + str(name_val[1])
        query = '&'.join(map(p, params.items()))
        if len(u.query) > 0:
            query = u.query + '&' + query
        path = u.path
        if ' ' in path:
            path = quote(path)
        parts = (u.scheme, u.netloc, path, None, query, None)
        return urlunparse(parts)

class SDPAuthPlugin(AuthPlugin):

    name = 'SDP API authentication'
    auth_type = 'sdp'
    description = 'Hash URLs for the SDP API using api_key and secret.'

    def get_auth(self, api_key, private_key):
        return SDPAuth(api_key, private_key)
