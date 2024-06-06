
from comp_search_func import compare_search_method
with open("text1.txt", "r") as fh:
    lines = fh.readlines()
    cmb_lines = ''.join(lines)
    pattern1 = 'технічний'
    pattern2 = '522264'
    pattern3 = 'Хуба-буба'
    compare_search_method(cmb_lines, 10, pattern1, pattern2, pattern3)


with open("text2.txt", "r") as fh:
    lines = fh.readlines()
    cmb_lines = ''.join(lines)
    pattern1 = 'соціальної'
    pattern2 = 'Кнут'
    pattern3 = 'Орбит'
    compare_search_method(cmb_lines, 10, pattern1, pattern2, pattern3)