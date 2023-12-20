import pandas as pd
import matplotlib.pyplot as plt


class Csv:
    def __init__(self, filename="avocado"):
        self.filename = filename

    def open_file(self):
        try:
            self.df = pd.read_csv(f"lab4/{self.filename}.csv", sep=",")
        except FileNotFoundError:
            print("Файл не найден.")

    # Первое задание (1/2)
    def rename_column(self, old_name, new_name):
        self.df.rename(columns={f"{old_name}": f"{new_name}"}, inplace=True)

    # Первое задание (2/2)
    def rename_object(self, old_name, column, new_name):
        self.df[column] = self.df[column].replace({old_name: new_name})

    # Второе задание (1/1)
    def new_column(self, column1, column2, new_column_name):
        self.df[f"{new_column_name}"] = (
            self.df[f"{column1}"] + " " + self.df[f"{column2}"]
        )

    # Третье задание (1/4)
    def min_int(self):
        return self.df.iloc[:, 1:].min(numeric_only=True)

    # Третье задание (2/4)
    def max_int(self):
        return self.df.iloc[:, 1:].max(numeric_only=True)

    # Третье задание (3/4)
    def avg_int(self):
        return self.df.iloc[:, 1:].mean(numeric_only=True)

    # Третье задание (4/4)
    def median_int(self):
        return self.df.iloc[:, 1:].median(numeric_only=True)

    # Четвертое задание
    def four_task(self):
        grouped = self.df.groupby("region")["AveragePrice"].mean()
        sorted_grouped = grouped.sort_values()
        sorted_grouped.plot(kind="bar", title="Средние значения цен")
        plt.xlabel("Штат")
        plt.ylabel("Средняя цена")
        plt.show()

    # Пятое задание
    def five_task(self):
        filtered_by_averageprice = self.df.query("AveragePrice > 1")
        unique_values = filtered_by_averageprice["AveragePrice"].unique()
        duplicate_values = filtered_by_averageprice.duplicated().sum()
        return unique_values, duplicate_values

    # Шестое задание
    def six_task(self):
        filtered_by_oraganic = self.df.groupby("type")["AveragePrice"].mean()
        filtered_by_oraganic.plot(kind="bar", title="Средняя цена по типу")
        plt.xlabel("Тип")
        plt.ylabel("Цена")
        plt.show()

    # Седьмое задание
    def seven_task(self):
        statistics = pd.DataFrame(
            {
                "Минимальное": self.min_int(),
                "Максимальное": self.max_int(),
                "Среднее": self.avg_int(),
                "Медиана": self.median_int(),
            }
        )
        # Создаем отдельные графики для каждого столбца
        fig, axes = plt.subplots(
            nrows=1, ncols=len(statistics.columns), figsize=(12, 4)
        )

        for idx, column in enumerate(statistics.columns):
            statistics[column].plot(kind="bar", ax=axes[idx])
            axes[idx].set_title(column)
            axes[idx].set_xlabel("Поля")
            axes[idx].set_ylabel("Значения")

        plt.suptitle("Перекрестная выборка")
        plt.show()


def main(csv):
    csv.open_file()
    try:
        start = int(
            input(
                "Выберите необходимое действие:\n\n"
                "Первое задание: 1 \n"
                "Второе задание: 2 \n"
                "Третье задание: 3 \n"
                "Четвертое задание: 4 \n"
                "Пятое задание: 5 \n"
                "Шестое задание: 6 \n"
                "Седьмое задание: 7 \n"
            )
        )
        if start == 1:
            first(csv)
        elif start == 2:
            second(csv)
        elif start == 3:
            third(csv)
        elif start == 4:
            fourth(csv)
        elif start == 5:
            fifth(csv)
        elif start == 6:
            six(csv)
        elif start == 7:
            seven(csv)
        else:
            print("Это действие не найдено.")
            main(csv)
    except ValueError:
        print("Нужно ввести число из предложенных.")
        main(csv)


def first(csv):
    print("DataFrame до переименования колонки и ячейки:")
    print(csv.df)

    csv.rename_column(old_name="year", new_name="Год")
    csv.rename_column(old_name="Date", new_name="дата")
    csv.rename_object(old_name="organic", column="type", new_name="Органический")

    print("DataFrame после переименования:")
    print(csv.df)
    main(csv)


def second(csv):
    print("DataFrame до добавления новой колонки:")
    print(csv.df)

    csv.new_column(column1="type", column2="region", new_column_name="region_type")

    print("DataFrame после добавления:")
    print(csv.df)
    main(csv)


def third(csv):
    print(f"Минимальное:\n{csv.min_int()}\n")
    print(f"Максимальное:\n{csv.max_int()}\n")
    print(f"Среднее:\n{csv.avg_int()}\n")
    print(f"Медиана:\n{csv.median_int()}")
    main(csv)


def fourth(csv):
    csv.four_task()
    main(csv)


def fifth(csv):
    unique, duplicate = csv.five_task()
    print(
        "При сортировке таблицы по средней цене выше 1$ мы получим:\n"
        f"Уникальных значений средней цены: {unique}\n"
        f"Повторений средней цены: {duplicate}"
    )
    main(csv)


def six(csv):
    csv.six_task()
    main(csv)


def seven(csv):
    csv.seven_task()
    main(csv)


csv = Csv()
main(csv)
