# Author(s): Noah Klaus, London Anderson
# Project: Quantum Checkers (though name has not been decided on as of 2/24/23)
# Common Issue(s): On line 22 (as of 3/3/23), the path to the google chrome app on a normal mac OS is listed. If you have changed the
# location of your chrome instance, you must fix this. If it isn't on line 22, check for "chrome_path" as a variable.
# Known Bugs: None As Of 04/27/23

# *FOR TESTING*
# print("X: " + str(x) + " Y: " + str(y)) # Helps with finding cursor for allocating space for buttons
# *FOR TESTING*

# START - IMPORTS
import pygame
import webbrowser
from game_logic import QuantumGame
from game_logic import SUPPORTED_GATES
# END - IMPORTS



# START - WEB SURFING
gitHubURL = 'https://github.com/cZAlpha/QuantumCheckers'  # The project's Github repository
dsuURL = 'https://www.desu.edu/'  # DSU's URL
chrome_path = 'open -a /Applications/Google\ Chrome.app %s'  # The path to chrome on most Macs
def openGithub():  # Opens github
    webbrowser.get(chrome_path).open(gitHubURL)
def openDSUWebsite():  # Opens DSU's website
    webbrowser.get(chrome_path).open(dsuURL)
# END - WEB SURFING



# START - SCREEN
    # START - PYGAME WINDOW INIT.
pygame.init()  # Init. Pygame
gameIcon = pygame.image.load("Assets/32x32Icon.png")  # Image conversion to pygame surface for game icon
pygame.display.set_icon(gameIcon)  # Changes window icon
FRAMERATE = 10
normalScreenRatio = (799,499)  # Screen ratio and game window creation (is supposed to be (800,500) but is smaller because of image conversion issues)
normalWidth = normalScreenRatio[0]
normalHeight = normalScreenRatio[1]
screen = pygame.display.set_mode(normalScreenRatio)
caption = pygame.display.set_caption("Quantum Checkers")  # Changes window caption
    # STOP - PYGAME WINDOW INIT.

    # START - Quantum Game Variables
DEFAULT_SHOTS = 1024
DEFAULT_CORR_COLOR = (216, 123, 104)
DEFAULT_IDEN_COLOR = (216, 123, 104)
DEFAULT_GRID_RESOLUTION = (640, 400)
    # STOP - Quantum Game Variables

    # START - SCOREBOARD SCREEN INFORMATION
# List that stores the (x,y) location in a tuple of where each level's score should be put on
scoreTextLocationList = [(190, 140), (190,188), (190,236), (190, 284), (190, 332), (422, 140), (422,188), (422,236), (422, 284), (422, 332), (654, 140), (654,188), (654,236), (654, 284), (654, 332)]
black = (0,0,0)  # The color black in RGB notation
scoreTextBackgroundColor = (239,239,239)  # The color of the score board menu background
scoreTextBackground = pygame.Surface((45,30))  # Makes the shape that will be the background of the score board text
scoreTextBackground.fill(scoreTextBackgroundColor)  # Fills in the background of the surface that was just made
scoreTextFont = pygame.font.SysFont("timesnewroman", 23)  # Stores the font times new roman in size 12 in a variable
    # STOP - SCOREBOARD SCREEN INFORMATION

    # START - GAMEPLAY UI SCREEN INFORMATION
        # Gate Indicator Text
leftGateIndicatorOverlayLocation = (38,330)    # The location, (x,y) notation of the gate overlays
rightGateIndicatorOverlayLocation = (675,330)  # ^
leftGateIndicatorTextLocation = (leftGateIndicatorOverlayLocation[0]   + 6, leftGateIndicatorOverlayLocation[1]  - 2)  # The location, (x,y) notation of the gate text
rightGateIndicatorTextLocation = (rightGateIndicatorOverlayLocation[0] + 6, rightGateIndicatorOverlayLocation[1] - 2)  # ^
currentGateIndicatorOverlayColor = (216,123,104) # The color of the peach background of the gate select buttons
currentGateIndicatorOverlay = pygame.Surface((25,22))  # Makes the shape that will be the background of the current gate indicator
currentGateIndicatorOverlay.fill(currentGateIndicatorOverlayColor)  # Fills in the background of the surface that was just made
currentGateTextFont = pygame.font.SysFont("timesnewroman", 20)  # Stores the font times new roman in size 12 in a variable
        # Current Level Indicator Text
currentLevelIndicatorOverlayLocation = (85, 22)    # The location, (x,y) notation of the current level indicator overlay
currentLevelIndicatorOverlayColor = (216,123,104)  # The color of the peach background of the buttons
currentLevelIndicatorOverlay = pygame.Surface((25,22))  # Makes the shape that will be the background of the current gate indicator
currentLevelIndicatorOverlay.fill(currentLevelIndicatorOverlayColor)
currentLevelIndicatorTextLocation = (currentLevelIndicatorOverlayLocation[0], currentLevelIndicatorOverlayLocation[1])
currentLevelIndicatorTextFont = pygame.font.SysFont("timesnewroman", 22)  # Stores the font times new roman in size 12 in a variable
        # Moves Left Indicator Text
movesLeftIndicatorOverlayLocation = (722, 128)  # The location, (x,y) notation of the current level indicator overlay
movesLeftIndicatorOverlayColor = (216, 123, 104)  # The color of the peach background of the buttons
movesLeftIndicatorOverlay = pygame.Surface((30, 25))  # Makes the shape that will be the background of the current gate indicator
movesLeftIndicatorOverlay.fill(movesLeftIndicatorOverlayColor)
movesLeftIndicatorTextLocation = (movesLeftIndicatorOverlayLocation[0], movesLeftIndicatorOverlayLocation[1])
movesLeftIndicatorTextFont = pygame.font.SysFont("timesnewroman",22)  # Stores the font times new roman in size 12 in a variable
    # Location of the origin
origin = (0,0)  # The location, (x,y) notation, of the goal indicator for any given level
    # STOP - GAMEPLAY UI SCREEN INFORMATION
# END - SCREEN



# START - METHODS
    # START - Display Methods
        # START - Menu Display Methods
def displayLevelSelectMenu(): # Displays the level select menu
    # Creation of the level select menu image & placing of image on the screen
    exitGameplayMenu = pygame.image.load('Assets/Third Iteration of Level Select UI.png').convert()
    screen.blit(exitGameplayMenu, origin)
    pygame.display.update()

def displayExitGameplayMenu():  # Displays the exit menu for gameplay
    # Creation of the exit gameplay menu image & placing of image on the screen
    exitGameplayMenu = pygame.image.load('Assets/ExitToMainMenuConfirmationMenu.png').convert()
    screen.blit(exitGameplayMenu, origin)
    pygame.display.update()

def displayMainMenu(): # Displays the rough outline of a main menu
    # Creation of the main menu's background & placing of image on the screen
    mainMenuBackground = pygame.image.load('Assets/Main Menu.png').convert()
    screen.blit(mainMenuBackground, origin)
    pygame.display.update()

def displayStartGameMenu(): # Displays the rough outline of the play menu
    # Creation of the play menu's background & placing of image on the screen
    playMenuBackground = pygame.image.load('Assets/Play Menu.png').convert()
    screen.blit(playMenuBackground, origin)
    pygame.display.update()

def displayCreditsMenu(): # Displays the rough outline of a credits menu
    # Creation of the credit menu's background & placing of image on the screen
    creditsMenuBackground = pygame.image.load('Assets/Credits Menu.png').convert()
    screen.blit(creditsMenuBackground, origin)
    pygame.display.update()
        # STOP - Menu Display Methods

        # START - How To Play Menu Display Methods
def displayHowToPlayMenu():  # Displays the how to play menu
    howToPlayMenuBackground = pygame.image.load('Assets/HowToPlayMenuAssets/HowToPlayMenu .png').convert()
    screen.blit(howToPlayMenuBackground, origin)
    pygame.display.update()

