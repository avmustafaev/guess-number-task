import numpy as np


def number_predict(guessed_number: int = 1, minium_range: int = 1, maximum_range: int = 100) -> int:
    """Функция угадывает число за минимальное количество попыток

    Args:
        guessed_number (int, optional): Отгадываемое число. Defaults to 1.
        minium_range (int, optional): Минимум диапазона. Defaults to 1.
        maximum_range (int, optional): Максимум диапазона. Defaults to 100.

    Returns:
        int: Возвращает количество попыток
    """
    predict_counter = 0

    while True:
        predict_counter += 1
        averaging = (minium_range+maximum_range) // 2

        if averaging > guessed_number:
            maximum_range = averaging

        elif averaging < guessed_number:
            minium_range = averaging

        else:
            print(
                f"Число {guessed_number}: отгадано за {predict_counter} попыток.")
            break  # отгадано: выход из цикла
    return predict_counter


if __name__ == "__main__":
    # Если запускаем из тела скрипта, то выполняется:
    min_range = 1
    max_range = 100
    random_number = np.random.randint(min_range, max_range)
    number_predict(random_number, min_range, max_range)
