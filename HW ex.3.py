# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

number = int(input("Введите номер месяца: "))
if number <= 12 and number >= 1:
    month_dict = {1: 'January',
                  2: 'February',
                  3: 'March',
                  4: 'April',
                  5: 'May',
                  6: 'June',
                  7: 'Jule',
                  8: 'August',
                  9: 'September',
                  10: 'October',
                  11: 'November',
                  12: 'December'}
else:
    print("Введи от 1 до 12: ")

if number == 1 or 2 or 12:
    print("зима")
elif number == 3 or 4 or 5:
    print("весна")
elif number == 6 or 7 or 8:
    print("лето")
else:
    print("осень")


#     month_list = list(month_dict.values())
#     for i, el in enumerate(month_list):
#         if i == number-1:
#             print(f"Month from list is {month_list[i]}")
#             break
#     print(f"Month from dict is {month_dict[number]}")
# else:
#     print("You made a mistake")