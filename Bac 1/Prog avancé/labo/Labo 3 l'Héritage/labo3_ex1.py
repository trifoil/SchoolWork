class Dog:
    kennel = 0 
    def __init__(self,breed):
        self.breed= breed 
        Dog.kennel +=1
    def __str__(self):
        return self.breed+ ' says: Woof!'
    
class SheepDog(Dog):
    def __str__(self) :
        return super().__str__() + " Don't run away, Little Lamb!"

class GardDog(Dog):
    def __str__(self):
        return super().__str__()+"Stay where you are, Mister Intruder"
    
class LowlandDog(SheepDog):
    def __str__(self):
        return super().__str__()+" Woof! Je n'aime pas les montagnes"
    
rocky = SheepDog("collie ")
luna = GardDog("doberman ")
marcel = LowlandDog("groschien")
print(marcel)
#print(rocky)
#print(luna)
#print(issubclass(SheepDog,Dog),issubclass(SheepDog,GardDog))
#print(isinstance(rocky,GardDog),isinstance(luna,GardDog))
#print(luna is luna,rocky is luna)
#print(rocky.kennel)
