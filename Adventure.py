# Adventure

# Items
MATRESS = False
LIGHTSWITCH = False
POTION = False
PARACHUTE = False
HANDGUN = False
FLASHLIGHT = False
BATTERIES = False

#Counters
DOORCOUNTER = 0
FLASHLIFE = 30
GUNLIFE = 6
PLAYERLIFE = 50
CANDYLIFE = 70

# Introduction
def introduction():
    print("On a dark and rainy night, you see your only choice of shelter.")
    print("The ominous and tall house seems to stare you down, with it's door wide open... waiting for you")
    print("The rain intesnifies, and you're far from home.")    
    print("You deside to enter the house until day break, regardless of instinct.")
    print("You walk up to the door, and notice a stack of matresses in the way, and move them.")
    print("Do you put the matresses in front of the door, or on the side?")
    choice1()
    
# Chose Matress Placement
def choice1():
    global MATRESS
    print("CHOOSE YOUR ADVENTURE")
    print("1 - In front of the door")
    print("2 - By the side of the door")
    firstChoice = ' '
    while firstChoice != '1' or firstChoice !='2':
        firstChoice = input()
        if firstChoice == '1':
            print("You moved the Matresses in fron of the door, and walk in")
            MATRESS = True
        if firstChoice == '2':
            print("You moved the Matresses to the side of the door, and walk in")
            MATRESS = False
      
          
        print("The house is dark... most likely abandoned.")
        print("Do you search for a Light Switch, or use your Flashlight?")
        choice2()
            
# Detects Electricity inside house
def choice2():
    global LIGHTSWITCH, FLASHLIGHT
    print("What do you choose?")
    print("1 - Light Switch")
    print("2 - Flash Light")
    
    secondChoice = ' '
    while secondChoice != '1' or secondChoice !='2':
        secondChoice = input()
        if secondChoice == '1':
           LIGHTSWITCH = True
        if secondChoice == '2':
           FLASHLIGHT = True

