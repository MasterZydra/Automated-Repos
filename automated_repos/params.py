class Params(object):
    def __init__(self, args):
        self.args = args

        # arg 0
        try:
            self.arg0 = self.args[0]
        except:
            self.arg0 = None
    
    def getNextArgLevel(self):
        return self.args[1:]