# 아래 클래스를 수정하시오.
class Shape:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def calculate_perimeter(self):
        return (self.num1 + self.num2) * 2

shape1 = Shape(5, 3)
perimeter1 = shape1.calculate_perimeter()
print(perimeter1)