def displayHowToPlayMenuWhatIsQuantumCheckers():  # Function name explains purpose
    howToPlayMenuBackground = pygame.image.load('Assets/HowToPlayMenuAssets/HowToPlayMenuWhatIsQuantumCheckers.png').convert()
    screen.blit(howToPlayMenuBackground, origin)
    pygame.display.update()

def displayHowToPlayMenuWhatIsAQubit():  # Function name explains purpose
    howToPlayMenuBackground = pygame.image.load('Assets/HowToPlayMenuAssets/HowToPlayMenuWhatIsAQubit.png').convert()
    screen.blit(howToPlayMenuBackground, origin)
    pygame.display.update()

def displayHowToPlayMenuWhatDoesTheGridMean():  # Function name explains purpose
    howToPlayMenuBackground = pygame.image.load('Assets/HowToPlayMenuAssets/HowToPlayMenuWhatDoesTheGridMean.png').convert()
    screen.blit(howToPlayMenuBackground, origin)
    pygame.display.update()

def displayHowToPlayMenuhatIsALogicGate():  # Function name explains purpose
    howToPlayMenuBackground = pygame.image.load('Assets/HowToPlayMenuAssets/HowToPlayMenuWhatIsALogicGate.png').convert()
    screen.blit(howToPlayMenuBackground, origin)
    pygame.display.update()

def displayHowToPlayMenuHowDoIPlay():  # Displays the how to play menu
    howToPlayMenuBackground = pygame.image.load('Assets/HowToPlayMenuAssets/HowToPlayMenuHowDoIPlay.png').convert()
    screen.blit(howToPlayMenuBackground, origin)
    pygame.display.update()
        # STOP - How To Play Menu Display Methods

        # START - Gameplay Display Methods
def displayBlankGameScreen(level):  # Displays the blank game screen
    # Creation of the blank game screen & placing of image on the screen
    gamePlayBlankScreen = pygame.image.load('Assets/Seventh Iteration of Gameplay UI.png').convert_alpha()
    screen.blit(gamePlayBlankScreen, origin)
    displayCurrentLevelGoal(level)
    pygame.display.update()

def displayWhiteScreen():  # Displays a white image on the entire screen
    # Creation of a white image (800x500) & placing the image on the screen
    whiteBackground = pygame.image.load('Assets/800x500WHITE.png').convert_alpha()
    screen.blit(whiteBackground, origin)
    pygame.display.update()

def displayYouWonScreen():  # Displays the screen that plays when the player wins a level
    youWonScreen = pygame.image.load('Assets/YouWonScreen.png').convert_alpha()
    screen.blit(youWonScreen, origin)
    pygame.display.update()

def displayYouLostScreen():  # Diplays the screen that plays when the player loses a level
    youLostScreen = pygame.image.load('Assets/YouLostScreen.png').convert_alpha()
    screen.blit(youLostScreen, origin)
    pygame.display.update()
        # STOP - Gameplay Display Methods

        # START - Level Explanation, Goal Methods
def displayCurrentLevelGoal(level):  # Displays the current level's goal to the player
    gameplayLevelGoalFileLocation = "Assets/Level" + str(level) + "Assets/Level " + str(level) + " Circuit Goal.png"
    goal = pygame.image.load(gameplayLevelGoalFileLocation).convert_alpha()
    screen.blit(goal, origin)  # Displays the current level goal based on the passed parameter

def displayLevelExplanation(level):  # Displays the explanation for the level
    levelExplanationFileLocation = "Assets/Level" + str(level) + "Assets/Level " + str(level) + " Explanation.png"
    explanation = pygame.image.load(levelExplanationFileLocation).convert_alpha()
    screen.blit(explanation, origin)

def displayLevelGoal(level):  # Displays the screen that further explains the level and what the goal is
    levelEGoalFileLocation = "Assets/Level" + str(level) + "Assets/Level " + str(level) + " Goal.png"
    goal = pygame.image.load(levelEGoalFileLocation).convert_alpha()
    screen.blit(goal, origin)
        # STOP - Level Explanation, Goal Methods

        # START - Non-image Based Display Methods
def displayScoreBoardMenu():  # Displays the rough outline of the scoreboard menu
    scoreboardMenu = pygame.image.load('Assets/Scoreboard Menu.png').convert()  # Image shit
    screen.blit(scoreboardMenu, origin)  # Menu Image Is Put on the Screen
    for locationTuple in scoreTextLocationList:  # Placing of the text for the score board background
        screen.blit(scoreTextBackground, locationTuple)
    scoreTextListIndex = 0
    for locationTuple in scoreTextLocationList:
        scoreText = scoreTextFont.render(str(populateScoreBoardTextList()[scoreTextListIndex]), True, black)
        screen.blit(scoreText, locationTuple)
        scoreTextListIndex += 1  # Increments the scoreTextListIndex every for loop cycle
    pygame.display.update()

def displayCurrentGates(leftGateState, rightGateState):  # Displays the currently selected gates by taking the indices of each gate state
    gateList = ['X', 'Y', 'Z', 'H', 'CZ']  # Gate List
    leftGateText = currentGateTextFont.render(gateList[leftGateState], True, black)    # The text for the left gate selector
    rightGateText = currentGateTextFont.render(gateList[rightGateState], True, black)  # The text for the right gate selector
    # Placing of rectangle overlays
    screen.blit(currentGateIndicatorOverlay, leftGateIndicatorOverlayLocation)
    screen.blit(currentGateIndicatorOverlay, rightGateIndicatorOverlayLocation)
    # Placing of current gate text ~ Has control flow due to "CZ" gate being a string with a length of two as opposed to one ~ UwU
    if (leftGateState == 4): # Left gate CZ check
        screen.blit(leftGateText, (leftGateIndicatorTextLocation[0] - 7,leftGateIndicatorTextLocation[1]))  # CZ placement
    else:
        screen.blit(leftGateText, leftGateIndicatorTextLocation)
    if (rightGateState == 4):  # Left gate CZ check
        screen.blit(rightGateText, (rightGateIndicatorTextLocation[0] - 7,rightGateIndicatorTextLocation[1]))  # CZ placement
    else:
        screen.blit(rightGateText, rightGateIndicatorTextLocation)

def displayCurrentLevel(level):  # Displays the current level the player is on, LEVEL MUST BE INPUTTED AS AN INTEGER
    if ( level <= 0 or level >= 16 or level == None ):  # Makes sure that you're only passing an integer between 1 and 15
        raise Exception("Level provided can't less than 1 or greater than 15.")
    else:  # If inputted parameter value is valid
        currentLevelText = currentLevelIndicatorTextFont.render(str(level), True, black)  # Init. text
        screen.blit(currentLevelIndicatorOverlay, currentLevelIndicatorOverlayLocation)  # Puts overlay on
        screen.blit(currentLevelText, currentLevelIndicatorTextLocation)  # Prints text

def displayMovesLeft(level, moveCount):  # Displays the current moves the player has left
    if (level <= 0 or level >= 16 or level == None):  # Makes sure that you're only passing an integer between 1 and 15
        raise Exception("Level provided can't less than 1 or greater than 15.")
    else:  # If inputted parameter value is valid
        movesLeftText = movesLeftIndicatorTextFont.render(str(moveCountCapList[level] - moveCount), True, black)  # Init. text
        screen.blit(movesLeftIndicatorOverlay, movesLeftIndicatorOverlayLocation)  # Puts overlay on
        screen.blit(movesLeftText, movesLeftIndicatorTextLocation)  # Prints text
        # STOP - Non-image Based Display Methods
    # STOP - Display Methods

    # START - Main Menu Buttons
def mainMenuStartGameButton_click(event):  # Play Button
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (x > 545 and x < 750) and (y > 45 and y < 93):
            print("Play Button Has Been Clicked")
            return True

def mainMenuHowToPlayButton_click(event):  # How To Play Button
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (x > 545 and x < 750) and (y > 140 and y < 190):
           print("Play Button Has Been Clicked")
           return True

