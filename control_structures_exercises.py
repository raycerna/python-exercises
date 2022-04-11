# 1. Conditional Basics

# a. prompt the user for a day of the week, print out whether the day is Monday or not

day_of_week = input ("enter day of week")
if day_of_week == 'Monday':
    print ("It is Monday.")
else:
    print ("No it is not Monday.")

day = input('Please enter the day of the week: ')

if day.lower() in ['monday', 'mon']:
    print('Today is Monday')
else:
    print(f'Today is {day.capitalize()}')


# b. prompt the user for a day of the week, 
# print out whether the day is a weekday or a weekend

weekend_or_not=input("Enter a day of the week")
if weekend_or_not in ['Saturday','Sunday']:
    print("Fiesta!") 
else:
     print(":( worktime") 

day = input('Please enter the day of the week: ')

while day.lower() not in ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']:
    print('invalid input. please enter the full name of the day')
    day = input('Please enter the day of the week:')

if day.lower() in ['sunday', 'saturaday']:


# c. create variables and make up values for
    #the number of hours worked in one week
    #the hourly rate
    #how much the week's paycheck will be
#write the python code that calculates the weekly paycheck. 
#You get paid time and a half if you work more than 40 hours

num_hours=65
hour_wage=100

if num_hours<=40:
    paycheck=num_hours*hour_wage
    print(paycheck)
else:
    paycheck=(num_hours-40)*1.5*hour_wage+40*hour_wage
    print("Weekley pay is: "+str(paycheck))

hourse_worked=45
hourly_rate=50
overtime_rate = hourly_rate *1.5

if hours_worked <=40:
    total_pay = hours_worked * hourly_rate
else:
    regular_pay=40*hourly_rate
    overtime_pay=(hours_worked-40)* overtime_pay
    total_pay=regular_pay + overtime_pay

total_pay

#2 Loop Basics

#a. While
    # Create an integer variable i with a value of 5.
    # Create a while loop that runs so long as i is less than or equal to 15
    # Each loop iteration, output the current value of i, then increment i by one.

i=5
while i<=15:
    print(i)
    i+=1  

# Create a while loop that will count by 2's starting with 0 and ending at 100. 
# Follow each number with a new line.

for i in range(0,102,2):
    print(i)

i=0    
while i<=100:
    print(i)
    i+=2

# Alter your loop to count backwards by 5's from 100 to -10.

for i in range(100,-10,-5):
    print(i)

i=100
while i>=-10:
    print(i)
    i-=5

i = 100
while i >= -10:


# Create a while loop that starts at 2, and displays the number squared on each line
#  while the number is less than 1,000,000. Output should equal:
# 2
# 4
# 16
# 256
# 65536

i=2
while i<1000000:
    print(i)
    i=i**2

i=2
while i<1_000_000:
    print(i)
    i=i**2
    
# Write a loop that uses print to create the output shown below.

for i in range(100,0,-5):
    print(i)

i=100
while i>=5:
    print(i)
    i-=5

# 2.b For Loops

# Write some code that prompts the user for a number, 
# then shows a multiplication table up through 10 for that number.

num=input("Enter a number") 
num=int(num)
for i in range(1,11):
    print(str(i)+"*"+str(num)+"="+str(i*num)) 

for i in range(1,11):
        print(f'{num} * {i} = {num')

# Create a for loop that uses print to create the output shown below.

for num in range(1,10):
    print(str(num)*num)

# 2.c break and continue
#Prompt the user for an odd number between 1 and 50. 
#Use a loop and a break statement to continue prompting the user if they enter invalid input. (Hint: use the isdigit method on strings to determine this). Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.

odd_num=""
while True:
    odd_num=input("Enter an odd number between 1 and 50")
    if odd_num.isdigit() and int(odd_num)%2==1 and int(odd_num)>1 and int(odd_num)<50:
        break

for i in range(1,50,2):
    if i==int(odd_num):
        print("Yikes! Skipping number: "+str(i))
        continue
    print("Here is an odd number: "+str(i))

#ravinder example:

