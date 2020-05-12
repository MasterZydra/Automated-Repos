from .gitMessages import GitMessages

class GitMessages_EN(GitMessages):
    @staticmethod
    def GIT_CHANGES_IN_COMMITED_FILES():
        return "Changes not staged for commit:"

    @staticmethod
    def GIT_LOCAL_COMMITS():
        return "Your branch is ahead of"

    @staticmethod
    def GIT_NOTHING_TO_COMMIT():
        return "nichts zu committen, Arbeitsverzeichnis unverändert"

    @staticmethod
    def GIT_SUCCESSFUL_PUSH():
        return "Resolving deltas: *., completed with *. local objects"

    @staticmethod
    def GIT_UNCOMMITED_NEW_FILES():
        return "Untracked files:"

    @staticmethod
    def NO_GIT_REPOSITORY():
        return "fatal: not a git repository \(or any of the parent directories\): \.git"
        