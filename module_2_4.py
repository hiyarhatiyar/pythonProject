numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
k = 0
n = 15
# пробегаем все числа от 2 до N
for i in range(2, n+1):
    # пробегаем все числа от 2 до текущего
    for j in range(2, i):
        # ищем количество делителей
        if i % j == 0:
            k = k + 1
    # если делителей нет, добавляем число в список
    if k == 0:
        primes.append(i)
    else:
        k = 0
        # выводим на экран список
print(primes)
print(not_primes)