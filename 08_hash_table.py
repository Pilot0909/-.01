"""
Задание 8. Своя хэш-таблица

Реализация хэш-таблицы с методом разрешения коллизий (цепочки).
"""


class HashTable:
    """
    Хэш-таблица с методом разрешения коллизий через цепочки.
    """
    
    def __init__(self, capacity: int = 16):
        """
        Инициализация хэш-таблицы.
        
        Args:
            capacity: Начальная вместимость таблицы
        """
        self.capacity = capacity
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]
    
    def _hash(self, key: str) -> int:
        """
        Хэш-функция для строк (djb2 алгоритм).
        
        Временная сложность: O(n), где n - длина строки
        
        Args:
            key: Ключ (строка)
            
        Returns:
            Хэш-значение
        """
        hash_value = 5381
        for char in key:
            hash_value = ((hash_value << 5) + hash_value) + ord(char)
        return hash_value % self.capacity
    
    def put(self, key: str, value):
        """
        Добавление или обновление пары ключ-значение.
        
        Временная сложность: O(1) в среднем случае, O(n) в худшем случае
        (если все ключи попадают в одну корзину)
        
        Args:
            key: Ключ
            value: Значение
        """
        index = self._hash(key)
        bucket = self.buckets[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        
        bucket.append((key, value))
        self.size += 1
        
        if self.size > self.capacity * 0.75:
            self._resize()
    
    def get(self, key: str):
        """
        Получение значения по ключу.
        
        Временная сложность: O(1) в среднем случае, O(n) в худшем случае
        
        Args:
            key: Ключ
            
        Returns:
            Значение или None, если ключ не найден
        """
        index = self._hash(key)
        bucket = self.buckets[index]
        
        for k, v in bucket:
            if k == key:
                return v
        
        return None
    
    def remove(self, key: str) -> bool:
        """
        Удаление пары ключ-значение.
        
        Временная сложность: O(1) в среднем случае, O(n) в худшем случае
        
        Args:
            key: Ключ
            
        Returns:
            True если ключ был удален, False если не найден
        """
        index = self._hash(key)
        bucket = self.buckets[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self.size -= 1
                return True
        
        return False
    
    def _resize(self):
        """
        Увеличение размера таблицы в 2 раза и перехеширование всех элементов.
        
        Временная сложность: O(n), где n - количество элементов
        """
        old_buckets = self.buckets
        self.capacity *= 2
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0
        
        for bucket in old_buckets:
            for key, value in bucket:
                self.put(key, value)
    
    def visualize(self):
        """
        Визуализация состояния таблицы.
        """
        print(f"\n=== Состояние хэш-таблицы (размер: {self.size}, вместимость: {self.capacity}) ===")
        for i, bucket in enumerate(self.buckets):
            if bucket:
                items = [f"{k}:{v}" for k, v in bucket]
                print(f"Корзина {i:2d}: {' -> '.join(items)}")
        print()


if __name__ == "__main__":
    ht = HashTable(capacity=8)
    
    print("=== Тестирование хэш-таблицы ===")
    
    ht.put("apple", 1)
    ht.put("banana", 2)
    ht.put("cherry", 3)
    ht.put("date", 4)
    ht.put("elderberry", 5)
    
    ht.visualize()
    
    print(f"get('apple') = {ht.get('apple')}")
    print(f"get('banana') = {ht.get('banana')}")
    print(f"get('nonexistent') = {ht.get('nonexistent')}")
    
    ht.put("apple", 10)
    print(f"\nПосле put('apple', 10):")
    print(f"get('apple') = {ht.get('apple')}")
    
    ht.remove("banana")
    print(f"\nПосле remove('banana'):")
    ht.visualize()
    
    print("Добавление больше элементов...")
    for i in range(10):
        ht.put(f"key{i}", i)
    
    ht.visualize()


