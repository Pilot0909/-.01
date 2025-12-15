"""
Задание 6. Очередь

Реализация очереди на циклическом массиве и на двух стеках.
"""


class CircularArrayQueue:
    """
    Очередь на основе циклического массива.
    """
    
    def __init__(self, capacity: int = 10):
        """
        Инициализация очереди.
        
        Временная сложность: O(1)
        """
        self.capacity = capacity
        self.data = [None] * capacity
        self.front = 0
        self.rear = 0
        self.size = 0
    
    def enqueue(self, value):
        """
        Добавление элемента в очередь.
        
        Временная сложность: O(1)
        """
        if self.size >= self.capacity:
            raise OverflowError("Очередь переполнена")
        
        self.data[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1
    
    def dequeue(self):
        """
        Извлечение элемента из очереди.
        
        Временная сложность: O(1)
        """
        if self.isEmpty():
            raise IndexError("Очередь пуста")
        
        value = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return value
    
    def peek(self):
        """
        Просмотр первого элемента без извлечения.
        
        Временная сложность: O(1)
        """
        if self.isEmpty():
            raise IndexError("Очередь пуста")
        return self.data[self.front]
    
    def isEmpty(self):
        """
        Проверка на пустоту.
        
        Временная сложность: O(1)
        """
        return self.size == 0
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        result = []
        for i in range(self.size):
            idx = (self.front + i) % self.capacity
            result.append(str(self.data[idx]))
        return "[" + ", ".join(result) + "]"


class StackQueue:
    """
    Очередь на основе двух стеков.
    """
    
    def __init__(self):
        """
        Инициализация очереди.
        
        Временная сложность: O(1)
        """
        self.stack_in = []
        self.stack_out = []
    
    def enqueue(self, value):
        """
        Добавление элемента в очередь.
        
        Временная сложность: O(1)
        """
        self.stack_in.append(value)
    
    def dequeue(self):
        """
        Извлечение элемента из очереди.
        
        Амортизированная временная сложность: O(1)
        В худшем случае (когда stack_out пуст): O(n)
        """
        if self.isEmpty():
            raise IndexError("Очередь пуста")
        
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        
        return self.stack_out.pop()
    
    def peek(self):
        """
        Просмотр первого элемента без извлечения.
        
        Амортизированная временная сложность: O(1)
        """
        if self.isEmpty():
            raise IndexError("Очередь пуста")
        
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        
        return self.stack_out[-1]
    
    def isEmpty(self):
        """
        Проверка на пустоту.
        
        Временная сложность: O(1)
        """
        return len(self.stack_in) == 0 and len(self.stack_out) == 0
    
    def __len__(self):
        return len(self.stack_in) + len(self.stack_out)


if __name__ == "__main__":
    print("=== Тестирование очереди на циклическом массиве ===")
    queue1 = CircularArrayQueue(5)
    queue1.enqueue(1)
    queue1.enqueue(2)
    queue1.enqueue(3)
    print(f"После enqueue(1,2,3): {queue1}")
    print(f"peek() = {queue1.peek()}")
    print(f"dequeue() = {queue1.dequeue()}")
    print(f"После dequeue(): {queue1}")
    queue1.enqueue(4)
    queue1.enqueue(5)
    print(f"После enqueue(4,5): {queue1}")
    
    print("\n=== Тестирование очереди на двух стеках ===")
    queue2 = StackQueue()
    queue2.enqueue(1)
    queue2.enqueue(2)
    queue2.enqueue(3)
    print(f"После enqueue(1,2,3): peek() = {queue2.peek()}")
    print(f"dequeue() = {queue2.dequeue()}")
    print(f"dequeue() = {queue2.dequeue()}")
    queue2.enqueue(4)
    queue2.enqueue(5)
    print(f"После enqueue(4,5): peek() = {queue2.peek()}")
    print(f"dequeue() = {queue2.dequeue()}")
    print(f"dequeue() = {queue2.dequeue()}")
    print(f"dequeue() = {queue2.dequeue()}")


