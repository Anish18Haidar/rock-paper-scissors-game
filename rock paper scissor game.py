import random
item_list = ["Rock", "Paper", "Scissor"]
user_choice = input("Enter your move = Rock, Paper, Scissor: ")
comp_choice = random.choice(item_list)
print(f"user choice = {user_choice}, computer choice = {comp_choice}")
if user_choice == comp_choice:
    print("Both chooses same = Match Tie")
elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper covers Rock = computer win")
    else:
        print("Rock smashes Scissor = you win")
elif user_choice == "Paper":
    if comp_choice == "Scissor":
        print("Scissor cuts Paper = computer win")
    else:
        print("Paper covers Rock = you win")         
elif user_choice == "Scissor":
    if comp_choice == "Paper":
        print("Scissor cuts Paper = you win")
    else:
        print("Rock smashes Scissor = computer win")


