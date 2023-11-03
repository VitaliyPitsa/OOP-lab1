import math


class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def read(self):
        self.side1 = float(input("Введите длину первой стороны треугольника: "))
        self.side2 = float(input("Введите длину второй стороны треугольника: "))
        self.side3 = float(input("Введите длину третьей стороны треугольника: "))

    def display(self):
        print("Длины сторон треугольника:")
        print(f"Сторона 1: {self.side1}")
        print(f"Сторона 2: {self.side2}")
        print(f"Сторона 3: {self.side3}")

    def get_side1(self):
        return self.side1

    def get_side2(self):
        return self.side2

    def get_side3(self):
        return self.side3

    def set_side1(self, side1):
        self.side1 = side1

    def set_side2(self, side2):
        self.side2 = side2

    def set_side3(self, side3):
        self.side3 = side3

    def  triangle_area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        area = math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
        return area

    def  triangle_perimeter(self):
        perimeter = self.side1 + self.side2 + self.side3
        return perimeter

    def  triangle_height(self, side_index):
        if side_index == 1:
            height = (2 * self.triangle_area()) / self.side1
        elif side_index == 2:
            height = (2 * self.triangle_area()) / self.side2
        elif side_index == 3:
            height = (2 * self.triangle_area()) / self.side3
        else:
            print("Ошибка: некорректный индекс стороны")
            return None
        return height

    def triangle_type(self):
        if self.side1 == self.side2 == self.side3:
            return "Равносторонний треугольник"
        elif self.side1 == self.side2 or self.side1 == self.side3 or self.side2 == self.side3:
            return "Равнобедренный треугольник"
        elif (self.side1 ** 2 == self.side2 ** 2 + self.side3 ** 2) or (
                self.side2 ** 2 == self.side1 ** 2 + self.side3 ** 2) or (
                self.side3 ** 2 == self.side1 ** 2 + self.side2 ** 2):
            return "Прямоугольный треугольник"
        else:
            return "Обычный треугольник"


if __name__ == "__main__":
    triangle = Triangle(0, 0, 0)

    triangle.read()
    triangle.display()

    print(f"Площадь треугольника: {triangle. triangle_area()}")
    print(f"Периметр треугольника: {triangle. triangle_perimeter()}")

    side_index = int(input("Введите индекс стороны (1, 2, 3), для которой нужно вычислить высоту: "))
    height = triangle. triangle_height(side_index)
    if height is not None:
        print(f"Высота треугольника от стороны {side_index}: {height}")

    print(f"Вид треугольника: {triangle.triangle_type()}")