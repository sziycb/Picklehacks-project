import pygame
import random as r

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
    for k in range(14):
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
tableImg = pygame.image.load('table.png')
tableX = 0
tableY = 0

#card
cardBack = pygame.image.load("card_back.png")

def table():
    screen.blit(tableImg, (tableX, tableY))


def sevenCards():
    screen.blit(cardBack, (520, 550))
    screen.blit(cardBack, (550, 540))
    screen.blit(cardBack, (580, 520))
    screen.blit(cardBack, (610, 500))
    screen.blit(cardBack, (640, 520))
    screen.blit(cardBack, (670, 540))
    screen.blit(cardBack, (700, 550))


def flipCards():
    x = 100
    y = 540
    for i in player1.hand:
        screen.blit(i.frontImg, (x, y))
        x += 80


#Game Loop
running = True
screen.fill((36, 115, 69))
table()
sevenCards()
pygame.display.update()
print("You may flip your cards.")
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    left, middle, right = pygame.mouse.get_pressed()

    if left:
        table()
        flipCards()
        pygame.display.update()
    #RGB values


