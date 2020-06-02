import random
#Declare variables
cheatCode = int()

#Enemy variables:
enemyHp = int()
enemyChance = int()
runFromChance = int()
enemyName = str()
currentEnemy = [enemyHp,enemyChance,enemyName,runFromChance] #Stored in array to be able to set a current enemy, and code within functions can adapt to change in enemy

#Player variables (ALL GLOBAL):
playerHp = 5 #Starting health at 5 HP
playerMorale = 30
smallPotion = 1 # Heals 1 HP
largePotion = 0 # Heals 3 HP
playerName = str()
inventory = []

isSuccess = 0 #For successfull run() from encounter
newNum = int() # THE ROLL
newChance = int() # CHANCE ROLL (NON COMBAT)

brokeIt = int()
leftIt = 0 # Leaving non combat chance open attempt

def chanceRoll(): # For non- combat rolls, chances are based out of 5
    global newChance
    newChance = random.randint(1,5)
    return newChance

def roll(): # for combat rolls, based out of 10
    global newNum
    newNum = random.randint(1,10)
    return newNum


def helpMenu(): #NEEDS FIX
    print('check your status and inventory by entering \'I\'. Combat is luck based,')
    print(' where you will have to \'roll the dice\' to determine if you do damage or take damage.')
    print(' When entering combat, you will be given stats on your enemy. They will look like this: Bat(HP: 2** 6/10)')
    print(', meaning, you will have to roll a 1-6 to do 1 point of damage. Additionally, MORALE affects chance-based systems outside of combat,')
    print(' and if your morale is too low, you will be unable to attempt certain things. Lastly, if you would like to quit, type \'quit\'')


def nonCombatRoll(successChance, successAttempts, nameOf):
    global leftIt
    global brokeIt
    print('You have a ' + str(successChance) + '/5 chance of success for: ' + str(nameOf) + '. You have ' + str(successAttempts) + ' attempts.' )
    print('Would you like to attempt?')
    i = 0
    brokeIt = 0
    pathChoice()
    print()
    if pathInt == 1:
        while i == 0:
            chanceRoll()
            if newChance <= successChance and successAttempts != 0:
                print('You rolled a: ' + str(newChance) + '. You are successful!')
                i = i +1
            elif newChance > successChance and successAttempts != 0:
                print('You rolled a: ' + str(newChance) + '. Your attempt was unsuccessful.')
                successAttempts = successAttempts -1
                print('You have: ' + str(successAttempts) + ' chances remaining.')
                pressToContinue()
            elif successAttempts ==0:
                print('You have no more attempts.')
                i = i +1
                brokeIt = brokeIt +1
                print('You can no longer attempt this.')
                pressToContinue()

    if pathInt == -1:
        print('Okay, You don\'t even want to try this.')
        leftIt = leftIt +1
    pressToContinue()
    return leftIt
    return brokeIt

def run(): # NEED INPUT WHILE LOOP
    global playerMorale
    global playerHp
    global isSuccess #Bool for if run() is successful, turn to 1. So I can use an IF to not allow item drop or gains from enemy defeat. 
    global currentEnemy
    x = input('You have a ' + str(currentEnemy[3]) + '/5 chance to successfully run from this encounter. If you run, your morale will decrease. If you fail chance roll to run, you will lose 1hp. Continue?(y or n) ')
    print() #AADD INPUT CORRECT WHILE LOOP
    if x == 'y':
        chanceRoll() #THIS RUN() NEEDS FIX 
        if newChance <= currentEnemy[3]: # CurrentEnemy[3] referrs to the CHANCE out of 5 to escape. Easier enemies are easier to escape from. NEEDS FIX
            if playerMorale != 0:
                print()
                print('You rolled a: ' + str(newChance) + '. You have sucessfully escaped the encounter.')
                print()
                print('Due to cowardice, your morale has decreased! (-10)')
                playerMorale = playerMorale - 10
                if playerMorale <0:
                    print('OOF, your morale is less than zero. You must really hate yourself.')
                    pressToContinue()
                print('Your current Morale is: ' + str(playerMorale) + '/100')
                input('Enter \'y\' to continue: ')
                isSuccess = isSuccess +1 #FOR ENCOUNTERS THAT DROP ITEMS, IF SUCCESSFUL RUN, NO ITEM
                return isSuccess
                return playerMorale
        elif newChance >= 3:
            print('You rolled a: ' + str(newChance) +'. Your escape was unsuccessful. You take damage. (-1HP)')
            playerHp = playerHp - 1
            if playerHp ==0:
                dead()
            print('Your current HP: ' + str(playerHp) + '/5')
            input('Enter \'y\' to continue: ')
            fight(currentEnemy[0], currentEnemy[1], currentEnemy[2],currentEnemy[3])
    elif x == 'n':
        input('Enter \'y\' to continue: ') # ANY KEY - FIX?
        fight(currentEnemy[0],currentEnemy[1],currentEnemy[2],currentEnemy[3])
    return playerMorale
    return playerHp



