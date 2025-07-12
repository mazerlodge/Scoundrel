import random

# make a list of 52
deck = list(range(1,53))

f1count=0
faceidx = 12
for x in range(1,53):
    xs = x % 4
    xf = x % 13
    print(f"x = {x} mod 4 = {xs}  face = {xf}")

# shuffle
shuffledDeck = []
rnd = random.Random()
for maxidx in range (52, 1, -1):
    idx = rnd.randrange(0,maxidx)
    shuffledDeck.append(deck.pop(idx))

# put last value on shuffled output
shuffledDeck.append(deck[0])

print(shuffledDeck)