def mainMenuScoreBoardButton_click(event):  # How To Play Button
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (x > 545 and x < 750) and (y > 228 and y < 280):
           print("Play Button Has Been Clicked")
           return True

def mainMenuCreditsButton_click(event):  # Credits Button
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (x > 545 and x < 750) and (y > 322 and y < 373):
            print("Credits Button Has Been Clicked")
            return True

def mainMenuExitButton_click(event):  # Exit Button
    x,y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (x > 545 and x < 750) and (y > 418 and y < 465):
            print("Exit Button Has Been Clicked")
            return True
    # STOP - Main Menu Buttons

    # START - Start Game Menu Buttons
def startGameMenuBackButton_click(event):  # Back Button
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if ( state == "startGameMenu"):
            if (x > 320 and x < 480) and (y > 410 and y < 462):
                print("Back Button Has Been Clicked")
                return True

def startGameMenuGithubButton_click(event):  # Git Hub Button
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (state == "startGameMenu"):
            if (x > 300 and x < 500) and (y > 145 and y < 350):
                print("GitHub Button Has Been Clicked")
                return True
    # STOP - Start Game Menu Buttons

    # START - How To Play Menu Buttons
def howToPlayMenuBackButton_click(event):  # Back Button
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if ( state == "howToPlayMenu" or state == "howToPlayMenuSubMenu"):
            if (x > 346 and x < 454) and (y > 410 and y < 468):
                print("Back Button Has Been Clicked")
                return True

def howToPlayMenuWhatIsQuantumCheckersButton_click(event):  # Function name explains purpose
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (state == "howToPlayMenu"):
            if (x > 136 and x < 378) and (y > 142 and y < 200):
                print("What Is Quantum Checkers Button Has Been Clicked")
                return True

def howToPlayMenuWhatIsAQubitButton_click(event):  # Function name explains purpose
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (state == "howToPlayMenu"):
            if (x > 422 and x < 662) and (y > 142 and y < 200):
                print("What Is A Qubit Button Has Been Clicked")
                return True

def howToPlayMenuWhatDoesTheGridMeanButton_click(event):  # Function name explains purpose
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (state == "howToPlayMenu"):
            if (x > 136 and x < 378) and (y > 226 and y < 282):
                print("What Does The Grid Mean Button Has Been Clicked")
                return True

def howToPlayMenuhatIsALogicGateButton_click(event):  # Function name explains purpose
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (state == "howToPlayMenu"):
            if (x > 422 and x < 662) and (y > 226 and y < 282):
                print("What Is A Logic Gate Button Has Been Clicked")
                return True

def howToPlayMenuHowDoIPlayButton_click(event):  # Displays the how to play menu
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (state == "howToPlayMenu"):
            if (x > 286 and x < 520) and (y > 310 and y < 366):
                print("How Do I Play Button Has Been Clicked")
                return True
    # STOP - How To Play Menu

    # START - Scoreboard Menu Buttons
def scoreBoardMenuBackButton_click(event):  # Back Button
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (x > 320 and x < 480) and (y > 410 and y < 462):
            print("Back Button Has Been Clicked")
            return True
        # STOP - Scoreboard Menu

    # START - Credits Menu Buttons
def creditsMenuBackButton_click(event):  # Exit Button
    x,y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (state == "creditsMenu"):
            if (x > 320 and x < 480) and (y > 410 and y < 462):
                print("Back Button Has Been Clicked")
                return True

def creditsMenuGithubButton_click(event):  # Git Hub Button
    x,y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if ( state == "creditsMenu" ):
            if (x > 605 and x < 670) and (y > 330 and y < 350):
                print("GitHub Button Has Been Clicked")
                return True

def creditsMenuDSUButton_click(event):  # Git Hub Button
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (state == "creditsMenu"):
            if (x > 345 and x < 600) and (y > 330 and y < 350):
                print("DSU Button Has Been Clicked")
                return True
    # STOP - Credits Menu Buttons

    # START - Scoreboard File Reading Methods
        # Writes to the file in order to update the player's high score for any respective level
        # Takes "level" and "score" as parameters, "level" denotes what line of the file should be changed, which also denotes
        # what level to change the score of. "Score" denotes what integer value is to be placed on the respective line in the file
def updateScoreBoardTextList(level, score):
    if (level > 0 and level < 15 and score >= 0 and score <= 100):
        with open('scoreBoard.txt', 'r') as file:
            lines = file.readlines()
        lines[level - 1] = str(score) + '\n'
        with open('scoreBoard.txt', 'w') as file:
            file.writelines(lines)
    else:
        print("ERROR: The value(s) inputted into the 'updateScoreBoardTextList' function are not valid.")
        print("       The values inputted into the function were: " + "level: " + str(level) + " score: " + str(score))
        raise Exception("Invalid Input in Function Call")

    # Populates a list of score board values based on the player's high score on each level
def populateScoreBoardTextList():
    with open('scoreBoard.txt') as f:
        scoreBoardTextList = []  # Initializes a list to hold the scores of the user for the various levels in the game
        for line in f:  # Loops thru each line in the file
            scoreBoardTextList.append(line.strip())  # Appends the text from the file into a list to be used in order to display the scoreboard
    return scoreBoardTextList
    # STOP - Scoreboard File Reading Methods

    # START - Gameplay Buttons
def levelSelectButton(event):  # Level Select Button
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (state == "gamePlay"):
            if (x > 15 and x < 125) and (y > 16 and y < 60):
                print("Level Select Button Has Been Clicked")
                return True

def leftGateUpButton(event):  # Changes the left gate to the previous
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (state == "gamePlay"):
            if (x > 70 and x < 90) and (y > 282 and y < 297):
                print("Left Gate Up Button Has Been Clicked")
                return True

def leftGateDownButton(event):  # Changes the left gate to the previous
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (state == "gamePlay"):
            if (x > 70 and x < 90) and (y > 384 and y < 400):
                print("Left Gate Down Button Has Been Clicked")
                return True

def leftGateSelectButton(event):  # Changes the left qubit based on the selected logic gate
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (state == "gamePlay"):
            if (x > 32 and x < 127) and (y > 302 and y < 380):
                print("Left Gate Selector Has Been Clicked")
                return True

def resetLevelButton(event):  # Resets the level based on whatever level the player is currently on
    # MISSING IMPLEMENTATION OF LEVEL-DEPENDENT RESET
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (state == "gamePlay"):
            if (x > 358 and x < 442) and (y > 406 and y < 483):
                print("Reset Level Button Has Been Clicked")
                return True

def rightGateUpButton(event): # Right gate up button
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (state == "gamePlay"):
            if (x > 706 and x < 728) and (y > 280 and y < 297):
                print("Right Gate Up Button Has Been Clicked")
                return True

def rightGateDownButton(event):  # Right gate down button
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (state == "gamePlay"):
            if (x > 706 and x < 728) and (y > 382 and y < 400):
                print("Right Gate Down Button Has Been Clicked")
                return True

def rightGateSelectButton(event): # Right gate select button
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (state == "gamePlay"):
            if (x > 669 and x < 765) and (y > 300 and y < 378):
                print("Right Gate Select Button Has Been Clicked")
                return True

def exitGameplayButton(event):  # Exit Gameplay Button
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (state == "gamePlay"):
            if (x > 738 and x < 789) and (y > 10 and y < 52):
                print("Right Gate Select Button Has Been Clicked")
                return True
    # STOP - Gameplay Buttons

    # START - Gameplay Exit Menu Buttons
def exitGameplayMenuYesButton(event):  # Exit Gameplay Menu Yes Button
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (state == "exitGameplayMenu"):
            if (x > 263 and x < 343) and (y > 305 and y < 384):
                print("Exit Gameplay Menu Yes Button Has Been Clicked")
                return True
def exitGameplayMenuNoButton(event):  # Exit Gameplay Menu No Button
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (state == "exitGameplayMenu"):
            if (x > 455 and x < 532) and (y > 305 and y < 384):
                print("Exit Gameplay Menu No Button Has Been Clicked")
                return True
    # STOP - Gameplay Exit Menu Buttons

    # START - Level Select Menu Buttons
