import random

def create_deck():
    suits = ["♥", "♦", "♣", "♠"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    deck = [(suit, rank) for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

def draw_card(deck, num_cards):
    hand = [deck.pop() for _ in range(num_cards) if deck]
    return hand, deck

def show_card(card):
    rank, suit = card
    if len(rank) == 1:
        rank = rank + " "
    print (f"""
    +-------+
    |{rank}     |
    |       |
    |   {suit}   |
    |       |
    |     {rank}|
    +-------+
    """)

deck = create_deck()

while len(deck) > 0:
    num_cards = int(input("How many cards do you want to draw? "))
    if num_cards <= len(deck):
        hand, deck = draw_card(deck, num_cards)
        for card in hand:
            show_card(card)
    else:
        print("Not enough cards in the deck.")

print("We are out of cards")
