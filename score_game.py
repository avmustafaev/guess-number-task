from game_predict_number import number_predict as predictor
import numpy as np


def score_game(tested_func, minium_range: int = 1, maximum_range: int = 101) -> int:
    """Функция тестер, в качестве аргумента принимает функцию которую будет тестировать
    и диапазон угадываемого числа

    Args:
        tested_func (_type_): Функция, которую необходимо протестировать
        minium_range (int, optional): Минимум диапазона. По умолчению равен 1.
        maximum_range (int, optional): Максимум диапазона. По умолчанию равен 101.

    Returns:
        int: Возвращем среднее число попыток угадывания.
    """
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(
        minium_range, maximum_range, size=(1000))  # загадали список чисел в соответствии с диапазоном
    count_ls = [tested_func(number, minium_range, maximum_range) for number in random_array] # Заполняем список попыток
    return int(np.mean(count_ls))


if __name__ == "__main__":
    # Если запускаем из тела скрипта, то выполняется:
    score = score_game(predictor, 1, 101)
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