def levelSelectMenuMainMenuButton(event):
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (state == "levelSelectMenuGame" or state == "levelSelectMenuMain"):
            if (x > 45 and x < 225) and (y > 442 and y < 478):
                print("Level Select Menu Main Menu Button Has Been Clicked")
                return True

def levelSelectMenuBackButton(event, level):
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (state == "levelSelectMenuGame" or state == "levelSelectMenuMain"):
            if (x > 635 and x < 772) and (y > 442 and y < 478):
                print("Level Select Menu Back Button Has Been Clicked")
                return True

def displayGameUIAfterLevelSelectButtonClick():  # Displays the game screen fresh without resetting the circuit or gates
    displayWhiteScreen()
    displayBlankGameScreen(level)
    displayCurrentGates(leftGateState, rightGateState)
    displayMovesLeft(level, moveCount)
    displayCurrentLevel(level)
    showGame(game)

def levelSelectLevel1Button(event):
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (state == "levelSelectMenuGame" or state == "levelSelectMenuMain"):
            if (x > 368 and x < 425) and (y > 450 and y < 480):
                print("Level 1 Button Has Been Clicked")
                return True

def levelSelectLevel2Button(event):
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (state == "levelSelectMenuGame" or state == "levelSelectMenuMain"):
            if (x > 368 and x < 425) and (y > 395 and y < 425):
                print("Level 2 Button Has Been Clicked")
                return True

def levelSelectLevel3Button(event):
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (state == "levelSelectMenuGame" or state == "levelSelectMenuMain"):
            if (x > 368 and x < 425) and (y > 340 and y < 368):
                print("Level 3 Button Has Been Clicked")
                return True

def levelSelectLevel4Button(event):
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (state == "levelSelectMenuGame" or state == "levelSelectMenuMain"):
             if (x > 315 and x < 372) and (y > 300 and y < 328):
                print("Level 4 Button Has Been Clicked")
                return True

def levelSelectLevel5Button(event):
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (state == "levelSelectMenuGame" or state == "levelSelectMenuMain"):
            if (x > 425 and x < 480) and (y > 300 and y < 330):
                print("Level 5 Button Has Been Clicked")
                return True

def levelSelectLevel6Button(event):
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (state == "levelSelectMenuGame" or state == "levelSelectMenuMain"):
            if (x > 368 and x < 425) and (y > 262 and y < 290):  # THE X IS ALREADY GOOD, WORRY ABOUT THE Y VALUES
                print("Level 6 Button Has Been Clicked")
                return True

def levelSelectLevel7Button(event):
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (state == "levelSelectMenuGame" or state == "levelSelectMenuMain"):
             if (x > 315 and x < 372) and (y > 212 and y < 242):
                print("Level 7 Button Has Been Clicked")
                return True

def levelSelectLevel8Button(event):
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (state == "levelSelectMenuGame" or state == "levelSelectMenuMain"):
            if (x > 444 and x < 605) and (y > 213 and y < 242):
                print("Level 8 Button Has Been Clicked")
                return True

def levelSelectLevel9Button(event):
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (state == "levelSelectMenuGame" or state == "levelSelectMenuMain"):
            if (x > 260 and x < 320) and (y > 170 and y < 200):
                print("Level 9 Button Has Been Clicked")
                return True

def levelSelectLevel10Button(event):
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (state == "levelSelectMenuGame" or state == "levelSelectMenuMain"):
            if (x > 186 and x < 244) and (y > 170 and y < 200):
                print("Level 10 Button Has Been Clicked")
                return True

def levelSelectLevel11Button(event):
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (state == "levelSelectMenuGame" or state == "levelSelectMenuMain"):
            if (x > 480 and x < 535) and (y > 170 and y < 200):
                print("Level 11 Button Has Been Clicked")
                return True

def levelSelectLevel12Button(event):
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (state == "levelSelectMenuGame" or state == "levelSelectMenuMain"):
            if (x > 560 and x < 612) and (y > 170 and y < 200):
                print("Level 12 Button Has Been Clicked")
                return True

def levelSelectLevel13Button(event):
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (state == "levelSelectMenuGame" or state == "levelSelectMenuMain"):
            if (x > 315 and x < 372) and (y > 125 and y < 155):
                print("Level 13 Button Has Been Clicked")
                return True

def levelSelectLevel14Button(event):
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (state == "levelSelectMenuGame" or state == "levelSelectMenuMain"):
            if (x > 425 and x < 480) and (y > 125 and y < 155):
                print("Level 14 Button Has Been Clicked")
                return True

def levelSelectLevel15Button(event):
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (state == "levelSelectMenuGame" or state == "levelSelectMenuMain"):
            if (x > 368 and x < 425) and (y > 82 and y < 112):  # THE X IS ALREADY GOOD, WORRY ABOUT THE Y VALUES
                print("Level 15 Button Has Been Clicked")
                return True
    # STOP - Level Select Menu Buttons

    # START - Level Explanation Buttons
def levelExplanationContinueButton(event):
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (state == "levelExplanation"):
            if (x > 232 and x < 366) and (y > 395 and y < 458):  # THE X IS ALREADY GOOD, WORRY ABOUT THE Y VALUES
                print("Level Explanation Continue Button Has Been Clicked")
                return True

def levelExplanationBackButton(event):
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (state == "levelExplanation"):
            if (x > 435 and x < 568) and (y > 395 and y < 458):  # THE X IS ALREADY GOOD, WORRY ABOUT THE Y VALUES
                print("Level Explanation Back Button Has Been Clicked")
                return True
    # STOP - Level Explanation Buttons

    # START - Level Goal Explanation Buttons
def levelGoalExplanationContinueButton(event):
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (state == "levelGoalExplanation"):
            if (x > 232 and x < 366) and (y > 395 and y < 458):  # THE X IS ALREADY GOOD, WORRY ABOUT THE Y VALUES
                print("Level Goal Explanation Continue Button Has Been Clicked")
                return True

def levelGoalExplanationBackButton(event):
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (state == "levelGoalExplanation"):
            if (x > 435 and x < 568) and (y > 395 and y < 458):  # THE X IS ALREADY GOOD, WORRY ABOUT THE Y VALUES
                print("Level Goal Explanation Back Button Has Been Clicked")
                return True
    # STOP - Level Goal Explanation Buttons

    # START - You Won Screen Buttons
def youWonScreenMainMenuButton(event):
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (state == "youWonMenu"):
            if (x > 232 and x < 366) and (y > 395 and y < 458):  # THE X IS ALREADY GOOD, WORRY ABOUT THE Y VALUES
                print("You Won Screen Main Menu Button")
                return True

def youWonScreenNextLevelButton(event):
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (state == "youWonMenu"):
            if (x > 435 and x < 568) and (y > 395 and y < 458):  # THE X IS ALREADY GOOD, WORRY ABOUT THE Y VALUES
                print("You Won Screen Next Level Button")
                return True
    # STOP - You Won Screen Buttons

    # START - You Lost Screen Buttons
def youLostScreenMainMenuButton(event):
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (state == "youLostMenu"):
            if (x > 232 and x < 366) and (y > 395 and y < 458):  # THE X IS ALREADY GOOD, WORRY ABOUT THE Y VALUES
                print("You Lost Screen Main Menu Button")
                return True

def youLostScreenReplayLevelButton(event):
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (state == "youLostMenu"):
            if (x > 435 and x < 568) and (y > 395 and y < 458):  # THE X IS ALREADY GOOD, WORRY ABOUT THE Y VALUES
                print("You Lost Screen Replay Level Button")
                return True
    # START - You Lost Screen Buttons

    # START - IMAGE CONVERSION
def bytes_to_pygame_image(bytes_io):
    surface = pygame.image.load(bytes_io)  # Load the image from the bytes into a pygame Surface
    image = surface.convert().convert_alpha()  # Convert the surface to a pygame compatible image
    return image
    # END - IMAGE CONVERSION

    # START - Quantum Method(s) Implementing "game_logic.py"
