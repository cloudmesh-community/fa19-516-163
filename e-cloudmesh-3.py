# fa19-516-163 E.Cloudmesh.Common.3

# Cloudmesh imports
from cloudmesh.common.FlatDict import FlatDict
from cloudmesh.common.util import banner

import urllib.request
import json

def fetchJson(url:str) -> str:
    json_url = urllib.request.urlopen(url)
    data = json.loads(json_url.read())
    return data

# Fetch some JSON
openapi = fetchJson("https://itpeople-api.apps.iu.edu/openapi.json")
dd = FlatDict(openapi)
print(dd)

# Present some info about it
banner("API Title")
print(dd.info__title)
banner("API Description")
print(dd.info__description)