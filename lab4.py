# Вводится строка, включающая строчные и прописные буквы. Требуется вывести ту же строку в одном регистре, который зависит от того, каких букв больше. При равном количестве преобразовать в нижний регистр. Например, вводится строка "HeLLo World", она должна быть преобразована в "hello world", потому что в исходной строке малых букв больше. В коде используйте цикл for, строковые методы upper() (преобразование к верхнему регистру) и lower() (преобразование к нижнему регистру), а также методы isupper() и islower(), проверяющие регистр строки или символа.
# print('Введите слово')
# string = str(input())
# upper = 0
# lower = 0
# for i in string:
#     if i.isupper():
#         upper += 1
#     elif i.islower():
#         lower += 1
# if upper > lower:
#     print(string.upper())
# else:
#     print(string.lower())

#	Строковый метод isdigit() проверяет, состоит ли строка только из цифр. Напишите программу, которая запрашивает с ввода два целых числа и выводит их сумму. В случае некорректного ввода программа не должна завершаться с ошибкой, а должна продолжать запрашивать числа. Обработчик исключений try-except использовать нельзя.
print('Введите первое число')
a = input()
print('Введите второе число')
b = input()
while not(a.isdigit() and b.isdigit()):
    print('Прошу введите число')
    a, b = input(), input()
print(int(a) + int(b))