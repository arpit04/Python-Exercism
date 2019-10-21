class Rational(object):
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __add__(self, other):
        numer = (self.numer*other.denom) + (self.denom*other.numer)
        denom =  self.denom*other.denom
        add = Rational(numer,denom)
        return add

    def __repr__(self):
        return '{}/{}'.format(self.numer,self.denom)

    def __sub__(self, other):
        numer = (self.numer*other.denom) - (self.denom*other.numer)
        denom = self.denom*other.denom
        sub = Rational(numer,denom)
        return sub

    def __mul__(self, other):
        numer = self.numer*other.numer
        denom = self.denom*other.denom
        mul = Rational(numer,denom)
        return mul

    def __truediv__(self, other):
        numer = self.numer*other.denom
        denom = self.denom*other.numer
        div = Rational(numer,denom)
        return div

    def __abs__(self):
        pass

    def __pow__(self, power):
        numer = self.numer**power
        denom = self.denom**power
        pow = Rational(numer,denom)
        print("hello", pow)
        return pow

    def __rpow__(self, base):
        numer = self.numer**power
        denom = self.denom**power
        rpow = Rational(numer,denom)
        return rpow

s1 = Rational(1,3)
s2 = Rational(1,2)

power = 5
print(s1.__sub__(s2))
print(s1.__add__(s2))
print(s1.__mul__(s2))
print(s1.__truediv__(s2))
print(s1.__eq__(s2))
print(s1.__pow__(s2))
print(s1.__rpow__(s2))