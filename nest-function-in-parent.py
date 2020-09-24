# def greeting(first, last):
#   def full_name():
#     return f'{first} {last}'

#   print(f'Hi {full_name()}!')


# greeting('Kristine', 'Hudgens')

# **********DEFAULT ARGUMENT**************

# def greeting(name = 'Guest'):
#     print(f'Hi, {name}!')

# greeting()
# greeting('Zac')


# def some_function(collection = []):
#   collection.append(1)
#   print(id(collection))
#   return collection


# print(some_function())
# print(some_function())

# ****************************************

# ************Collection function*******************

# def full_name(first, last):
#     print(f'{first} {last}')

# full_name(first ='Zac', last = 'Invergo')
# full_name(last = 'Invergo', first ='Zac')

# ********************************************

# **********Function Argument Unpacking*********

# *args creates a tuple

# def greeting(time_of_day, *args):

# # def greeting(*names): # not recommended though it works
    
#     print(f"Good {time_of_day}{' '.join(args)}!")
#     # print('Hi ' + ' '.join(names) + '!') # no need for asterisk when passed in

# greeting('Afternoon ''Zachary', 'T.', 'Invergo')
# greeting('Morning ', 'Zachary', 'T.', 'Invergo')

# *********************************************

# **************Keyword Arguments**************

# **kwargs creates dictionary
# def greeting(**kwargs):
#     if kwargs:
#         print(f"Hi {kwargs['first_name']} {kwargs['last_name']}, have a great day!")

# greeting(first_name = 'Zac', last_name = 'Invergo')

# **************************************************

# **************Combine ALL Arguments**********************

# def greeting(time_of_day, *args, **kwargs):
#     print(f"Hi {' '.join(args)}, I hope that you are having a great {time_of_day}!")

#     if kwargs:
#         print('Your tasks for the day are: ')
#         for key, val in kwargs.items():
#             print(f"{key} => {val}")


# greeting('morning', 
#          'Zac', 'Invergo',
#          first = 'Do the dishes',
#          second = 'Take Diesel outside',
#          third = 'Do coding homework')

# ****************************************************

# *******************Lambdas***************************
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# Wraps up process

# full_name = lambda first, last: f'{first} {last}'

# def greeting(name):
#     print(f'Hi there {name}!')

# greeting(full_name('Zac', 'Invergo'))

# print(full_name('Zac', 'Invergo'))

# numbers = lambda num_one, num_two:f'num_one + num_two'

# def sum(numbers):
#     print(f'num_one + num_two')

# sum(numbers)


# *************FIZZ BUZZ CHALLENGE********************

# def fizz_buzz():
#     for i in range (1, 101):
#         mult_three = i % 3 == 0
#         mult_five = i % 5 == 0
#         # if i % 3 == 0 and i % 5 == 0:
#         if mult_three and mult_five:
#             print("fizzbuzz")
#         elif mult_three:
#             print("fizz")
#         elif mult_five:
#             print("buzz")
        
#         else:
#             print(i)

# fizz_buzz()

# Cory's answer**************************************

# from operator import mod
# def fizz_buzz():
#     start_program = True
#     while start_program is True:
#         for number in range(1, int(input("What number would you like to go to?\n\t"))):
#             def find_truth(divider):
#                 return True if mod(number, divider) == 0 else False
#             if find_truth(3) and find_truth(5) is True:
#                 print("FizzBuzz")
#             elif find_truth(5) is True:
#                 print("Buzz")
#             elif find_truth(3) is True:
#                 print("Fizz")
#             else:
#                 print(number)
#         if input("Would you like to continue?\n Yes or No?\n\t") == 'Yes':
#             start_program = True
#         else:
#             start_program = False
# fizz_buzz()