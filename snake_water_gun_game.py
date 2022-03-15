print("\t Welcome to Snake Water Gun game")
print("Rules of the game")
print("\t snake kills water")
print("\t water kills gun")
print("\t Gun kills snake")
print("\t\t How to play")
print("player enters snake/water/gun  and according to the condition game moves forward")


import random
user_points=0
com_points=0

n = int(input("Enter number of rounds: "))

lst=['snake','water','gun']
rounds =1

while rounds <=n:
    print(f"Round:{rounds}")
#player input and invalid input handling
    player=input("Enter snake water gun: ").lower()
    if player not in('snake','water','gun'):
        print("Invalid input")
        continue
#computer input
    comp= random.choice(lst)
    print("com",comp)

    if comp==player:
        user_points+=0
        com_points+=0
        print("Round Draw")

    if comp=='snake' and player=='water':
        com_points+=1
    elif comp=='snake' and player=='gun':
        user_points+=1
    elif comp=='water' and player=='gun':
        com_points+=1
    elif comp=='water' and player=='snake':
        user_points+=1
    elif comp=='gun' and player=='water':
        user_points+=1
    elif comp=='gun' and player=='snake':
        com_points+=1

    # every round winner
#     if user_points > com_points:
#         print(f"player wins round {rounds}")
#     elif comp==player:
#         print("Draw")
#     else:
#         print(f"com wins round {rounds}")
#     rounds+=1
# Final winner

if user_points > com_points:
    print("you win")
elif user_points < com_points:
    print("you loose")
else:
    print("Draw")
