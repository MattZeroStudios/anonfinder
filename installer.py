import os
# TODO figure out a list of keys required to create at installation for usage.

required_modules = ["python-twitter"]

# set up workspace directory
try:
    os.mkdir('workspace')
    print("workspace . . . check!")
except FileExistsError:
    print("Workspace exists...")
except PermissionError:
    print("permissions error!")

# set up keys directory

try:
    os.mkdir('keys')
    print("keys . . . check!")

except FileExistsError:
    print("Keys exists...")
except PermissionError:
    print("permissions error!")

# install required modules

try:
    for module in required_modules:
        os.system('pip3 install {}'.format(module))

except ConnectionError or PermissionError or OSError:
    print("Something went wrong when installing required python modules for AnonFinder.")


finally:
    print("Happy hunting!")
