# age = 28

# if age < 25:
#     print(f"I'm sorry, you need to be at least 25 years old")
# elif age > 100:
#     print(f"You're too old bro.")
# else:
#     print(f"You're good to go, {age} fits in the range to rent a car.")


# answer = False
# number = 6

# if number > 5:
#     answer = True

# print(answer)


# def watermelonParty():
#     watermelons = 56
#     if watermelons > 50:
#         print(True)
    
#     else:
#         print(False)

# watermelonParty()

# watermelons = 44

# def watermelonParty(watermelons):
#     if watermelons > 50:
#         print(True)
    
#     else:
#         print(False)

# watermelonParty(44)



# def potential_driver(age):
#     if age == 15:
#         print("You can get a permit, but cannot get a license yet")
#     elif age > 15:
#         print("You can get a license!")
#     else:
#         print("You aren't old enough for a permit")

# potential_driver(15)
# potential_driver(17)
# potential_driver(13)

# ***********************
# *********TERNARY OPERATOR************

# role = 'admin'
# role = 'user'

# auth = 'can access' if role == 'admin' else 'cannot access'

# print(auth)

# ******** SAME AS*******

# role = 'admin'

# if role == 'admin':
#     auth = 'can access'
# else:
#     auth = 'cannot access'

# print(auth)

# *******************************
# NO TERNARY
# def ageVerification(age):
#     if age >= 25:
#         print("Can rent a car")
#     else:
#         print("Cannot rent a car")

# ageVerification(23)
# *************************
# FUNCTION WITH TERNARY ARGUMENT/LOGIC

# def ageVerification(age):
#     print('Can rent a car' if age >=25 else 'Cannot rent a car')

# ageVerification(27)

# ******************************
# Ternary
# age = 30

# ageVerification = 'Can rent a car' if age >= 25 else "Cannot rent a car"

# print(ageVerification)