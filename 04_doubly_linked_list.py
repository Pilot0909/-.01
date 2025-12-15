"""
Задание 4. Двусвязный список

Реализация двусвязного списка с итератором.
"""


class DoublyListNode:
    """Узел двусвязного списка."""
    
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    """
    Двусвязный список.
    """
    
    def __init__(self):
        """
        Инициализация пустого списка.
        
        Временная сложность: O(1)
        """
        self.head = None
        self.tail = None
        self.size = 0
    
    def pushBack(self, value):
        """
        Вставка элемента в конец списка.
        
        Временная сложность: O(1)
        """
        new_node = DoublyListNode(value)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
    
    def pushFront(self, value):
        """
        Вставка элемента в начало списка.
        
        Временная сложность: O(1)
        """
        new_node = DoublyListNode(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1
    
    def insertAfter(self, node: DoublyListNode, value):
        """
        Вставка элемента после произвольного узла.
        
        Временная сложность: O(1)
        """
        if node is None:
            raise ValueError("Узел не может быть None")
        
        new_node = DoublyListNode(value)
        new_node.prev = node
        new_node.next = node.next
        
        if node.next is not None:
            node.next.prev = new_node
        else:
            self.tail = new_node
        
        node.next = new_node
        self.size += 1
    
    def remove(self, node: DoublyListNode):
        """
        Удаление узла без поиска "сначала".
        
        Временная сложность: O(1) - не требуется поиск узла
        """
        if node is None:
            return False
        
        if node.prev is not None:
            node.prev.next = node.next
        else:
            self.head = node.next
        
        if node.next is not None:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        
        self.size -= 1
        return True
    
    def find(self, value):
        """
        Поиск узла по значению.
        
        Временная сложность: O(n)
        """
        current = self.head
        while current is not None:
            if current.value == value:
                return current
            current = current.next
        return None
    
    def __iter__(self):
        """
        Возвращает итератор по списку.
        """
        return DoublyLinkedListIterator(self)
    
    def __str__(self):
        """Строковое представление списка."""
        if self.head is None:
            return "[]"
        
        result = []
        current = self.head
        while current is not None:
            result.append(str(current.value))
            current = current.next
        return " <-> ".join(result)
    
    def __len__(self):
        return self.size


class DoublyLinkedListIterator:
    """
    Итератор по двусвязному списку.
    """
    
    def __init__(self, linked_list: DoublyLinkedList):
        self.current = linked_list.head
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current is None:
            raise StopIteration
        value = self.current.value
        self.current = self.current.next
        return value


if __name__ == "__main__":
    lst = DoublyLinkedList()
    
    print("=== Тестирование двусвязного списка ===")
    
    lst.pushBack(1)
    lst.pushBack(2)
    lst.pushBack(3)
    print(f"После pushBack(1,2,3): {lst}")
    
    lst.pushFront(0)
    print(f"После pushFront(0): {lst}")
    
    node = lst.find(2)
    if node:
        lst.insertAfter(node, 99)
        print(f"После insertAfter(узел со значением 2, 99): {lst}")
    
    print("\nИтерация по списку:")
    for value in lst:
        print(f"  {value}", end=" ")
    print()
    
    node_to_remove = lst.find(2)
    if node_to_remove:
        lst.remove(node_to_remove)
        print(f"\nПосле remove(узел со значением 2): {lst}")
    
    print(f"\nРазмер списка: {len(lst)}")


