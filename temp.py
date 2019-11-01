# -*- coding: utf-8 -*-
"""
Spyderエディタ

これは一時的なスクリプトファイルです
    
"""
# =============================================================================
# greeting = "Hi there "
# name = "Iqbal"
# greet = gretting + name
# print(greet)    
# silly = greeting + (" "+ name)*3
# print(silly)
# 
# =============================================================================
# =============================================================================
# x = 3
# print(x)
# x_str = str(x)
# print(x_str)
# print("my fav num is", x, ".", "x = ", x)
# print("my fav num is"+ x_str+ ". "+ "x = "+ x_str)
# =============================================================================

# =============================================================================
# if 1==2:
#     text = input("Nandemo kaite kudasai....")
#     print(5*text)
# elif 1==1:
#     num = int(input("bango o Kaite kudasai..."))
#     print(5*num)
# 
# =============================================================================
# =============================================================================
# n = input("You are in the lost forest,,,, go left or right?\n")
# while n=="right" or  n=="left":
#     n = input("You are in the lost forest,,,, go left or right?\n")
#     
# =============================================================================
# =============================================================================
# mysum= 0
# for i in range(7, 10):
#     mysum+= i
#     print(mysum)
# =============================================================================
# =============================================================================
#     
# s  = "Iqbal Ahmad Kabir San"
# print(len(s))
# print(s [::-1])
#     
# =============================================================================
# =============================================================================
# s  = "Iqbal Ahmad Kabir San"
# 
# for char in s:
#     if char == 'I':
#         print("Iqbal ")  
#     elif   char == 'A':
#         print("Ahmad")
#     elif char == 'K':
#         print("Kabir")
# =============================================================================
 
# Robots cheerleaders code
# =============================================================================
# anLetters = "aefhilmnorsxAEFHILMNORSX"
# word = input("I will cheer for you if you enter a word....")
# times = int( input("Enthusiasm level (1~10) : "))
# =============================================================================
# =============================================================================
# 
# #i = 0
# for char in word:
#     
#     if char in anLetters:
#         print("Give me an " + char + "!" + char)
#     else:
#         print("Give me an " + char + "!" + char)
# 
#    
# print("What that spell??")
# for char in range(times):
#     print(word, "!!!")
# 
# 
# =============================================================================

# Guess & Check Algorithm
# =============================================================================
# cube = int(input("please give a number to check perfect cube or not,,,"))
# 
# for guess in range(abs(cube)+1):
#      if guess**3 >= abs(cube):
#          break # guess is updated and break
#          
# if guess**3 != abs(cube):
#     print(cube, "Its not perfect cube!!")
# else:
#     if cube < 0:
#         guess = -guess
#     print("Cube root of " + str(cube) + " is " + str(guess))
# =============================================================================
# =============================================================================
# 
# cube = 27
# cube =  8120601
# #cube = 10000
# 
# eps = 0.01
# guess = 0.0 
# increment = 0.0001
# num_guesses = 0
# 
# while abs(guess**3 - cube) >= eps and guess <= cube:
#     guess += increment
#     num_guesses += 1
# print("num_guesses= ", num_guesses)
# if abs(guess**3 - cube) >= eps:
#     print("Failed!!!")
# else:
#     print(guess, "is close to the cube root of ", cube)
# 
# 
# =============================================================================
#Proble 0
# =============================================================================
# import math
# 
# x = int(input("X = "))
# y = int(input("Y = "))
# print("X^Y is ",x**y)
# print("log(",x,") is ",math.log(x,2))
# 
# =============================================================================

#Problem 1

# Part A House Hunting----------------------------------------------------------------
# =============================================================================
# current_savings = 0
# r_rate = 0.04
# 
# annual_salary = int(input("Enter your annual salary:"))
# monthly_salary = annual_salary/12
# 
# percent = float(input("Enter the percent of your salary to save, as a decimal: "))
# saving_salary = monthly_salary * percent
# 
# cost_of_house = int(input("Enter the cost of your dream home:"))
# down_payment = cost_of_house * 0.25
# 
# months = 0
# while current_savings <= down_payment:
#     current_savings += saving_salary + current_savings * ((r_rate)/12)
#     months += 1
#     
#     #print("months ",months,"savings",current_savings)
#     
# print("Number of months: ",months)
# =============================================================================
#Part A end---------------------------------------------------------------

# =============================================================================
# #Part B Saving, with a raise------------------------------------------------------------------
# current_savings = 0
# r_rate = 0.04
# 
# annual_salary = int(input("Enter your annual salary:"))
# monthly_salary = annual_salary/12
# 
# percent = float(input("Enter the percent of your salary to save, as a decimal: "))
# saving_salary = monthly_salary * percent
# 
# cost_of_house = int(input("Enter the cost of your dream home:"))
# down_payment = cost_of_house * 0.25
# 
# semi_annual = float(input("Enter the semi­annual raise, as a decimal:"))
# 
# months = 0
# while current_savings <= down_payment:
#     current_savings += saving_salary + current_savings * (r_rate/12)
#     months += 1
#    
#     if( months%6 )== 0 : # after six months
#         annual_salary += (annual_salary*semi_annual)
#         monthly_salary = annual_salary/12
#         saving_salary = monthly_salary * percent
#    
#     
# print("Number of months: ",months)
# 
# #Part B end-----------------------------------------------------------------
# =============================================================================

#Part C Finding the right amount to save away











   
    
    