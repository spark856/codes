from fractions import Fraction

class Float(object):

    def __init__(self, obj, sub=1, frac=None, pown=1):
        self.ab = Fraction(obj, sub) if frac is None else frac
        self.pown = pown 
        self.val = self.ab**self.pown

    def __pow__(self, other):
        return Float(1,frac=self.ab, pown=self.pown * other.val)


    def __str__(self):
        return str(float(self.val))

    def inverse(self):
        return Float(1,frac=1/self.ab, pown=self.pown)
        
class Float2(object):

    def __init__(self, obj, sub=1, frac=None, pown=1):
        self.val = Fraction(obj, sub)**pown if frac is None else frac**pown

    def __pow__(self, other):
        return Float(1,frac=self.val, pown=other.val)


    def __str__(self):
        return str(float(self.val))

    def inverse(self):
        return Float(1,frac=1/self.val)

if __name__ == '__main__':
    num = (Float(1,4)**Float(1,3))**Float(1,2)

    print(num.val)
    print((num**Float(2))**Float(3))

    a = Float(3)**num

    print(a)
    print(a**(num.inverse()))
