"""
Задание 9. Частотный словарь

Построение HashMap частот встречаемости слов в тексте.
Сравнение времени построения при плохой и хорошей хэш-функции.
"""

import time
import re
from collections import Counter


class BadHashTable:
    """
    Хэш-таблица с плохой хэш-функцией (всегда возвращает 1).
    """
    
    def __init__(self, capacity: int = 16):
        self.capacity = capacity
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]
    
    def _hash(self, key: str) -> int:
        """Плохая хэш-функция - всегда возвращает 1."""
        return 1
    
    def put(self, key: str, value):
        index = self._hash(key)
        bucket = self.buckets[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        
        bucket.append((key, value))
        self.size += 1
    
    def get(self, key: str):
        index = self._hash(key)
        bucket = self.buckets[index]
        
        for k, v in bucket:
            if k == key:
                return v
        
        return None
    
    def items(self):
        """Возвращает все пары ключ-значение."""
        for bucket in self.buckets:
            for k, v in bucket:
                yield (k, v)


class GoodHashTable:
    """
    Хэш-таблица с хорошей хэш-функцией (djb2).
    """
    
    def __init__(self, capacity: int = 16):
        self.capacity = capacity
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]
    
    def _hash(self, key: str) -> int:
        """Хорошая хэш-функция djb2."""
        hash_value = 5381
        for char in key:
            hash_value = ((hash_value << 5) + hash_value) + ord(char)
        return hash_value % self.capacity
    
    def put(self, key: str, value):
        index = self._hash(key)
        bucket = self.buckets[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        
        bucket.append((key, value))
        self.size += 1
    
    def get(self, key: str):
        index = self._hash(key)
        bucket = self.buckets[index]
        
        for k, v in bucket:
            if k == key:
                return v
        
        return None
    
    def items(self):
        """Возвращает все пары ключ-значение."""
        for bucket in self.buckets:
            for k, v in bucket:
                yield (k, v)


def build_frequency_dict(text: str, hash_table_class):
    """
    Построение частотного словаря с использованием заданной хэш-таблицы.
    
    Args:
        text: Текст для анализа
        hash_table_class: Класс хэш-таблицы (BadHashTable или GoodHashTable)
        
    Returns:
        Хэш-таблица с частотами слов
    """
    words = re.findall(r'\b\w+\b', text.lower())
    
    freq_dict = hash_table_class(capacity=1000)
    
    for word in words:
        current_count = freq_dict.get(word) or 0
        freq_dict.put(word, current_count + 1)
    
    return freq_dict


def get_top_words(freq_dict, top_n: int = 10):
    """
    Получение топ-N самых частых слов.
    
    Args:
        freq_dict: Частотный словарь
        top_n: Количество слов для возврата
        
    Returns:
        Список кортежей (слово, частота), отсортированный по убыванию частоты
    """
    items = list(freq_dict.items())
    items.sort(key=lambda x: x[1], reverse=True)
    return items[:top_n]


def compare_hash_functions():
    """
    Сравнение времени построения частотного словаря при плохой и хорошей хэш-функции.
    """
    sample_text = """
    The quick brown fox jumps over the lazy dog. The dog was sleeping under a tree.
    A fox is a clever animal. The brown fox is quick. The lazy dog likes to sleep.
    """ * 1000
    
    print("=== Сравнение хэш-функций ===")
    print(f"Длина текста: {len(sample_text)} символов")
    print(f"Количество слов: {len(re.findall(r'\\b\\w+\\b', sample_text.lower()))}")
    
    start_time = time.time()
    bad_freq_dict = build_frequency_dict(sample_text, BadHashTable)
    bad_time = time.time() - start_time
    print(f"\nПлохая хэш-функция (всегда 1): {bad_time:.4f} сек")
    
    start_time = time.time()
    good_freq_dict = build_frequency_dict(sample_text, GoodHashTable)
    good_time = time.time() - start_time
    print(f"Хорошая хэш-функция (djb2): {good_time:.4f} сек")
    
    print(f"\nОтношение времени (плохая/хорошая): {bad_time/good_time:.2f}")
    
    print("\n=== Топ-10 самых частых слов (хорошая хэш-функция) ===")
    top_words = get_top_words(good_freq_dict, 10)
    for i, (word, count) in enumerate(top_words, 1):
        print(f"{i:2d}. {word:15s} : {count}")


if __name__ == "__main__":
    text = """
    Python is a high-level programming language. Python is known for its simplicity.
    Python has a large standard library. Many developers love Python.
    Python is used in web development, data science, and automation.
    """
    
    print("=== Построение частотного словаря ===")
    freq_dict = build_frequency_dict(text, GoodHashTable)
    
    print("\nВсе слова и их частоты:")
    for word, count in sorted(freq_dict.items(), key=lambda x: x[1], reverse=True):
        print(f"  {word}: {count}")
    
    print("\n=== Топ-10 самых частых слов ===")
    top_words = get_top_words(freq_dict, 10)
    for i, (word, count) in enumerate(top_words, 1):
        print(f"{i:2d}. {word:15s} : {count}")
    
    print("\n" + "="*60)
    compare_hash_functions()


