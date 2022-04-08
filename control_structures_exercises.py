# 1. Conditional Basics

# a. prompt the user for a day of the week, print out whether the day is Monday or not

day_of_week = input ("enter day of week")
if day_of_week == 'Monday':
    print ("It is Monday.")
else:
    print ("No it is not Monday.")

# b. prompt the user for a day of the week, 
# print out whether the day is a weekday or a weekend

weekend_or_not=input("Enter a day of the week")
if weekend_or_not in ['Saturday','Sunday']:
    print("Fiesta!") 
else:
     print(":( worktime") 

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

