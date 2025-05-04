# Представьте, что вы шпионы)
# Придумайте шифр, в котором буквы заменяются на какие-то символы
# и реализуйте шифроватор и дешифроватор
def code(string):
    result = ''
    for el in string:
        result += chr(ord(el) + 52)
    return result


def decode(string):
    result = ''
    for el in string:
        result += chr(ord(el) - 52)
    return result


print(code('abcdefg'))
print(decode(''))
