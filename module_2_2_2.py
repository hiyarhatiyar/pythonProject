# Все ли равны?
# N1
first = 1,2,3
second = 4,5,6
third = 7,8,9
if first == second and second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)

# 2
first = 42
second = 69
third = 42
if first == second and second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)

# 3
first = 1,2,3
second = 4,5,6
third = 7,8,9
if not first == second and not second == third:
    print(0)


    print('Введите поочерёдно три целых числа')
    first = int(input("Введите первое число: "))
    second = int(input("Введите второе число: "))
    third = int(input("Введите третье число: "))

    if first == second == third:
        print("3")
    elif first == second or first == third or second == third:
        print("2")
    else:
        print("0")