
# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
input_data = int(input('Введите произвольное целое число от 0 до 10:'))
i = 0
while i <= input_data:
    print(i)
    i = i + 1
print('Выполнение программы завершено')


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.

a = input("Введите значение переменной a: ")
b = input("Введите значение переменной b: ")
print(a, b)
a, b = b, a
print(a, b)
print('Выполнение программы завершено')


# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

age = int(input("Введите ваш возраст: "))
if age >= 18:
    print("Доступ разрешен")
else:
    print("Извините, пользование данным ресурсом только с 18 лет")
print('Выполнение программы завершено')