class Params(object):
    def __init__(self, args):
        self.args = args

        # arg 0
        if len(self.args) > 0:
            self.arg0 = self.args[0].lower()
        else:
            self.arg0 = None

        # arg 1
        if len(self.args) > 1:
            self.arg1 = self.args[1].lower()
        else:
            self.arg1 = None

        # arg 2
        if len(self.args) > 2:
            self.arg2 = self.args[2].lower()
        else:
            self.arg2 = None

    @staticmethod
    def nextArgLevel(params):
        return Params(params.args[1:])