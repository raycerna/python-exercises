# 1 

# definition of the function is is_two with a parameter of x
def is_two(x):
    # the parameter must be an interger thas is equal to 2 then return true else false
    if int(x)==2:
        return True
    else:
        return False 
#this answer will not work for decimal points
        
# correct answer must compare parameter to 2 or '2' to return true or false boolean
def is_two(x):
    return x == 2 or x == '2'


# 2 

# definition of the function is is_vowel with a parameter of x
def is_vowel(x):
    # if the parameter is a character in this list then return true else false
  if x in ["a","e","i","o","u","A","E","I","O","U"]:
    return True
  else:
    return False

def is_vowel(x):
    if x in ['a','e','i','o','u','A','E','I','O','U']:
        return True
    else:
        return False

def is_vowel(somestring):
    if type(somestring) == str:
        result = somestring.lower() in ['a','e','i','o','u']
        return result
    else:
        return False

 def is_vowel(x):
    return x.lower() in ["a", "e", "i", "o", "u"]

# 3

#definition of this function is is_consonant with parameter of x.
def is_consonant(x):
    #using the function above to return true if it is a vowel
     if is_vowel(x)==True:
         return False
     else:
         return True 

def is_consonant(somestring):
    if type(somestring) == str:
        only_letters = somestring.isalpha()
        return only_letters and not is_vowel(somestring)
    return False

# 4

def captialize_consonant(word):
    if is_consonant(word[0])==True:
        return word[0].upper()+word[1:]
    else:
         return word

def capitalize_starting_consonant(string):
    if type(string) !=str:
        return False
    first_letter = string[0]
    if is_consonant(first_letter):
        string = string.capitalize()
    return string


# 5

def calculate_tip(tip_percent,bill):
    return (tip_percent/100*bill)

calculate_tip(10,159)

def calculate_tip(bill, tip_percentage=0.2):
    if type(tip_percentage) != float:
        return False
    if tip_percentage < 0 or tip_percentage > 1:
        return 'the tip percentage must be between 0 and 1'
    return tip_percentage * bill

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

def handle_commas(somestring):
    if type(somestring) != str:
        return 'input must be a string'
    somestring = somestring.replace(',', '')



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



