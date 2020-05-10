from .gitMessages import GitMessages

class GitMessages_DE(GitMessages):
    @staticmethod
    def GIT_CHANGES_IN_COMMITED_FILES():
        return "Änderungen, die nicht zum Commit vorgemerkt sind"

    @staticmethod
    def GIT_LOCAL_COMMITS():
        return "Ihr Branch ist .* Commits vor"

    @staticmethod
    def GIT_NOTHING_TO_COMMIT():
        return "nichts zu committen, Arbeitsverzeichnis unverändert"

    @staticmethod
    def GIT_SUCCESSFUL_PUSH():
        return "Resolving deltas: *., completed with *. local objects."

    @staticmethod
    def GIT_UNCOMMITED_NEW_FILES():
        return "Unversionierte Dateien:"