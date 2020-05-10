import os

# Import helper classes
from . import constants
from .gitLanguages import GitLanguages

class GitConfig(object):
    @staticmethod
    def __callGitHelp():
        return os.popen(constants.GIT_HELP).readline()

    @staticmethod
    def __callGitVersion():
        return os.popen(constants.GIT_VERSION).readline()

    @staticmethod
    def isGitInstalled():
        return GitConfig.__callGitVersion().startswith('git version')

    @staticmethod
    def getGitLanguage():
        gitHelp = GitConfig.__callGitHelp()
        if (gitHelp.startswith('Verwendung: git')):
            return GitLanguages.DE
        elif (gitHelp.startswith('usage: git')):
            return GitLanguages.EN