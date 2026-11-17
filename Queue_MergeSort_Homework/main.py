import time
import random


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if self.is_empty():
            return None
        return self.items[0]


print("ЗАДАНИЕ 1: РАБОТА С ОЧЕРЕДЬЮ")

queue = Queue()

queue.enqueue("Задача 1")
queue.enqueue("Задача 2")
queue.enqueue("Задача 3")

print("Первый элемент:", queue.peek())
print("Удаленный элемент:", queue.dequeue())
print("Очередь пуста?", queue.is_empty())
print()


print("ЗАДАНИЕ 2: ОБРАБОТКА ЗАДАЧ")

tasks = Queue()

tasks.enqueue(("Задача 1", 3))
tasks.enqueue(("Задача 2", 5))
tasks.enqueue(("Задача 3", 2))
tasks.enqueue(("Задача 4", 4))

current_time = 0

while not tasks.is_empty():
    task_name, duration = tasks.dequeue()
    current_time += duration

    print(
        task_name,
        "- время выполнения:",
        duration,
        "мин.",
        "| Завершение:",
        current_time,
        "мин."
    )

print()


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2

    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


print("ЗАДАНИЕ 3: СОРТИРОВКА СЛИЯНИЕМ")

numbers = [38, 12, 27, 43, 9, 31, 18, 25]

print("Исходный список:", numbers)
print("Отсортированный список:", merge_sort(numbers))
print()


def bubble_sort(arr):
    arr = arr.copy()

    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


print("ЗАДАНИЕ 4: СРАВНЕНИЕ СОРТИРОВОК")

sizes = [10, 100, 1000]

for size in sizes:
    data = [random.randint(1, 10000) for _ in range(size)]

    start = time.perf_counter()
    merge_sort(data)
    merge_time = time.perf_counter() - start

    start = time.perf_counter()
    bubble_sort(data)
    bubble_time = time.perf_counter() - start

    print("Количество элементов:", size)
    print("Merge Sort:", round(merge_time, 6), "сек.")
    print("Bubble Sort:", round(bubble_time, 6), "сек.")
    print()
