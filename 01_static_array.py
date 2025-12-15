"""
Задание 1. Статический массив

Реализация статического массива с основными операциями.
"""


class StaticArray:
    """
    Статический массив фиксированного размера.
    """
    
    def __init__(self, capacity: int):
        """
        Инициализация массива заданной вместимости.
        
        Временная сложность: O(1)
        """
        self.capacity = capacity
        self.size = 0
        self.data = [None] * capacity
    
    def pushBack(self, value):
        """
        Добавление элемента в конец массива.
        
        Временная сложность: O(1)
        """
        if self.size >= self.capacity:
            raise IndexError("Массив переполнен")
        self.data[self.size] = value
        self.size += 1
    
    def pushFront(self, value):
        """
        Добавление элемента в начало массива.
        
        Временная сложность: O(n) - требуется сдвиг всех элементов вправо
        """
        if self.size >= self.capacity:
            raise IndexError("Массив переполнен")
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
            raise IndexError("Массив переполнен")
        
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
        Поиск элемента по значению. Возвращает индекс или -1.
        
        Временная сложность: O(n) - в худшем случае просматриваем все элементы
        """
        for i in range(self.size):
            if self.data[i] == value:
                return i
        return -1
    
    def __str__(self):
        return str(self.data[:self.size])
    
    def __len__(self):
        return self.size


if __name__ == "__main__":
    arr = StaticArray(10)
    
    print("=== Тестирование статического массива ===")
    
    arr.pushBack(1)
    arr.pushBack(2)
    arr.pushBack(3)
    print(f"После pushBack(1,2,3): {arr}")
    
    arr.pushFront(0)
    print(f"После pushFront(0): {arr}")
    
    arr.insert(2, 99)
    print(f"После insert(2, 99): {arr}")
    
    idx = arr.find(99)
    print(f"find(99) вернул индекс: {idx}")
    
    arr.remove(2)
    print(f"После remove(2): {arr}")
    
    print(f"Размер массива: {len(arr)}")


