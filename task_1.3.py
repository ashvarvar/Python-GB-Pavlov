# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
# nn = n*10 + n
# nnn = n*100 + n*10 + n
# n + nn + nnn = n+(n*10)+n + (n*100)+(n*10)+n = n*3 + 2(n*10) + 100*n = 123n

numbers = int(input("Введите число: "))
answer = 123 * numbers
print(answer)

