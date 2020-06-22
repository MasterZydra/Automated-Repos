# Import helper classes
from . import help_job
from . import constants
from .params import Params
from .jobWrapper import JobWrapper

class Job(object):
    def __init__(self, params: Params):
        self.params = params
    
    def run(self):
        if self.params.arg0 in ('--help', 'help'):
            self.__printHelp()
            return
        
        elif self.params.arg0 == 'add':
            if len(self.params.args) != 2:
                print(constants.ERROR + constants.MSG_JOB_NAME_EXPECTED)
                return

            JobWrapper.addJob(self.params.arg1)
            return

        elif self.params.arg0 == 'edit':
            print('edit')
            return

        elif self.params.arg0 == 'rem':
            if len(self.params.args) != 2:
                print(constants.ERROR + constants.MSG_JOB_NAME_EXPECTED)
                return

            JobWrapper.remJob(self.params.arg1)
            return

        elif self.params.arg0 == 'show':
            JobWrapper.showJobs()
            return

        else:
            self.__printHelp()
            return

    def __printHelp(self):
        print(help_job.__doc__)