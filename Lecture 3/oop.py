class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def has_student_discount(self):
        if self.age>26:
            return False
        else:
            return True
  
   
# Class attributes   
class FormalPerson:
    TITLES = ('Dr', 'Mr', 'Mrs', 'Ms')

    def __init__(self, title, name, surname, allowed_titles=TITLES):
        if title not in allowed_titles:
            raise ValueError("%s is not a valid title." % title)

        self.title = title
        self.name = name
        self.surname = surname    
        
             
# Inheritance
class Czech(Person):
    def likes_svickova(self):
        return True
    
    
    
## EXAMPLE: Consumer
class Consumer:
    def __init__(self, w):
        "Initialize consumer with w euros of wealth"
        self.wealth = w
    
    def earn(self, y):
        "The consumer earns y euros"
        self.wealth += y

    def spend(self, x):
        "The consumer spends x euros if feasible"
        new_wealth = self.wealth - x
        if new_wealth < 0:
            print("Insufficent funds")
        else:
            self.wealth = new_wealth    
           
            