import Art, random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
print(Art.logo1)

def assigning_cards():
    user = []
    computer = []
    user = random.sample(cards,2)
    computer = random.sample(cards, 2)
    return user, computer
 
def calculations(cards):
    cards = sum(cards)
    if cards == 21:
        return 0

    if 11 in user_cards and cards > 21:
        user_cards.remove(11)
        user_cards.append(1)
    return cards
    

def compare(user_score, computer_score):
    if user_score == 21:
        return "You Win"
    elif computer_score == 21:
        return "You Lose"
    elif user_score == 0:
        return "You Win with blackjack"
    elif computer_score == 0:
        return"You lose. Computer had blackjack."
    elif user_score == computer_score:
        return "It's a draw"
    elif user_score > 21:
        return "You went over. You lose."
    elif computer_score > 21:
        return "Computer went over. You WIN!!"
    elif user_score > computer_score:
        return "You WIN!!"
    else:
        return "Computer had bigger score. You lose."

#start of game
choice = str(input("Type 'y' to play blackjack. Else Type 'n'.\n")).lower()
if choice == 'y':
    play_game = True
else:
    play_game = False
user_cards, computer_cards = assigning_cards()

#main part of game for computing scores and to get more cards
while play_game:
    
    user_score = calculations(user_cards)
    computer_score = calculations(computer_cards)
    print(f"Your cards are {user_cards}. Your score is {user_score}")
    print(f"The computers first card is {computer_cards[0]}")

    if user_score == 0 or user_score > 21 or computer_score == 0:
        play_game = False

    else:
        dealing_card = str(input("Type 'y' if you want another card. Else type 'n'\n")).lower()
        if dealing_card == 'y':
            user_cards.append(random.choice(cards))
            user_score = calculations(user_cards)
        else:
            play_game = False
# have dealer draw more cards
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(random.choice(cards))
        computer_score = calculations(computer_cards)

    print(f"You had {user_cards} with a score of {user_score}") 
    print(f"The computer had {computer_cards}")
    print(compare(user_score, computer_score))
