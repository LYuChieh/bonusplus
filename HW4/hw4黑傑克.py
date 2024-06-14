import random
ranks=["ACE","2","3","4","5","6","7","8","9","10","JACK","QUEEN","KING"]
suits=["SPADE","HEART","DIAMOND","CLUB"]
def createshuffledeck():
    deck=[]
    for r in ranks:
        for s in suits:
            deck.append(r+"-"+s)
    random.shuffle(deck)
    return deck
deck=createshuffledeck()
def draw(deck):
    i=1
    cards=[]
    while i<3:
        card=deck.pop(0)
        cards.append(card)
        i=i+1
    return cards
def draw1(deck):
    card1=deck.pop(0)
    return card1
v,n=deck[0].split("-")
v1,n1=deck[1].split("-")
        #現在的問題是要怎麼算出兩張卡的值
print("with the hand: ",",".join(draw(deck)))
print()
while True:
    b=input("Hit or stay? (Hit=1,stay=0): ")
    if b=="1":
        print("You draw ",draw1(deck))
    if b=="0":
        break
print("Dealer's with the hand: ",",".join(draw(deck)))
