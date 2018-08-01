#Saha p144 #4

import random


class card(object):
    def __init__(self, number, suit, rank):
        self.number=number
        self.suit=suit
        self.rank=rank
        

cardarray=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,
          26,27,28,29,30,31,31,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54]
          

deck=[card(0," ", " ") for i in range(1,55)]

for x in range(1,14):
    if(x == 1):
        deck[x]=card(x,"clubs", "ace")
    elif(x==11):
        deck[x]=card(x,"clubs", "jack")
    elif(x==12):
        deck[x]=card(x,"clubs", "queen")
    elif(x==13):
        deck[x]=card(x,"clubs", "king")      
    else:
        r=str(x)
        deck[x]=card(x,"clubs", r)
        
for x in range(14,28):
    if(x == 14):
        deck[x]=card(x,"spades", "ace")
    elif(x==25):
        deck[x]=card(x,"spades", "jack")
    elif(x==26):
        deck[x]=card(x,"spades", "queen")
    elif(x==27):
        deck[x]=card(x,"spades", "king")
    else:
        r=str(x-14)
        deck[x]=card(x,"spades", r)
        
for x in range(28,41):
    if(x == 28):
        deck[x]=card(x,"diamonds", "ace")
    elif(x==38):
        deck[x]=card(x,"diamonds", "jack")
    elif(x==39):
        deck[x]=card(x,"diamonds", "queen")
    elif(x==40):
        deck[x]=card(x,"diamonds", "king")
    else:
       r=str(x-27)
       deck[x]=card(x,"diamonds", r)
        
for x in range(41,54):
    if(x ==41):
        deck[x]=card(x,"hearts", "ace")
    elif(x==51):
        deck[x]=card(x,"hearts", "jack")
    elif(x==52):
        deck[x]=card(x,"hearts", "queen")
    elif(x==53):
        deck[x]=card(x,"hearts", "king")
    else:
        r=str(x-40)
        deck[x]=card(x,"hearts", r)
    
random.shuffle(cardarray)
i=1
k=1
for i in range(1,54):
    temp=cardarray[i]
    for k in range(1,54):
        if(deck[k].number == temp):
            print(temp)
            print(deck[k].suit)
            print(deck[k].rank)
    print("\n")
    
        
    

    