def initGame(): # init. a quantum game instance and returns said game
    game = QuantumGame(
        initialize = [],
        allowed_gates = SUPPORTED_GATES,
        shots = DEFAULT_SHOTS,
        corr_color = DEFAULT_CORR_COLOR,
        iden_color = DEFAULT_IDEN_COLOR,
        grid_resolution = DEFAULT_GRID_RESOLUTION
    )
    return game

def showGame(game): # returns an image of the game inputted into the parameter
    image, win = game.draw_grid() # win is a boolean representing if the user won with this configuration or not
    if win:
        pass # put whatever code to run when the user wins here
    newImage = bytes_to_pygame_image(image)
    screen.blit(newImage, (79,0))
    # STOP - Quantum Method(s) Implementing "game_logic.py"
# END - METHODS



# START - GAME LOOP
    # Init. Quantum Game Backend
game = initGame()
    # Gameplay Variables and List Init.
gatePossibilitiesList = ['x', 'y', 'z', 'h', 'cz']
leftGateState = 0  # Init. the state of the left gate selector
rightGateState = 0  # Init. the state of the right gate selector
level = 1  # Variable that indicates the current level the player is on
moveCount = 0  # Variable that holds the number of logic gates the player has enacted onto the circuit
moveCountCapList = ["Placeholder",1,2,"Undecided","Undecided","Undecided","Undecided","Undecided","Undecided","Undecided","Undecided","Undecided","Undecided","Undecided","Undecided","Undecided"]  # The move cap for each level is state in index order of each level, hence the placeholder in index 0
    # Scoreboard Init.
populateScoreBoardTextList()  # Populates the score board text list so that the scoreboard menu works correctly
    # Pygame Init.
