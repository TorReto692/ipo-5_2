spis1 = input("Введите первую строку:")  # Запрашивает у пользователя ввод первой строки
spis2 = input("Введите вторую строку:")  # Запрашивает у пользователя ввод второй строки

sort_spis1 = sorted(spis1.lower())  # Сортирует символы первой строки в алфавитном порядке, игнорируя регистр
sort_spis2 = sorted(spis2.lower())  # Сортирует символы второй строки в алфавитном порядке, игнорируя регистр

if sort_spis1 == sort_spis2:  # Сравнивает отсортированные списки символов
    print('Списки анаграммы')  # Выводит сообщение, если списки анаграммы
else:
    print('Списки не анаграммы')  # Выводит сообщение, если списки не анаграммы