from enum import Enum
# Git status
class GitStatus(Enum):
    NOTHING_TO_COMMIT = 0
    LOCAL_COMMITS = 1
    CHANGES_IN_COMMITED_FILES = 2
    UNCOMMITED_NEW_FILES = 3