def inventoryS(): # Open inventory, use potions for hp, check hp morale status.
    global playerHp
    global playerMorale
    global smallPotion
    global largePotion
    global inventory
    print()
    print('---------------------------------------------')
    print('Your current HP is: ' + str(playerHp) + '/5')
    print('Your current Morale is: ' + str(playerMorale) + '/100')
    print('You have ' + str(smallPotion) + ' small potions and ' + str(largePotion) + ' large potions')
    print('You have the following items: ' + str(inventory))
    print('---------------------------------------------')
    print()

    a = 1  #WHILE LOOP ESCAPE
    z = 1  #WHILE LOOP ESCAPE
    if smallPotion == 0 and largePotion == 0:
        print('You have no potions you can use.')
        while a ==1: # correct input while loop
            i = input('Enter \'y\' to continue: ')
            if i == 'y':
                a = a+1
            else:
                print('Please enter a valid command.')
    if smallPotion != 0 or largePotion !=0:
        while z ==1: # correct input while loop 1
            i = input('Use small potion(s). Use large potion(l). Exit Inventory(y): ')
            if i == 's' and smallPotion ==0:
                print('You have no small potions.')
                z = z+1
            if i == 's' and smallPotion != 0:
                z = z+1 #TO ESCAPE LOOP
                if playerHp <5:
                    smallPotion = smallPotion -1
                    playerHp = playerHp + 1
                    print('You used a small potion. Your HP is now: ' + str(playerHp) + '/5')
                    print()
                elif playerHp == 5:
                    print('You are already at max health. Why are you trying to use a potion?')
            elif i == 'l' and largePotion ==0:
                z = z+1
                print('You have no large potions.')
            elif i == 'l' and largePotion !=0 :
                z = z+1 # TO ESCAPE LOOP
                if playerHp < 3:
                    largePotion = largePotion -1
                    playerHp = playerHp + 3
                    print()
                    print('You used a large potion. Your HP is now: ' + str(playerHp) + '/5')
                    print()
                elif playerHp >=3 and playerHp != 5:
                    largePotion = largePotion -1
                    playerHp = 5
                    print()
                    print('You used a large potion. It increased you to max health.')
                    print()
                elif playerHp == 5:
                    print('You are already at max health. Why are you trying to use a potion? ')
            elif i =='y':
                z =z+1
            else:
                print('Please enter a valid command.')
    pressToContinue()
    print()
    return playerHp
    return smallPotion
    return largePotion
    return easter2


def dead():
    print()
    print('Your HP has reached 0, you are dead.')
    print('  _____')
    print(' /     \ ')
    print('| () () |')
    print(' \  ^  /')
    print('  |||||  ')
    print('  ||||| ')
    print()
    print('Thanks for playing!')
    print()
    #score?
    quit()

