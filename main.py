def remove_even_after_max(A):
    # Находим индекс максимального элемента
    max_index = A.index(max(A))

    # Оставляем только те элементы, которые идут до максимального и после максимального исключаем чётные
    result = A[:max_index + 1] + [x for x in A[max_index + 1:] if x % 2 != 0]

    return result


# Ввод данных
A = list(map(int, input("Введите элементы списка через пробел: ").split()))

# Обработка данных
result = remove_even_after_max(A)

# Вывод результата
print("Результат:", result)
print("HELL")
#HELLO
