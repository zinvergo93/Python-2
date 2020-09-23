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

full_name = lambda first, last: f'{first} {last}'

def greeting(name):
    print(f'Hi there {name}!')

greeting(full_name('Zac', 'Invergo'))

# print(full_name('Zac', 'Invergo'))


