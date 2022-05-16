import numpy as np


def number_predict(guessed_number: int = 49, minium_range: int = 1, maximum_range: int = 101) -> int:
    """Функция угадывает число за минимальное количество попыток

    Args:
        guessed_number (int, optional): Отгадываемое число. По умолчанию равно 49.
        minium_range (int, optional): Минимум диапазона. По умолчанию равно 1.
        maximum_range (int, optional): Максимум диапазона. По умолчанию равно 100.

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
            break  # отгадано: выход из цикла
    return predict_counter


# RUN
if __name__ == "__main__":
    # Если запускаем из тела скрипта, то выполняется:
    min_range = 1
    max_range = 10001
    random_number = np.random.randint(min_range, max_range) # Загадываем случайное число в рамках диапазона
    counter = number_predict(random_number, min_range, max_range) 
    print(f"Число {random_number}: отгадано за {counter} попыток.")