displayMainMenu()  # Places the main menu screen on the game window to initialize the game
state = "mainMenu"  # Initializing the FSM in the "mainMenu" state because the game starts on the main menu
clock = pygame.time.Clock()  # Clock (used in game loop to limit frame rate)
running = True  # Init. loop variable
while running:  # GAME LOOP
    for event in pygame.event.get():  # For loop to check for user input (events)
        if event.type == pygame.QUIT:  # If the "quit" button is clicked in the mac os's game window
            running = False
            pygame.quit()
            quit()

        # START - BUTTON CONTROL FLOW
        #
        if (event.type == pygame.constants.MOUSEBUTTONDOWN and event.button == 1):  # If the mouse has been clicked
            if ( state == "mainMenu" ):
                if ( mainMenuStartGameButton_click(event) ):  # If the start game button is clicked
                    state = "levelSelectMenuMain"
                    displayLevelSelectMenu()
                    break
                if ( mainMenuHowToPlayButton_click(event) ):
                    displayHowToPlayMenu()  # Displays the how to play menu
                    state = "howToPlayMenu"  # State change
                    break
                if ( mainMenuScoreBoardButton_click(event) ):
                    displayScoreBoardMenu()  # Displays the scoreboard menu
                    state = "scoreBoardMenu"  # State change
                    break
                if ( mainMenuCreditsButton_click(event) ):  # If the credits button is clicked
                    displayCreditsMenu()  # Displays the credits menu
                    state = "creditsMenu"  # State change
                    break
                if (mainMenuExitButton_click(event)):  # If the exit game button is clicked
                    running = False
                    pygame.quit()
                    quit()
                    break

            # Start Game Menu Button Control Flow
            if ( state == "startGameMenu" ):
                if ( startGameMenuBackButton_click(event) ):  # Back Button On Start Game Menu
                    displayMainMenu()  # Displays the main menu
                    state = "mainMenu"  # State change
                    break
                if ( startGameMenuGithubButton_click(event) ):  # Github Button On Start Game Menu
                    openGithub()  # Opens the project's Github repository in a native google chrome instance
                    break

            # How To Play Submenu(s) Button Control Flow
            if ( state == "howToPlayMenuSubMenu" ):
                if ( howToPlayMenuBackButton_click(event) ):  # Back button (same function used in actual HTP menu)
                    displayHowToPlayMenu()  # Displays the how to play menu
                    state = "howToPlayMenu"
                    break

            # How To Play Menu Button Control Flow
            if ( state == "howToPlayMenu" ):
                if ( howToPlayMenuBackButton_click(event) ):  # Back Button On How To Play Menu
                    displayMainMenu()  # Displays the main menu
                    state = "mainMenu"  # State change
                    break
                if ( howToPlayMenuWhatIsQuantumCheckersButton_click(event) ):  # What is quantum checkers button
                    displayHowToPlayMenuWhatIsQuantumCheckers()  # Displays what is quantum checkers asset
                    state = "howToPlayMenuSubMenu"  # State change
                    break
                if ( howToPlayMenuWhatIsAQubitButton_click(event) ):  # What is a qubit button
                    displayHowToPlayMenuWhatIsAQubit()  # Displays what is a qubit asset
                    state = "howToPlayMenuSubMenu"  # State change
                    break
                if ( howToPlayMenuWhatDoesTheGridMeanButton_click(event) ):  # What does the grid mean button
                    displayHowToPlayMenuWhatDoesTheGridMean()  # Displays what does the grid mean asset
                    state = "howToPlayMenuSubMenu"  # State change
                    break
                if ( howToPlayMenuhatIsALogicGateButton_click(event) ):  # What is a logic gate button
                    displayHowToPlayMenuhatIsALogicGate()  # Displays what is a logic gate asset
                    state = "howToPlayMenuSubMenu"  # State change
                    break
                if ( howToPlayMenuHowDoIPlayButton_click(event) ):  # How do I play button
                    displayHowToPlayMenuHowDoIPlay()  # Displays the how do I play asset
                    state = "howToPlayMenuSubMenu"  # State change
                    break

            # Scoreboard Menu Button Control Flow
            if ( state == "scoreBoardMenu" ):
                if ( scoreBoardMenuBackButton_click(event) ):  # Back Button On How To Play Menu
                    displayMainMenu()  # Displays the main menu
                    state = "mainMenu"  # State change
                    break

            # Credits Menu Button Control Flow
            if ( state == "creditsMenu" ):
                if ( creditsMenuBackButton_click(event) ):  # Back Button
                    displayMainMenu()  # Displays the main menu
                    state = "mainMenu"  # State change
                    break
                if ( creditsMenuGithubButton_click(event) ):  # Github Hypertext-lookalike Button
                    openGithub()  # Opens the project's Github repository in a native google chrome instance
                    break
                if ( creditsMenuDSUButton_click(event) ):  # DSU Hypertext-lookalike Button
                    openDSUWebsite()  # Opens DSU's website
                    break

            # Exit Gameplay Menu Button Control Flow
            if ( state == "exitGameplayMenu"):
                if ( exitGameplayMenuYesButton(event) ):  # If the yes button on the exit gameplay menu has been clicked
                    state = "mainMenu"
                    displayMainMenu()
                if ( exitGameplayMenuNoButton(event) ):  # If the no button on the exit gameplay menu has been clicked
                    state = "gamePlay"
                    displayWhiteScreen()
                    displayBlankGameScreen(level)
                    showGame(game) # Redisplays the saved game (May need to be moved for this to work)

            # Level Select Menu Button Control Flow (from in a game)
            if ( state == "levelSelectMenuGame" ):
                if (levelSelectMenuMainMenuButton(event)):  # Main menu button
                    displayWhiteScreen()
                    displayExitGameplayMenu()
                    state = "exitGameplayMenu"
                if ( levelSelectMenuBackButton(event, level) ): # Back Button
                    state = "gamePlay"
                    displayWhiteScreen()
                    showGame(game)
                if (levelSelectLevel1Button(event)):
                    leftGateState = 0  # Resets both gate states
                    rightGateState = 0  # ^
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                    displayMovesLeft(level, moveCount)  # Displays the # of moves the user is able to make before losing
                    game = initGame()  # Initializes a blank game
                    showGame(game)  # Displays the qubits
                    level = 1
                    state = "gamePlay"
                    displayGameUIAfterLevelSelectButtonClick()
                    break
                elif (levelSelectLevel2Button(event)):
                    leftGateState = 0  # Resets both gate states
                    rightGateState = 0  # ^
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                    displayMovesLeft(level, moveCount)  # Displays the # of moves the user is able to make before losing
                    game = initGame()  # Initializes a blank game
                    showGame(game)  # Displays the qubits
                    level = 2
                    state = "gamePlay"
                    displayGameUIAfterLevelSelectButtonClick()
                    break
                elif (levelSelectLevel3Button(event)):
                    leftGateState = 0  # Resets both gate states
                    rightGateState = 0  # ^
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                    displayMovesLeft(level, moveCount)  # Displays the # of moves the user is able to make before losing
                    game = initGame()  # Initializes a blank game
                    showGame(game)  # Displays the qubits
                    level = 3
                    state = "gamePlay"
                    displayGameUIAfterLevelSelectButtonClick()
                    break
                elif (levelSelectLevel4Button(event)):
                    leftGateState = 0  # Resets both gate states
                    rightGateState = 0  # ^
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                    displayMovesLeft(level, moveCount)  # Displays the # of moves the user is able to make before losing
                    game = initGame()  # Initializes a blank game
                    showGame(game)  # Displays the qubits
                    level = 4
                    state = "gamePlay"
                    displayGameUIAfterLevelSelectButtonClick()
                    break
                elif (levelSelectLevel5Button(event)):
                    leftGateState = 0  # Resets both gate states
                    rightGateState = 0  # ^
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                    displayMovesLeft(level, moveCount)  # Displays the # of moves the user is able to make before losing
                    game = initGame()  # Initializes a blank game
                    showGame(game)  # Displays the qubits
                    level = 5
                    state = "gamePlay"
                    displayGameUIAfterLevelSelectButtonClick()
                    break
                elif (levelSelectLevel6Button(event)):
                    leftGateState = 0  # Resets both gate states
                    rightGateState = 0  # ^
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                    displayMovesLeft(level, moveCount)  # Displays the # of moves the user is able to make before losing
                    game = initGame()  # Initializes a blank game
                    showGame(game)  # Displays the qubits
                    level = 6
                    state = "gamePlay"
                    displayGameUIAfterLevelSelectButtonClick()
                    break
                elif (levelSelectLevel7Button(event)):
                    leftGateState = 0  # Resets both gate states
                    rightGateState = 0  # ^
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                    displayMovesLeft(level, moveCount)  # Displays the # of moves the user is able to make before losing
                    game = initGame()  # Initializes a blank game
                    showGame(game)  # Displays the qubits
                    level = 7
                    state = "gamePlay"
                    displayGameUIAfterLevelSelectButtonClick()
                    break
                elif (levelSelectLevel8Button(event)):
                    leftGateState = 0  # Resets both gate states
                    rightGateState = 0  # ^
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                    displayMovesLeft(level, moveCount)  # Displays the # of moves the user is able to make before losing
                    game = initGame()  # Initializes a blank game
                    showGame(game)  # Displays the qubits
                    level = 8
                    state = "gamePlay"
                    displayGameUIAfterLevelSelectButtonClick()
                    break
                elif (levelSelectLevel9Button(event)):
                    leftGateState = 0  # Resets both gate states
                    rightGateState = 0  # ^
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                    displayMovesLeft(level, moveCount)  # Displays the # of moves the user is able to make before losing
                    game = initGame()  # Initializes a blank game
                    showGame(game)  # Displays the qubits
                    level = 9
                    state = "gamePlay"
                    displayGameUIAfterLevelSelectButtonClick()
                    break
                elif (levelSelectLevel10Button(event)):
                    leftGateState = 0  # Resets both gate states
                    rightGateState = 0  # ^
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                    displayMovesLeft(level, moveCount)  # Displays the # of moves the user is able to make before losing
                    game = initGame()  # Initializes a blank game
                    showGame(game)  # Displays the qubits
                    level = 10
                    state = "gamePlay"
                    displayGameUIAfterLevelSelectButtonClick()
                    break
                elif (levelSelectLevel11Button(event)):
                    leftGateState = 0  # Resets both gate states
                    rightGateState = 0  # ^
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                    displayMovesLeft(level, moveCount)  # Displays the # of moves the user is able to make before losing
                    game = initGame()  # Initializes a blank game
                    showGame(game)  # Displays the qubits
                    level = 11
                    state = "gamePlay"
                    displayGameUIAfterLevelSelectButtonClick()
                    break
                elif (levelSelectLevel12Button(event)):
                    leftGateState = 0  # Resets both gate states
                    rightGateState = 0  # ^
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                    displayMovesLeft(level, moveCount)  # Displays the # of moves the user is able to make before losing
                    game = initGame()  # Initializes a blank game
                    showGame(game)  # Displays the qubits
                    level = 12
                    state = "gamePlay"
                    displayGameUIAfterLevelSelectButtonClick()
                    break
                elif (levelSelectLevel13Button(event)):
                    leftGateState = 0  # Resets both gate states
                    rightGateState = 0  # ^
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                    displayMovesLeft(level, moveCount)  # Displays the # of moves the user is able to make before losing
                    game = initGame()  # Initializes a blank game
                    showGame(game)  # Displays the qubits
                    level = 13
                    state = "gamePlay"
                    displayGameUIAfterLevelSelectButtonClick()
                    break
                elif (levelSelectLevel14Button(event)):
                    leftGateState = 0  # Resets both gate states
                    rightGateState = 0  # ^
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                    displayMovesLeft(level, moveCount)  # Displays the # of moves the user is able to make before losing
                    game = initGame()  # Initializes a blank game
                    showGame(game)  # Displays the qubits
                    level = 14
                    state = "gamePlay"
                    displayGameUIAfterLevelSelectButtonClick()
                    break
                elif (levelSelectLevel15Button(event)):
                    leftGateState = 0  # Resets both gate states
                    rightGateState = 0  # ^
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                    displayMovesLeft(level, moveCount)  # Displays the # of moves the user is able to make before losing
                    game = initGame()  # Initializes a blank game
                    showGame(game)  # Displays the qubits
                    level = 15
                    state = "gamePlay"
                    displayGameUIAfterLevelSelectButtonClick()
                    break

            # Level Select Menu Button Control Flow (from main menu)
            if (state == "levelSelectMenuMain"):
                if (levelSelectMenuMainMenuButton(event) or levelSelectMenuBackButton(event, level)):  # Both the main menu and back button will bring the user back to the main menu, hence why there isn't control flow for both buttons separately
                    displayMainMenu()  # Displays the main menu
                    state = "mainMenu"  # State change
                    break
                if (levelSelectLevel1Button(event)):
                    leftGateState = 0  # Resets both gate states
                    rightGateState = 0  # ^
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                    displayMovesLeft(level, moveCount)  # Displays the # of moves the user is able to make before losing
                    game = initGame()  # Initializes a blank game
                    showGame(game)  # Displays the qubits
                    level = 1
                    state = "levelExplanation"
                    displayLevelExplanation(level)  # Displays the currently selected level's explanation
                    break
                elif (levelSelectLevel2Button(event)):
                    leftGateState = 0  # Resets both gate states
                    rightGateState = 0  # ^
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                    displayMovesLeft(level, moveCount)  # Displays the # of moves the user is able to make before losing
                    game = initGame()  # Initializes a blank game
                    showGame(game)  # Displays the qubits
                    level = 2
                    state = "levelExplanation"
                    displayLevelExplanation(level)  # Displays the currently selected level's explanation
                    break
                elif (levelSelectLevel3Button(event)):
                    leftGateState = 0  # Resets both gate states
                    rightGateState = 0  # ^
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                    displayMovesLeft(level, moveCount)  # Displays the # of moves the user is able to make before losing
                    game = initGame()  # Initializes a blank game
                    showGame(game)  # Displays the qubits
                    level = 3
                    state = "levelExplanation"
                    displayLevelExplanation(level)  # Displays the currently selected level's explanation
                    break
                elif (levelSelectLevel4Button(event)):
                    leftGateState = 0  # Resets both gate states
                    rightGateState = 0  # ^
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                    displayMovesLeft(level, moveCount)  # Displays the # of moves the user is able to make before losing
                    game = initGame()  # Initializes a blank game
                    showGame(game)  # Displays the qubits
                    level = 4
                    state = "levelExplanation"
                    displayLevelExplanation(level)  # Displays the currently selected level's explanation
                    break
                elif (levelSelectLevel5Button(event)):
                    leftGateState = 0  # Resets both gate states
                    rightGateState = 0  # ^
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                    displayMovesLeft(level, moveCount)  # Displays the # of moves the user is able to make before losing
                    game = initGame()  # Initializes a blank game
                    showGame(game)  # Displays the qubits
                    level = 5
                    state = "levelExplanation"
                    displayLevelExplanation(level)  # Displays the currently selected level's explanation
                    break
                elif (levelSelectLevel6Button(event)):
                    leftGateState = 0  # Resets both gate states
                    rightGateState = 0  # ^
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                    displayMovesLeft(level, moveCount)  # Displays the # of moves the user is able to make before losing
                    game = initGame()  # Initializes a blank game
                    showGame(game)  # Displays the qubits
                    level = 6
                    state = "levelExplanation"
                    displayLevelExplanation(level)  # Displays the currently selected level's explanation
                    break
                elif (levelSelectLevel7Button(event)):
                    leftGateState = 0  # Resets both gate states
                    rightGateState = 0  # ^
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                    displayMovesLeft(level, moveCount)  # Displays the # of moves the user is able to make before losing
                    game = initGame()  # Initializes a blank game
                    showGame(game)  # Displays the qubits
                    level = 7
                    state = "levelExplanation"
                    displayLevelExplanation(level)  # Displays the currently selected level's explanation
                    break
                elif (levelSelectLevel8Button(event)):
                    leftGateState = 0  # Resets both gate states
                    rightGateState = 0  # ^
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                    displayMovesLeft(level, moveCount)  # Displays the # of moves the user is able to make before losing
                    game = initGame()  # Initializes a blank game
                    showGame(game)  # Displays the qubits
                    level = 8
                    state = "levelExplanation"
                    displayLevelExplanation(level)  # Displays the currently selected level's explanation
                    break
                elif (levelSelectLevel9Button(event)):
                    leftGateState = 0  # Resets both gate states
                    rightGateState = 0  # ^
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                    displayMovesLeft(level, moveCount)  # Displays the # of moves the user is able to make before losing
                    game = initGame()  # Initializes a blank game
                    showGame(game)  # Displays the qubits
                    level = 9
                    state = "levelExplanation"
                    displayLevelExplanation(level)  # Displays the currently selected level's explanation
                    break
                elif (levelSelectLevel10Button(event)):
                    leftGateState = 0  # Resets both gate states
                    rightGateState = 0  # ^
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                    displayMovesLeft(level, moveCount)  # Displays the # of moves the user is able to make before losing
                    game = initGame()  # Initializes a blank game
                    showGame(game)  # Displays the qubits
                    level = 10
                    state = "levelExplanation"
                    displayLevelExplanation(level)  # Displays the currently selected level's explanation
                    break
                elif (levelSelectLevel11Button(event)):
                    leftGateState = 0  # Resets both gate states
                    rightGateState = 0  # ^
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                    displayMovesLeft(level, moveCount)  # Displays the # of moves the user is able to make before losing
                    game = initGame()  # Initializes a blank game
                    showGame(game)  # Displays the qubits
                    level = 11
                    state = "levelExplanation"
                    displayLevelExplanation(level)  # Displays the currently selected level's explanation
                    break
                elif (levelSelectLevel12Button(event)):
                    leftGateState = 0  # Resets both gate states
                    rightGateState = 0  # ^
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                    displayMovesLeft(level, moveCount)  # Displays the # of moves the user is able to make before losing
                    game = initGame()  # Initializes a blank game
                    showGame(game)  # Displays the qubits
                    level = 12
                    state = "levelExplanation"
                    displayLevelExplanation(level)  # Displays the currently selected level's explanation
                    break
                elif (levelSelectLevel13Button(event)):
                    leftGateState = 0  # Resets both gate states
                    rightGateState = 0  # ^
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                    displayMovesLeft(level, moveCount)  # Displays the # of moves the user is able to make before losing
                    game = initGame()  # Initializes a blank game
                    showGame(game)  # Displays the qubits
                    level = 13
                    state = "levelExplanation"
                    displayLevelExplanation(level)  # Displays the currently selected level's explanation
                    break
                elif (levelSelectLevel14Button(event)):
                    leftGateState = 0  # Resets both gate states
                    rightGateState = 0  # ^
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                    displayMovesLeft(level, moveCount)  # Displays the # of moves the user is able to make before losing
                    game = initGame()  # Initializes a blank game
                    showGame(game)  # Displays the qubits
                    level = 14
                    state = "levelExplanation"
                    displayLevelExplanation(level)  # Displays the currently selected level's explanation
                    break
                elif (levelSelectLevel15Button(event)):
                    leftGateState = 0  # Resets both gate states
                    rightGateState = 0  # ^
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                    displayMovesLeft(level, moveCount)  # Displays the # of moves the user is able to make before losing
                    game = initGame()  # Initializes a blank game
                    showGame(game)  # Displays the qubits
                    level = 15
                    state = "levelExplanation"
                    displayLevelExplanation(level)  # Displays the currently selected level's explanation
                    break

            # Level Explanation Button Control Flow
            if (state == "levelExplanation"):
                if (levelExplanationContinueButton(event)):  # Continue Button is clicked
                    state = "levelGoalExplanation"  # State change
                    displayLevelGoal(level)  # Displays a further explanation of the level in conjunction with the goal of the level
                    break
                if (levelExplanationBackButton(event)):  # Back Button is clicked
                    state = "levelSelectMenuMain"  # State change
                    displayLevelSelectMenu()  # Goes back to the level select menu

            # Level Goal Explanation Button Control Flow
            if (state == "levelGoalExplanation"):
                if (levelGoalExplanationContinueButton(event)):  # Continue button is clicked
                    state = "gamePlay"  # State change
                    displayWhiteScreen()  # Blanks the screen
                    displayGameUIAfterLevelSelectButtonClick()  # Displays the game UI
                    break
                if (levelGoalExplanationBackButton(event)):  # Back button is clicked
                    state = "levelExplanation"  # State change
                    displayLevelExplanation(level)  # Displays menu change
                    break

            # You Lost Screen Button Control Flow
            if (state == "youLostMenu"):
                if (youLostScreenMainMenuButton(event)):  # Continue button is clicked
                    state = "mainMenu"  # State change
                    displayWhiteScreen()  # Blanks the screen
                    displayMainMenu()  # Main Menu
                    break
                if (youLostScreenReplayLevelButton(event)):  # Back button is clicked
                    state = "gamePlay"  # State change
                    displayWhiteScreen()  # Blanks the screen
                    leftGateState = 0  # Resets both gate states
                    rightGateState = 0  # ^
                    displayBlankGameScreen(level)
                    displayCurrentLevel(level)  # Displays the current level the player is on
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                    displayMovesLeft(level, moveCount)  # Displays the # of moves the user is able to make before losing
                    game = initGame()  # Initializes a blank game
                    showGame(game)  # Displays the qubits
                    break

            # Gameplay Button Control Flow
            if (state == "gamePlay"):
                # Displays gameplay UI
                displayBlankGameScreen(level)  # Displays the game UI with an indicator for the goal of the level
                displayCurrentGates(leftGateState, rightGateState)  # Displays the currently selected gates
                displayCurrentLevel(level)  # Displays the current level the player is on
                displayMovesLeft(level, moveCount)  # Displays the # of moves the user is able to make before losing
                showGame(game)  # Displays the output of the quantum circuit

                # LEVEL SELECT BUTTON
                if ( levelSelectButton(event) ):  # Level Select Button
                    state = "levelSelectMenuGame"  # THIS SHOULD EVENTUALLY BE MIGRATED TO AN ACTUAL LEVEL SELECT MENU
                    displayLevelSelectMenu()
                    break
                # LEFT GATE BUTTONS
                if ( leftGateUpButton(event) ):  # Left Gate Up Button (MOVING UP MEANS GOING LEFT IN THE LIST, SUBTRACTING)
                    if ( leftGateState == 0 ):
                        leftGateState = len(gatePossibilitiesList) - 1  # Makes the left gate state loop back to end of list
                    elif ( leftGateState != 0 and leftGateState > 0 ):
                        leftGateState -= 1  # De-increments the leftGateState
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                if ( leftGateDownButton(event) ):  # Left Gate Down Button (MOVING DOWN MEANS GOING RIGHT IN THE LIST, ADDING)
                    if ( leftGateState == len(gatePossibilitiesList) - 1 ):
                        leftGateState = 0  # Makes the left gate state loop back to end of list
                    elif ( leftGateState != len(gatePossibilitiesList) - 1 and leftGateState < len(gatePossibilitiesList) - 1):
                        leftGateState += 1  # De-increments the leftGateState
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                if ( leftGateSelectButton(event) ):  # Left Gate Select Button
                    moveCount += 1  # Increments # of moves made by player
                    displayMovesLeft(level, moveCount)  # Displays the # of moves the user is able to make before losing
                    if (leftGateState == 4):  # Handles CZ gate applications
                        game.apply_gate(0, gatePossibilitiesList[leftGateState], target_qubit = 1)  # This will apply the currently selected game to the quantum game instance
                    else:  # Handles non-CZ gate applications
                        game.apply_gate(0, gatePossibilitiesList[leftGateState])  # This will apply the currently selected game to the quantum game instance
                    showGame(game)  # Updates the Qubits on the UI

                # RESET LEVEL BUTTON
                if ( resetLevelButton(event) ):  # Reset Level Button
                    moveCount = 0  # Resets move count to zero
                    leftGateState = 0  # Resets both gate states
                    rightGateState = 0  # ^
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                    displayMovesLeft(level, moveCount)  # Displays the current moves left
                    game = initGame()  # Initializes a blank game
                    showGame(game)  # Displays the qubits

                # RIGHT GATE BUTTONS
                if ( rightGateUpButton(event) ):  # Left Gate Up Button (MOVING UP MEANS GOING LEFT IN THE LIST, SUBTRACTING)
                    if (rightGateState == 0):
                        rightGateState = len(gatePossibilitiesList) - 1  # Makes the left gate state loop back to end of list
                    elif (rightGateState != 0 and rightGateState > 0):
                        rightGateState -= 1  # De-increments the leftGateState
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                if ( rightGateDownButton(event) ):  # Left Gate Down Button (MOVING DOWN MEANS GOING RIGHT IN THE LIST, ADDING)
                    if (rightGateState == len(gatePossibilitiesList) - 1):
                        rightGateState = 0  # Makes the left gate state loop back to end of list
                    elif (rightGateState != len(gatePossibilitiesList) - 1 and rightGateState < len(gatePossibilitiesList) - 1):
                        rightGateState += 1  # De-increments the leftGateState
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                if ( rightGateSelectButton(event) ):  # Left Gate Select Button
                    moveCount += 1  # Increments # of moves made by player
                    displayMovesLeft(level, moveCount)  # Displays the # of moves the user is able to make before losing
                    if ( rightGateState == 4):  # Handles CZ gate applications
                        game.apply_gate(1, gatePossibilitiesList[rightGateState], target_qubit = 0)  # This will apply the currently selected game to the quantum game instance
                    else:  # Handles non-CZ gate applications
                        game.apply_gate(1, gatePossibilitiesList[rightGateState])  # This will apply the currently selected game to the quantum game instance
                    showGame(game)  # Updates the Qubits on the UI

                # MOVE CAP CONTROL FLOW FOR LEVELS (Basically loss detecting control flow)
                if (level == 1 and moveCount == moveCountCapList[level]):  # Checks if the move cap of 1 has been exceeded for level 1
                    displayYouLostScreen()
                    state = "youLostMenu"
                    moveCount = 0
                if (level == 2 and moveCount == moveCountCapList[level]):  # Checks if the move cap of 2 has been exceeded for level 2
                    displayYouLostScreen()
                    state = "youLostMenu"
                    moveCount = 0
                if (level == 3 and moveCount == moveCountCapList[level]):  # Checks if the move cap of 2 has been exceeded for level 2
                    displayYouLostScreen()
                    state = "youLostMenu"
                    moveCount = 0
                if (level == 4 and moveCount == moveCountCapList[level]):  # Checks if the move cap of 2 has been exceeded for level 2
                    displayYouLostScreen()
                    state = "youLostMenu"
                    moveCount = 0
                if (level == 5 and moveCount == moveCountCapList[level]):  # Checks if the move cap of 2 has been exceeded for level 2
                    displayYouLostScreen()
                    state = "youLostMenu"
                    moveCount = 0
                if (level == 6 and moveCount == moveCountCapList[level]):  # Checks if the move cap of 1 has been exceeded for level 1
                    displayYouLostScreen()
                    state = "youLostMenu"
                    moveCount = 0
                if (level == 7 and moveCount == moveCountCapList[level]):  # Checks if the move cap of 2 has been exceeded for level 2
                    displayYouLostScreen()
                    state = "youLostMenu"
                    moveCount = 0
                if (level == 8 and moveCount == moveCountCapList[level]):  # Checks if the move cap of 2 has been exceeded for level 2
                    displayYouLostScreen()
                    state = "youLostMenu"
                    moveCount = 0
                if (level == 9 and moveCount == moveCountCapList[level]):  # Checks if the move cap of 2 has been exceeded for level 2
                    displayYouLostScreen()
                    state = "youLostMenu"
                    moveCount = 0
                if (level == 10 and moveCount == moveCountCapList[level]):  # Checks if the move cap of 2 has been exceeded for level 2
                    displayYouLostScreen()
                    state = "youLostMenu"
                    moveCount = 0
                if (level == 11 and moveCount == moveCountCapList[level]):  # Checks if the move cap of 1 has been exceeded for level 1
                    displayYouLostScreen()
                    state = "youLostMenu"
                    moveCount = 0
                if (level == 12 and moveCount == moveCountCapList[level]):  # Checks if the move cap of 2 has been exceeded for level 2
                    displayYouLostScreen()
                    state = "youLostMenu"
                    moveCount = 0
                if (level == 13 and moveCount == moveCountCapList[level]):  # Checks if the move cap of 2 has been exceeded for level 2
                    displayYouLostScreen()
                    state = "youLostMenu"
                    moveCount = 0
                if (level == 14 and moveCount == moveCountCapList[level]):  # Checks if the move cap of 2 has been exceeded for level 2
                    displayYouLostScreen()
                    state = "youLostMenu"
                    moveCount = 0
                if (level == 15 and moveCount == moveCountCapList[level]):  # Checks if the move cap of 2 has been exceeded for level 2
                    displayYouLostScreen()
                    state = "youLostMenu"
                    moveCount = 0

                # EXIT LEVEL BUTTON
                if ( exitGameplayButton(event) ):  # If the exit level button has been clicked
                    displayExitGameplayMenu()  # Displays the exit gameplay menu
                    state = "exitGameplayMenu"  # Changes state
            #
            # STOP - BUTTON CONTROL FLOW

    pygame.display.update()  # Update the screen
    pygame.display.set_icon(gameIcon)  # Changes window icon
    clock.tick(FRAMERATE)  # Sets the frame rate to 60
# END - GAME LOOP
