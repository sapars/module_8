def personal_sum(numbers: [int | float]):
    total = 0
    incorrect_data = 0
    try:
        for num in numbers:
            try:
                total += num
            except TypeError:
                incorrect_data += 1
                print('Некорректный тип данных для подсчёта суммы - ', num)
    except TypeError:
        print('В numbers записан некорректный тип данных')
    return total, incorrect_data


def calculate_average(numbers):
    summa, wrongs = personal_sum(numbers)
    try:
        return summa / (len(numbers) - wrongs)
    except ZeroDivisionError:
        return 0
    except TypeError:
        return None


def main():
    print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
    print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
    print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
    print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать


if __name__ == '__main__':
    main()