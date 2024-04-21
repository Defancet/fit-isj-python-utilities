#!/usr/bin/env python3

class Polynomial:

    def __init__(self, *args, **kwargs):
        self.polynom = []
        for i in args:
            if isinstance(i, list):
                self.polynom = i
        if not self.polynom:
            if args:
                self.polynom = list(args)
            else:
                for key, item in kwargs.items():
                    for i in range(int(key[1:]) + 1 - len(self.polynom)):
                        self.polynom.append(0)
                    self.polynom[int(key[1:])] = item
            for i in range(len(self.polynom) - 1, 0, -1):
                if self.polynom[i] == 0:
                    del self.polynom[i]
                else:
                    break

    def __str__(self):
        result = ""
        length = len(self.polynom)
        if length == 1:
            result += str(self.polynom[0])
            return result
        for i in range(length - 1):
            if self.polynom[length - i - 1] != 0:
                if self.polynom[length - i - 1] > 0:
                    if len(result) != 0:
                        result += ' + '
                else:
                    result += ' - '
                if abs(self.polynom[length - i - 1]) != 1:
                    result += str(abs(self.polynom[length - i - 1]))
                result += 'x'
                if length - i - 1 > 1:
                    result += '^' + str(length - i - 1)
        if self.polynom[0] != 0:
            if self.polynom[0] > 0:
                result += ' + ' + str(self.polynom[0])
            else:
                result += ' - ' + str(abs(self.polynom[0]))
        if len(result) == 0:
            result = '0'
        return result

    def __eq__(self, other):
        if len(other.polynom) != len(self.polynom):
            return False
        for first, second in zip(other.polynom, self.polynom):
            if first != second:
                return False
        return True

    def __add__(self, other):
        result = self.polynom.copy()
        i = 0
        for tmp_polynom, o_polynom in zip(self.polynom, other.polynom):
            result[i] = tmp_polynom + o_polynom
            i = i + 1
        if len(self.polynom) < len(other.polynom):
            for i in range(len(self.polynom), len(other.polynom)):
                result.append(other.polynom[i])
        return Polynomial(result)

    def __mul__(self, other):
        result = [0] * (1 + len(self.polynom) + len(other.polynom))
        for i in range(len(self.polynom)):
            for j in range(len(other.polynom)):
                result[i + j] += self.polynom[i] * other.polynom[j]
        return Polynomial(result)

    def __pow__(self, power):
        if power > 1:
            result = self
            for i in range(1, power):
                result *= self
            return Polynomial(result)
        elif power == 1:
            return Polynomial(self.polynom)
        if power == 0:
            return 1

    def derivative(self):
        result = self.polynom[1:]
        if len(self.polynom) == 1:
            return 0
        for i in range(len(result)):
            result[i] = result[i] * (i + 1)
        return Polynomial(result)

    def at_value(self, x1, x2=None):
        result = 0
        if not x2:
            for i in range(len(self.polynom)):
                result = result + self.polynom[i] * (x1 ** i)
            return result
        for i in range(len(self.polynom)):
            result = result - self.polynom[i] * (x1 ** i) + self.polynom[i] * (x2 ** i)
        return result

def test():
    assert str(Polynomial(0, 1, 0, -1, 4, -2, 0, 1, 3, 0)) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x"
    assert str(Polynomial([-5, 1, 0, -1, 4, -2, 0, 1, 3, 0])) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x - 5"
    assert str(Polynomial(x7=1, x4=4, x8=3, x9=0, x0=0, x5=-2, x3=-1, x1=1)) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x"
    assert str(Polynomial(x2=0)) == "0"
    assert str(Polynomial(x0=0)) == "0"
    assert Polynomial(x0=2, x1=0, x3=0, x2=3) == Polynomial(2, 0, 3)
    assert Polynomial(x2=0) == Polynomial(x0=0)
    assert str(Polynomial(x0=1) + Polynomial(x1=1)) == "x + 1"
    assert str(Polynomial([-1, 1, 1, 0]) + Polynomial(1, -1, 1)) == "2x^2"
    pol1 = Polynomial(x2=3, x0=1)
    pol2 = Polynomial(x1=1, x3=0)
    assert str(pol1 + pol2) == "3x^2 + x + 1"
    assert str(pol1 + pol2) == "3x^2 + x + 1"
    assert str(Polynomial(x0=-1, x1=1) ** 1) == "x - 1"
    assert str(Polynomial(x0=-1, x1=1) ** 2) == "x^2 - 2x + 1"
    pol3 = Polynomial(x0=-1, x1=1)
    assert str(pol3 ** 4) == "x^4 - 4x^3 + 6x^2 - 4x + 1"
    assert str(pol3 ** 4) == "x^4 - 4x^3 + 6x^2 - 4x + 1"
    assert str(Polynomial(x0=2).derivative()) == "0"
    assert str(Polynomial(x3=2, x1=3, x0=2).derivative()) == "6x^2 + 3"
    assert str(Polynomial(x3=2, x1=3, x0=2).derivative().derivative()) == "12x"
    pol4 = Polynomial(x3=2, x1=3, x0=2)
    assert str(pol4.derivative()) == "6x^2 + 3"
    assert str(pol4.derivative()) == "6x^2 + 3"
    assert Polynomial(-2, 3, 4, -5).at_value(0) == -2
    assert Polynomial(x2=3, x0=-1, x1=-2).at_value(3) == 20
    assert Polynomial(x2=3, x0=-1, x1=-2).at_value(3, 5) == 44
    pol5 = Polynomial([1, 0, -2])
    assert pol5.at_value(-2.4) == -10.52
    assert pol5.at_value(-2.4) == -10.52
    assert pol5.at_value(-1, 3.6) == -23.92
    assert pol5.at_value(-1, 3.6) == -23.92

if __name__ == '__main__':
    test()
