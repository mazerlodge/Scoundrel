import random

# make a list of 52
deck = list(range(1,53))
suits = ['d', 'h', 'c', 's']


def getSuit(card):
    # return suit assoc w/ card
   
    return(suits[card % 4])

def getFace(card):
    # return face assoc w/ card
    fval = card % 13
    rval = str(fval+1)

    specialFaces = ['A', 'T', 'J', 'Q', 'K']

    if (fval == 0):
        rval = specialFaces[fval]
    else:
        if (fval > 8):
            rval = specialFaces[fval-8]
   
    return rval

def getCardString(card):
    # return numeric card (e.g. 37 as string like Qs)    

    rval = getFace(card) + getSuit(card)

    return rval


f1count=0
faceidx = 12
for x in range(1,53):
    xs = x % 4
    xf = x % 13
    cs = getCardString(x)
    print(f"x = {x} mod 4 = {xs}  face = {xf} cardString={cs}")

# shuffle
shuffledDeck = []
rnd = random.Random()
for maxidx in range (52, 1, -1):
    idx = rnd.randrange(0,maxidx)
    shuffledDeck.append(deck.pop(idx))

# put last value on shuffled output
shuffledDeck.append(deck[0])

print(shuffledDeck)
