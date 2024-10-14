import itertools
import random

# Create a deck of cards
carddeck = list(itertools.product(range(1, 14), ["Spade", "Club", "Diamond", "Heart"]))

def card(n):
    # Shuffle the deck and deal n cards
    local_deck = carddeck.copy()  # Use a copy of the original deck
    random.shuffle(local_deck)
    for i in range(n):
        print(local_deck[i][0], local_deck[i][1])
        local_deck.remove(local_deck[i])

# Deal 4 cards initially
card(4)

print("\nPress 1 to shuffle cards")
print("Press 2 to exit\n")

choice = int(input("Enter a choice: "))
if choice == 1:
    print("Shuffled Cards:")
    card(4)
elif choice == 2:
    print("Exited")
else:
    print("Invalid Choice")