# Contiue to move around
def choice3():
    global LIGHTSWITCH, FLASLIGHT
    print("")
    if LIGHTSWITCH == True:
        print("You realize the abandoned house does mysteriously has power.")
    if FLASHLIGHT == True:
        print("Thankfully, a friend gifted you a flashlight recently.")
        print("You turn it on and see...")
        print("A STAIRCASE!")
        print("Do you go up the stairwell?)
              choice4()

# Stairs choice
def choice4():
    print("Make a safe decision:")
    print("... It could mean your life")
    print("1 - Up")
    print("2 - Stay")
    thirdChoice = ' '
    while thirdChoice != '1' or thirdChoice !='2':
        thirdChoice = input()
        if thirdChoice == '1':
            choice3Doors()
        if thirdChoice == '2':
            candyman()

# Non-death more adventure
def choice3Doors():
    global LIGHTSWITCH, MATRESSES
    print("You make it through up the stairs as the creak Noisely... it feels like someone is watching you")
    print("3 doors appear in front of you")
    if LIGHTSWITCH == True:
        print("You remeber that the house has power, and turn on the Light Switch.")
        print("A loud buzzing sound seems to come from all around you, like the house coming alive.")
        print("An elctric picto-graph reveals itself on each of the doors."
        print("To the left, a red door with a growing plant.")
        print("directly in front, a green door with a Platic bottle in the dirt.")
        print("To the right, a blue door with a rock being rained on.")
        print("A scratchy voice coms over a speaker...")
        print("-- am t-e l--- of 15 -orn, yet p--me in --sdom.")
        print("Often ---sed by the eld-st; -- -ays i- the o-- one -ut, but --'s the o--y one with an e-en fa--.")
        print("Seek out -- id-nti--, and you wi-l choose you- f-te.")
        doorChoice()

    else if FLASHLIGHT == True:
        print("You remember the flashlight that was given to you, and use it to illuminate the doors")
        print("To the left, a red door.")
        print("directly in front, a green door.")
        print("To the right, a blue door.")
        print("All thee doors seem to have a discoloration in the middle, put you cannot makeout any meaningful marks.")
        print("A voice echoes faintly in the distance...")
        print("I am the last of 15 born, yet prime in wisdom.")
        print("Often teased by eldest; he says im the odd one out, but hes the only one with an even face.")
        print("Seek out my identity, and you will choose your fate.")           
        doorChoice()

# Player instant death
def candyman():
    global FLASHLIGHT, DOORCOUNTER
    print("You hear a scurry from behind, but it's too fast and too dark to see")
    print("The sound comes from all around, as it circles you, defensless as you are")
    print("I havent eaten in a long time... you seem to come right in time for a SNACK!")

    if FLASHLIGHT == True and DOORCOUNTER > -1:
        print("It scratched you pretty bad, but you grabbed your flashlight just in time and pointed the white beam towards it.")
        print("the creature's skin started to boil, and ran off... Time to continue.")
        CANDYLIFE -= 1
        FLASHLIFE -= 1
        PLAYERLIFE -= 7
        doorChoice()

    elif HANDGUN == True and DOORCOUNTER > -1:
        print("You shot it, and it screeched as it ran off... it looked like you injured it badly")
        CANDYLIFE -= 10
        GUNLIFE -= 1
        PLAYERLIFE -= 2
        doorChoice()

    elif FLASHLIGHT == False:
        print("The CANDY MAN ate you, you died")
        PLAYERLIFE = 0
        ending()

# Counter +1 (How you Win)
def choiceUP():
    global DOORCOUNTER
    if DOORCOUNTER = 47:
        print("A creak came from above, and a door slowely drew open...")
        roofTop()
    
    elif DOORCOUNTER >= 25 and < 47:
        print("We're walking the stairway to heaven")
        doorChoice()
    
    elif DOORCOUNTER = 24:
        print("Whoaaaaaaaa You're half-way there")
        doorChoice()
        
    elif DOORCOUNTER <= 23 and > -1:
        print("Carry on my wayward son")
        doorChoice()
        
    elif DOORCOUNTER = -1:
        choiceDown()

    

# Counter -1 (How you Lose)
def choiceDown():
global DOORCOUNTER
if DOORCOUNTER < -1:
    print("A bell rang above, and a draft of wind streamed by, like a door was opened elsewhere...")
    candyman()

elif DOORCOUNTER > -1:
    print("We continue another day?")
    doorChoice()


# Counter Repeat (Common Loop)
def doorChoice():
global DOORCOUNTER
FLASHLIFE -=1

    FLASHLIFE += 15

    print("The exact set of doors appear once again
    print("NOW CHOOSE A DOOR SO YOUR FATE DETERMINED!")
    print("1 - Red")
    print("2 - Green")
    print("3 - Blue")

    doorChoice = ' '
    while doorChoice != '1' or doorChoice !='2' or doorChoice == '3':
        doorChoice = input()
        
        if doorChoice == '1':
            DOORCOUNTER -= 1
            choiceDown()
            
        if doorChoice == '2':
            DOORCOUNTER = DOORCOUNTER
            doorChoice()
            
        if doorChoice == '3':
            DOORCOUNTER += 1
            choiceUP()

        
# Endgame
def ending():
    global DOORCOUNTER
  print("The CANDY MAN found you, and ate you... you are not the lst of his many victims.")
  print("Your score was: " + (DOORCOUNTER) + "! Better luck next time!")

# Item Handler
   global MATRESS, LIGHTSWITCH, FLASHLIGHT, POTION, HANDGUN, PARACHUTE, DOORCOUNTER, FLASHLIFE, GUNLIFE
    if DOORCOUNTER >= 40 and GUNLIFE > 0:
        Print("You found an Item!")
        HANDGUN == True
        print("I can Protect myselff from him with this")
       
    elif DOORCOUNTER >= 30:
        Print("You found an Item!")
        PARACHUTE = True
        print("I now have an option out... Keep Climbing those Stairs")
       
    elif DOORCOUNTER >= 20:
        Print("You found an Item!")
        POTION = True
        print("What's this? A Potion of Immortality? No Way!!")
      
    elif DOORCOUNTER >= 10 and FLASHLIGHT == True and FLASHLIFE > 0:
        Print("You found an Item!")
        BATTERIES = True
        FLASHLIFE += 15
        print("More for my Flashlight?")
        
   
    
# rooftop
def rooftop():
    global MATRESS, LIGHTSWITCH, FLASHLIGHT, POTION, HANDGUN, PARACHUTE, DOORCOUNTER, FLASHLIFE, GUNLIFE
    print("You Entered through the single door above you, and felt fresh air for the first time in hours.")
    print("The roof looked like a junkyard-- but for killing machines...")
    print("You hear a screech, like the one from earlier, and the CANDY MAN pounces on top of you
    print("CANDY MAN: I would eat you now, but you've made it to the top.")
    print("CANDY MAN: If you can choose a way to get off of this roof, without dying from the tramua, you can go free, and the rain will stop.")
    print("CANDY MAN: However, If the way you choose ends in your death, I'll feast upin your soul eternally, and contue my devious hunt.")
    print("NOW CHOOSE A DOOR SO YOUR FATE DETERMINED!")

    print("You can die in 5 different ways: ")
          print("1 - Jump off the front of the house")
          print("2 - Sit in the Electric Chair")
          print("3 - Shoot Yourself in the head")
          print("4 - Jump off the back of the house")
          print("5 - Drink the imortality Potion")
          print("6 - Fight Me")
           while rooftop != '1' or rooftop !='2' or rooftop == '3' or rooftop !='4' or rooftop == '5' or rooftop !='6':
        doorChoice = input()
        
        if doorChoice == '1':
            print("I'll Jump off the front!!")
            if MATRESS == True:
                finish()
            else:
                ending()
       
         
        if doorChoice == '2':
            print("I Wonder if the Lights Worked...")
            if LIGHTSWITCH == True:
                ending()
            else:
               finish()

                        
        if doorChoice == '3':
            print("I'll take one for the Team")
            if HANDGUN == True and GUNLIFE < 0 and CANDYLIFE <=10:
                finish()
            else:
                ending()
        
            
        if doorChoice == '4':
            print("I have a parachute for a Reason!")
            if Parachute == True and PLAYERLIFE > 40:
                finish()
            else:
                ending()

                 if doorChoice == '5':
            print("I believe in Science! NOT GOD!")
            if POTION == True:
                print("Too Bad the Potion was just bleach with food coloring...")
                ending()
            else:
                finish()
        
        if doorChoice == '6':
            print("I can and will kill you, you son of a bitch")
             if CANDYLIFE < 10 and FLASHLIFE > 20 or GUNLIFE > 4:
                 finish()
             else:
                 ending()


# Finish-Introduction Relay
def finish():
    print("Play Again?"
          print("(Yes / No) Case Sensative")
    restart = ' '
    while restart != 'Yes' and restart != 'No':
        restart = input("Would you like to play agian?(yes or no) ")
        if restart == 'yes':
        MATRESS = False
        LIGHTSWITCH = False
        POTION = False
        PARACHUTE = False
        HANDGUN = False
        FLASHLIGHT = False
        BATTERIES = False
        int DOORCOUNTER = 0
        int FLASHLIFE = 30
        int GUNLIFE = 6
        int PLAYERLIFE = 50
        int CANDYLIFE = 70
        if playAgain == 'no':
            break

introduction()
