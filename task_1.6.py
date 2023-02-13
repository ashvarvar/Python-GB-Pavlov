# 1.6 Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
# Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.

a = int(input("Результат спортсмена в первый день: "))
b = int(input("Необходимый спортсмену результат: "))
i = 1
while b >= a:
    a = a + (a * 0.1)
    print("{}-й день: {:.2f}".format(i, a))
    i += 1
# print('на ', i, '-й день спортсмен достиг результата — не менее 3 км')
print('на {}-й день спортсмен достиг результата — не менее 3 км'.format(i))
