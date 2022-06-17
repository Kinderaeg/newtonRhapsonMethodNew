import re


test = "-3x**23+12x**23"
symbol = 'x'


class Reader():
    def __init__(self, ch):
        self.pattern = '(([\+\-]?\d*)'+ch+'\*{0,2}(\d*))'
        self.terms = []

    def read(self, inp):
        self.terms = re.findall(self.pattern, inp)
        return


    def poly_derivative(self):
        res = ''
        for i in range(0,len(self.terms)):
            inputToFn = self.terms[i]
            if int(inputToFn[1]) > 0:
                res+='+'
            res += self.poly_term_derivative(inputToFn)
        return res


    def poly_term_derivative(self, f):
        if f[2] != '':
            exp = int(f[2])
        else:
            exp =1
        return str(int(f[1])*int(exp))+'*x**'+str(exp-1)