def fight(enemyHp, enemyChance, enemyName, runFromChance):# ROLL , do or take damage, repeat. 
    global playerHp
    global playerMorale
    global currentEnemy

    print()
    print('--------ENCOUNTER-------')
    print('Player has: ' + str(playerHp) + 'HP')
    print(str(enemyName) + ' has: ' + str(enemyHp) + 'HP')
    print('Player has: ' + str(enemyChance) +'/10 hit chance on ' + str(enemyName))
    userInput = input('Would you like to attack(y) or run(n)?')
    print()
    if userInput == 'y':
        while enemyHp != 0:
            roll()#ROLL WILL HAPPEN IF INVENTORY CALLED, NEED FIX
            if int(newNum) <= int(enemyChance): #If roll is less than or equal to the enemy hit chance out of 10, does damage
                enemyHp = enemyHp - 1
                print('You rolled: ' + str(newNum) + ', dealing damage to ' + enemyName + '(' + str(enemyChance) + '/10)' + ' Enemy has ' + str(enemyHp) + 'HP remaining.')
                i = input('Enter \'y\' to continue, or \'i\' for inventory: ')
                print()
                if i == 'i':
                    inventoryS()
            else:
                playerHp = playerHp - 1
                print('You rolled: ' + str(newNum) + ', and took damage from ' + enemyName + '(' + str(enemyChance) + '/10)' )
                print('Player HP: ' + str(playerHp) + '/5')
                if playerHp == 0:
                    dead()
                e = input('Enter \'y\' to continue, or \'i\' for inventory: ')
                print()
                if e == 'i':
                    inventoryS()
        if enemyHp == 0:
            print()
            print('You defeated ' + enemyName + '! Your morale has increased!')
            playerMorale = playerMorale + 5
            print('Morale: ' + str(playerMorale) + '/100')
            input('Enter \'y\' to continue: ')
            print()

    elif userInput == 'n':
        run()
    else:
        print('Please enter a valid command') #INVALID COMMAND DOESNT LOOP THRU, IF INVALID RESTART INPUT 
    return playerHp
    return playerMorale

def pathChoice(): # Change a global variable that is a bool = pathInt is changed based on (y or n) answer. then i use if statements to check pathInt to decide what route was taken
    global pathInt
    pathInt = int()# resetting pathInt on pathChoice() call for reusability.
    a = 1
    while a == 1:
        c = input('Enter \'y\' or \'n\': ')
        if c == 'y':
            a = a +1
        elif c == 'n':
            a = a +1
        else:
            print('Please enter a valid command.')
    if c == 'y':
        pathInt = pathInt +1
    elif c=='n':
        pathInt = pathInt - 1
    return pathInt


def saySorry(): # This is all literally just an easter egg. If you say no to entering the dungeon and don't apologize, easter egg. If you do apologize, you go home. game over. lol
    a = 1
    i = 0
    print()
    print('Apologize to me for wasting my time then.')
    while a == 1:
        if i >=2:
            a = a+1
        c = input('Say \"sorry\": ')
        if c == 'sorry':
            a = a +1
        else:
            print('...you aren\'t going to apologize for wasting my time?')
            i = i+1
    if c =='sorry':
        print()
        print('Thanks for the apology. Now go home.')
        print('**You head home, ashamed of your cowardice.')
        pressToContinue()
        print('Thanks for playing....I guess.')
        print()
        quit()
    if  i >= 2:
        print()
        print('You are rude. The least you could do is apologize.')
        print('I guess I will just kill you instead.')
        print('**Dungeon keeper stabs you with his sword.')
        print()
        pressToContinue()
        print()
        print('You just found an easter egg. (1/3) Cool!')
        pressToContinue()
        dead()

