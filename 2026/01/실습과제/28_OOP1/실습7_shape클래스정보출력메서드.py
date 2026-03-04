# 아래 클래스를 수정하시오.
class Shape:

    def __init__(self, Width, Height):
        self.Width = Width
        self.Height = Height

    def print_info(self):
        print(f"Width: {self.Width}")
        print(f"Height: {self.Height}")
        print(f"Area: {self.Width * self.Height}")
        print(f"Perimeter: {(self.Width + self.Height) * 2}")
        return

shape1 = Shape(5, 3)
shape1.print_info()
