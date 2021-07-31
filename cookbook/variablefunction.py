class function_class:
    def __init__(self):
        pass
    def A(self): print('here runs function A')
    def B(self): print('here runs function B')
    def C(self): print('here runs function C')
    def run_function(self):
        self.fActive()
    def runner(self,case):
        fDic = {'A':self.A,
                'B':self.B,
                'C':self.C}

        self.fActive = self.A
        self.fActive()

foo = function_class()
foo.runner('A')
