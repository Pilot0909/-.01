"""
Задание 15. Куча

Реализация бинарной мин-кучи с операциями вставки, извлечения минимума
и построения кучи из массива.
"""


class MinHeap:
    """
    Бинарная мин-куча.
    
    Свойства кучи:
    - Полное бинарное дерево
    - Значение в узле <= значениям в потомках (min-heap)
    """
    
    def __init__(self):
        """
        Инициализация пустой кучи.
        
        Временная сложность: O(1)
        """
        self.heap = []
    
    def _parent(self, index: int) -> int:
        """Индекс родителя узла."""
        return (index - 1) // 2
    
    def _left_child(self, index: int) -> int:
        """Индекс левого потомка узла."""
        return 2 * index + 1
    
    def _right_child(self, index: int) -> int:
        """Индекс правого потомка узла."""
        return 2 * index + 2
    
    def _swap(self, i: int, j: int):
        """Обмен элементов по индексам."""
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def _heapify_up(self, index: int):
        """
        Просеивание вверх (для восстановления свойства кучи после вставки).
        
        Временная сложность: O(log n)
        """
        while index > 0:
            parent = self._parent(index)
            if self.heap[index] < self.heap[parent]:
                self._swap(index, parent)
                index = parent
            else:
                break
    
    def _heapify_down(self, index: int):
        """
        Просеивание вниз (для восстановления свойства кучи после удаления).
        
        Временная сложность: O(log n)
        """
        while True:
            smallest = index
            left = self._left_child(index)
            right = self._right_child(index)
            
            if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
                smallest = left
            
            if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
                smallest = right
            
            if smallest != index:
                self._swap(index, smallest)
                index = smallest
            else:
                break
    
    def insert(self, value):
        """
        Вставка элемента в кучу.
        
        Временная сложность: O(log n)
        
        Args:
            value: Значение для вставки
        """
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)
    
    def extract_min(self):
        """
        Извлечение минимального элемента из кучи.
        
        Временная сложность: O(log n)
        
        Returns:
            Минимальный элемент
            
        Raises:
            IndexError: Если куча пуста
        """
        if len(self.heap) == 0:
            raise IndexError("Куча пуста")
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        
        return min_value
    
    def peek(self):
        """
        Просмотр минимального элемента без извлечения.
        
        Временная сложность: O(1)
        """
        if len(self.heap) == 0:
            raise IndexError("Куча пуста")
        return self.heap[0]
    
    def build_heap(self, array: list):
        """
        Построение кучи из массива (алгоритм Флойда).
        
        Временная сложность: O(n) - линейное время!
        
        Args:
            array: Массив для построения кучи
        """
        self.heap = array.copy()
        
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._heapify_down(i)
    
    def is_valid_heap(self) -> bool:
        """
        Проверка корректности свойств кучи.
        
        Временная сложность: O(n)
        
        Returns:
            True если куча корректна, False иначе
        """
        for i in range(len(self.heap)):
            left = self._left_child(i)
            right = self._right_child(i)
            
            if left < len(self.heap) and self.heap[i] > self.heap[left]:
                return False
            
            if right < len(self.heap) and self.heap[i] > self.heap[right]:
                return False
        
        return True
    
    def __len__(self):
        return len(self.heap)
    
    def __str__(self):
        return str(self.heap)


if __name__ == "__main__":
    print("=== Тестирование бинарной мин-кучи ===")
    
    heap = MinHeap()
    
    print("\n1. Вставка элементов:")
    values = [5, 3, 8, 1, 9, 2, 7, 4, 6]
    for value in values:
        heap.insert(value)
        print(f"  После insert({value}): {heap}")
        print(f"  Куча корректна: {heap.is_valid_heap()}")
    
    print(f"\nИтоговая куча: {heap}")
    print(f"Куча корректна: {heap.is_valid_heap()}")
    
    print("\n2. Извлечение минимума:")
    while len(heap) > 0:
        min_val = heap.extract_min()
        print(f"  extract_min() = {min_val}, куча: {heap}")
        if len(heap) > 0:
            print(f"  Куча корректна: {heap.is_valid_heap()}")
    
    print("\n3. Построение кучи из массива:")
    array = [9, 5, 2, 7, 1, 8, 3, 6, 4]
    print(f"  Исходный массив: {array}")
    heap.build_heap(array)
    print(f"  Куча после build_heap: {heap}")
    print(f"  Куча корректна: {heap.is_valid_heap()}")
    
    print("\n4. Проверка корректности после операций:")
    test_heap = MinHeap()
    test_heap.insert(10)
    print(f"  После insert(10): корректна = {test_heap.is_valid_heap()}")
    test_heap.insert(5)
    print(f"  После insert(5): корректна = {test_heap.is_valid_heap()}")
    test_heap.insert(15)
    print(f"  После insert(15): корректна = {test_heap.is_valid_heap()}")
    test_heap.insert(3)
    print(f"  После insert(3): корректна = {test_heap.is_valid_heap()}")
    test_heap.extract_min()
    print(f"  После extract_min(): корректна = {test_heap.is_valid_heap()}")


