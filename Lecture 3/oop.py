## EXAMPLE: Consumer
class Consumer:
    def __init__(self, w):
        "Initialize consumer with w dollars of wealth"
        self.wealth = w
    
    def earn(self, y):
        "The consumer earns y dollars"
        self.wealth += y

    def spend(self, x):
        "The consumer spends x dollars if feasible"
        new_wealth = self.wealth - x
        if new_wealth < 0:
            print("Insufficent funds")
        else:
            self.wealth = new_wealth


## EXAMPLE: Rational numbers
class Rational:
    def __init__(self, num, denom):
        self.numerator = num
        self.denominator = denom

    def add(self, other):
        newNumerator = self.numerator * other.denominator +  self.denominator * other.numerator
        newDenominator = self.denominator*other.denominator
        return Rational(newNumerator, newDenominator)


## EXERCISE
class Polynomial:
    def __init__(self, coefs):
        pass
    
    def evaluate(self, x):
        pass
    
    def derive(self,x):
        pass