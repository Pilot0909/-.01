"""
Задание 11. Бинарное дерево поиска (BST)

Реализация BST с операциями вставки, поиска, удаления и обходами.
"""


class TreeNode:
    """Узел бинарного дерева."""
    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    """
    Бинарное дерево поиска (BST).
    """
    
    def __init__(self):
        self.root = None
        self.size = 0
    
    def insert(self, value):
        """
        Вставка значения в BST.
        
        Временная сложность: O(h), где h - высота дерева
        В среднем случае: O(log n)
        В худшем случае (вырожденное дерево): O(n)
        
        Args:
            value: Значение для вставки
        """
        self.root = self._insert_recursive(self.root, value)
        self.size += 1
    
    def _insert_recursive(self, node: TreeNode, value) -> TreeNode:
        """Рекурсивная вставка."""
        if node is None:
            return TreeNode(value)
        
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        
        return node
    
    def search(self, value) -> bool:
        """
        Поиск значения в BST.
        
        Временная сложность: O(h), где h - высота дерева
        В среднем случае: O(log n)
        В худшем случае: O(n)
        
        Args:
            value: Значение для поиска
            
        Returns:
            True если значение найдено, False иначе
        """
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, node: TreeNode, value) -> bool:
        """Рекурсивный поиск."""
        if node is None:
            return False
        
        if value == node.value:
            return True
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)
    
    def delete(self, value):
        """
        Удаление значения из BST.
        
        Временная сложность: O(h), где h - высота дерева
        В среднем случае: O(log n)
        В худшем случае: O(n)
        
        Args:
            value: Значение для удаления
        """
        if self.search(value):
            self.root = self._delete_recursive(self.root, value)
            self.size -= 1
    
    def _delete_recursive(self, node: TreeNode, value) -> TreeNode:
        """Рекурсивное удаление."""
        if node is None:
            return None
        
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                min_node = self._find_min(node.right)
                node.value = min_node.value
                node.right = self._delete_recursive(node.right, min_node.value)
        
        return node
    
    def _find_min(self, node: TreeNode) -> TreeNode:
        """Поиск узла с минимальным значением."""
        while node.left is not None:
            node = node.left
        return node
    
    def inorder(self) -> list:
        """
        Обход дерева in-order (левый -> корень -> правый).
        Возвращает отсортированную последовательность.
        
        Временная сложность: O(n)
        """
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node: TreeNode, result: list):
        """Рекурсивный in-order обход."""
        if node is not None:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)
    
    def preorder(self) -> list:
        """
        Обход дерева pre-order (корень -> левый -> правый).
        
        Временная сложность: O(n)
        """
        result = []
        self._preorder_recursive(self.root, result)
        return result
    
    def _preorder_recursive(self, node: TreeNode, result: list):
        """Рекурсивный pre-order обход."""
        if node is not None:
            result.append(node.value)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)
    
    def postorder(self) -> list:
        """
        Обход дерева post-order (левый -> правый -> корень).
        
        Временная сложность: O(n)
        """
        result = []
        self._postorder_recursive(self.root, result)
        return result
    
    def _postorder_recursive(self, node: TreeNode, result: list):
        """Рекурсивный post-order обход."""
        if node is not None:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.value)
    
    def _height(self, node: TreeNode) -> int:
        """Вычисление высоты поддерева."""
        if node is None:
            return -1
        return 1 + max(self._height(node.left), self._height(node.right))
    
    def is_balanced(self) -> bool:
        """
        Проверка, является ли дерево сбалансированным.
        
        Дерево считается сбалансированным, если для каждого узла
        разница высот левого и правого поддеревьев не превышает 1.
        
        Временная сложность: O(n)
        
        Returns:
            True если дерево сбалансировано, False иначе
        """
        return self._is_balanced_recursive(self.root) != -1
    
    def _is_balanced_recursive(self, node: TreeNode) -> int:
        """
        Рекурсивная проверка балансировки.
        Возвращает высоту поддерева или -1, если оно несбалансировано.
        """
        if node is None:
            return 0
        
        left_height = self._is_balanced_recursive(node.left)
        if left_height == -1:
            return -1
        
        right_height = self._is_balanced_recursive(node.right)
        if right_height == -1:
            return -1
        
        if abs(left_height - right_height) > 1:
            return -1
        
        return 1 + max(left_height, right_height)
    
    def __len__(self):
        return self.size


if __name__ == "__main__":
    bst = BinarySearchTree()
    
    print("=== Тестирование бинарного дерева поиска ===")
    
    values = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45]
    for value in values:
        bst.insert(value)
    
    print(f"Вставлены значения: {values}")
    print(f"Размер дерева: {len(bst)}")
    
    print(f"\nПоиск 40: {bst.search(40)}")
    print(f"Поиск 100: {bst.search(100)}")
    
    print(f"\nIn-order обход: {bst.inorder()}")
    print(f"Pre-order обход: {bst.preorder()}")
    print(f"Post-order обход: {bst.postorder()}")
    
    print(f"\nДерево сбалансировано: {bst.is_balanced()}")
    
    bst.delete(30)
    print(f"\nПосле удаления 30:")
    print(f"In-order обход: {bst.inorder()}")
    print(f"Дерево сбалансировано: {bst.is_balanced()}")
    
    print("\n=== Тест несбалансированного дерева ===")
    unbalanced_bst = BinarySearchTree()
    for i in range(10):
        unbalanced_bst.insert(i)
    
    print(f"In-order обход: {unbalanced_bst.inorder()}")
    print(f"Дерево сбалансировано: {unbalanced_bst.is_balanced()}")


