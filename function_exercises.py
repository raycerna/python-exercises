# 1 

from ast import Num


def is_two(x):
    if int(x)==2:
        return True
    else:
        return False 

# 2 
def is_vowel(x):
  if x in ["a","e","i","o","u","A","E","I","O","U"]:
    return True
  else:
    return False

def is_vowel(x):
    if x in ['a','e','i','o','u']:
        return True
    else:
        return False

# 3

def is_consonant(x):
     if is_vowel(x)==True:
         return False
     else:
         return True 

# 4

def captialize_consonant(word):
    if is_consonant(word[0])==True:
        return word[0].upper()+word[1:]
    else:
         return word

# 5

def calculate_tip(tip_per,bill):
    return (tip_per/100*bill)

calculate_tip(10,159)

# 6

def apply_discount(dis_per,orig_price):
    discount = orig_price * (dis_per/100)
    return orig_price - discount

apply_discount(20, 199)

# 7

def handle_commas(number):
    return int(number.replace(',', ''))

handle_commas("999,999,999")

def handle_commas(some_input):
    if type(some_input) == str:
        return some_input.replace(",", "")
    return some_input

some_input(9999999)


#8

def get_letter_grade(num):
    num = int(num)
    if num >= 90:
        return('A')
    elif num >= 80:
        return('B')
    elif num >= 70:
        return('C')
    elif num >= 60:
        return('D')
    else:
        return('F')
        
