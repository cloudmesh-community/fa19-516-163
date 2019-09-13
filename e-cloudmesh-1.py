# fa19-516-163 E.Cloudmesh.Common.1

# Cloudmesh imports
from cloudmesh.common.console import Console
from cloudmesh.common.util import HEADING, banner
from cloudmesh.common.debug import VERBOSE

# Mypy imports
from typing import Dict

def add(x:int, y:int) -> Dict[str, int]:
    """Take two numbers and return a dictionary that includes the sum.
    
    Arguments:
        x {int}
        y {int}
    
    Returns:
        Dict[str, int]
    """
    HEADING()
    return {"x":x, "y":y, "sum": x+y}

# Announce our intention
banner("Adding two numbers")
# Add the numbers
result = add (1, 2)
# Print the result
VERBOSE(result)
