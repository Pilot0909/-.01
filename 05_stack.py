"""
Задание 5. Стек

Реализация стека на массиве и связном списке.
Проверка корректности скобочной последовательности.
"""

import importlib.util
import sys

spec = importlib.util.spec_from_file_location("static_array", "01_static_array.py")
static_array_module = importlib.util.module_from_spec(spec)
sys.modules["static_array"] = static_array_module
spec.loader.exec_module(static_array_module)
StaticArray = static_array_module.StaticArray


class ArrayStack:
    """
    Стек на основе массива.
    """
    
    def __init__(self, capacity: int = 100):
        """
        Инициализация стека.
        
        Временная сложность: O(1)
        """
        self.capacity = capacity
        self.data = StaticArray(capacity)
        self.top_index = -1
    
    def push(self, value):
        """
        Добавление элемента в стек.
        
        Временная сложность: O(1)
        """
        if self.top_index >= self.capacity - 1:
            raise OverflowError("Стек переполнен")
        self.top_index += 1
        self.data.pushBack(value)
    
    def pop(self):
        """
        Извлечение элемента из стека.
        
        Временная сложность: O(1)
        """
        if self.isEmpty():
            raise IndexError("Стек пуст")
        value = self.data.data[self.top_index]
        self.data.remove(self.top_index)
        self.top_index -= 1
        return value
    
    def peek(self):
        """
        Просмотр верхнего элемента без извлечения.
        
        Временная сложность: O(1)
        """
        if self.isEmpty():
            raise IndexError("Стек пуст")
        return self.data.data[self.top_index]
    
    def isEmpty(self):
        """
        Проверка на пустоту.
        
        Временная сложность: O(1)
        """
        return self.top_index == -1
    
    def __len__(self):
        return self.top_index + 1


class ListNode:
    """Узел для стека на списке."""
    
    def __init__(self, value):
        self.value = value
        self.next = None


class ListStack:
    """
    Стек на основе связного списка.
    """
    
    def __init__(self):
        """
        Инициализация стека.
        
        Временная сложность: O(1)
        """
        self.head = None
        self.size = 0
    
    def push(self, value):
        """
        Добавление элемента в стек.
        
        Временная сложность: O(1)
        """
        new_node = ListNode(value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def pop(self):
        """
        Извлечение элемента из стека.
        
        Временная сложность: O(1)
        """
        if self.isEmpty():
            raise IndexError("Стек пуст")
        value = self.head.value
        self.head = self.head.next
        self.size -= 1
        return value
    
    def peek(self):
        """
        Просмотр верхнего элемента без извлечения.
        
        Временная сложность: O(1)
        """
        if self.isEmpty():
            raise IndexError("Стек пуст")
        return self.head.value
    
    def isEmpty(self):
        """
        Проверка на пустоту.
        
        Временная сложность: O(1)
        """
        return self.head is None
    
    def __len__(self):
        return self.size


def check_brackets(expression: str) -> bool:
    """
    Проверка корректности скобочной последовательности.
    
    Поддерживаемые скобки: (), [], {}
    
    Временная сложность: O(n), где n - длина выражения
    Пространственная сложность: O(n) в худшем случае
    
    Args:
        expression: Строка со скобками
        
    Returns:
        True если последовательность корректна, False иначе
    """
    stack = ListStack()
    opening_brackets = {'(', '[', '{'}
    closing_brackets = {')': '(', ']': '[', '}': '{'}
    
    for char in expression:
        if char in opening_brackets:
            stack.push(char)
        elif char in closing_brackets:
            if stack.isEmpty():
                return False
            if stack.pop() != closing_brackets[char]:
                return False
    
    return stack.isEmpty()


if __name__ == "__main__":
    print("=== Тестирование стека на массиве ===")
    stack1 = ArrayStack(10)
    stack1.push(1)
    stack1.push(2)
    stack1.push(3)
    print(f"После push(1,2,3): peek() = {stack1.peek()}")
    print(f"pop() = {stack1.pop()}")
    print(f"После pop(): peek() = {stack1.peek()}")
    
    print("\n=== Тестирование стека на списке ===")
    stack2 = ListStack()
    stack2.push(1)
    stack2.push(2)
    stack2.push(3)
    print(f"После push(1,2,3): peek() = {stack2.peek()}")
    print(f"pop() = {stack2.pop()}")
    print(f"После pop(): peek() = {stack2.peek()}")
    
    print("\n=== Проверка скобочных последовательностей ===")
    test_cases = [
        "()",
        "()[]{}",
        "([{}])",
        "((()))",
        "([)]",
        "(((",
        ")))",
        "()(",
        ""
    ]
    
    for expr in test_cases:
        result = check_brackets(expr)
        print(f"'{expr}' -> {'✓ Корректно' if result else '✗ Некорректно'}")

