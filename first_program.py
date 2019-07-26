import random

def check_len(word, rand_len):
    if len(word) == rand_len:
        print(str(len(word)) + " characters was the correct length!")
        return True
    else:
        print(str(len(word)) + " characters was the wrong length!")
        return False

rand_num = random.randint(3, 7)

ex_cond = False

while ex_cond == False:
    print("Please choose a word with a length between 3 and 7.")
    user_input = input()
    
    ex_cond = check_len(user_input, rand_num)