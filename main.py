import timeit


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


execution_time = timeit.timeit(bubble_sort, number=200)
print(f"Среднее время выполнения: {execution_time} секунд")


# Стандартная сортировка
def standard_sort():
    arr = [64, 34, 37, 80, 94, 125, 55, 34, 47, 81, 5, 19, 71, 31, 22, 97, 101, 158, 111, 7, 1, 9, 161, 14, 29, 88]
    arr.sort()


execution_time = timeit.timeit(standard_sort, number=200)
print(f"Среднее время выполнения: {execution_time} секунд")

