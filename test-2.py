# 2.5 --------------------- Eggs Per Box ---------------------

# eggs_in_box = 6
# number_of_eggs = 28
# boxes_farmer_needs = number_of_eggs // eggs_in_box
# eggs_in_uncompleted_box = number_of_eggs - (boxes_farmer_needs * eggs_in_box)
# eggs_needed_in_uncompleted_box = eggs_in_box - eggs_in_uncompleted_box

# print("Number of boxes a farmer need: ", boxes_farmer_needs)
# print("Number of eggs in uncompleted box: ", eggs_in_uncompleted_box)
# print("Number of eggs needed to fill uncompleted box: ", eggs_needed_in_uncompleted_box)

# 2.6 --------------------- Odd or Even ---------------------

# number = int(input("Enter a number: "))
# if (number % 2 == 0):
#     print("Number is even.")
# else:
#     print("Number is odd.")

# 2.7 --------------------- The Remainder Operator ---------------------

# marbles = 22
# friends = 4
# if (marbles % friends != 0):
#     print("Equal amount of marbles is not possible.")
# else:
#     print("Equal amount of marbles is possible.")

# 2.8 --------------------- Table with Number of Bacteria ---------------------   
 
# number_of_bacteria = 200
# n = 5
# print("Hour \tNumber of Bacteria")
# print(0, "\t", number_of_bacteria)
# print(n, "\t", number_of_bacteria * 2 ** n)
# print(n + 5, "\t", number_of_bacteria * 2 ** (n + 5))
# print(n + 10, "\t", number_of_bacteria * 2 ** (n + 10))
# print("\n")
# print("Hour \tNumber of Bacteria")
# print(f"{0:>4}{number_of_bacteria:>22}")
# print(f"{n:>4}{number_of_bacteria * 2 ** n:>22}")
# print(f"{n + 5:>4}{number_of_bacteria * 2 ** (n + 5):>22}")
# print(f"{n + 10:>4}{number_of_bacteria * 2 ** (n + 10):>22}")

# 2.9 --------------------- Integer Value of a Character ---------------------   

# tom_sum = ord("t") + ord("o") + ord("m")
# jim_sum = ord("j") + ord("i") + ord("m")

# if(tom_sum > jim_sum):
#     print("Tom begins to play.")
# else:
#     print("Jim begins to play.")

# print("\n")
# print(int(ord("B")))
# print(int(ord("C")))
# print(int(ord("D")))
# print(int(ord("b")))
# print(int(ord("c")))
# print(int(ord("d")))
# print(int(ord("0")))
# print(int(ord("1")))
# print(int(ord("2")))
# print(int(ord("$")))
# print(int(ord("*")))
# print(int(ord("+")))
# print(int(ord(" ")))

# 2.10 --------------------- Arithmetic, Highest and Lowest --------------------- 

# course_1 = input("Enter the name of your first course: ")
# grade_1 = int(input("Enter your first grade: "))
# course_2 = input("Enter the name of your second course: ")
# grade_2 = int(input("Enter your first grade: "))
# course_3 = input("Enter the name of your third course: ")
# grade_3 = int(input("Enter your first grade: "))

# average = (grade_1 + grade_2 + grade_3) / 3

# print("Average of your courses is: ", average)
# print("Names of the courses are: ", course_1, course_2, course_3)
# print("Grades of your courses are: ", grade_1, grade_2, grade_3)

# lowest_grade = 0

# if(course_1 < course_2):
#     lowest_grade = course_1
# if(course_2 < course_3):
#     lowest_grade = course_2
# if(course_3 < course_1):
#     lowest_grade = course_3

# highest_grade = 0

# if(course_1 > course_2):
#     highest_grade = course_1
# if(course_2 > course_3):
#     highest_grade = course_2
# if(course_3 > course_1):
#    highest_grade = course_3

# print("Lowest grade is: ", lowest_grade)
# print("Highest grade is: ", highest_grade)

# 2.11 --------------------- Calculating Time --------------------- 

# number_of_seconds = int(input("Number of seconds: "))
# hours = number_of_seconds // 3600
# minutes = (number_of_seconds % 3600) // 60
# seconds = number_of_seconds % 60
# print(hours, "-", minutes, "-", seconds)

