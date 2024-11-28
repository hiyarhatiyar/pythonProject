# Мой код не работает! Только выводит на консоль числа, любые, в том числе не из списка и отрицательные. Не пойму в чем причина?

my_list: list[int] = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
positive_namber = []
index = 0
while index < len(my_list):
    positive_namber = int(input('Введите число: '))
    if my_list[index] < 0:
        break
    elif my_list[index] > 0:
        print(positive_namber)
        continue
    else:
        positive_namber.append(my_list[index])
        index += 1
print(positive_namber)