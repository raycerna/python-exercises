# 1 

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

#ryan's example
def handle_commas(some_input):
    if type(some_input) == str:
        return some_input.replace(",", "")
    return some_input

some_input(999,999)

def handle_commas(x):
    if type(x) == str:
        return x.replace(",", "")
    return x


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
        
#9

def remove_vowels(x):
  for i in "aeiouAEIOU":
            x = x.replace(i,"")
  return x

remove_vowels("banana")

#10

def normalize_name(string):
    string=string.lstrip().rstrip().lower().replace(' ','_')
    counter=1
    while True:
        if string.isidentifier():
            break
        else:
            string=string[counter:] 
            counter +=1 
    return string


def normalize_name(string):
    output = ''
    string = string.lower()
    for character in string:
        if character.isidentifier() or character == ' ':
            output += character
    output = output.strip()
    output = output.replace(' ', '_')
    return output


#11

def cumulative_sum(num_list):
    output = []
    for i, num in enumerate(num_list):
        sum_counter = sum(num_list[:i + 1])
        output.append(sum_counter)
    return output

