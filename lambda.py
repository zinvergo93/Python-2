
# *******************Lambdas***************************
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# Wraps up process

# full_name = lambda first, last: f'{first} {last}'

# def greeting(name):
#     print(f'Hi there {name}!')

# greeting(full_name('Zac', 'Invergo'))

# print(full_name('Zac', 'Invergo'))

numbers = lambda num_one, num_two: num_one + num_two

print(numbers(4, 5))