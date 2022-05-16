from game_predict_number import number_predict as predictor
import numpy as np


def score_game(tested_func,minium_range: int = 1, maximum_range: int = 101) -> int:
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(minium_range, maximum_range, size=(1000))  # загадали список чисел
    count_ls = [tested_func(number, minium_range, maximum_range) for number in random_array]
    score = int(np.mean(count_ls))  # находим среднее количество попыток
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return score


if __name__ == "__main__":
    print(type(score_game(predictor, 1, 101)))
