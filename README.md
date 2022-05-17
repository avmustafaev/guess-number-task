# Проект 0. Угадай число

## Оглавление  
[1. Описание проекта](README.md#Описание-проекта)  
[2. Какой кейс решаем?](README.md#Какой-кейс-решаем)  
[3. Краткая информация о данных](README.md#Краткая-информация-о-данных)  
[4. Этапы работы над проектом](README.md#Этапы-работы-над-проектом)  
[5. Результат](README.md#Результаты)    
[6. Выводы](README.md#Выводы) 

### Описание проекта    
Угадать загаданное компьютером число за минимальное число попыток.

:arrow_up: [к оглавлению](README.md#Оглавление)


### Какой кейс решаем?    
Нужно написать программу, которая угадывает число за минимальное число попыток

**Условия соревнования:**  
- Компьютер загадывает целое число от 0 до 100, и нам его нужно угадать. Под «угадать», подразумевается «написать программу, которая угадывает число».
- Алгоритм учитывает информацию о том, больше ли случайное число или меньше нужного нам.

**Метрика качества**     
Результаты оцениваются по среднему количеству попыток при 1000 повторений

**Что практикуем**     
Учимся писать хороший код на python

### Этапы работы над проектом  
Сделал функцию `number_predict()`, угадывает число и возвращает число попыток.

Вторая функция `score_game()`, генерирует массив из 1000 чисел, передаёт первой функции и считает среднее число попыток.

На вход можно подавать минимальное и максимальное значение диапазона в котором будет генерироваться случайное число.

Сделал Jupiter Notebook, в котором наглядно показана работа функций.

:arrow_up: [к оглавлению](README.md#Оглавление)


### Результаты:  
Результат достигнут. Функция угадывает число за минимальное количество попыток.

Код оформлен в соответствии с PEP8.

Для возможности воспроизводимости кода создан файл requirements.txt в котором указаны необходимые библиотеки, которые легко установить командой:
```
pip install -r requirements.txt
```

:arrow_up: [к оглавлению](README.md#Оглавление)


### Выводы:  
Полезная штука Git! и конечно становится понятно насколько важен PEP8 праивльное именование переменных, функций и комментирование своего и конечно правильно документированные проекты.

:arrow_up: [к оглавлению](README.md#Оглавление)

