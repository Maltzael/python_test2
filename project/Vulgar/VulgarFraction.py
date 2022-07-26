import math

global ROUNDFLOAT
ROUNDFLOAT = 4


class VulgarFraction:
    def __init__(self, numerator: int, denominator: int):
        self.numerator = numerator
        self.denominator = denominator
        self.makeValgarFraction()
        self.checkIfZeroError()

    def checkIfZeroError(self):
        try:
            self.numerator / self.denominator
        except ZeroDivisionError:
            print("Zero w mianowniku/dzielenie przez zeroi. Zlituj się no.")
            exit(1)

    def makeValgarFraction(self):

        x = math.gcd(self.numerator, self.denominator)
        try:
            self.numerator //= x
            self.denominator //= x
        except:
            print("cos poszlo nie tak")
            exit(1)

    def __str__(self):
        if self.numerator == 0:
            return "0"
        else:
            return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        if type(other) == type(self):
            firstNumerator = self.numerator * other.denominator
            secondNumerator = other.numerator * self.denominator
            return VulgarFraction(firstNumerator + secondNumerator, self.denominator * other.denominator)
        elif type(other) == int:
            firstNumerator = self.numerator + (other * self.denominator)
            return VulgarFraction(firstNumerator, self.denominator)
        elif type(other) == float:
            other = round(other, ROUNDFLOAT)
            if other == 0.0:
                return VulgarFraction(self.numerator, self.denominator)
            else:
                # convert into Vulgar Fraction
                other = VulgarFraction(int(other * 10 ** ROUNDFLOAT), int(10 ** ROUNDFLOAT))
                firstNumerator = self.numerator * other.denominator
                secondNumerator = other.numerator * self.denominator
                return VulgarFraction(firstNumerator + secondNumerator, self.denominator * other.denominator)

    def __sub__(self, other):
        if type(other) == type(self):
            firstNumerator = self.numerator * other.denominator
            secondNumerator = other.numerator * self.denominator
            return VulgarFraction(firstNumerator - secondNumerator, self.denominator * other.denominator)
        elif type(other) == int:
            firstNumerator = self.numerator - (other * self.denominator)
            return VulgarFraction(firstNumerator, self.denominator)
        elif type(other) == float:
            other = round(other, ROUNDFLOAT)
            if other == 0.0:
                return VulgarFraction(self.numerator, self.denominator)
            else:
                # convert into Vulgar Fraction
                other = VulgarFraction(int(other * 10 ** ROUNDFLOAT), int(10 ** ROUNDFLOAT))
                firstNumerator = self.numerator * other.denominator
                secondNumerator = other.numerator * self.denominator
                return VulgarFraction(firstNumerator - secondNumerator, self.denominator * other.denominator)

    def __mul__(self, other):
        if type(other) == type(self):
            return VulgarFraction(self.numerator * other.numerator, self.denominator * other.denominator)
        elif type(other) == int:
            return VulgarFraction(self.numerator * other, self.denominator)
        elif type(other) == float:
            other = round(other, ROUNDFLOAT)
            if other == 0.0:
                return VulgarFraction(self.numerator, self.denominator)
            else:
                # convert into Vulgar Fraction
                other = VulgarFraction(int(other * 10 ** ROUNDFLOAT), int(10 ** ROUNDFLOAT))
                return VulgarFraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __truediv__(self, other):
        if type(other) == type(self):
            return VulgarFraction(self.numerator * other.denominator, self.denominator * other.numerator)
        elif type(other) == int:
            return VulgarFraction(self.numerator, self.denominator * other)
        elif type(other) == float:
            try:
                # convert into Vulgar Fraction with precysion in ROUNDFLOAT
                other = round(other, ROUNDFLOAT)
                other = VulgarFraction(int(other * 10 ** ROUNDFLOAT), int(10 ** ROUNDFLOAT))
                return VulgarFraction(self.numerator * other.denominator, self.denominator * other.numerator)
            except ZeroDivisionError:
                print("Wartość zero, lub bliska zeru. Zwiększ ROUNDFLOAD dla wiekszej precyzji")
                exit(1)

    def __eq__(self, other):
        if type(other) == type(self):
            if self.numerator == other.numerator and self.denominator == other.denominator:
                return True
            else:
                return False
        elif type(other) == int:
            secondNumerator = other.numerator * self.denominator
            if self.numerator == secondNumerator:
                return True
            else:
                return False
        elif type(other) == float:
            other = round(other, ROUNDFLOAT)
        if other == 0.0:
            return ZeroDivisionError
        else:
            # convert into Vulgar Fraction
            other = VulgarFraction(int(other * 10 ** ROUNDFLOAT), int(10 ** ROUNDFLOAT))
            if self.numerator == other.numerator and self.denominator == other.denominator:
                return True
            else:
                return False


if __name__ == '__main__':
    a = VulgarFraction(1, 2)
    b = VulgarFraction(1, 2)
    c = a / b
    print(c)
