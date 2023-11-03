class Money:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def read(self):
        self.first = int(input("Введите номинал купюры (1, 2, 5, 10, 50, 100, 500, 1000, 5000): "))
        self.second = int(input("Введите количество купюр данного достоинства: "))

    def display(self):
        print(f"Номинал купюры: {self.first}")
        print(f"Количество купюр данного достоинства: {self.second}")
        print(f"cумма купюр: {self.first * self.second}")


if __name__ == '__main__':
    m = Money(1, 1)
    m.display()
    m.read()
    m.display()