def pressToContinue(): #Press y to continue, or i for inventory
    global largePotion
    global cheatCode
    global playerMorale
    global playerHp
    global smallPotion
    a = 1
    while a == 1: # While loop to check what the user input is.. Needs to be y for continue or i to open inventory. (Or cheats)
        c = input('Continue(\'y\') -- Inventory(\'i\'): ')
        if c == 'y':
            a = a + 1
            print()
        elif c == 'i':
            a = a + 1
        elif c == 'motherlode': #CHEAT
            largePotion = largePotion + 50
            print('Wow... so you have to use cheatcodes? Brilliant. (Large potion +50)')
            cheatCode = cheatCode +1

        elif c=='misanthropy': #CHEAT
            playerHp = 1
            playerMorale = 1
            smallPotion = 0
            largePotion = 0
            print('WOW! what an awesome cheat code! (Everything sucks now)')
            cheatCode = cheatCode +1

        elif c =='samuelstenerson': # CHEAT
            playerHp = 1000
            playerMorale = 100
            largePotion = largePotion +100
            smallPotion = smallPotion +100
            print('Hey you entered the name of the guy who made this. (Dirty Cheater!)')
            cheatCode = cheatCode +1

        elif c == 'justkillme': #CHEAT
            dead()
        else:
            print('Please enter a valid command.')
    if c == 'y':
        print()
    elif c=='i':
        inventoryS()
    return largePotion
    return cheatCode
    return playerMorale
    return playerHp
    return smallPotion

def runFromFirst(): #RE USED MULTIPLE TIMES FOR FIRST ENCOUNTER, FOR READABILITY. made a function because it was getting really messy in ###Adventure prints down below
    print()
    print('**You ran from the first enemy. He had a key. You probably needed that.')
    pressToContinue()
    print('**After running past the skeleton, you come across a door. It is locked. That key would be useful..')
    pressToContinue()
    print('**You try shaking and pulling on the door. It won\'t budge.')
    print('So do you want to go back and fight the skeleton(y) or just hang out here?(n)')
    pathChoice()
    if pathInt ==1: # Go back to fight
        if 'Torch' in inventory: #CHECKS IF YOU HAVE TORCH, WHICH CHANGES HIT CHANCE
            currentEnemy = [1,7,'Skeleton',4] 
            fight(currentEnemy[0],currentEnemy[1],currentEnemy[2],currentEnemy[3])
        else:
            currentEnemy = [1,6,'Skeleton?',4] # NO TORCH, HIT CHANCE DECREASED
            fight(currentEnemy[0],currentEnemy[1],currentEnemy[2],currentEnemy[3])
        if isSuccess == 2:#IF RUN AGAIN, ENDGAME
            print()
            print('Okay.... You ran again... Just go home.')
            pressToContinue()
            dead()
    if pathInt == -1: #SAME AS ABOVE DECISION TREE
        print()
        print('**You sit in the same spot until you die of starvation and boredom. Nice.')
        pressToContinue()
        dead()



#ADVENTURE PRINTS#####################################################################################################################
print()
print()
print()
c = str()
playerName = input('Hello Traveler, what is your name? ')

#Tutorial y/n
print('Okay, ' + playerName + ' would you like to hear the tutorial?')#HEAR TUTORIAl?>>>>>>>>>>>>>>>>>>>>
pathChoice()
if pathInt == 1:
    helpMenu()
    smallPotion = smallPotion + 2
    print('Hey, thanks for reading the tutorial. Heres 2 small health potions to help you out.')
    pressToContinue()
    pathInt = 0
elif pathInt == -1:
    print()
    print('Okay, so you don\'t want to hear the tutorial, you just have it all figured out.')
    pressToContinue()
    pathInt = 0
#CHOICE 1 : Continue or go home.
print('Okay, are you ready to brave the dungeon?(y or n) ')#GO INTO DUNGEON>>>>>>>>>>>>>>>>>>>>>>>>>>>
pathChoice()
if pathInt == 1:
    print()
    print('Best of luck, ' + playerName + '!')
    print()
    print('**You enter a cellar door, and proceed down a spiral stone staircase.')
    pathInt = 0
    pressToContinue()
elif pathInt == -1:
    saySorry() # Easter egg to leave game by saying no before it begins

