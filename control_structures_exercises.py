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
hour_wage=20

if num_hours<=40:
    paycheck=num_hours*hour_wage
    print(paycheck)
else:
    paycheck=(num_hours-40)*1.5*hour_wage+40*hour_wage
    print("Weekley pay is: "+str(paycheck))