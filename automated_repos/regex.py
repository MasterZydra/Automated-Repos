import re

class Regex(object):
    @staticmethod
    def contains(pattern: str, haystack: str):
        return re.search(pattern, haystack, re.IGNORECASE | re.MULTILINE)