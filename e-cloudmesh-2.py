# fa19-516-163 E.Cloudmesh.Common.2

# Cloudmesh imports
from cloudmesh.common.dotdict import dotdict
from cloudmesh.common.util import banner

import urllib.request
import json

def fetchJson(url:str) -> dotdict:
    json_url = urllib.request.urlopen(url)
    data = json.loads(json_url.read())
    return data

# Fetch some JSON
openapi = fetchJson("https://itpeople-api.apps.iu.edu/openapi.json")
dd = dotdict(openapi)

# Dotdict works OK with simple objects.
banner("Dotdict provides dotted access at one level deep.")
print(dd.info)

# Dotdict doesn't work with complex objects.
banner("Accessing dotted property at lower levels throws exception.")
try:
    print(dd.info.title)
except ValueError:
    print("Exception thrown.")

banner("Accessing named property at lower levels throws exception.")
try:
    print(dd.info["title"])
except ValueError:
    print("Exception thrown.")
