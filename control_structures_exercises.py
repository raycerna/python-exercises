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
    



