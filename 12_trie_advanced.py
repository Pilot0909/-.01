"""
Задание 12. Trie (углубление)

Расширенная реализация Trie с возможностью:
- хранения слов целиком
- подсчета количества вариантов по префиксу
- удаления слова
"""


class TrieNode:
    """Узел расширенного Trie."""
    
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.word_count = 0
        self.prefix_count = 0


class AdvancedTrie:
    """
    Расширенная реализация Trie.
    """
    
    def __init__(self):
        self.root = TrieNode()
        self.total_words = 0
    
    def insert(self, word: str):
        """
        Вставка слова в Trie.
        
        Временная сложность: O(m), где m - длина слова
        
        Args:
            word: Слово для вставки
        """
        node = self.root
        node.prefix_count += 1
        
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.prefix_count += 1
        
        if not node.is_end_of_word:
            self.total_words += 1
            node.is_end_of_word = True
        
        node.word_count += 1
    
    def search(self, word: str) -> bool:
        """
        Поиск слова в Trie.
        
        Временная сложность: O(m), где m - длина слова
        
        Args:
            word: Слово для поиска
            
        Returns:
            True если слово найдено, False иначе
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word
    
    def count_words_with_prefix(self, prefix: str) -> int:
        """
        Подсчет количества слов с заданным префиксом.
        
        Временная сложность: O(m), где m - длина префикса
        
        Args:
            prefix: Префикс для поиска
            
        Returns:
            Количество слов с этим префиксом
        """
        node = self.root
        
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
        
        return node.prefix_count
    
    def get_all_words_with_prefix(self, prefix: str) -> list:
        """
        Получение всех слов с заданным префиксом.
        
        Временная сложность: O(m + k), где m - длина префикса, k - количество найденных слов
        
        Args:
            prefix: Префикс для поиска
            
        Returns:
            Список всех слов с этим префиксом
        """
        node = self.root
        
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        
        words = []
        self._collect_words(node, prefix, words)
        return words
    
    def _collect_words(self, node: TrieNode, prefix: str, words: list):
        """
        Рекурсивный сбор всех слов с заданным префиксом.
        
        Args:
            node: Текущий узел
            prefix: Текущий префикс
            words: Список для сохранения найденных слов
        """
        if node.is_end_of_word:
            for _ in range(node.word_count):
                words.append(prefix)
        
        for char, child_node in node.children.items():
            self._collect_words(child_node, prefix + char, words)
    
    def delete(self, word: str) -> bool:
        """
        Удаление слова из Trie.
        
        Временная сложность: O(m), где m - длина слова
        
        Args:
            word: Слово для удаления
            
        Returns:
            True если слово было удалено, False если не найдено
        """
        def _delete_helper(node: TrieNode, word: str, index: int) -> tuple[bool, bool]:
            """
            Рекурсивное удаление.
            Возвращает (успешно удалено, можно удалить узел).
            """
            if index == len(word):
                if not node.is_end_of_word:
                    return False, False
                
                node.word_count -= 1
                if node.word_count == 0:
                    node.is_end_of_word = False
                    self.total_words -= 1
                    return True, len(node.children) == 0
                return True, False
            
            char = word[index]
            if char not in node.children:
                return False, False
            
            child_node = node.children[char]
            deleted, should_delete_child = _delete_helper(child_node, word, index + 1)
            
            if not deleted:
                return False, False
            
            node.prefix_count -= 1
            
            if should_delete_child:
                del node.children[char]
                return True, len(node.children) == 0 and not node.is_end_of_word
            
            return True, False
        
        deleted, _ = _delete_helper(self.root, word, 0)
        if deleted:
            self.root.prefix_count -= 1
        return deleted
    
    def get_all_words(self) -> list:
        """
        Получение всех слов, хранящихся в Trie.
        
        Временная сложность: O(n * m), где n - количество слов, m - средняя длина слова
        """
        words = []
        self._collect_words(self.root, "", words)
        return words
    
    def __len__(self):
        """Возвращает общее количество уникальных слов."""
        return self.total_words


if __name__ == "__main__":
    trie = AdvancedTrie()
    
    print("=== Тестирование расширенного Trie ===")
    
    words = ["apple", "app", "application", "apply", "banana", "band", "bandana", "app"]
    print(f"Добавляем слова: {words}")
    
    for word in words:
        trie.insert(word)
    
    print(f"\nОбщее количество уникальных слов: {len(trie)}")
    print(f"Все слова в Trie: {sorted(set(trie.get_all_words()))}")
    
    print(f"\nПоиск 'app': {trie.search('app')}")
    print(f"Поиск 'apple': {trie.search('apple')}")
    print(f"Поиск 'appl': {trie.search('appl')}")
    
    print(f"\nКоличество слов с префиксом 'app': {trie.count_words_with_prefix('app')}")
    print(f"Количество слов с префиксом 'ban': {trie.count_words_with_prefix('ban')}")
    print(f"Количество слов с префиксом 'a': {trie.count_words_with_prefix('a')}")
    
    print(f"\nВсе слова с префиксом 'app': {trie.get_all_words_with_prefix('app')}")
    print(f"Все слова с префиксом 'ban': {trie.get_all_words_with_prefix('ban')}")
    
    print(f"\nУдаление 'app': {trie.delete('app')}")
    print(f"После удаления 'app':")
    print(f"  Поиск 'app': {trie.search('app')}")
    print(f"  Количество слов с префиксом 'app': {trie.count_words_with_prefix('app')}")
    print(f"  Все слова с префиксом 'app': {trie.get_all_words_with_prefix('app')}")
    print(f"  Общее количество уникальных слов: {len(trie)}")
    
    print(f"\nУдаление 'banana': {trie.delete('banana')}")
    print(f"После удаления 'banana':")
    print(f"  Количество слов с префиксом 'ban': {trie.count_words_with_prefix('ban')}")
    print(f"  Все слова с префиксом 'ban': {trie.get_all_words_with_prefix('ban')}")


