
from fractions import Fraction


class Str(str):

    def __sub__(self, obj):
        main = str(self)
        return "".join(main.split(obj))

class Float(object):

    def __init__(self, obj, sub=1):
        self.ab = Fraction(obj,sub)
        self.pown = Fraction(1) 
        self.val = float(self.ab**self.pown)

    def __pow__(self, other):
        self.pown = self.pown * (other.ab**other.pown)
        self.val = float(self.ab**self.pown)
        return self

    def __str__(self):
        return str(self.val)

num = (Float(1,4)**Float(1,3))**Float(1,2)

print(num.pown)
print((num**Float(2))**Float(3))

a = Float(3)**num

print(a)
print(a.ab, a.pown)
