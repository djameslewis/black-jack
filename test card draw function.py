#testcard draw function
#attempting to get card object to work

import random

class card:
    def __init__(att, suit, number, face):
        att.suit = suit
        att.number = number
        att.face = face



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
    

def generate_card():
    num = get_number()
    if num == 10:
        face = get_face()
    else:
        face = ''

    drawn_card = card(get_suit(), num, face)
    print("suit: ",drawn_card.suit)
    print("number: ",drawn_card.number)
    if drawn_card.face != '':
        print("face: ",drawn_card.face)
    else:
        ''

generate_card()
print ("card 2:")
generate_card()