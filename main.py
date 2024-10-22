import timeit



# Количество циклов измерений
number_=1000

# Сортировка пузырьком
def bubble_sort():
    arr = [64, 34, 37, 80, 94, 125, 55, 34, 47, 81, 5, 19, 71, 31, 22, 97, 101, 158, 111, 7, 1, 9, 161, 14, 29, 88]
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            # меняем местами (swap)
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break


execution_time = timeit.timeit(bubble_sort, number=number_)
print(f"Сортировка пузырьком. Среднее время выполнения: {execution_time} секунд")


# Сортировка вставкой
def insertion_sort():
    arr = [64, 34, 37, 80, 94, 125, 55, 34, 47, 81, 5, 19, 71, 31, 22, 97, 101, 158, 111, 7, 1, 9, 161, 14, 29, 88]
    # Проходим по всему массиву, начиная со второго элемента (т.к. первый элемент уже "отсортирован")
    for i in range(1, len(arr)):
        key = arr[i]  # текущий элемент, который нужно вставить в правильное место
        j = i - 1

        # Сдвигаем элементы, которые больше текущего (key), вправо
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Вставляем текущий элемент на правильное место
        arr[j + 1] = key

    return arr


execution_time = timeit.timeit(insertion_sort, number=number_)
print(f"Сортировка вставкой. Среднее время выполнения: {execution_time} секунд")


# Сортировка выбором
def selection_sort():
    arr = [64, 34, 37, 80, 94, 125, 55, 34, 47, 81, 5, 19, 71, 31, 22, 97, 101, 158, 111, 7, 1, 9, 161, 14, 29, 88]
    # Проходим по всем элементам массива
    for i in range(len(arr)):
        # Предполагаем, что текущий элемент — минимальный
        min_idx = i

        # Ищем минимальный элемент в оставшейся части массива
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Меняем найденный минимальный элемент с текущим элементом
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


execution_time = timeit.timeit(selection_sort, number=number_)
print(f"Сортировка выбором. Среднее время выполнения: {execution_time} секунд")


# Стандартная сортировка
def standard_sort():
    arr = [64, 34, 37, 80, 94, 125, 55, 34, 47, 81, 5, 19, 71, 31, 22, 97, 101, 158, 111, 7, 1, 9, 161, 14, 29, 88]
    arr.sort()


execution_time = timeit.timeit(standard_sort, number=number_)
print(f"Стандартная сортировка. Среднее время выполнения: {execution_time} секунд")

