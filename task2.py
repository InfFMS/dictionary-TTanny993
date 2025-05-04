# Напишите программу, которая получает на вход строку чисел, разделенных пробелами, и формирует словарь,
#  в котором ключами служат числа, а значениями – слово "четное" или "нечетное".
string = list(map(int, input().split()))
dictionary = dict()
for el in string:
    if el % 2 == 0:
        dictionary[el] = 'четное'
    else:
        dictionary[el] = 'нечетное'
print(dictionary)
