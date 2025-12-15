"""
Задание 3. Односвязный список

Реализация односвязного списка с основными операциями.
"""


class ListNode:
    """Узел односвязного списка."""
    
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    """
    Односвязный список.
    """
    
    def __init__(self):
        """
        Инициализация пустого списка.
        
        Временная сложность: O(1)
        """
        self.head = None
        self.size = 0
    
    def pushFront(self, value):
        """
        Вставка элемента в начало списка.
        
        Временная сложность: O(1)
        """
        new_node = ListNode(value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def pushBack(self, value):
        """
        Вставка элемента в конец списка.
        
        Временная сложность: O(n) - требуется пройти до конца списка
        """
        new_node = ListNode(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.size += 1
    
    def remove(self, value):
        """
        Удаление первого узла с заданным значением.
        
        Временная сложность: O(n) - в худшем случае просматриваем весь список
        """
        if self.head is None:
            return False
        
        if self.head.value == value:
            self.head = self.head.next
            self.size -= 1
            return True
        
        current = self.head
        while current.next is not None:
            if current.next.value == value:
                current.next = current.next.next
                self.size -= 1
                return True
            current = current.next
        
        return False
    
    def find(self, value):
        """
        Поиск узла по значению. Возвращает узел или None.
        
        Временная сложность: O(n) - в худшем случае просматриваем весь список
        """
        current = self.head
        while current is not None:
            if current.value == value:
                return current
            current = current.next
        return None
    
    def reverse(self):
        """
        Разворот списка in-place.
        
        Временная сложность: O(n) - проходим по всем узлам один раз
        Пространственная сложность: O(1) - используем только константную память
        """
        prev = None
        current = self.head
        
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        self.head = prev
    
    def __str__(self):
        """Строковое представление списка."""
        if self.head is None:
            return "[]"
        
        result = []
        current = self.head
        while current is not None:
            result.append(str(current.value))
            current = current.next
        return " -> ".join(result) + " -> None"
    
    def __len__(self):
        return self.size


def compare_with_array():
    """
    Сравнение операций вставки/удаления списка с массивом.
    """
    import time
    import importlib.util
    import sys
    
    spec = importlib.util.spec_from_file_location("static_array", "01_static_array.py")
    static_array_module = importlib.util.module_from_spec(spec)
    sys.modules["static_array"] = static_array_module
    spec.loader.exec_module(static_array_module)
    StaticArray = static_array_module.StaticArray
    
    n = 10000
    
    print("=== Сравнение односвязного списка и массива ===")
    
    print("\n1. Вставка в начало:")
    
    start = time.time()
    arr = StaticArray(n)
    for i in range(n):
        arr.pushFront(i)
    array_time = time.time() - start
    print(f"   Массив: {array_time:.4f} сек")
    
    start = time.time()
    lst = SinglyLinkedList()
    for i in range(n):
        lst.pushFront(i)
    list_time = time.time() - start
    print(f"   Список: {list_time:.4f} сек")
    print(f"   Список быстрее в {array_time/list_time:.2f} раз")
    
    print("\n2. Вставка в конец:")
    
    start = time.time()
    arr = StaticArray(n)
    for i in range(n):
        arr.pushBack(i)
    array_time = time.time() - start
    print(f"   Массив: {array_time:.4f} сек")
    
    start = time.time()
    lst = SinglyLinkedList()
    for i in range(n):
        lst.pushBack(i)
    list_time = time.time() - start
    print(f"   Список: {list_time:.4f} сек")
    print(f"   Массив быстрее в {list_time/array_time:.2f} раз")
    
    print("\n3. Удаление из начала:")
    
    arr = StaticArray(n)
    for i in range(n):
        arr.pushBack(i)
    start = time.time()
    for i in range(min(1000, n)):
        arr.remove(0)
    array_time = time.time() - start
    print(f"   Массив (удаление первого элемента): {array_time:.4f} сек")
    
    lst = SinglyLinkedList()
    for i in range(n):
        lst.pushBack(i)
    start = time.time()
    for i in range(min(1000, n)):
        lst.remove(i)
    list_time = time.time() - start
    print(f"   Список (удаление по значению): {list_time:.4f} сек")


if __name__ == "__main__":
    lst = SinglyLinkedList()
    
    print("=== Тестирование односвязного списка ===")
    
    lst.pushBack(1)
    lst.pushBack(2)
    lst.pushBack(3)
    print(f"После pushBack(1,2,3): {lst}")
    
    lst.pushFront(0)
    print(f"После pushFront(0): {lst}")
    
    node = lst.find(2)
    print(f"find(2) нашел узел со значением: {node.value if node else None}")
    
    lst.remove(2)
    print(f"После remove(2): {lst}")
    
    lst.reverse()
    print(f"После reverse(): {lst}")
    
    print(f"\nРазмер списка: {len(lst)}")
    
    compare_with_array()

