# Import helper classes
from .params import Params
from . import help_exec

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