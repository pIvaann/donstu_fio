from abc import ABC, abstractmethod


class Currency(ABC):
    @abstractmethod
    def to_rubles(self):
        pass

    @abstractmethod
    def show(self):
        pass


class Dollar(Currency):
    def __init__(self, dollars):
        self.dollars = dollars

    def to_rubles(self):
        return self.dollars * 95.76

    def show(self):
        return f"{self.dollars} долл."


class Euro(Currency):
    def __init__(self, euros):
        self.euros = euros

    def to_rubles(self):
        return self.euros * 102.27

    def show(self):
        return f"{self.euros} евро"


class Pound(Currency):
    def __init__(self, pounds):
        self.pounds = pounds

    def to_rubles(self):
        return self.pounds * 117.97

    def show(self):
        return f"{self.pounds} фунт."


class Purse:
    def __init__(self, currencies):
        self.currencies = currencies

    def total_in_rubles(self):
        return sum([all.to_rubles() for all in self.currencies])

    def show_total(self):
        print(f"\nВсего: {self.total_in_rubles()} руб.")

    def show_by_currency(self):
        for all in self.currencies:
            print(f"{all.show()} = {all.to_rubles()} руб.")


def check_errors(wallet):
    while True:
        try:
            value = float(input(f"{wallet}"))
            if value < 0:
                print("Введено отрицательное число. Попробуйте еще раз.")
                continue
            return value
        except ValueError:
            print("Введено не число. Попробуйте еще раз.")
            continue


purse = Purse(
    [
        Dollar(check_errors("Кол-во долларов: ")),
        Euro(check_errors("Кол-во евро: ")),
        Pound(check_errors("Кол-во фунтов: ")),
    ]
)


purse.show_by_currency()
purse.show_total()
