"""
Задание 2. Динамический массив

Реализация динамического массива с автоматическим расширением (стратегия ×2).
"""

import time
import importlib.util
import sys

spec = importlib.util.spec_from_file_location("static_array", "01_static_array.py")
static_array_module = importlib.util.module_from_spec(spec)
sys.modules["static_array"] = static_array_module
spec.loader.exec_module(static_array_module)
StaticArray = static_array_module.StaticArray


class DynamicArray:
    """
    Динамический массив с автоматическим расширением.
    Стратегия расширения: увеличение размера в 2 раза при переполнении.
    """
    
    def __init__(self, initial_capacity: int = 4):
        """
        Инициализация динамического массива.
        
        Временная сложность: O(1)
        """
        self.capacity = initial_capacity
        self.size = 0
        self.data = [None] * initial_capacity
    
    def _resize(self):
        """
        Увеличение размера массива в 2 раза.
        
        Временная сложность: O(n) - копирование всех элементов
        """
        old_capacity = self.capacity
        self.capacity *= 2
        new_data = [None] * self.capacity
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data
    
    def pushBack(self, value):
        """
        Добавление элемента в конец массива.
        
        Амортизированная временная сложность: O(1)
        В худшем случае (при ресайзе): O(n)
        """
        if self.size >= self.capacity:
            self._resize()
        self.data[self.size] = value
        self.size += 1
    
    def pushFront(self, value):
        """
        Добавление элемента в начало массива.
        
        Временная сложность: O(n) - требуется сдвиг всех элементов
        """
        if self.size >= self.capacity:
            self._resize()
        for i in range(self.size, 0, -1):
            self.data[i] = self.data[i - 1]
        self.data[0] = value
        self.size += 1
    
    def insert(self, index: int, value):
        """
        Вставка элемента по индексу.
        
        Временная сложность: O(n) - требуется сдвиг элементов
        """
        if index < 0 or index > self.size:
            raise IndexError("Индекс вне допустимого диапазона")
        
        if self.size >= self.capacity:
            self._resize()
        
        for i in range(self.size, index, -1):
            self.data[i] = self.data[i - 1]
        self.data[index] = value
        self.size += 1
    
    def remove(self, index: int):
        """
        Удаление элемента по индексу.
        
        Временная сложность: O(n) - требуется сдвиг элементов
        """
        if index < 0 or index >= self.size:
            raise IndexError("Индекс вне допустимого диапазона")
        
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]
        self.data[self.size - 1] = None
        self.size -= 1
    
    def find(self, value):
        """
        Поиск элемента по значению.
        
        Временная сложность: O(n)
        """
        for i in range(self.size):
            if self.data[i] == value:
                return i
        return -1
    
    def __str__(self):
        return str(self.data[:self.size])
    
    def __len__(self):
        return self.size


def compare_insertion_time():
    """
    Сравнение времени вставки 100000 элементов в статический и динамический массивы.
    """
    n = 100000
    
    print("=== Сравнение времени вставки ===")
    
    start_time = time.time()
    static_arr = StaticArray(n)
    for i in range(n):
        static_arr.pushBack(i)
    static_time = time.time() - start_time
    print(f"Статический массив (pushBack {n} элементов): {static_time:.4f} сек")
    
    start_time = time.time()
    dynamic_arr = DynamicArray()
    for i in range(n):
        dynamic_arr.pushBack(i)
    dynamic_time = time.time() - start_time
    print(f"Динамический массив (pushBack {n} элементов): {dynamic_time:.4f} сек")
    
    print(f"\nОтношение времени (динамический/статический): {dynamic_time/static_time:.2f}")
    print(f"Финальная вместимость динамического массива: {dynamic_arr.capacity}")
    print(f"Финальный размер: {dynamic_arr.size}")


if __name__ == "__main__":
    arr = DynamicArray()
    
    print("=== Тестирование динамического массива ===")
    for i in range(10):
        arr.pushBack(i)
        print(f"После pushBack({i}): размер={len(arr)}, вместимость={arr.capacity}")
    
    print(f"\nМассив: {arr}")
    
    print("\n")
    compare_insertion_time()

