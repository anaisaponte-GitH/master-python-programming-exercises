# Your code here
class MathOperations:
    pi = 3.14159

    @classmethod
    def calculate_circle_area(cls,radio):
        return (radio**2) * cls.pi

print(MathOperations.calculate_circle_area(5))
