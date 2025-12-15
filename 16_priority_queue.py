"""
Задание 16. Приоритетная очередь

Реализация приоритетной очереди на основе кучи.
Применение к задачам планирования задач и поиска k минимальных элементов.
"""

import importlib.util
import sys

spec = importlib.util.spec_from_file_location("heap_module", "15_heap.py")
heap_module = importlib.util.module_from_spec(spec)
sys.modules["heap_module"] = heap_module
spec.loader.exec_module(heap_module)
MinHeap = heap_module.MinHeap


class PriorityQueue:
    """
    Приоритетная очередь на основе мин-кучи.
    
    Элемент с минимальным приоритетом извлекается первым.
    """
    
    def __init__(self):
        """
        Инициализация приоритетной очереди.
        
        Временная сложность: O(1)
        """
        self.heap = MinHeap()
        self.counter = 0
    
    def push(self, value, priority: int):
        """
        Добавление элемента с приоритетом.
        
        Временная сложность: O(log n)
        
        Args:
            value: Значение элемента
            priority: Приоритет (меньше = выше приоритет)
        """
        self.heap.insert((priority, self.counter, value))
        self.counter += 1
    
    def pop(self):
        """
        Извлечение элемента с минимальным приоритетом.
        
        Временная сложность: O(log n)
        
        Returns:
            Значение элемента с минимальным приоритетом
            
        Raises:
            IndexError: Если очередь пуста
        """
        priority, counter, value = self.heap.extract_min()
        return value
    
    def peek(self):
        """
        Просмотр элемента с минимальным приоритетом без извлечения.
        
        Временная сложность: O(1)
        """
        priority, counter, value = self.heap.peek()
        return value
    
    def isEmpty(self):
        """
        Проверка на пустоту.
        
        Временная сложность: O(1)
        """
        return len(self.heap) == 0
    
    def __len__(self):
        return len(self.heap)


class Task:
    """
    Задача для планирования.
    """
    
    def __init__(self, name: str, priority: int, duration: int):
        """
        Args:
            name: Название задачи
            priority: Приоритет (меньше = выше приоритет)
            duration: Длительность выполнения
        """
        self.name = name
        self.priority = priority
        self.duration = duration
    
    def __str__(self):
        return f"{self.name} (приоритет: {self.priority}, длительность: {self.duration})"


def task_scheduling(tasks: list) -> list:
    """
    Планирование задач с использованием приоритетной очереди.
    
    Задачи выполняются в порядке приоритета (сначала самые важные).
    
    Временная сложность: O(n log n), где n - количество задач
    
    Args:
        tasks: Список задач (Task)
        
    Returns:
        Список задач в порядке выполнения
    """
    pq = PriorityQueue()
    
    for task in tasks:
        pq.push(task, task.priority)
    
    schedule = []
    while not pq.isEmpty():
        schedule.append(pq.pop())
    
    return schedule


def find_k_minimum(array: list, k: int) -> list:
    """
    Поиск k минимальных элементов массива с использованием приоритетной очереди.
    
    Временная сложность: O(n log k), где n - размер массива
    Пространственная сложность: O(k)
    
    Args:
        array: Массив чисел
        k: Количество минимальных элементов для поиска
        
    Returns:
        Список k минимальных элементов
    """
    if k <= 0:
        return []
    
    if k >= len(array):
        return sorted(array)
    
    pq = PriorityQueue()
    
    for value in array:
        pq.push(value, value)
    
    result = []
    for _ in range(k):
        result.append(pq.pop())
    
    return result


if __name__ == "__main__":
    print("=== Тестирование приоритетной очереди ===")
    
    pq = PriorityQueue()
    
    pq.push("задача1", 3)
    pq.push("задача2", 1)
    pq.push("задача3", 2)
    pq.push("задача4", 5)
    pq.push("задача5", 1)
    
    print("\nЭлементы добавлены в очередь:")
    print("  задача1 (приоритет 3)")
    print("  задача2 (приоритет 1)")
    print("  задача3 (приоритет 2)")
    print("  задача4 (приоритет 5)")
    print("  задача5 (приоритет 1)")
    
    print("\nИзвлечение элементов:")
    while not pq.isEmpty():
        print(f"  pop() = {pq.pop()}")
    
    print("\n=== Планирование задач ===")
    
    tasks = [
        Task("Написать код", 2, 120),
        Task("Исправить баги", 1, 60),
        Task("Написать документацию", 3, 90),
        Task("Провести тестирование", 2, 45),
        Task("Критический баг", 0, 30),
        Task("Оптимизация", 4, 180)
    ]
    
    print("\nИсходные задачи:")
    for task in tasks:
        print(f"  {task}")
    
    schedule = task_scheduling(tasks)
    
    print("\nПлан выполнения (по приоритету):")
    total_time = 0
    for i, task in enumerate(schedule, 1):
        total_time += task.duration
        print(f"  {i}. {task.name} (приоритет: {task.priority}, время: {task.duration} мин)")
    
    print(f"\nОбщее время выполнения: {total_time} минут")
    
    print("\n=== Поиск k минимальных элементов ===")
    
    array = [64, 34, 25, 12, 22, 11, 90, 5, 77, 88, 1, 99, 3, 45]
    k = 5
    
    print(f"\nИсходный массив: {array}")
    print(f"k = {k}")
    
    k_min = find_k_minimum(array, k)
    print(f"\n{k} минимальных элементов: {k_min}")
    print(f"Отсортированный массив (для проверки): {sorted(array)[:k]}")
    
    print("\n=== Дополнительные тесты ===")
    
    test_cases = [
        ([1, 2, 3, 4, 5], 3),
        ([5, 4, 3, 2, 1], 3),
        ([3, 1, 4, 1, 5, 9, 2, 6], 4),
        ([10], 1),
        ([1, 2, 3], 5)  # k больше размера массива
    ]
    
    for arr, k_val in test_cases:
        result = find_k_minimum(arr, k_val)
        print(f"\nМассив: {arr}, k={k_val}")
        print(f"Результат: {result}")

