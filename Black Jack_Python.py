import Art, random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
print(Art.logo1)

def assigning_cards():
    user = []
    computer = []
    user = random.sample(cards,2)
    computer = random.sample(cards, 2)
    return user, computer
 
def calculations(user_cards, computer_cards):
    sum_user = sum(user_cards)
    sum_computer = sum(computer_cards)
    if 11 in user_cards and sum_user > 21:
        user_cards.remove(11)
        user_cards.append(1)
    return sum_user, sum_computer

def continue_playing(choice):
    if choice == 'n':
        play_game = False
        return play_game
    else:
        return True
    

def compare(sum_user, sum_computer):
    if sum_user == 21:
        print("You Win")
    elif sum_computer == 21:
        print("You Lose")
    else:
        return True




choice = str(input("Type 'y' to play blackjack. Else Type 'n'.\n")).lower()
if choice == 'y':
    play_game = True

while play_game:
    user_cards, computer_cards = assigning_cards()
    sum_user, sum_computer = calculations(user_cards, computer_cards)
    compare(sum_user,sum_computer)
    print(f"Your cards are {user_cards}. Your score is {sum_user}")
    print(f"The computers first card is {computer_cards[0]}")
    
    choice = str(input("Type 'y' to continue or type 'n' to stop\n")).lower()
    play_game = continue_playing(choice)
  
