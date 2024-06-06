def build_shift_table(pattern):
    """Створити таблицю зсувів для алгоритму Боєра-Мура."""
    table = {}
    length = len(pattern)
    for index, char in enumerate(pattern[:-1]):
        table[char] = length - index - 1
    table.setdefault(pattern[-1], length)
    return table

def boyer_moore_search(text, pattern):
    shift_table = build_shift_table(pattern)
    i = 0  
    while i <= len(text) - len(pattern):
        j = len(pattern) - 1  
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1  #
        if j < 0:
            return i  
        i += shift_table.get(text[i + len(pattern) - 1], len(pattern))
    return -1