#CHOICE 2 : TORCH LMAO PATH INT 1 IS YES
print('**You are in a damp stone hallway, there is little light. You see a torch on the wall. Grab it? (y or n)')
pathChoice()
if pathInt ==1: #YES x1 (Yes to grab torch.)
    print()
    print('Torch was added to inventory')
    inventory.append("Torch")
    pressToContinue()
    print()
    print('**You continue to walk down the hall. There are spiders and cobwebs everywhere.')
    print('\'This light sure is handy\', you think to yourself')
    pressToContinue()
    print('**Just ahead you see a skeleton on the ground. He is clenching a key. Grab it? (y or n)')
    pathChoice()
    if pathInt ==1: #YES x2 (Yes to grab Key.)
        print()
        print('**As you reach down to grab the key, the skeletal remains rise and strike at you.')
        pressToContinue()
        currentEnemy = [1,7,"Skeleton",4]
        fight(currentEnemy[0],currentEnemy[1],currentEnemy[2],currentEnemy[3])
        if isSuccess ==1: #isSuccess means successfully ran. So the code below is if u successfully run from this enemy.
            runFromFirst()# SEE ABOVE FUNCTION
    elif pathInt == -1: #NO x2 (No to grab key)
        print()
        print('**As you attempt to step over the skeleton, all of a sudden he starts moving!')
        print('**The skeleton strikes your legs, causing damage. (HP -1)')
        playerHp = playerHp - 1
        pressToContinue()
        print('Your current HP is now: ' + str(playerHp) + '/5')
        if playerHp ==0:
            print('How did you die here. You used the bad cheat code didnt you?')
            pathChoice()
            if pathInt ==1:
                print('Yeah I thought so.')
                pressToContinue()
                dead()
            elif pathInt ==-1:
                print('You\'re a cheater and a liar. Nice.')
                pressToContinue()
                dead()
        pressToContinue()
        currentEnemy = [1,7, "Skeleton",4]
        fight(currentEnemy[0], currentEnemy[1], currentEnemy[2],currentEnemy[3])
        if isSuccess ==1: #YES TO RUNNING
            runFromFirst()
            

    print('A Gold Key was added to your inventory!')
    inventory.append('Gold Key')
    pressToContinue()
    print('**You continue down the hall and come across a door.')
    print('Open door?')
    pathChoice()
    print()
    if pathInt ==1:
        print('You use: Gold Key to open the door.')
        print('\'Gold Key\' was removed from your inventory.')
        inventory.remove('Gold Key')
        pressToContinue()
    elif pathInt == -1:
        print('Okay.. so what are you going to do? Just stand here?(y) or open the door?(n)')
        pathChoice()
        print()
        if pathInt ==1:
            print('You stand outside of the door until you die of hunger and boredom. Nice.')
            pressToContinue()
            dead()
        elif pathInt ==-1:
            print('Okay.. I don\'t get why you would say no in the first place...')
            print('You use: Gold Key to open the door.')
            print('\'Gold Key\' was removed from your inventory.')
            inventory.remove("Gold Key")
            pressToContinue()


