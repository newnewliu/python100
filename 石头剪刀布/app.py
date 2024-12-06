import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
rps = [scissors, rock, paper]
user_original_choice = input("出招：1 for 剪刀，2 for 石头，3 for 布")
check = len(user_original_choice)

if check > 1:
    print("别耍我")

else:
    user_choice = int(user_original_choice)
    print(rps[user_choice - 1])
    computer_choice = random.randint(1,3)
    print("电脑选择：" + rps[computer_choice - 1])
    if user_choice == computer_choice :
        print("平局")
    elif user_choice - computer_choice == 1 :
        print("你赢了")
    elif computer_choice - user_choice == 2 :
        print("你赢了")
    else:
        print("你输了")
