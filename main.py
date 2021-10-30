import pygame
import random as r
import sys

class Card:
    def __init__(self, v, s):
        self.value = v
        self.suit = s
        self.frontImg = ""
        self.backImg = ""

    def printCard(self):
        print(self.value, "of", self.suit)


class Player:
    def __init__(self, n):
        self.name = ""
        self.hand = []
        self.cardCount = 0
        self.icon = ""


    def addCard(self, c):
        self.hand.append(c)
        self.cardCount += 1


    def playCard(self, c):
        self.hand.remove(c)
        self.cardCount -= 1
        return c

    def printCards(self):
        for i in self.hand:
            i.printCard()

#create a standard deck of cards
standardDeck = []

for k in ["Spades", "Hearts", "Diamonds", "Clubs"]:
    for i in range(1, 14):
        c = Card(1, "Spades")
        if i == 1:
            c = Card("Ace", k)
            standardDeck.append(c)
        elif i < 11:
            c = Card(str(i), k)
            standardDeck.append(c)
        elif i == 11:
            c = Card("Jack", k)
            standardDeck.append(c)
        elif i == 12:
            c = Card("Queen", k)
            standardDeck.append(c)
        elif i == 13:
            c = Card("King", k)
            standardDeck.append(c)


#set image fronts
for i in range(1, 53):
    f = str(i) + ".png"
    standardDeck[i-1].frontImg = pygame.image.load(f)

#shuffle the deck
r.shuffle(standardDeck)

#create players
player1 = Player("Austen")
player2 = Player("Sami")
player3 = Player("Gabe")

for i in (player1, player2, player3):
    for k in range(7):
        i.addCard(standardDeck.pop())

#print("PLAYER1")
#player1.printCards()
#print("PLAYER2")
##player2.printCards()
#print("PLAYER3")
#player3.printCards()

#Initialize the pygame
pygame.init()

screen = pygame.display.set_mode((1600, 1100))

#Title and Icon
pygame.display.set_caption("Mao")
icon = pygame.image.load('ace.jpg')
pygame.display.set_icon(icon)

#table
tableImg1 = pygame.image.load('table1.png')
tableImg2 = pygame.image.load('table2.png')
tableImg3 = pygame.image.load('table3.png')
tableX = 0
tableY = 0

#card
cardBack = pygame.image.load("card_back.png")

def table(player):
    if player == player1:
        screen.blit(tableImg1, (tableX, tableY))
    elif player == player2:
        screen.blit(tableImg2, (tableX, tableY))
    elif player == player3:
        screen.blit(tableImg3, (tableX, tableY))


def sevenCards():
    screen.blit(cardBack, (520, 550))
    screen.blit(cardBack, (550, 540))
    screen.blit(cardBack, (580, 520))
    screen.blit(cardBack, (610, 500))
    screen.blit(cardBack, (640, 520))
    screen.blit(cardBack, (670, 540))
    screen.blit(cardBack, (700, 550))


def flipCards():
    x = 500
    y = 540
    for i in player1.hand:
        screen.blit(i.frontImg, (x, y))
        x += 80

players = [player1, player2, player3]
playerCounter = 0
def nextPlayer():
    global playerCounter
    playerCounter += 1
    playerCounter %= 3
    return playerCounter

def isLegalPlay(topCard, playCard):
    pass

def playCard(player, card):
    global topCard
    topCard = card
    player.playCard(card)
    if len(player.hand) == 0:
        print("WINNER", player.name)
        sys.exit()

def displayCards(player):
    x = 500
    y = 540
    table(player)
    showTopCard()
    for i in player.hand:
        screen.blit(i.frontImg, (x, y))
        x += 80
    pygame.display.update()

def showTopCard():
    global topCard
    screen.blit(topCard.frontImg, (550, 10))

#Game Loop
running = True
screen.fill((36, 115, 69)) #RGB values
table(player1)
sevenCards()
pygame.display.update()
topCard = standardDeck.pop()
print("You may flip your cards.")


currentPlayer = player1
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    left, middle, right = pygame.mouse.get_pressed()
    if left:
        table(currentPlayer)
        flipCards()
        screen.blit(topCard.frontImg, (550, 10))
        pygame.display.update()
    left = False
    left, middle, right = pygame.mouse.get_pressed()
    if left:
        playCard(currentPlayer, currentPlayer.hand[0])
        screen.blit(topCard.frontImg, (550, 10))
        pygame.display.update()
        currentPlayer = players[nextPlayer()]
        displayCards(currentPlayer)







     
