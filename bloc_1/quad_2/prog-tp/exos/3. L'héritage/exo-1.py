class Dog():
    kennel = 1
    def __init__(self, breed):
        self.bred = breed
        Dog.kennel += 1

    def __str__(self):
        return self.breed + " says : Woof!"
class SheepDog(Dog):
    def __str__(self):
        return super().__str__() + " Don't run away, little lamb!"


class LowlandDog(SheepDog):
    def __str__(self):
        return  "Woof! Je n’aime pas les montagnes!"
