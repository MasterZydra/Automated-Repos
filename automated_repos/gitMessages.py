import abc

class GitMessages(abc.ABC):
    @abc.abstractstaticmethod
    def GIT_CHANGES_IN_COMMITED_FILES():
        return

    @abc.abstractstaticmethod
    def GIT_LOCAL_COMMITS():
        return

    @abc.abstractstaticmethod
    def GIT_NOTHING_TO_COMMIT():
        return

    @abc.abstractstaticmethod
    def GIT_UNCOMMITED_NEW_FILES():
        return