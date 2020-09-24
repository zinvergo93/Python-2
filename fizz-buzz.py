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