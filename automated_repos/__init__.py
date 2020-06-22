import os.path
import sys

# Import helper classes
from .params import Params
from . import help_aure

# Import commands
from .exec import Exec
from .job import Job
from .repo import Repo

# Meta data
__version__ = '0.0.1'

# Add path of this file to system path
sys.path.append(os.path.dirname(__file__))

# Entry point
def main_entry_point():
    main()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Main logic
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def main(config_file=None, args=None, config=None):
    # Get args from system
    if args is None:
        args = sys.argv[1:]

    if len(args) == 0:
        printHelp()
        return

    params = Params(args)

    if params.arg0 == '--version':
        print('automated-repos version %s' % (__version__,))
        return

    elif params.arg0 in ('--help', 'help'):
        printHelp()
        return
    
    elif params.arg0 == 'exec':
        Exec(Params.nextArgLevel(params)).run()
        return
    
    elif params.arg0 == 'job':
        Job(Params.nextArgLevel(params)).run()
        return

    elif params.arg0 == 'repo':
        Repo(Params.nextArgLevel(params)).run()
        return

    else:
        printHelp()
        return

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Helper functions
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def printHelp():
    print(help_aure.__doc__)