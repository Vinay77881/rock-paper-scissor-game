import random
Rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''
Paper='''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

Scissors='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game=[Rock,Paper,Scissors]
print("0 for rock\n1 for paper\n2 for scissor\n")
user_choice=int(input("Enter your choice: "))
computer_choice=random.randint(0,2)
if(user_choice>=0 and user_choice<=2):
    print(game[user_choice])
    print()
    print(f"computer choice is {computer_choice}")
    print(game[computer_choice])
    if((user_choice>=0 and user_choice<=2)):
        if(user_choice==computer_choice):
            print("Draw")
        elif(user_choice==0 and computer_choice==2):
            print("You Win")
        elif(user_choice==2 and computer_choice==0):
            print("You Lose")
        elif(user_choice < computer_choice):
            print("You Lose")
        elif(user_choice > computer_choice):
            print("You Win")
else:
    print("Enter correct choice")