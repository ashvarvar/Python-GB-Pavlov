# 1.1 Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные,
# выведите  на экран.

name = 'Максим'
surname = 'Павлов'
age = 39
print('Привет!', name, surname, age, 'лет')

name = input("Введите Ваше имя: ")
surname = input("Введите Вашу фамилию: ")
age = int(input("Введите Ваш возраст: "))
print('Привет!', name, surname, age, 'лет')


number_1 = int(input("Введите первое число: "))
number_2 = int(input("Введите второе число: "))
number_3 = int(input("Введите третье число: "))
sum_numbers = number_1 + number_2 + number_3
print("Сумма чисел равна: ", sum_numbers)
