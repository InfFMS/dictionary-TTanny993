# Напишите программу, которая получает на вход строку и подсчитывает, 
# сколько раз в ней встречается каждый символ (независимо от регистра).
# Результат нужно вывести без фигурных скобок
# Пример. 
# ввод:
# Абракадабра
# Вывод
# а-5 б-2 д-1 к-1 р-2
string = input().lower()
dictionary = dict()
for el in string:
    if el in dictionary:
        dictionary[el] += 1
    else:
        dictionary[el] = 1
for el in dictionary:
    print(el + '-' + str(dictionary[el]), end=' ')
