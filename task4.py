import random
def get_choices():
    player_choice= input("enter a choice (rock,paper,scissor) = ")
    options=["rock","paper","scissor"]
    computer_choice= random.choice(options)
    choices={"player": player_choice, "computer": computer_choice}
    return choices

choices=get_choices()
print(choices)

def check_win(player,computer):
    print(f"You chose  {player} , Computer chose  {computer}") #fstring
    if player==computer:
     return "Its a tie"
    elif player=="rock" :
      if computer=="scissor":
         return "rock smashes scissors. You win!"
      else:
         return "paper covers rock. You lose."

    elif player=="paper" :
      if computer=="rock":
         return "paper covers rock. You win!"
      else:
         return "scissors cut paper. You lose."    
     
    elif player=="scissors" :
      if computer=="paper":
         return "scissors cut paper. You win!"
      else:
         return "Rock smashes scissors. You lose."


choices = get_choices()
result = check_win(choices["player"],choices["computer"])
print(result)

