# 5. Реализовать структуру «Рейтинг»,
# представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
#
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

ratings = [22, 10, 4]
while True:
    rating = input('Введите новое значение рейтинга: ')
    try:
        rating = abs(int(rating))
    except ValueError as e:
        print('Ошибка ввода')
        continue

    if not ratings.count(rating):
        if rating > ratings[0]:
            ratings.insert(0, rating)
        elif rating < ratings[-1]:
            ratings.append(rating)
        else:
            for k, v in enumerate(ratings):
                if rating > v:
                    ratings.insert(k, rating)
                    break
    else:
        new_index = ratings.index(rating) + ratings.count(rating)
        ratings.insert(new_index, rating)

    print(ratings)


