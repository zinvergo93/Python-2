# List of comparison operators
# == Equality
# != Inequality
# <> Inequality (deprecated - don't use)
# >  Greater than
# >= Greater than or equal to
# < Less than
# <= Less than or equal to

# username = 'jonsnow'

# if username == 'jonsnow':
#   print('Welcome Jon')
# else:
#   print('You shall not pass!')

# age = 25

# if age <= 25:
#   print(f"I'm sorry, you need to be at least 25 years old")

# ***************************************************
#   how to check if a value is included IN a Python string or list

# sentence = 'The quick brown fox jumped over the lazy Dog'
# word = 'quick'

# if word in sentence:
#   print('The word is in the sentence')
# else:
#   print('The word is not in the sentence')

# prints 'The word is in the sentence'

# IS CASE SENSITIVE

# sentence = 'The quick brown fox jumped over the lazy Dog'
# word = 'dog'

# if word in sentence:
#   print('The word is in the sentence')
# else:
#   print('The word is not in the sentence')

# Prints 'The word is not in the sentence', because 'Dog' is capitalized in the string

# sentence = 'The quick brown fox jumped over the lazy Dog'
# word = 'dog'

# if word.lower() in sentence.lower():
#   print('The word is in the sentence')
# else:
#   print('The word is not in the sentence')

# Prints 'The word is in the sentence' because it overrides case sensitive
# Makes sentence ALL lower case, and therefore will recognize the word


# nums = [1, 2, 3, 4]

# if 3 in nums:
#   print('The number was found')
# else:
#   print('The number was not found')


# sentence = 'Python is the best!'
# word = 'Python'

# if word.lower() in sentence.lower():
# # if word in sentence:
#     print('The word is in the sentence')
# else:
#     print('The word is not in the sentence')


# ********************************************

# nums = [1, 2, 3, 4]
# num = 6
# # num = 3

# if num in nums:
#     print('The number was found')
# else:
#     print('The number was not found')


# *************Compound Conditionals***************

# username = 'jonsnow'
# email = 'jon@snow.com'
# password = 'thenorth'

# # if username == 'jonsnow' and password == 'thenorth':
# # if (username == 'jonsnow' or email == 'jon@snow.com') and password == 'thenorth':
# if (username == 'snowmanjon' or email == 'jon@snow.com') and password == 'thenorth':
# # if username == 'snowmanjon' and password == 'thenorth':
# # if username == 'snowmanjon' or password == 'thenorth':
#     print('Access permitted')
# else:
#     print('You shall not pass!')

# 'or' operator is flexible. If first value doesn't match
# but the value after 'or' DOES match, it will return as true
# statement and work with the 'if' statement



# *********AND NOT STATEMENTS*************

# logged_in = True
# # standard_user = False
# standard_user = True

# if logged_in and not standard_user:
#   print('You can access the admin dashboard')
# else:
#   print('You can only access the standard dashboard')

# left hand needs to be true and right side needs to be false
# for if statement to process.


a= 200
b = 33
c = 500

# if a == 200 and c == 500:
if a == 200 and a > b:
    print("Both conditions are True")


a= 200
b = 33
c = 500
if a == 301 or b == 33:
# if b == 33 or b == 500:
    print("At least one of the conditions is True")

if a == 200 and not c == 203:
    print('At least one of the conditoins is True')