elif pathInt == -1: #NO x1 (No to grab torch.)
    print()
    print('**You proceed down the pitch black hallway, asking yourself why you wouldn\'t bring the torch.')
    pressToContinue()
    print('**You feel stupid.')
    pressToContinue()
    print('Negative thoughts have lowered your morale! (-10)')
    playerMorale = playerMorale - 10
    if playerMorale < 0:
        print('OOF your morale is less than zero. You must really hate yourself.')
    print('Your current morale is now: ' + str(playerMorale) + '/100')
    pressToContinue()
    print('**Your morale has lowered. would you like to cheer yourself up? (y or n)')
    pathChoice()
    if pathInt == 1: #YES to cheering yourself up.
        print()
        print('**Talking to yourself** \'Just because I made a stupid decision doesn\'t mean I\'M stupid!')
        pressToContinue()
        print('Positive reinforcement has restored some Morale (+5)')
        playerMorale = playerMorale + 5
        print()
        print('Your current morale is now: ' + str(playerMorale) + '/100')
        pressToContinue()
    print()
    print('**You continue down the dark hall')
    pressToContinue()
    print('**All of a sudden, you feel something moving near your feet.')
    print('**You hear the creaking and clinking of bones, along with chattering.')
    pressToContinue()
    print('**Something has struck you in the dark!! (HP -1)')
    playerHp = playerHp -1
    print('Player Hp is now: ' + str(playerHp) + '/5')
    if playerHp == 0:
        print('How did you die here. You used the bad cheat code didnt you?')
        pathChoice()
        if pathInt ==1:
            print('Yeah I thought so.')
            pressToContinue()
            dead()
        elif pathInt ==-1:
            print('You\'re a cheater and a liar. Nice.')
            pressToContinue()
            dead()
    pressToContinue()
    print('The enemy got a surprise attack on you!')
    print('Because of darkness, your hit chance has decreased from 7 to 6!')
    pressToContinue()
    currentEnemy = [1,6,"Skeleton?",4]
    fight(currentEnemy[0], currentEnemy[1], currentEnemy[2],currentEnemy[3])
    if isSuccess ==1:
        runFromFirst()
    print('A Gold Key was added to your inventory!')
    inventory.append("Gold Key")
    pressToContinue()
    print()
    print('**You continue down the hall, and come across a door.')
    print('**You feel around for a key hole.. A torch would have made this easier.')
    pressToContinue()
    nonCombatRoll(1,10,"Door in the dark")
    if brokeIt == 1:
        print('The key broke. You can\'t open the door.')
        pressToContinue()
        print()
        print('So do you want to head home(y) or just hang out(n)?')
        pathChoice()
        if pathInt == 1:
            print('You head home, disgusted with your decision making and your bad luck.')
            pressToContinue()
            print('Thanks for playing... I guess.')
            quit()
        elif pathInt == -1:
            print('You hang out with your broken key in the dark.')
            pressToContinue()
            print('You die of starvation and boredom. Nice.')
            dead()
    print('You use: Gold Key to open the door.')
    print('\'Gold Key\' was removed from your inventory.')
    inventory.remove("Gold Key")
    pressToContinue()
    if leftIt != 0:
        print('**You stand around in the dark..')
        print('You think about the door in front of you. Do you want to approach the door again?(y) or not(n)')
        pathChoice()
        print()
        if pathInt == 1:
            nonCombatRoll(1,10,"Door in the dark")
            if brokeIt == 1:
                print('The key broke. You can\'t open the door.')
                pressToContinue()
                print()
                print('So do you want to head home(y) or just hang out(n)?')
                pathChoice()
                print()
                if pathInt == 1:
                    print('You head home, disgusted with your decision making and your bad luck.')
                    pressToContinue()
                    print('Thanks for playing... I guess.')
                    quit()
                elif pathInt == -1:
                    print()
                    print('You hang out with your broken key in the dark.')
                    pressToContinue()
                    print('You die of starvation and boredom. Nice.')
                    pressToContinue
                    dead()
            elif brokeIt == 0:
                print('You use: Gold Key to open the door.')
                print('\'Gold Key\' was removed from your inventory.')
                inventory.remove("Gold Key")
                pressToContinue()
        elif pathInt == -1:
            print('You stand around in the dark until you die of starvation and boredom. Nice.')
            pressToContinue()
            dead()
    if leftIt ==2:
        print('You decide not to attempt to open the door a second time.')
        pressToContinue()
        print('You die due to poor decision making.')
        pressToContinue()
        dead()

if 'Torch' in inventory:
    print('You open the door to a lit up hallway.')
    pressToContinue()
elif 'Torch' not in inventory:
    print('You open the door to a lit up hallway. There is another torch on the wall. Grab it?')
    pathChoice()
    if pathInt == 1:
        print()
        inventory.append("Torch")
        print('\'Torch\' has been added to your inventory. Good call.')
        pressToContinue()
    elif pathInt == -1:
        print()
        print('What is your deal? Are you trying to only make the wrong decision? I won\'t have it.')
        pressToContinue()
        print('You die due to absolutely horrendous decision making.')
        pressToContinue()
        dead()
print('You can see that the path splits up ahead.')
print('Would you like to go left(y) or right(n)')
pathChoice()