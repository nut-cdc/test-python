# 3.1 --------------------- Validating User Input ---------------------

# initialize variables
passes = 0 # number of passes
failures = 0 # number of failures

# process 10 students
for student in range(10):
    # get one exam result
    result = int(input('Enter result (1=pass, 2=fail): '))
    if ((result != 1) or (result != 2)):
        result = int(input('Enter result (1=pass, 2=fail): '))

if result == 1:
    passes = passes + 1
else:
    failures = failures + 1

# termination phase
print('Passed:', passes)
print('Failed:', failures)

if passes > 8:
    print('Bonus to instructor')

# 3.3 --------------------- What Does This Code Do --------------------

# for row in range(10):
#     for column in range(10):
#         print('<' if row % 2 == 1 else '>', end='')
#     print()

# 3.4 --------------------- Fill in the Missing Code ------------------

# for row in range(3):
#     for column in range(3):
#         print('O', end='')
#     print()

# 3.5 --------------------- if…else Statements ---------------------

# print('Enter two integers, and I will tell you',
# 'the relationships they satisfy.')

# # read first integer
# number1 = int(input('Enter first integer: '))

# # read second integer
# number2 = int(input('Enter second integer: '))

# if number1 == number2:
#     print(number1, 'is equal to', number2)

# elif number1 != number2:
#     print(number1, 'is not equal to', number2)

# if number1 < number2:
#     print(number1, 'is less than', number2)

# elif number1 > number2:
#     print(number1, 'is greater than', number2)

# elif number1 <= number2:
#     print(number1, 'is less than or equal to', number2)

# else:
#     print(number1, 'is greater than or equal to', number2)

# 3.6 --------------------- Turing Test ---------------------

# prompt = input("What is your problem? ")
# # Si la réponse n'est pas vide et que la touche Entrée est pressée
# while (prompt != ""):
#     new_prompt = input("Have you had this problem before (yes or no)? ")
#     break

# if (new_prompt == "yes"):
#     print("Well, you have it again.")
# else:
#     print("Well, you have it now.")

# 3.7 --------------------- Table of Bacteria ---------------------

# number_of_bacteria = 200
# hour = 0
# n = 5
# print("Hour \tNumber of Bacteria")

# for hour in range(0, 20, 5):
#     print(f'{hour:>4}{number_of_bacteria:>22}')
#     number_of_bacteria = number_of_bacteria * (2 ** n)

# 3.8 --------------------- Flu Patients Data Processing -----------------
# 3.9 --------------------- Calculating Time -----------------
# 3.10 --------------------- Hourly Wage Calculator --------------------
# 3.11 --------------------- Rabbit Births ------------------
# 3.12 --------------------- Triangles --------------------
# 3.13 --------------------- Perfect Numbers ------------------
# 3.14 ---------- Approximating the Mathematical Constant ---------
# 3.15 --------------------- Fibonacci Sequence ------------------
# 3.16 --------------------- Fastest Runners ------------------
# 3.17 --------------------- Nested Loops ------------------
# 3.18 --------------------- Nested Looping ------------------
# 3.19 --------------------- Prime Factorization ------------------
# 3.20 ------------------ Binary-to-Decimal Conversion --------------
# 3.21 ----------- Calculate Distance in m, dm, cm and mm ----------
# 3.22 ---------------- Optional else Clause of a Loop ---------------
# 3.23 -------------------- Validating Indentation -------------------
# 3.24 --------- Using the prospector Static Code Analysis Tool ---------
# 3.25 ----- Using prospector to Analyze Open-Source Code on GitHub -----
# 3.26 -------------------- Anscombe’s Quartet -------------------
# 3.27 -------------------- World Population Growth -------------------
# 3.28 -------------------- Mean, Median and Mode -------------------
# 3.29 -------------------- Problem with the Median -------------------
# 3.30 -------------------- Outliers -------------------
# 3.31 -------------------- Categorical Data -------------------