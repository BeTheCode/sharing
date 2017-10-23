import random
import os

class Player(object):
    
    def __init__(self,name,bank=100):
        self.name = name
        self.bank = bank
        self.playercards = dict()
        self.busted = False
        self.cardvalue = 0
    
    def addbank(self,bank):
        self.bank += bank

    def subbank(self,bank):
        self.bank -= bank

    def __setitem__(self,card,val):
        self.playercards[card] = val
    
    def getcurrentCards(self):
        return self.playercards

    def setcardsValue(self):
        if 1 in self.playercards.values():
            if sum(self.playercards.values())+10 < 22:
                self.cardvalue = sum(self.playercards.values())+10
        else:
            self.cardvalue = sum(self.playercards.values())

    def resetPlayer(self):
        self.playercards = dict()
        self.cardvalue = 0


class Deck(object):
    def __init__(self):
        self.cards = dict((str(x)+' of Diamonds', x) for x in range(1,11))
        self.cards.update({'Jack of Diamonds':10,'Queen of Dimonds':10,'King of Dimonds':10})
        self.cards.update(dict((str(x)+' of Harts', x) for x in range(1,11))) 
        self.cards.update({'Jack of Harts':10,'Queen of Harts':10,'King of Harts':10})
        self.cards.update(dict((str(x)+' of Spades', x) for x in range(1,11))) 
        self.cards.update({'Jack of Spades':10,'Queen of Spades':10,'King of Spades':10})
        self.cards.update(dict((str(x)+' of Clubs', x) for x in range(1,11)))
        self.cards.update({'Jack of Clubs':10,'Queen of Clubs':10,'King of Clubs':10})
       
    def __getitem__(self,key):
        val = self.cards.__getitem__(key)
        return val
        
    def shuffle(self):
        self.shuffled = list(self.cards.keys())
        random.shuffle(self.shuffled)
        return self.shuffled

class Game(object):

    def __init__(self,deck,players):
        self.dealer = Player('Dealer',1000)
        self.deck = deck
        self.shuffle = self.deck.shuffle()
        self.players = players
        self.winner = False
        self.replay = True

    def dealcards(self,shuffle,player):
        self.player = player
        self.player.playercards[self.shuffle[len(self.shuffle)-1]] = self.deck[self.shuffle[len(self.shuffle)-1]]
        self.shuffle.pop()

    def playgame(self):
        while self.replay == True:
            self.winner = False
            self.players.resetPlayer()
            self.dealer.resetPlayer()
            print("{}, what would you like to wager?".format(self.players.name))
            bet = int(input())
            self.players.subbank(bet)
            self.dealer.subbank(bet)
            self.dealcards(self.shuffle,self.dealer)
            self.dealcards(self.shuffle,self.dealer)
            self.dealcards(self.shuffle,self.players)
            hit = 'Y'
            while self.winner == False and self.player.busted == False and hit != 'N':
                os.system('clear')  # For Linux/OS X
                print('Dealer shows a {}'.format(list(self.dealer.playercards)[0]))
                if hit != 'N':
                    self.dealcards(self.shuffle,self.players)
                    self.players.setcardsValue()
                    print('Player has {}'.format(list(self.players.playercards)))
                    if self.players.cardvalue > 21:
                        print('Busted, Dealer is winner and takes pot {}'.format(bet))
                        self.dealer.addbank(bet)
                        self.winner = 'Dealer'
                        print('Player bank is {}'.format(self.players.bank))
                        break
                    print("Hit?")
                    hit = str(input())
                    if (hit == 'N'):
                        while self.winner == False:
                            os.system('clear')  # For Linux/OS X
                            self.dealer.setcardsValue()
                            print('Dealer has {}'.format(list(self.dealer.playercards)))
                            print('Dealer has {}'.format(self.dealer.cardvalue))
                            print('Player has {}'.format(self.players.cardvalue))
                            if self.dealer.cardvalue > 21:
                                self.winner = self.players.name
                                print('Dealer busted, winner is {}'.format(self.winner))
                                print('Dealer ended with {}'.format(list(self.dealer.playercards)))
                                self.players.addbank(bet*2)
                                break
                            #if (self.dealer.cardvalue > 16) or (self.dealer.cardvalue >= self.players.cardvalue):
                            if (self.dealer.cardvalue < 16):
                                self.dealcards(self.shuffle,self.dealer)
                            elif self.dealer.cardvalue < self.players.cardvalue:
                                self.winner = self.players.name
                                print('Dealer loses'.format(self.winner))
                                print(self.dealer.cardvalue)
                                self.players.addbank(bet*2)
                                break
                            
                            if self.dealer.cardvalue > self.players.cardvalue:
                                self.winner = self.players.name
                                print('Dealer won with {}'.format(self.dealer.cardvalue))
                                break
                            
                            if self.dealer.cardvalue == self.players.cardvalue:
                                print('No Winners, Tie Game')
                                self.winner = 'No'
                                break
                                

        
playdeck1 = Deck()
tim = Player('Tim')
game = Game(playdeck1,tim)
game.playgame()