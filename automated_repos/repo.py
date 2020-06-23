# Import helper classes
from . import constants
from . import help_repo
from .params import Params
from .repoWrapper import RepoWrapper

class Repo(object):
    def __init__(self, params: Params):
        self.params = params
    
    def run(self):
        if self.params.arg0 in ('--help', 'help'):
            self.__printHelp()
            return
        
        # Add
        elif self.params.arg0 == 'add':
            if len(self.params.args) != 3:
                print(constants.ERROR + constants.MSG_PATH_JOB_EXPECTED)
                return

            RepoWrapper.addRepo(self.params.arg2, self.params.arg1)
            return

        # Remove
        elif self.params.arg0 == 'rem':
            if len(self.params.args) != 3:
                print(constants.ERROR + constants.MSG_PATH_JOB_EXPECTED)
                return

            RepoWrapper.remRepo(self.params.arg2, self.params.arg1)
            return

        # Show
        elif self.params.arg0 == 'show':
            RepoWrapper.showRepo()
            return

        else:
            self.__printHelp()
            return

    def __printHelp(self):
        print(help_repo.__doc__)