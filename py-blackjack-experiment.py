import random

##progress marker = duplicate check needs to be checked, just got the card_total working
# To Do: cpu_move() 20% done, check_card = 80% done

cpu_hand = []
user_hand = []
cards_in_play_number = []
cards_in_play_suit = []
cards_in_play_face = []



#att = attributes/card attributes, 
class card:
    def __init__(att, suit, number, face):
        att.suit = suit
        att.number = number
        att.face = face

        
def user_move():
    print("you have ", card_total(user_hand), "\nthe cpu has ", card_total(cpu_hand),"\nWhats the move?")
    user_move = input()
    if user_move.lower() == "hit":
        user_card = generate_card()
        check_card(user_card)
        cards_in_play_number.append(user_card.number)
        cards_in_play_suit.append(user_card.suit)
        cards_in_play_face.append(user_card.face)
        user_hand.append(user_card)
        print("user drew: ", user_card.number, user_card.suit,user_card.face, "new total = ", card_total(user_hand))
        #cpu_move()
    elif user_move.lower() == "stand":
        print("no balls.\nyou have ",user_hand,"\ncpu has ",cpu_hand)
        cpu_move()
    else:
        print("enter hit or stand (no split functionality yet)")

def start_game():
    user_card = generate_card()
    check_card(user_card)
    print("user drew: ", user_card.number, user_card.suit,user_card.face)
    user_hand.append(user_card)
    # print("test ---- user hand is holding: ", user_hand[0].number, user_hand[0].suit, user_hand[0].face)
    cards_in_play_number.append(user_card.number)
    cards_in_play_suit.append(user_card.suit)
    cards_in_play_face.append(user_card.face)
    cpu_card = generate_card()
    check_card(cpu_card)
    print("cpu drew: ",cpu_card.number, cpu_card.suit,cpu_card.face)
    cpu_hand.append(cpu_card)
    cards_in_play_number.append(cpu_card.number)
    cards_in_play_suit.append(cpu_card.suit)
    cards_in_play_face.append(cpu_card.face)
    user_card2 = generate_card()
    check_card(user_card2)
    cards_in_play_number.append(user_card2.number)
    cards_in_play_suit.append(user_card2.suit)
    cards_in_play_face.append(user_card2.face)
    print("user drew: ", user_card2.number, user_card2.suit,user_card2.face)
    user_hand.append(user_card2)
    user_move()

def check_card(card):
    #print("entering card check function")
    if card.number in cards_in_play_number:
        #print("SAME NUMBER")
        if card.suit in cards_in_play_suit:
           # print("DUPE bar face")
            if card.face in cards_in_play_face:
                #print("CARD WAS DUPE")
                card = generate_card()
                return card
            else:
                return card
        else:
            return card
    else:
        return card

def cpu_move():
    ##if card_total(cpu_hand) < 16 and card_total(user_hand) > card_total(cpu_hand):
      ##  print("You Win")
    ##else:
    cpu_card = generate_card()
    check_card(cpu_card)
    print("cpu drew: ",cpu_card.number, cpu_card.suit,cpu_card.face)
    cpu_hand.append(cpu_card)
    cards_in_play_number.append(cpu_card.number)
    cards_in_play_suit.append(cpu_card.suit)
    cards_in_play_face.append(cpu_card.face)
    user_move()

### Card drawing logic

def get_suit():
    drawn_suit = random.randint(1,4)
    if drawn_suit == 1:
        return 'Clubs'
    elif drawn_suit == 2:
        return 'Hearts'
    elif drawn_suit == 3:
        return 'Spades'
    else:
        return 'Diamonds'
    
def get_number():
    return random.randint(1,10)

def get_face():
    drawn_face = random.randint(1,3)
    if drawn_face == 1:
        return 'K'
    elif drawn_face == 2:
        return 'Q'
    elif drawn_face == 3:
        return 'J'
    else:
        return ''
    
def card_total(hand):
    i = 0
    count = 0
    while i < len(hand):
        count += hand[i].number
        i += 1
    print ("count = ", count)
    return count
    

def generate_card():
    num = get_number()
    if num == 10:
        face = get_face()
    else:
        face = ''

    drawn_card = card(get_suit(), num, face)
    #testing print("suit: ",drawn_card.suit)
    #testing print("number: ",drawn_card.number)
    #testing if drawn_card.face != '':
        #testing return 
        # testing print("face: ",drawn_card.face)
    #testing else:
#testing         ''

    return drawn_card

start_game()