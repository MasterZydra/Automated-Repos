class Params(object):
    def __init__(self, args):
        self.args = args

        # arg 0
        try:
            self.arg0 = self.args[0].lower()
        except:
            self.arg0 = None

        # arg 1
        if len(self.args) >= 2:
            self.arg1 = self.args[1]

    @staticmethod
    def nextArgLevel(params):
        return Params(params.args[1:])