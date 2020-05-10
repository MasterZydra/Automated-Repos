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
        self.gitMessages = None
    
    def run(self):
        if self.params.arg0 in ('--help', 'help'):
            self.__printHelp()
            return
        
        elif len(self.params.args) == 0: # or -- all ....
            if not GitConfig.isGitInstalled():
                print(constants.ERROR + constants.MSG_NO_GIT_INSTALLED)
            
            if not self.__importGitMessages(GitConfig.getGitLanguage()):
                return
        else:
            self.__printHelp()
            return
    
    def __importGitMessages(self, langauge: GitLanguages):
        if langauge == GitLanguages.UNKNOWN:
            print(constants.ERROR + constants.MSG_LANG_IS_UNKNOWN)
            return False
        if langauge == GitLanguages.DE:
            from .gitMessages_DE import GitMessages_DE
            self.gitMessages = GitMessages_DE
        elif langauge == GitLanguages.EN:
            from .gitMessages_EN import GitMessages_EN
            self.gitMessages = GitMessages_EN
        else:
            print(constants.ERROR + constants.MSG_LANG_NOT_SUPPORTED)
            return False
        
        return True


    def __printHelp(self):
        print(help_exec.__doc__)