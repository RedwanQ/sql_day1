import random
class Blackjack():
    
    def __init__(self, score):
        self.score = 0
        
    
    def game_start():
        print(f"you have {hand}")

        print(f"Dealer has {hand} ")

    def player():
        pass
    def dealer():
        pass
    
class Card(Blackjack):
    
    cards = [] 
    
    def main_deck():
        
        for f in ["A", "Q", "K", "J"]:
            for n in range(1, 11):
                Card.cards.append(f,n)
                
    def deck_shuffle():

        random.shuffle(Card.cards)

    def sample_hand():

        hand = random.sample(Card(cards, k=2))
        


def run_game():

    while True:
        user = input('Do you want to play Blackjack? Y/N').lower()
        if user == 'n':
            print('Come back soon!')
        elif user == 'y':
            Blackjack.game_start
        else:
            return ('Invaild response, please try again.')

