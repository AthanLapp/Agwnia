import random

cardsnumbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52]
cardsnames = ["Ace Clubs", "2 Clubs","3 Clubs","4 Clubs","5 Clubs","6 Clubs","7 Clubs","8 Clubs","9 Clubs","10 Clubs","Jack Clubs","Queen Clubs","King Clubs","Ace Diamonds", "2 Diamonds","3 Diamonds","4 Diamonds","5 Diamonds","6 Diamonds","7 Diamonds","8 Diamonds","9 Diamonds","10 Diamonds","Jack Diamonds","Queen Diamonds","King Diamonds","Ace Hearts", "2 Hearts","3 Hearts","4 Hearts","5 Hearts","6 Hearts","7 Hearts","8 Hearts","9 Hearts","10 Hearts","Jack Hearts","Queen Hearts","King Hearts","Ace Spades", "2 Spades","3 Spades","4 Spades","5 Spades","6 Spades","7 Spades","8 Spades","9 Spades","10 Spades","Jack Spades","Queen Spades","King Spades"]

# Shuffling deck

deck = random.sample(cardsnumbers,k=52)
i=0
decknames = []
for i in range(0,52):
        decknames.append(cardsnames[deck[i]-1])

##Show cards
##        
##for i in range(0,52):
##       print(deck[i], decknames[i], i+1)

#Game with one player against the computer
cardsplayer=[]
cardscomputer=[]
cardsplayer.append(deck[51])
cardsplayer.append(deck[50])
cardscomputer.append(deck[49])
cardscomputer.append(deck[48])
cardsplayer.append(deck[47])
cardsplayer.append(deck[46])
cardsplayer.append(deck[45])
cardscomputer.append(deck[44])
cardscomputer.append(deck[43])
cardscomputer.append(deck[42])
cardsplayer.append(deck[41])
cardsplayer.append(deck[40])
cardscomputer.append(deck[39])
cardscomputer.append(deck[38])
drawncard=deck[37]
deckn=36
#Print hand
#for i in range(len(cardsplayer)):
#       print("card", i + 1,":", cardsnames[cardsplayer[i]-1])

