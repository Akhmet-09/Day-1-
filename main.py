# 1
# color = input('Enter the color : ')
# x  = color.lower()
# if x == 'red':
#     print('Stop!')
# elif x == 'yellow':
#     print('Slow down!')
# elif x == 'green':
#     print('Go!')
# else:
#     print('Invalid Color ')

# 2
# number = int(input('Enter a number : '))
# if number<0:
#     print('Negative Number ')
# elif number==0:
#     print('Zero ')
# elif number % 2 == 0:
#     print('Postive Even ')
# else:
#    print('Positive Odd')

# 3
# import random 
# score = random.randint(1,101)
# if score >=90 and score <=100 :
#     print('A')
# elif score >= 80 and score <=89:
#     print('B ')
# elif score>=70 and score <=79 :
#     print('C')
# elif score>=60 and score<=69:
#     print('D')
# else:
#     print('F')

# 4
# age  = int(input('Enter your  budget : '))
# if age<=5 :
#     print('Free')
# elif age>=5 and age<=17:
#     print('8$')
# elif age >=18 and age <=64 :
#     print('15$')
# else:
#     print('10$')

# 1
# temp = int(input('Enter the temperature :  '))
# raining = bool()
# if temp<10 and raining is True :
#     print(f"Wear a heavy winter coat and bring an umbrella!\nRaining : {raining}")
# elif temp<=10 and raining is False :
#     print(f"Wear a heavy winter coat, no umbrella needed. \nRaining : {raining}")
# elif temp>=10 and temp<=20 and raining is True :
#     print(f"Wear a jacket and bring an umbrella. \nRaining : {raining}")
# elif temp>=10 and temp<20 and raining is False : 
#     print(f"Wear a jacket and bring an umbrella. \nRaining : {raining}")
# else:
#     print(f"It's warm! Wear a t-shirt.\nRaining : {raining}")


# amount = int(input('Enter your total amount of purchase : '))
# is_member = input('Are a loyal member : (yes/no)').lower()
# if is_member == 'yes':
#     if amount>=50:
#         discount = 0.20
#     else:
#         discount  = 0.10
# else:
#     if amount>=100:
#         discount =0.05
#     else:
#         discount = 0.0
# final_price = amount * (91-discount )
# print(f"Discount: {int(discount*100)}%")        
# print(f"Final Price To Pay :${final_price }")

# Exercise 1 
# password = input("Enter a password: ")
# length = len(password)
# has_num = False
# has_let = False
# for c in password:
#   if c.isdigit():
#     has_num = True
#   if c.isalpha():
#     has_let = True
# if length < 6:
#   print("Strength: Very Weak (Too short)")
# elif length >= 10 and has_let and has_num:
#   print("Strength: Strong (Long and mixed)")
# elif length >= 6 and has_num:
#   print("Strength: Medium (Has numbers)")
# elif 6 <= length <= 9 and has_let and not has_num:
#   print("Strength: Weak (Letters only)")
# else:
#   print("Strength: Medium")

# Exercise 2 
import random

player = input("Enter rock, paper, or scissors: ").lower()

# Computer's random choice
options = ["rock", "paper", "scissors"]
computer = random.choice(options)
print(f"Computer chose: {computer}")

# Game logic
if player not in options:
  print("Invalid choice! Please type rock, paper, or scissors.")
elif player == computer:
  print("It's a tie!")
elif (
    (player == "rock" and computer == "scissors")
    or (player == "scissors" and computer == "paper")
    or (player == "paper" and computer == "rock")
):
  print("You win! 🎉")
else:
  print("Computer wins! 🤖")











