# httpie-sdp-auth-plugin

Authentication plugin for python's httpie library

### Installation

```bash
# install httpie; may require sudo
pip install httpie

# clone SDP auth plugin
git clone git@github.com:Selventa/httpie-sdp-auth-plugin.git
cd httpie-sdp-auth-plugin

# install SDP auth plugin; may require sudo
python setup.py install
```

*Confirmation*

You should now see *sdp* under the *--auth-type* option of the httpie help:

```bash
http --help
```

*Example output*

> Authentication:
>
>  --auth USER[:PASS], -a USER[:PASS]
>      If only the username is provided (-a username), HTTPie will prompt
>      for the password.
>      
>
>  --auth-type {basic,digest,sdp}
>      The authentication mechanism to be used. Defaults to "basic".
>      
>      "basic": Basic HTTP auth
>      "digest": Digest HTTP auth
>      "sdp": SDP API authentication (provided by sdp-api-auth)
>        Hash URLs for the SDP API using api_key and secret.

### Usage

```
http --auth-type=sdp --auth='API_KEY:PRIVATE_KEY' https://sdp/api/...
```
