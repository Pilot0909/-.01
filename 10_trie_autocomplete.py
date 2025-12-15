"""
Задание 10. Trie + HashMap: автодополнение

Реализация Trie для хранения слов и автодополнения с учетом частот.
"""


class TrieNode:
    """Узел Trie."""
    
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.frequency = 0


class Trie:
    """
    Trie (префиксное дерево) для хранения слов.
    """
    
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str, frequency: int = 1):
        """
        Вставка слова в Trie.
        
        Временная сложность: O(m), где m - длина слова
        
        Args:
            word: Слово для вставки
            frequency: Частота слова (по умолчанию 1)
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        node.frequency += frequency
    
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
    
    def _collect_words(self, node: TrieNode, prefix: str, words: list):
        """
        Рекурсивный сбор всех слов с заданным префиксом.
        
        Args:
            node: Текущий узел
            prefix: Текущий префикс
            words: Список для сохранения найденных слов (слово, частота)
        """
        if node.is_end_of_word:
            words.append((prefix, node.frequency))
        
        for char, child_node in node.children.items():
            self._collect_words(child_node, prefix + char, words)
    
    def autocomplete(self, prefix: str) -> list:
        """
        Поиск всех слов с заданным префиксом.
        
        Временная сложность: O(m + k), где m - длина префикса, k - количество найденных слов
        
        Args:
            prefix: Префикс для поиска
            
        Returns:
            Список кортежей (слово, частота), отсортированный по убыванию частоты
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        
        words = []
        self._collect_words(node, prefix, words)
        
        words.sort(key=lambda x: x[1], reverse=True)
        
        return words
    
    def count_prefix(self, prefix: str) -> int:
        """
        Подсчет количества слов с заданным префиксом.
        
        Временная сложность: O(m + k), где m - длина префикса, k - количество найденных слов
        
        Args:
            prefix: Префикс для поиска
            
        Returns:
            Количество слов с этим префиксом
        """
        return len(self.autocomplete(prefix))
    
    def delete(self, word: str) -> bool:
        """
        Удаление слова из Trie.
        
        Временная сложность: O(m), где m - длина слова
        
        Args:
            word: Слово для удаления
            
        Returns:
            True если слово было удалено, False если не найдено
        """
        def _delete_helper(node: TrieNode, word: str, index: int) -> bool:
            if index == len(word):
                if not node.is_end_of_word:
                    return False
                node.is_end_of_word = False
                node.frequency = 0
                return len(node.children) == 0
            
            char = word[index]
            if char not in node.children:
                return False
            
            child_node = node.children[char]
            should_delete_child = _delete_helper(child_node, word, index + 1)
            
            if should_delete_child:
                del node.children[char]
                return len(node.children) == 0 and not node.is_end_of_word
            
            return False
        
        return _delete_helper(self.root, word, 0)


class TrieAutocomplete:
    """
    Система автодополнения на основе Trie + HashMap.
    
    Использует HashMap для хранения частот слов и Trie для быстрого поиска по префиксу.
    """
    
    def __init__(self):
        self.trie = Trie()
        self.word_frequencies = {}  # HashMap: слово -> частота
    
    def add_word(self, word: str, frequency: int = 1):
        """
        Добавление слова с частотой.
        
        Args:
            word: Слово
            frequency: Частота слова
        """
        self.word_frequencies[word] = self.word_frequencies.get(word, 0) + frequency
        
        self.trie.insert(word, self.word_frequencies[word])
    
    def autocomplete(self, prefix: str, max_results: int = 10) -> list:
        """
        Автодополнение по префиксу с учетом частот.
        
        Args:
            prefix: Префикс для поиска
            max_results: Максимальное количество результатов
            
        Returns:
            Список слов, отсортированный по убыванию частоты
        """
        words_with_freq = self.trie.autocomplete(prefix)
        
        return [word for word, freq in words_with_freq[:max_results]]
    
    def get_suggestions(self, prefix: str) -> list:
        """
        Получение подсказок с частотами.
        
        Args:
            prefix: Префикс для поиска
            
        Returns:
            Список кортежей (слово, частота), отсортированный по убыванию частоты
        """
        return self.trie.autocomplete(prefix)


if __name__ == "__main__":
    print("=== Тестирование Trie ===")
    trie = Trie()
    
    words = ["apple", "app", "application", "apply", "banana", "band", "bandana"]
    for word in words:
        trie.insert(word)
    
    print(f"Поиск 'app': {trie.search('app')}")
    print(f"Поиск 'apple': {trie.search('apple')}")
    print(f"Поиск 'appl': {trie.search('appl')}")
    
    print(f"\nАвтодополнение для 'app': {trie.autocomplete('app')}")
    print(f"Автодополнение для 'ban': {trie.autocomplete('ban')}")
    print(f"Количество слов с префиксом 'app': {trie.count_prefix('app')}")
    
    print("\n=== Тестирование Trie + HashMap автодополнения ===")
    autocomplete = TrieAutocomplete()
    
    word_freqs = {
        "python": 100,
        "programming": 80,
        "program": 60,
        "programmer": 50,
        "data": 90,
        "database": 70,
        "data science": 85,
        "algorithm": 75,
        "algorithms": 65
    }
    
    for word, freq in word_freqs.items():
        autocomplete.add_word(word, freq)
    
    print("\nАвтодополнение для 'pro':")
    suggestions = autocomplete.get_suggestions("pro")
    for word, freq in suggestions:
        print(f"  {word:20s} : {freq}")
    
    print("\nАвтодополнение для 'data':")
    suggestions = autocomplete.get_suggestions("data")
    for word, freq in suggestions:
        print(f"  {word:20s} : {freq}")
    
    print("\nАвтодополнение для 'alg':")
    suggestions = autocomplete.get_suggestions("alg")
    for word, freq in suggestions:
        print(f"  {word:20s} : {freq}")


