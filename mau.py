# mau / mao

cards = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
Player = ["Player 1", "Player 2", "Player 3"]
# rules fall into a few categories
# Say rules, you must say a phrase before or after playing a card
# Power Rules, power rules can be draw 4, skip, 
SayB = [["Ace", "Ace of Spades", "Failed to recognize Ace of Spades"], ["Dummy", "This will never occur", "How did this happen?"]]
SayA = [["Four", "Four score and seven years ago", "AMERICA!"], ["Seven", "Four score and seven years ago", "AMERICA!"]]

Power = [["Four", "Player 2", "Take 4 Player 2"], ["Seven", "Next 1", "Take 4 {}"], ["Six", "Skip 1", "Skip to {}"]]
#shows hand a list []
#Say?: #if nothing to say press enter to go to next player
#Card: #if card not found draw card
#Say?: #if nothing to say press enter to go to next player
#

def newRule(Player_Name):
    print("Hello {}, you are #blessed with the opportunity to make a new rule!".format(Player_Name))
    input_invalid = True
    RuleType = ""
    Condition = ""
    while input_invalid == True:
        while(not(RuleType == "Say" or RuleType == "Power")):
            print("Would you like a Say rule or a Power rule?(Say/Power)")
            RuleType = input()
        if RuleType == "Say":
            while(not(Condition == "Before" or Condition == "After")):
                print("You said Say type rule. Would you like the player to say before or after the card is played?(Before/After)")
                Condition = input()
            
            if(Condition == "Before"):
                
            else:


            return
        else:
            
            while(not(Condition == "Take" or Condition == "Skip")):
                print("You said Power type rule. Would you like the rule to be able to have a player Take cards or S a players turn?(Take/Skip)")
                Condition = input()
                return
