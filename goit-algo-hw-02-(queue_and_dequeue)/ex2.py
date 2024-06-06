from collections import deque
import re

def cheking_pali(pali_word):
    pali_word = deque(re.sub(r'\s+', '', pali_word.lower()))
    while len(pali_word)>1:
        if pali_word.pop() != pali_word.popleft():
            return False
    return True

def cheking_pali_vol2(pali_word):
    pali_word = deque(pali_word.lower().replace(' ',''))
    return list(pali_word) == list(pali_word)[::-1]
    



if __name__ == "__main__":
    user_input = input("Enter word I should check\n")
    if cheking_pali(user_input) == True:
        print("It is pali ac first")
    else:
        print("Its not ac first")

    if cheking_pali_vol2(user_input) == True:
        print("It is pali ac second")
    else:
        print("Its not ac second")
