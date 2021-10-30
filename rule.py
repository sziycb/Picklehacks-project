class rules:

    def __init__():
        importRules()

    def importRules():
        f = open('rules.txt', 'r')
        ruleList = f.read()
        print(ruleList)
        f.close()
        return


    def newRule(Player_Name):
        print("Hello {}, you are #blessed with the opportunity to make a new rule!".format(Player_Name))
        input_invalid = True
        RuleType = ""
        Condition = ""
        
        Sure = False
        Card = ""
        Suit = ""
        Say = ""
        Penalty = ""

        temp = ""
        Cards = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
        Suits = ["Club", "Diamond", "Heart", "Spade"]
        numPlayers = 3

        while (input_invalid == True):
            while (not(RuleType == "Say" or RuleType == "Power")):
                print("Would you like a Say rule or a Power rule?(Say/Power)")
                RuleType = input()
            if (RuleType == "Say"):
                while (not(Condition == "Before" or Condition == "After")):
                    print("You said Say type rule. Would you like the player to say before or after the card is played?(Before/After)")
                    Condition = input()
                while (Sure == False):
                    print("Which card would you like this to apply to?")
                    print(Cards)
                    Card = input()
                    if (Card in Cards):
                        print("Are you sure?(Y/n)")
                        temp = input()
                        if (temp.lower() == "y"):
                            Sure = True
                Sure = False
                while (Sure == False):
                    print("What suit would you like to apply this two?")
                    print(Suits)
                    Suit = input()
                    if (Suit in Suits):
                        print("Are you sure?(Y/n)")
                        temp = input()
                        if (temp.lower() == "y"):
                            Sure = True
                Sure = False
                while (Sure == False):
                    print("What would you like the player to say?")
                    Say = input()
                    print("Are you sure?(Y/n)")
                    temp = input()
                    if (temp.lower() == "y"):
                        Sure = True
                Sure = False
                while (Sure == False):
                    print("What would you like to be said if they break this rule?")
                    Penalty = input()
                    print("Are you sure?(Y/n)")
                    temp = input()
                    if (temp.lower() == "y"):
                        Sure = True
                
                return ["Say{}".format(Condition[0]),Card,Suit,Say,Penalty]
                
            else:
                
                while(not(Condition == "Take" or Condition == "Skip")):
                    print("You said Power type rule. Would you like the rule to be able to have a player Take cards or S a players turn?(Take/Skip)")
                    Condition = input()
                while (Sure == False):
                    print("Which card would you like this to apply to?")
                    print(Cards)
                    Card = input()
                    if (Card in Cards):
                        print("Are you sure?(Y/n)")
                        temp = input()
                        if (temp.lower() == "y"):
                            Sure = True
                Sure = False
                while (Sure == False):
                    print("What suit would you like to apply this two?")
                    print(Suits)
                    Suit = input()
                    if (Suit in Suits):
                        print("Are you sure?(Y/n)")
                        temp = input()
                        if (temp.lower() == "y"):
                            Sure = True
                Sure = False
                if(Condition == "Take"):
                    while (Sure == False):
                        print("How many cards would you like the person to take?(1-7)")
                        try:
                            Num = int(input())
                            if (Num > 0 and Num <=7):
                                print("Are you sure?(Y/n)")
                                temp = input()
                                if (temp.lower() == "y"):
                                    Sure = True
                        except:
                            print("Invalid number")
                    Sure = False
                    while (Sure == False):
                        print("Who would you like to take the card?(Player ID/Next #)=(Player 1/Next 2)")
                        Who = input()
                        temp = Who.split(" ")
                        if (temp[0].lower() == "player" or temp[0].lower() == "next"):
                            if(int(temp[1]) > 0 and int(temp[1]) <= numPlayers):
                                print("Are you sure?(Y/n)")
                                temp = input()
                                if (temp.lower() == "y"):
                                    Sure = True
                    temp = "Take " + str(Num) + " {}"
                    return [Card, Suit, Who, temp]
                else:
                    while (Sure == False):
                        print("Who would you like to skip?(Player ID/Next #)=(Skip Player 1/Skip 2)")
                        Who = input()
                        temp = Who.split(" ")
                        if (temp[0].lower() == "skip"):
                            if(temp[1].lower == "player"):
                                if(int(temp[2]) > 0 and int(temp[2]) <= numPlayers):
                                    print("Are you sure?(Y/n)")
                                    temp = input()
                                    if (temp.lower() == "y"):
                                        Sure = True
                            elif(int(temp[1]) > 0 and int(temp[1]) <= numPlayers):
                                print("Are you sure?(Y/n)")
                                temp = input()
                                if (temp.lower() == "y"):
                                    Sure = True
                    if (len(temp) == 2):
                        temp = "Skip to {}"
                    else:
                        temp = "Skip {}".format(Who)
                    return [Card, Suit, Who, temp]
