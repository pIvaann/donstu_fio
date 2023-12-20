class Number:
    def __init__(self, number):
        self.number = int(number)

    def simple(self):
        k = 0
        for i in range(2, self.number // 2 + 1):
            if self.number % i == 0:
                k = k + 1
        if k <= 0:
            return "простое"
        else:
            return "непростое"

    def __add__(self, other):
        return Number(self.number + other.number)

    def __sub__(self, other):
        return Number(self.number - other.number)

    def __mul__(self, other):
        return Number(self.number * other.number)

    def __truediv__(self, other):
        if other.number == 0:
            return "Нелья делить на ноль... ;("
        return Number(self.number / other.number)

    def __eq__(self, other):
        if isinstance(other, Number):
            return self.number == other.number
        return False

    def __str__(self):
        return str(self.number)


def check_errors(number):
    while True:
        try:
            value = float(input(f"{number}"))
            return value
        except ValueError:
            print("Введено не число. Попробуйте еще раз.")
            return


c1 = Number(check_errors("Введите первое число: "))
c2 = Number(check_errors("Введите второе число: "))

plus = c1 + c2
minus = c1 - c2
mul = c1 * c2
div = c1 / c2
eq = c1 == c2

print(
    f"Число {c1} - {c1.simple()}\n"
    f"Число {c2} - {c2.simple()}\n\n"
    f"Сложение: {plus}\n"
    f"Вычитание: {minus}\n"
    f"Умножение: {mul}\n"
    f"Деление: {div}\n"
    f"Сравнение: {eq}"
)
