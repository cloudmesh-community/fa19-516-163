# fa19-516-163 E.Cloudmesh.Common.3

# Cloudmesh imports
from cloudmesh.common.StopWatch import StopWatch
from cloudmesh.common.util import banner

import urllib.request
import json

def fetchJson(url: str) -> str:
    json_url = urllib.request.urlopen(url)
    data = json.loads(json_url.read())
    return data


# Reset the stopwatch
StopWatch.clear()

# Fetch the JSON
banner("Ping API spec: itpeople-api.apps.iu.edu")
StopWatch.start("fetch")
openapi = fetchJson("https://itpeople-api.apps.iu.edu/openapi.json")
StopWatch.stop("fetch")

# Print how long the fetch took.
banner("Benchmark")
print(StopWatch.benchmark())
