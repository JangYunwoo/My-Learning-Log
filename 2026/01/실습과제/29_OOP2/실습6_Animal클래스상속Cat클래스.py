# 아래 클래스를 수정하시오.
class Animal:
    num_of_animal = 0
    def __init__(self):
        self.increase_animal()
        

    @classmethod
    def increase_animal(cls):
        Animal.num_of_animal += 1
        return

class Cat(Animal):
    def meow(self):
        print("야옹!")


cat1 = Cat()
cat1.meow()
