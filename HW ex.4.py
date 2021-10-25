# 4. Пользователь вводит строку из нескольких слов,
# разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

my_str = input("введите строку ")
word = []
num = 1
for element in range(my_str.count(' ') + 1):
    word = my_str.split()
    if len(str(word)) <= 10:
        print(f" {num} {word [element]}")
        num += 1
    else:
        print(f" {num} {word [element] [0:10]}")
        num += 1


