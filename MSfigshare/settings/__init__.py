#This is the package initialisation settings
from .base import *

LOCAL=True # when in production set to false 
#These are the optinal settings files
if LOCAL:
    try:
        from .local import *

    except:
        pass

# set the local first 
else:
    try:
        from .production import *

    except:
        pass
