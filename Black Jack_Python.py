import Art, random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def assigning_cards():
    user = []
    computer = []
    user = random.sample(cards,2)
    computer = random.sample(cards, 2)
    print(f"Your cards are {user}\nThe computers cards are {computer}")

    return user, computer
 
def calculations(user_cards, computer_cards):
    sum_user = sum(user_cards)
    sum_computer = sum(computer_cards)
    print(sum_user,sum_computer)

def continue_playing(choice):
    if choice == 'n':
        play_game = False
        return play_game
    else:
        return True
#def user_hit_or_stand(choice):



choice = str(input("Type 'y' to play blackjack. Else Type 'n'.\n")).lower()
if choice == 'y':
    play_game = True

while play_game:
    user_cards, computer_cards = assigning_cards()
    calculations(user_cards, computer_cards)
    
    choice = str(input("Type 'y' to continue or type 'n' to stop\n")).lower()
    play_game = continue_playing(choice)
  