num = input('please enter a odd number between 1 and 50: ')

    while True:
        if (num.isdigit()= False or int(num) > or int(num) <1 or int(num)% 2==0:
            print('invalid input')
            num =  input('please enter a odd number between 1 and 50: ')
        else:
            break

num = int(num)

print('Number to skip is:', num)

for i in range(1,50):
    if i % 2 == 0:
        continue
    elif i == num:
        print('yikes, skipping this number', i)
    else:
        print ('Here is an odd number', i)

# 2.d The input function can be used to prompt for input and 
# use that input in your python code. Prompt the user to enter a positive number 
# and write a loop that counts from 0 to that number. 
# (Hints: first make sure that the value the user entered is a valid number, 
# also note that the input function returns a string, 
# so you'll need to convert this to a numeric type.)

pos_num=""

while True:
    pos_num=input("Please enter a positive number")
    if pos_num.isdigit() and int(pos_num)>0:
        break

for i in range(1,int(pos_num)+1):
    print(i)

# 2.e Write a program that prompts the user for a positive integer. 
# Next write a loop that prints out the numbers 
# from the number the user entered down to 1.

pos_num=""
while True:
    pos_num=input("Please enter a positive number")
    if pos_num.isdigit() and int(pos_num)>0:
        break
for i in range(int(pos_num),0,-1):
    print(i)

# 3 Fizzbuzz
# One of the most common interview questions for entry-level programmers is 
# the FizzBuzz test. Developed by Imran Ghory, the test is designed to test 
# basic looping and conditional logic skills.
# 
# Write a program that prints the numbers from 1 to 100.
# For multiples of three print "Fizz" instead of the number
# For the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".

for i in range (1,101):
     if i%3==0 and i%5==0:
         print("FizzBuzz")
     elif i%3==0:
         print("Fizz")
     elif i%5==0:
         print("Buzz")
     else:
         print(str(i))

#4 Display a table of powers.

# Prompt the user to enter an integer.
# Display a table of squares and cubes from 1 to the value entered.
# Ask if the user wants to continue.
# Assume that the user will enter valid data.
# Only continue if the user agrees to.

while True:
    num_test=int(input("Please enter an integer"))
    for i in range(1,num_test+1):
        if i==1:
            print('number  | squared  | cubed')
            print('______  |  ______  |  ______')
    print(i,'  |', i**2,'  |',i**3)
    user_choice=input("Should we continue ?")
    if user_choice="no":
        break

#5 Convert given number grades into letter grades.

#Prompt the user for a numerical grade from 0 to 100.
#Display the corresponding letter grade.
#Prompt the user to continue.
#Assume that the user will enter valid integers for the grades.
#The application should only continue if the user agrees to.
#Grade Ranges:

# A : 100 - 88
# B : 87 - 80
# C : 79 - 67
# D : 66 - 60
# F : 59 - 0

while True:
    num_grade=input("Please enter a grade between 0 and 100")
    num_grade=int(num_grade)
    if num_grade>=88:
        print('A')
    elif num_grade>=80:
        print('B')
    elif num_grade>=67:
        print('C')
    elif num_grade>=60:
        print('D') 
    else:
        print('F')


#6 Create a list of dictionaries where each dictionary represents a book that you have read. 
# Each dictionary in the list should have the keys title, author, and genre. 
# Loop through the list and print out information about each book.

book_list=[{'title':"First to Fight",'author':"Victor H. Krulak",'genre':"War"},
{'title':"Black Hearts",'author':"Jim Fredrick",'genre':"War"},{'title':"The Marines at Montford Point",'author':"Melton Mclaurin",'genre':"History"},{'title':"Tattoos as Punishment",'author':"Eric Shahan",'genre':"History"}]

for book in book_list:
    print("The book title is: "+book['title'])
    print("The book author is: "+book['author'])
    print("The book genre is: "+book['genre'])


# Prompt the user to enter a genre, then loop through your books list 
# and print out the titles of all the books in that genre.

genre_filter=input("Please enter a genre")
for book in book_list:
    if book['genre']==genre_filter:
        print("The book title is: "+book['title'])
        print("The book author is: "+book['author'])