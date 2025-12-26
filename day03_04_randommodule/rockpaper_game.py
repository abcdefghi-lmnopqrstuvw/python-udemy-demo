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
game=["rock","paper","scissors"]
img=[rock,paper,scissors]

user = int(input("chose 0 for rock, 1 for paper, 2 for scissors.\n"))
if user>2 or user<0:
    print("invalid choice")
    exit()
print("you chose:\n",img[user])

comp=random.randint(0,2)
print("computer chose:\n",img[comp])

if comp==user:
    print("tie")
elif user==2 and comp==0:
    print("you lose")
elif user>comp or (user==0 and comp==2):
    print("you win")
else:
    print("you lose")