# 2.12 --------------------- Hourly Wage Calculator --------------------- 

# hourly_wage = 10
# raise_wage = 0.03
# good_years = 5
# bad_years = 2

# increase_hourly_wage = hourly_wage * ((1 + raise_wage)**good_years)
# decrease_hourly_wage = hourly_wage * ((1 + raise_wage)**bad_years)

# new_hourly_wage = hourly_wage + increase_hourly_wage - decrease_hourly_wage
# print("New hourly wage: ", new_hourly_wage)

# 2.14 --------------------- Target Heart-Rate Calculator --------------------- 

# age = int(input("Enter your age: "))
# max_heart_rate = 220 - age  
# print("Maximum heart rate: ", max_heart_rate)

# lowest_heart_rate = max_heart_rate * 50 / 100
# highest_heart_rate = max_heart_rate * 85 / 100
# print("Range of your target heart rate: [", lowest_heart_rate, "-", highest_heart_rate, "]")

# 2.15 --------------------- Sort in Ascending Order --------------------- 

# print("----------Runner 1----------")
# time_runner1_1 = float(input("Enter first time in seconds: "))
# time_runner1_2 = float(input("Enter second runner in seconds: "))
# time_runner1_3 = float(input("Enter third runner in seconds: "))
# min_runner1 = min(time_runner1_1, time_runner1_2, time_runner1_3)
# max_runner1 = max(time_runner1_1, time_runner1_2, time_runner1_3)
# middle_runner1 = 0
# if(time_runner1_1 != min_runner1):
#     if(time_runner1_1 != max_runner1):
#         middle_runner1 = time_runner1_1
# if(time_runner1_2 != min_runner1):
#     if(time_runner1_2 != max_runner1):
#         middle_runner1 = time_runner1_2
# if(time_runner1_3 != min_runner1):
#     if(time_runner1_3 != max_runner1):
#         middle_runner1 = time_runner1_3

# print("\n----------Runner 2----------")
# time_runner2_1 = float(input("Enter first time in seconds: "))
# time_runner2_2 = float(input("Enter second runner in seconds: "))
# time_runner2_3 = float(input("Enter third runner in seconds: "))
# min_runner2 = min(time_runner2_1, time_runner2_2, time_runner2_3)
# max_runner2 = max(time_runner2_1, time_runner2_2, time_runner2_3)
# middle_runner2 = 0
# if(time_runner2_1 != min_runner1):
#     if(time_runner2_1 != max_runner2):
#         middle_runner2 = time_runner2_1
# if(time_runner2_2 != min_runner2):
#     if(time_runner2_2 != max_runner2):
#         middle_runner2 = time_runner2_2
# if(time_runner2_3 != min_runner2):
#     if(time_runner2_3 != max_runner2):
#         middle_runner2 = time_runner2_3

# print("\n----------Runner 3----------")
# time_runner3_1 = float(input("Enter first time in seconds: "))
# time_runner3_2 = float(input("Enter second runner in seconds: "))
# time_runner3_3 = float(input("Enter third runner in seconds: "))
# min_runner3 = min(time_runner3_1, time_runner3_2, time_runner3_3)
# max_runner3 = max(time_runner3_1, time_runner3_2, time_runner3_3)
# middle_runner3 = 0
# if(time_runner3_1 != min_runner3):
#     if(time_runner3_1 != max_runner3):
#         middle_runner3 = time_runner3_1
# if(time_runner3_2 != min_runner3):
#     if(time_runner3_2 != max_runner3):
#         middle_runner3 = time_runner3_2
# if(time_runner3_3 != min_runner3):
#     if(time_runner3_3 != max_runner3):
#         middle_runner3 = time_runner3_3

# print("Times in increasing order for runner 1: ", min_runner1, "-", middle_runner1, "-", max_runner1)
# print("Times in increasing order for runner 2: ", min_runner2, "-", middle_runner2, "-", max_runner2)
# print("Times in increasing order for runner 3: ", min_runner3, "-", middle_runner3, "-", max_runner3)
