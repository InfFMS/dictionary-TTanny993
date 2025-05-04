# Даны два словаря. Напишите программу, которая объединит эти словари. 
# Если ключи встречаются в обоих исходных словарях, значения, 
# которые хранятся по этим ключам складываются.
# Пример:

# Первый словарь: {'a': 100, 'b': 200, 'c':300}
# Второй словарь: {'a': 300, 'b': 200, 'd':400}
# Результат: {'a': 400, 'b': 400, 'd': 400, 'c': 300}
dictionary1 = {'a': 100, 'b': 200, 'c': 300}
dictionary2 = {'a': 300, 'b': 200, 'd': 400}
dictionary = dict()
for key in list(dictionary1.keys()) + list(dictionary2.keys()):
    if key in dictionary2 and key in dictionary1:
        dictionary[key] = dictionary1[key] + dictionary2[key]
    elif key in dictionary2:
        dictionary[key] = dictionary2[key]
    else:
        dictionary[key] = dictionary1[key]
print(dictionary)
