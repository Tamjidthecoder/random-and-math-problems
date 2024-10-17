import random
options=["Rock","paper","scissors"]
user1=input("choose rock,paper or scissors")
user2=input("choose rock,paper or scissors")
print("user1 choice",user1)
print("user2 choice",user2)
if user1=='rock' and user2=='paper':
    print('user2 wins')
if user1=='paper' and user2=='rock':
    print('user1 wins')
if user1=='rock' and user2=='scissors':
    print('user1 wins')
if user1=='scissors' and user2=='rock':
    print('user2 wins')
if user1=='scissors' and user2=='paper':
    print('user1 wins')
if user1=='paper' and user2=='scissors':
    print('user2 wins')
else:
    print("draw")