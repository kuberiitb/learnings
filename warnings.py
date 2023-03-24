# module link: https://docs.python.org/3/library/warnings.html#module-warnings

import warnings
# the default option
warnings.simplefilter("default")

def fxn():
    warnings.warn("writtten deprecated", DeprecationWarning)
    print("Running Function")

# default function call result in warning on the stdout    
fxn()
# Running Function
"""
workspace_kuber/envs/pys_env/lib/python3.6/site-packages/ipykernel_launcher.py:5: DeprecationWarning: writtten deprecated
"""
# Two options to ignore the warning

# option 1 : ignore each warning on case basis using catch_warnings 
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    fxn()
# Running Function

# option 2 : ignore all warning in the module
warnings.simplefilter("ignore")
fxn()
# Running Function
