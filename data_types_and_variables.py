# You have rented some movies for your kids: 
# The little mermaid (for 3 days), 
# Brother Bear (for 5 days, they love it), and 
# Hercules (1 day, you don't know yet if they're going to like it). 
# If price for a movie per day is 3 dollars, how much will you have to pay?

# When do you know you need a variable?
# Variables are the nouns in our programs

price_per_day = 3
little_mermaid_days = 3
brother_bear_days = 5
hercules_days = 1
total_days = little_mermaid_days + brother_bear_days + hercules_days
total_days

amount_spent = total_days * price_per_day
print(amount_spent)


# Suppose you're working as a contractor for 3 companies:
# Google, Amazon and Facebook, they pay you a 
# different rate per hour. 
# Google pays 400 dollars per hour, 
# Amazon 380, 
# and Facebook 350. 
# How much will you receive in payment for this week? 
# You worked 10 hours for Facebook, 
# 6 hours for Google and 4 hours for Amazon.

google_rate = 400
amazon_rate = 380
facebook_rate = 350

google_hours = 6
facebook_hours = 10
amazon_hours = 4
total_comp = (google_rate * google_hours) + (facebook_rate * facebook_hours) + (amazon_rate * amazon_hours)
print(total_comp)

# A student can be enrolled to a class only if the class is not full 
# and the class schedule does not conflict with her current schedule.

class_not_full = True
schedule_not_full = False
student_can_enroll = class_not_full and schedule_not_full
print(student_can_enroll)


# A product offer can be applied only if people buys more than 2 items, 
# and the offer has not expired.
# Premium members do not need to buy a specific amount of products.

is_premium_member = True
more_than_two_items = False
# (is_premium_member or more_than_two_items)
offer_not_expired = True
discount_valid = offer_not_expired and (is_premium_member or more_than_two_items)
print('Is discount valid?')
print(discount_valid)

# Continue working in your data_types_and_variables.py file. 
# Use the following code to follow the instructions below:

username = 'codeup'
password = 'notastrongpassword'

# Create a variable that holds a boolean value for each of the following conditions:

# the password must be at least 5 characters
# the username must be no more than 20 characters
# the password must not be the same as the username
# bonus neither the username or password can start or end with whitespace

password_is_length = len(password) >= 5
username_is_length = len(username) <= 20
username_and_password_are_different = username != password
username_has_spaces = username != username.strip()
password_has_spaces = password != password.strip()

password.strip()

password_has_spaces
