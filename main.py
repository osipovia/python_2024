# Задача 1
# Числа, кратные 3 или 5
# Если выписать все натуральные числа меньше 10, кратные 3 или 5, то получим 3, 5, 6 и 9. Сумма этих чисел равна 23.

# Найдите сумму всех чисел меньше 1000, кратных 3 или 5.

num_f = 3
num_s = 5
num_sum = 1000
numbers = []

while num_sum >= 0:
    if num_sum % num_f == 0 or num_sum % num_s == 0:
        numbers.append(num_sum)
    num_sum = num_sum - 1
numbers = numbers[1:]

print(sum(numbers))


# Задача 2
# Четные числа Фибоначчи
# Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих. Начиная с 1 и 2, первые 10 элементов будут:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.

a, b = 1, 2  # Инициализация первых двух чисел Фибоначчи
sum_fib = 0

while a <= 4000000:
    if a % 2 == 0:
        sum_fib += a
    a, b = b, a + b  # Обновление значений для следующего числа Фибоначчи

print(sum_fib)


# Задача 5
# Наименьшее кратное
# 2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.
#
# Какое самое маленькое число делится нацело на все числа от 1 до 20?

# Функция для нахождения НОД двух чисел
def greatest_common_divider(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Функция для нахождения НОК двух чисел
def smallest_common_multiple(a, b):
    return a * b // greatest_common_divider(a, b)

# Функция для нахождения НОК для всех чисел от 1 до n
def smallest_common_multiple_multiple(n):
    multiple = 1
    for i in range(1, n + 1):
        multiple = smallest_common_multiple(multiple, i)
    return multiple

# Находим НОК для чисел от 1 до 20
result = smallest_common_multiple_multiple(20)
print(result)


