import os

# Import helper classes
from . import constants
from .gitLanguages import GitLanguages
from .gitMessages import GitMessages
from .gitStatus import GitStatus
from .regex import Regex

class GitWrapper(object):
    @staticmethod
    def gitHelp():
        return os.popen(constants.GIT_HELP).readline()

    @staticmethod
    def gitPush():
        return os.popen(constants.GIT_PUSH + " 2>&1").read()

    @staticmethod
    def gitStatus():
        return os.popen(constants.GIT_STATUS + " 2>&1").read()

    @staticmethod
    def gitVersion():
        return os.popen(constants.GIT_VERSION).readline()

    @staticmethod
    def isGitInstalled():
        return GitWrapper.gitVersion().startswith('git version')

    @staticmethod
    def isFolderGitRepo(gitMessages: GitMessages):
        status = GitWrapper.gitStatus()
        return not Regex.contains(gitMessages.NO_GIT_REPOSITORY(), status)

    @staticmethod
    def getGitLanguage():
        gitHelp = GitWrapper.gitHelp()
        if (gitHelp.startswith('Verwendung: git')):
            return GitLanguages.DE
        elif (gitHelp.startswith('usage: git')):
            return GitLanguages.EN
    
    @staticmethod
    def getGitStatus(gitMessages: GitMessages):
        gitStatus = []
        status = GitWrapper.gitStatus()

        if Regex.contains(gitMessages.GIT_CHANGES_IN_COMMITED_FILES(), status):
            gitStatus.append(GitStatus.CHANGES_IN_COMMITED_FILES)
        if Regex.contains(gitMessages.GIT_LOCAL_COMMITS(), status):
            gitStatus.append(GitStatus.LOCAL_COMMITS)
        if Regex.contains(gitMessages.GIT_UNCOMMITED_NEW_FILES(), status):
            gitStatus.append(GitStatus.UNCOMMITED_NEW_FILES)
        
        if Regex.contains(gitMessages.GIT_NOTHING_TO_COMMIT(), status):
            if len(gitStatus) != 0:
                raise Exception("Something is wrong. Nothing to commit but also other status")
            gitStatus.append(GitStatus.NOTHING_TO_COMMIT)
        
        return gitStatus
