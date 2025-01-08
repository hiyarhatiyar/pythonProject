calls = 0 # cоздаем глобальную переменную вне функций
def count_calls(): # cоздаем функцию подсчитывающую вызовы
    global calls # применяем оператор global для доступа к переменной calls
    calls+=1 # увеличиваем значение переменной calls
    return calls # возвращаем значение переменной calls

def string_info(string): # cоздаем функцию с аргументом строка
    count_calls() # подсчитываем вызовы функции
    tuple = (len(string),string.upper(),string.lower()) # создаем кортеж
    return tuple # возвращаем кортеж

def is_contains(string , list_to_search): # создаем функцию со строкой и списком в качестве аргументов
    count_calls() # подсчитываем вызовы функции
    for i in range(len(list_to_search)):
        if string.lower() == list_to_search[i].lower():
            return True # возвращает True, когда строка находится в списке
    return False # возвращает False – если отсутствует

# вызов функций с выводом результатов, а также вывод значения переменной calls в консоль
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)