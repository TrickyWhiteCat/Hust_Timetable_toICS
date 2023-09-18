import sys
import subprocess
import pkg_resources

def setup(required):
    installed = {pkg.key for pkg in pkg_resources.working_set}
    missing   = required - installed

    if missing:
        # implement pip as a subprocess:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', *missing])
    else: # Update all required packages
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', *required])
required = {'selenium', 'ics', 'webdriver-manager'}
setup(required)