# Напишите программу, которая получает на вход две строки, и формирует из них словарь. 
# Ключами служат слова из первой строки, значениями – целые числа из второй.
# Пример ввода
# яблоки сливы груши персики манго киви апельсины
# 34 56 23 89 55 32 11
string1 = input().split()
string2 = input().split()
dictionary = dict()
for i in range(len(string1)):
    dictionary[string1[i]] = int(string2[i])
print(dictionary)