# GAME LOOP
while (len(cardsplayer)>0 and len(cardscomputer)>0):
        for i in range(len(cardsplayer)):
                print("card", i + 1,":", cardsnames[cardsplayer[i]-1])
        print("Card on Table:", cardsnames[drawncard-1])
        playc=input("Select card number to play or press enter to draw a card")
        if playc == "":
                print("Card drawn:", cardsnames[deck[deckn]-1])
                cardsplayer.append(deck[deckn])
                deckn-=1
        else:
                drawncard = cardsplayer.pop(int(playc)-1)

        while drawncard%13  == 9 or drawncard%13  == 8:
                for i in range(len(cardsplayer)):
                        print("card", i + 1,":", cardsnames[cardsplayer[i]-1])
                print("Card on Table:", cardsnames[drawncard-1])
                playc=input("Select card number to play or press enter to draw a card")
                if playc == "":
                        print("Card drawn:", cardsnames[deck[deckn]-1])
                        cardsplayer.append(deck[deckn])
                        deckn-=1
                else:
                        drawncard = cardsplayer.pop(int(playc)-1)

        if drawncard == 1 or drawncard == 14 or drawncard == 27 or drawncard == 40 and (playc != ""):
                playc=int(input("press 1:Clubs,2:Diamonds,3:Hearts,4:Spades"))
                if playc == 1:
                        drawncard = 1
                elif playc == 2:
                        drawncard = 14
                elif playc == 3:
                        drawncard = 27
                elif playc == 4:
                        drawncard = 40
                
        if drawncard%13  == 7:
                if 7 not in cardscomputer and 20 not in cardscomputer and 33 not in cardscomputer and 46 not in cardscomputer:
                        cardscomputer.append(deck[deckn])
                        deckn-=1
                        cardscomputer.append(deck[deckn])
                        deckn-=1
                else:
                        skip=False
                        while not skip:
                                for i in range(len(cardscomputer)):
                                        if not skip:
                                                if cardscomputer[i]%13==drawncard%13:
                                                        drawncard = cardscomputer.pop(i)
                                                        skip=True
                                                        break
                                                elif i == len(cardscomputer)-1:
                                                        cardscomputer.append(deck[deckn])
                                                        deckn-=1
                                                        skip = True
                                                        break
                                                elif i == len(cardscomputer)-1:
                                                        skip = True
                                                        break
                        if 7 not in cardsplayer and 20 not in cardsplayer and 33 not in cardsplayer and 46 not in cardsplayer:
                                cardsplayer.append(deck[deckn])
                                deckn-=1
                                cardsplayer.append(deck[deckn])
                                deckn-=1
                                cardsplayer.append(deck[deckn])
                                deckn-=1
                                cardsplayer.append(deck[deckn])
                                deckn-=1
                        else:
                                plays=""
                                plays=input("Do you want to play your 7? (y/n)")
                                if plays=="y":
                                        playc=input("Select card number to play or press enter to draw a card")
                                        drawncard = cardsplayer.pop(int(playc)-1)
                                        if 7 not in cardscomputer and 20 not in cardscomputer and 33 not in cardscomputer and 46 not in cardscomputer:
                                                cardscomputer.append(deck[deckn])
                                                deckn-=1
                                                cardscomputer.append(deck[deckn])
                                                deckn-=1
                                                cardscomputer.append(deck[deckn])
                                                deckn-=1
                                                cardscomputer.append(deck[deckn])
                                                deckn-=1
                                                cardscomputer.append(deck[deckn])
                                                deckn-=1
                                                cardscomputer.append(deck[deckn])
                                                deckn-=1
                                        else:
                                                skip=False
                                                while not skip:
                                                        for i in range(len(cardscomputer)):
                                                                if not skip:
                                                                        if cardscomputer[i]%13==drawncard%13:
                                                                                drawncard = cardscomputer.pop(i)
                                                                                skip=True
                                                                                break
                                                                        elif i == len(cardscomputer)-1:
                                                                                cardscomputer.append(deck[deckn])
                                                                                deckn-=1
                                                                                skip = True
                                                                                break
                                                                        elif i == len(cardscomputer)-1:
                                                                                skip = True
                                                                                break
                                        cardsplayer.append(deck[deckn])
                                        deckn-=1
                                        cardsplayer.append(deck[deckn])
                                        deckn-=1
                                        cardsplayer.append(deck[deckn])
                                        deckn-=1
                                        cardsplayer.append(deck[deckn])
                                        deckn-=1
                                        cardsplayer.append(deck[deckn])
                                        deckn-=1
                                        cardsplayer.append(deck[deckn])
                                        deckn-=1
                                        cardsplayer.append(deck[deckn])
                                        deckn-=1
                                        cardsplayer.append(deck[deckn])
                                        deckn-=1
                                else:
                                        cardsplayer.append(deck[deckn])
                                        deckn-=1
                                        cardsplayer.append(deck[deckn])
                                        deckn-=1
                                        cardsplayer.append(deck[deckn])
                                        deckn-=1
                                        cardsplayer.append(deck[deckn])
                                        deckn-=1
        print("Card on Table:", cardsnames[drawncard-1])
        skip=False
        while not skip:
                for i in range(len(cardscomputer)):
                        if not skip:
                                if cardscomputer[i]<14 and drawncard<14:
                                        drawncard = cardscomputer.pop(i)
                                        skip=True
                                        break
                                elif cardscomputer[i]>13 and cardscomputer[i]<27 and drawncard>13 and drawncard<27:
                                        drawncard = cardscomputer.pop(i)
                                        skip=True
                                        break
                                elif cardscomputer[i]>26 and cardscomputer[i]<40 and drawncard>26 and drawncard<40:
                                        drawncard = cardscomputer.pop(i)
                                        skip=True
                                        break
                                elif cardscomputer[i]>39 and drawncard>39:
                                        drawncard = cardscomputer.pop(i)
                                        skip=True
                                        break
                                elif cardscomputer[i]==1 and drawncard != 14 and drawncard != 27 and drawncard != 40:
                                        drawncard = cardscomputer.pop(i)
                                        skip=True
                                        break
                                elif cardscomputer[i]==14 and drawncard != 1 and drawncard != 27 and drawncard != 40:
                                        drawncard = cardscomputer.pop(i)
                                        skip=True
                                elif cardscomputer[i]==27 and drawncard != 1 and drawncard != 14 and drawncard != 40:
                                        drawncard = cardscomputer.pop(i)
                                        skip=True
                                        break
                                elif cardscomputer[i]==40 and drawncard != 1 and drawncard != 14 and drawncard != 27:
                                        drawncard = cardscomputer.pop(i)
                                        skip=True
                                        break
                                elif cardscomputer[i]%13==drawncard%13:
                                        drawncard = cardscomputer.pop(i)
                                        skip=True
                                        break
                                elif i == len(cardscomputer)-1:
                                        cardscomputer.append(deck[deckn])
                                        deckn-=1
                                        skip = True
                                        break
                                elif i == len(cardscomputer)-1:
                                        skip = True
                                        break
        
        
        while drawncard%13  == 9 or drawncard%13  == 8:
                skip=False
                while not skip:
                        for i in range(len(cardscomputer)):
                                if not skip:
                                        if cardscomputer[i]<14 and drawncard<14:
                                                drawncard = cardscomputer.pop(i)
                                                skip=True
                                                break
                                        elif cardscomputer[i]>13 and cardscomputer[i]<27 and drawncard>13 and drawncard<27:
                                                drawncard = cardscomputer.pop(i)
                                                skip=True
                                                break
                                        elif cardscomputer[i]>26 and cardscomputer[i]<40 and drawncard>26 and drawncard<40:
                                                drawncard = cardscomputer.pop(i)
                                                skip=True
                                                break
                                        elif cardscomputer[i]>39 and drawncard>39:
                                                drawncard = cardscomputer.pop(i)
                                                skip=True
                                                break
                                        elif cardscomputer[i]==1 and drawncard != 1 and drawncard != 14 and drawncard != 27 and drawncard != 40:
                                                drawncard = cardscomputer.pop(i)
                                                skip=True
                                                break
                                        elif cardscomputer[i]==14 and drawncard != 1 and drawncard != 14 and drawncard != 27 and drawncard != 40:
                                                drawncard = cardscomputer.pop(i)
                                                skip=True
                                        elif cardscomputer[i]==27 and drawncard != 1 and drawncard != 14 and drawncard != 27 and drawncard != 40:
                                                drawncard = cardscomputer.pop(i)
                                                skip=True
                                                break
                                        elif cardscomputer[i]==40 and drawncard != 1 and drawncard != 14 and drawncard != 27 and drawncard != 40:
                                                drawncard = cardscomputer.pop(i)
                                                skip=True
                                                break
                                        elif cardscomputer[i]%13==drawncard%13:
                                                drawncard = cardscomputer.pop(i)
                                                skip=True
                                                break
                                        elif i == len(cardscomputer)-1:
                                                cardscomputer.append(deck[deckn])
                                                deckn-=1
                                                skip = True
                                                break
                                        elif i == len(cardscomputer)-1:
                                                skip = True
                                                break
        if drawncard%13  == 7:
                if 7 not in cardsplayer and 20 not in cardsplayer and 33 not in cardsplayer and 46 not in cardsplayer:
                        cardsplayer.append(deck[deckn])
                        deckn-=1
                        cardsplayer.append(deck[deckn])
                        deckn-=1
                else:
                        plays=""
                        plays=input("Do you want to play your 7? (y/n)")
                        if plays=="y":
                                playc=input("Select card number to play or press enter to draw a card")
                                drawncard = cardsplayer.pop(int(playc)-1)
                                if 7 not in cardscomputer and 20 not in cardscomputer and 33 not in cardscomputer and 46 not in cardscomputer:
                                        cardscomputer.append(deck[deckn])
                                        deckn-=1
                                        cardscomputer.append(deck[deckn])
                                        deckn-=1
                                        cardscomputer.append(deck[deckn])
                                        deckn-=1
                                        cardscomputer.append(deck[deckn])
                                else:
                                        skip=False
                                        while not skip:
                                                for i in range(len(cardscomputer)):
                                                        if not skip:
                                                                if cardscomputer[i]%13==drawncard%13:
                                                                        drawncard = cardscomputer.pop(i)
                                                                        skip=True
                                                                        break
                                                                elif i == len(cardscomputer)-1:
                                                                        cardscomputer.append(deck[deckn])
                                                                        deckn-=1
                                                                        skip = True
                                                                        break
                                                                elif i == len(cardscomputer)-1:
                                                                        skip = True
                                                                        break
                                        if 7 not in cardsplayer and 20 not in cardsplayer and 33 not in cardsplayer and 46 not in cardsplayer:
                                                cardsplayer.append(deck[deckn])
                                                deckn-=1
                                                cardsplayer.append(deck[deckn])
                                                deckn-=1
                                                cardsplayer.append(deck[deckn])
                                                deckn-=1
                                                cardsplayer.append(deck[deckn])
                                                deckn-=1
                                                cardsplayer.append(deck[deckn])
                                                deckn-=1
                                                cardsplayer.append(deck[deckn])
                                                deckn-=1
                                                cardsplayer.append(deck[deckn])
                                                deckn-=1
                                                cardsplayer.append(deck[deckn])
                                                deckn-=1
                        else:
                                cardsplayer.append(deck[deckn])
                                deckn-=1
                                cardsplayer.append(deck[deckn])
                                deckn-=1
        print("Card on Table:", cardsnames[drawncard-1])
        if deckn < 9:
                j=0
                tempdeck=[]
                for j in range(deckn-1):
                        tempdeck.append(deck[j])
                deckn = 52
                deck = random.sample(cardsnumbers,k=52)
                for i in range(len(cardsplayer)-1):
                        if cardsplayer[i] in deck:
                                deck.remove(cardsplayer[i])
                                deckn-=1
                for i in range(len(cardscomputer)-1):
                    if cardscomputer[i] in deck:
                            deck.remove(cardscomputer[i])
                            deckn-=1
                for i in range(len(tempdeck)-1):
                        if tempdeck[i] in deck:
                                deck.remove(tempdeck[i])
                                deckn-=1
                deck.append(tempdeck)
                deckn+=len(tempdeck)
        if len(cardscomputer)<3 and len(cardscomputer)>0:
                print("!!!!!!!!!!!!!!!!!!!!!!!")
                print("CPU remaining cards =", len(cardscomputer))
                print("!!!!!!!!!!!!!!!!!!!!!!!")

if len(cardsplayer)<1:
        print("Player Wins !!!")
else:
        print("CPU Wins ...")
