# fa19-516-163 E.Cloudmesh.Common.3

# Cloudmesh imports
from cloudmesh.common.Shell import Shell
from cloudmesh.common.util import banner

# Ping a host
banner("Ping API: itpeople-api.apps.iu.edu")
ping = Shell.ping("itpeople-api.apps.iu.edu")

# Print the result
banner("Ping result")
print(ping)

