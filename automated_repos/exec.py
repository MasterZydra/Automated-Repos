import os
import re

# Import helper classes
from . import help_exec
from . import constants
from .gitConfig import GitConfig
from .gitLanguages import GitLanguages
from .params import Params

class Exec(object):
    def __init__(self, params: Params):
        self.params = params
    
    def run(self):
        if self.params.arg0 in ('--help', 'help'):
            self.__printHelp()
            return
        
        else:
            self.__printHelp()
            return

    def __printHelp(self):
        print(help_exec.__doc__)