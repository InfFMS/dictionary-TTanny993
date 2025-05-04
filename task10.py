# Нужно считать файл parameters.txt. 
# Это файл с настройками расчетной модели.
# Формат в файле следующий первое слово в строке - это ключ, 
# потом после пробела - значение (может быть строкой, числом, или набором чисел),
# все, что после символа "//" это комментарий  должно игнорироваться.
# Реализуйте считывание значений из файла и запись этих значений в словарь.
with open('parameters.txt', 'r') as f:
    dictionary = dict()
    for line in f.readlines():
        if '//' in line:
            line = line[:line.find('//')]
        line = line.replace('\t', '')
        line = line.replace('\n', '')
        key = line[:line.find(' ')]
        value = line[line.find(' ') + 1:]
        if len(key) > 0:
            dictionary[key] = value
    print(dictionary)
