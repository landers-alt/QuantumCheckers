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
import time
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
gameIcon = pygame.image.load("Assets/IconAssets/32x32Icon.png")  # Image conversion to pygame surface for game icon
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
        # You Lost Score Info Text
youLostScoreInfoIndicatorOverlayLocation = (455, 230)  # The location, (x,y) notation of the current level indicator overlay
youLostScoreInfoIndicatorOverlayColor = (216, 123, 104)  # The color of the peach background of the buttons
youLostScoreInfoIndicatorOverlay = pygame.Surface((30, 25))  # Makes the shape that will be the background of the current gate indicator
youLostScoreInfoIndicatorOverlay.fill(youLostScoreInfoIndicatorOverlayColor)
youLostScoreInfoIndicatorTextLocation = (youLostScoreInfoIndicatorOverlayLocation[0], youLostScoreInfoIndicatorOverlayLocation[1])
youLostScoreInfoIndicatorTextFont = pygame.font.SysFont("timesnewroman",22)  # Stores the font times new roman in size 12 in a variable
        # You Won Score Info Text
youWonScoreInfoIndicatorOverlayLocation = (470, 225)  # The location, (x,y) notation of the current level indicator overlay
youWonScoreInfoIndicatorOverlayColor = (216, 123, 104)  # The color of the peach background of the buttons
youWonScoreInfoIndicatorOverlay = pygame.Surface((30, 25))  # Makes the shape that will be the background of the current gate indicator
youWonScoreInfoIndicatorOverlay.fill(youWonScoreInfoIndicatorOverlayColor)
youWonScoreInfoIndicatorTextLocation = (youWonScoreInfoIndicatorOverlayLocation[0], youWonScoreInfoIndicatorOverlayLocation[1])
youWonScoreInfoIndicatorTextFont = pygame.font.SysFont("timesnewroman",22)  # Stores the font times new roman in size 12 in a variable
youWonScoreInfoTextHighScoreOverlayLocation = (435, 253)
youWonScoreInfoTextHighScoreTextLocation = (youWonScoreInfoTextHighScoreOverlayLocation[0], youWonScoreInfoTextHighScoreOverlayLocation[1])
        # Location of the origin
origin = (0,0)  # The location, (x,y) notation, of the goal indicator for any given level
    # STOP - GAMEPLAY UI SCREEN INFORMATION
# END - SCREEN



# START - METHODS
    # START - Display Methods
        # START - Logo Display Method
def displayLogo():  # Displays the Quantum Checkers game logo
    logoImage = pygame.image.load('Assets/Quantum Checkers Logo.png').convert_alpha()
    screen.blit(logoImage, origin)
    pygame.display.update()
        # STOP - Logo Display Method

        # START - Menu Display Methods
def displayLevelSelectMenu(): # Displays the level select menu
    # Creation of the level select menu image & placing of image on the screen
    levelSelectMenu = pygame.image.load('Assets/Fourth Iteration of Level Select UI.png').convert()
    screen.blit(levelSelectMenu, origin)
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
    if ( level != "sandbox" ):  # Only show the current level goal if the user isn't in sandbox mode
        displayCurrentLevelGoal(level)
    pygame.display.update()

def displayWhiteScreen():  # Displays a white image on the entire screen
    # Creation of a white image (800x500) & placing the image on the screen
    whiteBackground = pygame.image.load('Assets/800x500WHITE.png').convert_alpha()
    screen.blit(whiteBackground, origin)
    pygame.display.update()

def displayYouWonScreen(level, moveCount):  # Displays the screen that plays when the player wins a level
    youWonScreen = pygame.image.load('Assets/WinLoseAssets/YouWonScreen.png').convert_alpha()
    screen.blit(youWonScreen, origin)
    displayYouWonScoreInfo(level, moveCount)
    pygame.display.update()

def displayWinBorder():  # Displays a green border surrounding the qubit display
    winBorder = pygame.image.load('Assets/WinLoseAssets/WinBorder.png').convert_alpha()
    screen.blit(winBorder, origin)
    pygame.display.update()

def displayYouLostScreen(level):  # Diplays the screen that plays when the player loses a level
    youLostScreen = pygame.image.load('Assets/WinLoseAssets/YouLostScreen.png').convert_alpha()
    screen.blit(youLostScreen, origin)
    displayYouLostScoreInfo(level)  # Displays the user's high score (if any)
    pygame.display.update()

def displayLoseBorder():  # Displays a red border surrounding the qubit display
    loseBorder = pygame.image.load("Assets/WinLoseAssets/LoseBorder.png").convert_alpha()
    screen.blit(loseBorder, origin)
    pygame.display.update()

def displayYouWonScreenForLevel15():  # Name is self explanatory
    youWonScreenForLevel15 = pygame.image.load('Assets/WinLoseAssets/YouWonScreenForLevel15.png').convert_alpha()
    screen.blit(youWonScreenForLevel15, origin)
    pygame.display.update()
        # STOP - Gameplay Display Methods

        # START - Level Explanation, Goal Methods
def displayCurrentLevelGoal(level):  # Displays the current level's goal to the player
    if ( level != "sandbox" ):  # If the user is actually playing a level
        gameplayLevelGoalFileLocation = "Assets/Level Assets/Level" + str(level) + "Assets/Level " + str(level) + " Circuit Goal.png"
        goal = pygame.image.load(gameplayLevelGoalFileLocation).convert_alpha()
        screen.blit(goal, origin)  # Displays the current level goal based on the passed parameter
    elif ( level == "sandbox" ):  # If user is in the sandbox
        print("Sandbox mode...")
    else:  # Error handling
        raise Exception("Inputted level is not valid.")

def displayLevelExplanation(level):  # Displays the explanation for the level
    levelExplanationFileLocation = "Assets/Level Assets/Level" + str(level) + "Assets/Level " + str(level) + " Explanation.png"
    explanation = pygame.image.load(levelExplanationFileLocation).convert_alpha()
    screen.blit(explanation, origin)

def displayLevelGoal(level):  # Displays the screen that further explains the level and what the goal is
    levelEGoalFileLocation = "Assets/Level Assets/Level" + str(level) + "Assets/Level " + str(level) + " Goal.png"
    goal = pygame.image.load(levelEGoalFileLocation).convert_alpha()
    screen.blit(goal, origin)
        # STOP - Level Explanation, Goal Methods

        # START - Scoreboard Menu Display Methods
def displayScoreBoardMenuAreYouSure():
    FileLocation = "Assets/ScoreBoardMenuAssets/Scoreboard AreYouSure Menu.png"
    areYouSureMenu = pygame.image.load(FileLocation).convert_alpha()
    screen.blit(areYouSureMenu, origin)
        # STOP - Scoreboard Menu Display Methods

        # START - Non-image Based Display Methods
def displayScoreBoardMenu():  # Displays the rough outline of the scoreboard menu
    scoreboardMenu = pygame.image.load('Assets/ScoreBoardMenuAssets/Scoreboard Menu.png').convert()  # Image shit
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

def displayCurrentLevel(level):  # Displays the current level the player is on, LEVEL MUST BE INPUTTED AS AN INTEGER OR SANDBOX AS A STR
    if ( level == "sandbox" ):  # If the user is in sandbox mode
        currentLevelText = currentLevelIndicatorTextFont.render("N/A", True, black)  # Init. text
        screen.blit(currentLevelIndicatorOverlay, currentLevelIndicatorOverlayLocation)  # Puts overlay on
        screen.blit(currentLevelText, currentLevelIndicatorTextLocation)  # Prints text
    elif ( level <= 0 or level >= 16 or level == None ):  # Makes sure that you're only passing an integer between 1 and 15
        raise Exception("Level provided can't less than 1 or greater than 15.")
    else:  # If inputted parameter value is valid
        currentLevelText = currentLevelIndicatorTextFont.render(str(level), True, black)  # Init. text
        screen.blit(currentLevelIndicatorOverlay, currentLevelIndicatorOverlayLocation)  # Puts overlay on
        screen.blit(currentLevelText, currentLevelIndicatorTextLocation)  # Prints text

def displayMovesLeft(level, moveCount):  # Displays the current moves the player has left
    if (level == "sandbox"):
        movesLeftText = movesLeftIndicatorTextFont.render("N/A", True, black)  # Init. text
        screen.blit(movesLeftIndicatorOverlay, movesLeftIndicatorOverlayLocation)  # Puts overlay on
        screen.blit(movesLeftText, movesLeftIndicatorTextLocation)  # Prints text
    elif (level <= 0 or level >= 16 or level == None or level == "Undecided" or level == "Placeholder"):  # Makes sure that you're only passing an integer between 1 and 15
        raise Exception("Level provided can't less than 1 or greater than 15, and cannot be a string.")
    else:  # If inputted parameter value is valid
        movesLeftText = movesLeftIndicatorTextFont.render(str(moveCountCapList[level] - moveCount), True, black)  # Init. text
        screen.blit(movesLeftIndicatorOverlay, movesLeftIndicatorOverlayLocation)  # Puts overlay on
        screen.blit(movesLeftText, movesLeftIndicatorTextLocation)  # Prints text

def displayYouLostScoreInfo(level):  # Displays the high score of the user on the you lost menu screen
    if (level == "sandbox" or level <= 0 or level >= 16 or level == None or level == "Undecided" or level == "Placeholder"):
        raise Exception("Level provided can't less than 1 or greater than 15, also can't be in sandbox.")
    else:  # If inputted parameter value is valid
        youLostScoreInfoText = youLostScoreInfoIndicatorTextFont.render(readScoreBoardTextText(level), True, black)  # Init. text
        screen.blit(youLostScoreInfoIndicatorOverlay, youLostScoreInfoIndicatorOverlayLocation)  # Puts overlay on
        screen.blit(youLostScoreInfoText, youLostScoreInfoIndicatorTextLocation)  # Prints text

def displayYouWonScoreInfo(level, moveCount): # Displays both the high score of the user and their current score (their moveCount)
    if (level == "sandbox" or level <= 0 or level >= 16 or level == None or level == "Undecided" or level == "Placeholder"):
        raise Exception("Level provided can't less than 1 or greater than 15, also can't be in sandbox.")
    else:  # If inputted parameter value is valid
        youWonScoreInfoTextCurrentScore = youWonScoreInfoIndicatorTextFont.render(str(moveCount), True, black)  # Init. text
        screen.blit(youWonScoreInfoIndicatorOverlay, youWonScoreInfoIndicatorOverlayLocation)  # Puts overlay on
        screen.blit(youWonScoreInfoTextCurrentScore, youWonScoreInfoIndicatorTextLocation)  # Prints text

        youWonScoreInfoTextHighScore = youWonScoreInfoIndicatorTextFont.render(readScoreBoardTextText(level), True, black)  # Init. text
        screen.blit(youWonScoreInfoIndicatorOverlay, youWonScoreInfoTextHighScoreOverlayLocation)  # Puts overlay on
        screen.blit(youWonScoreInfoTextHighScore, youWonScoreInfoTextHighScoreTextLocation)  # Prints text
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
        if ( state == "scoreBoardMenu"):
            if (x > 320 and x < 480) and (y > 410 and y < 462):
                print("Back Button Has Been Clicked")
                return True

def scoreBoardMenuClearProgressButton_click(event):  # Clears user progress
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (state == "scoreBoardMenu"):
            if (x > 628 and x < 740) and (y > 32 and y < 88):
                print("Clear Progress Button Has Been Clicked")
                return True

            # START - Scoreboard Menu Are You Sure Buttons
def scoreBoardAreYouSureMenuYesButton_click(event):
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (state == "scoreBoardAreYouSureMenu"):
            if (x > 150 and x < 352) and (y > 280 and y < 332):
                print("Yes Button Has Been Clicked")
                return True
def scoreBoardAreYouSureMenuNoButton_click(event):
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (state == "scoreBoardAreYouSureMenu"):
            if (x > 440 and x < 644) and (y > 280 and y < 332):
                print("No Button Has Been Clicked")
                return True
            # START - Scoreboard Menu Are You Sure Buttons
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
def updateScoreBoardTextFile(level, score):
    score = returnHighScore(level, score)
    if (level != "sandbox"):
        if (level > 0 and level < 16 and score >= 0 and score <= 100):
            with open('scoreBoard.txt', 'r') as file:
                lines = file.readlines()
            lines[level - 1] = str(score) + '\n'
            with open('scoreBoard.txt', 'w') as file:
                file.writelines(lines)
    elif(level == "sandbox"):
        pass
    else:
        print("ERROR: The value(s) inputted into the 'updateScoreBoardTextList' function are not valid.")
        print("       The values inputted into the function were: " + "level: " + str(level) + " score: " + str(score))
        raise Exception("Invalid Input in Function Call")

def readScoreBoardTextText(level):  # Reads the file and returns the value specified on the level parameter
    if ( level != "sandbox"):
        if (level >= 0 and level < 16):
            try:
                with open('scoreBoard.txt', 'r') as file:
                    lines = file.readlines()
                    line = lines[level - 1]
                    line = str(line)
                    if (line != '\n'):
                        return line.strip()
                    else:
                        return "N/A"
            except FileNotFoundError:
                return "File not found."
    elif ( level == "sandbox"):
        return "N/A"
    else:
        print("ERROR: The value(s) inputted into the 'updateScoreBoardTextList' function are not valid.")
        print("       The values inputted into the function were: " + "level: " + str(level))
        raise Exception("Invalid Input in Function Call")

def populateScoreBoardTextList(): # Populates a list of score board values based on the player's high score on each level
    with open('scoreBoard.txt') as f:
        scoreBoardTextList = []  # Initializes a list to hold the scores of the user for the various levels in the game
        for line in f:  # Loops thru each line in the file
            scoreBoardTextList.append(line.strip())  # Appends the text from the file into a list to be used in order to display the scoreboard
    return scoreBoardTextList

def clearUserProgress():  # Clears the scoreBoard.txt of data
    scoreBoardFile = "scoreBoard.txt"
    with open(scoreBoardFile, 'r') as file:
        lines = file.readlines()

    with open(scoreBoardFile, 'w') as file:
        for _ in lines:
            file.write('\n')
    # STOP - Scoreboard File Reading Methods

    # START - Highscore Checking method
def returnHighScore(level, score):  # Returns the high score of a level based on the previous high score and the current score
    if (score == 0):
        raise Exception("You can't have a score of 0, something went wrong.")
    if ( level != "sandbox" ):  # This if statement serves to ignore score while in sandbox mode
        if (level <= 0 or level >= 16 ):
            raise Exception("You can't have a level 0 or below, or 16 or above.")
    if (readScoreBoardTextText(level) != "N/A"):
        integerA = int(readScoreBoardTextText(level))#  The user's high score for the given level
        integerB = score  # The user's current score
        print("AAAAA")
        return min(integerA, integerB)
    else:
        print("BBBBB")
        return score  # If there was no high score, return the user's score
    # STOP - Highscore Checking method

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

def levelSelectSandboxButton(event):
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (state == "levelSelectMenuGame" or state == "levelSelectMenuMain"):
            if (x > 646 and x < 762) and (y > 34 and y < 70):
                print("Sandbox Button Has Been Clicked")
                return True

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

    # START - You Lost/Won Screen Buttons
def loseWinScreenMainMenuButton(event):
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (state == "youLostMenu" or state == "youWonMenu"):
            if (x > 232 and x < 366) and (y > 395 and y < 458):
                print("You Lost Screen Main Menu Button was clicked")
                return True

def loseWinLevelButton(event):
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (state == "youLostMenu" or state == "youWonMenu"):
            if (x > 435 and x < 568) and (y > 395 and y < 458):
                print("You Lost Screen Replay Level Button was clicked")
                return True

        # START - You Won Level 15 Menu Buttons
def youWonLevel15MainMenuButton(event):
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (state == "youWonLevel15Menu"):
            print("X: " + str(x) + " Y: " + str(y))  # Helps with finding cursor for allocating space for buttons
            if (x > 332 and x < 466) and (y > 400 and y < 460):
                print("Main Menu Button was clicked")
                return True

        # STOP - You Won Level 15 Menu Buttons
    # START - You Lost/Won Screen Buttons

    # START - IMAGE CONVERSION
def bytes_to_pygame_image(bytes_io):
    surface = pygame.image.load(bytes_io)  # Load the image from the bytes into a pygame Surface
    image = surface.convert().convert_alpha()  # Convert the surface to a pygame compatible image
    return image
    # END - IMAGE CONVERSION

    # START - Quantum Method(s) Implementing "game_logic.py"
def displayGameUIAfterLevelSelectButtonClick():  # Displays the game screen fresh without resetting the circuit or gates
    displayWhiteScreen()
    displayBlankGameScreen(level)
    displayCurrentGates(leftGateState, rightGateState)
    displayMovesLeft(level, moveCount)
    displayCurrentLevel(level)
    showGame(game)

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

def initGameBasedOnLevel(level):  # Function that inits. a game based on the current level
    if (level == 1):
        return initLevelOne()
    elif (level == 2):
        return initLevelTwo()
    elif (level == 3):
        return initLevelThree()
    elif (level == 4):
        return initLevelFour()
    elif (level == 5):
        return initLevelFive()
    elif (level == 6):
        return initLevelSix()
    elif (level == 7):
        return initLevelSeven()
    elif (level == 8):
        return initLevelEight()
    elif (level == 9):
        return initLevelNine()
    elif (level == 10):
        return initLevelTen()
    elif (level == 11):
        return initLevelEleven()
    elif (level == 12):
        return initLevelTwelve()
    elif (level == 13):
        return initLevelThirteen()
    elif (level == 14):
        return initLevelFourteen()
    elif (level == 15):
        return initLevelFifteen()
    # IMPORTANT!!!
    # MAKE SURE TO PUT THE REST OF THE CONTROL FLOW FOR THE OTHER 12 LEVELS!!!
    # IMPORTANT!!!
    else:
        print("AN ERROR IN THE initGameBasedOnLevel FUNCTION HAS OCCURED, MOST LIKELY DUE TO BAD INPUT")

def initLevelOne():  # Init. a quantum game instance with win conditions for level 1
    game = QuantumGame(
        initialize=[],
        allowed_gates=SUPPORTED_GATES,
        shots=DEFAULT_SHOTS,
        corr_color=DEFAULT_CORR_COLOR,
        iden_color=DEFAULT_IDEN_COLOR,
        grid_resolution=DEFAULT_GRID_RESOLUTION,
        win_condition = {'XI': 0, 'XZ': 0, 'XX': 0, 'ZI': 0, 'ZZ': 0, 'ZX': 0, 'IZ': 1, 'IX': 0}
    )
    return game

def initLevelTwo():  # Init. a quantum game instance with win conditions for level 2
    game = QuantumGame(
        initialize=[],
        allowed_gates=SUPPORTED_GATES,
        shots=DEFAULT_SHOTS,
        corr_color=DEFAULT_CORR_COLOR,
        iden_color=DEFAULT_IDEN_COLOR,
        grid_resolution=DEFAULT_GRID_RESOLUTION,
        win_condition={'XI': 0, 'XZ': 0, 'XX': 0, 'ZI': 0, 'ZZ': 1, 'ZX': 0, 'IZ': 0, 'IX': 0}
    )
    return game

def initLevelThree():  # Init. a quantum game instance with win conditions for level 3
    game = QuantumGame(
        initialize=[],
        allowed_gates=SUPPORTED_GATES,
        shots=DEFAULT_SHOTS,
        corr_color=DEFAULT_CORR_COLOR,
        iden_color=DEFAULT_IDEN_COLOR,
        grid_resolution=DEFAULT_GRID_RESOLUTION,
        win_condition={'XI': 0, 'XZ': 0, 'XX': 0, 'ZI': 1, 'ZZ': 0, 'ZX': 0, 'IZ': 0, 'IX': 0}
    )
    return game

def initLevelFour():  # Init. a quantum game instance with win conditions for level 4
    game = QuantumGame(
        initialize=[],
        allowed_gates=SUPPORTED_GATES,
        shots=DEFAULT_SHOTS,
        corr_color=DEFAULT_CORR_COLOR,
        iden_color=DEFAULT_IDEN_COLOR,
        grid_resolution=DEFAULT_GRID_RESOLUTION,
        win_condition={'XI': 1, 'XZ': 1, 'XX': 0, 'ZI': 0, 'ZZ': 0, 'ZX': 0, 'IZ': 1, 'IX': 0}
    )
    return game

def initLevelFive():  # Init. a quantum game instance with win conditions for level 5
    game = QuantumGame(
        initialize=[],
        allowed_gates=SUPPORTED_GATES,
        shots=DEFAULT_SHOTS,
        corr_color=DEFAULT_CORR_COLOR,
        iden_color=DEFAULT_IDEN_COLOR,
        grid_resolution=DEFAULT_GRID_RESOLUTION,
        win_condition={'XI': 0, 'XZ': 0, 'XX': 0, 'ZI': 1, 'ZZ': 0, 'ZX': 1, 'IZ': 0, 'IX': 1}
    )
    return game

def initLevelSix():  # Init. a quantum game instance with win conditions for level 6
    game = QuantumGame(
        initialize=[],
        allowed_gates=SUPPORTED_GATES,
        shots=DEFAULT_SHOTS,
        corr_color=DEFAULT_CORR_COLOR,
        iden_color=DEFAULT_IDEN_COLOR,
        grid_resolution=DEFAULT_GRID_RESOLUTION,
        win_condition={'XI': 1, 'XZ': 0, 'XX': 1, 'ZI': 0, 'ZZ': 0, 'ZX': 0, 'IZ': 0, 'IX': 1}
    )
    return game

def initLevelSeven():  # Init. a quantum game instance with win conditions for level 7
    game = QuantumGame(
        initialize=[],
        allowed_gates=SUPPORTED_GATES,
        shots=DEFAULT_SHOTS,
        corr_color=DEFAULT_CORR_COLOR,
        iden_color=DEFAULT_IDEN_COLOR,
        grid_resolution=DEFAULT_GRID_RESOLUTION,
        win_condition={'XI': 1, 'XZ': 0, 'XX': 0, 'ZI': 0, 'ZZ': 0, 'ZX': 0, 'IZ': 0, 'IX': 0}
    )
    return game

def initLevelEight():  # Init. a quantum game instance with win conditions for level 8
    game = QuantumGame(
        initialize=[],
        allowed_gates=SUPPORTED_GATES,
        shots=DEFAULT_SHOTS,
        corr_color=DEFAULT_CORR_COLOR,
        iden_color=DEFAULT_IDEN_COLOR,
        grid_resolution=DEFAULT_GRID_RESOLUTION,
        win_condition={'XI': 0, 'XZ': 0, 'XX': 0, 'ZI': 0, 'ZZ': 0, 'ZX': 0, 'IZ': 0, 'IX': 1}
    )
    return game

def initLevelNine():  # Init. a quantum game instance with win conditions for level 8
    game = QuantumGame(
        initialize=[],
        allowed_gates=SUPPORTED_GATES,
        shots=DEFAULT_SHOTS,
        corr_color=DEFAULT_CORR_COLOR,
        iden_color=DEFAULT_IDEN_COLOR,
        grid_resolution=DEFAULT_GRID_RESOLUTION,
        win_condition={'XI': 0, 'XZ': 1, 'XX': 0, 'ZI': 0, 'ZZ': 0, 'ZX': 1, 'IZ': 0, 'IX': 0}
    )
    return game

def initLevelTen():
    game = QuantumGame(
        initialize=[],
        allowed_gates=SUPPORTED_GATES,
        shots=DEFAULT_SHOTS,
        corr_color=DEFAULT_CORR_COLOR,
        iden_color=DEFAULT_IDEN_COLOR,
        grid_resolution=DEFAULT_GRID_RESOLUTION,
        win_condition={'XI': 0, 'XZ': 1, 'XX': 0, 'ZI': 0, 'ZZ': 0, 'ZX': 0, 'IZ': 0, 'IX': 0}
    )
    return game

def initLevelEleven():
    game = QuantumGame(
        initialize=[],
        allowed_gates=SUPPORTED_GATES,
        shots=DEFAULT_SHOTS,
        corr_color=DEFAULT_CORR_COLOR,
        iden_color=DEFAULT_IDEN_COLOR,
        grid_resolution=DEFAULT_GRID_RESOLUTION,
        win_condition={'XI': 0, 'XZ': 0, 'XX': 0, 'ZI': 0, 'ZZ': 0, 'ZX': 0, 'IZ': 0, 'IX': 0}
    )
    return game

def initLevelTwelve():
    game = QuantumGame(
        initialize=[],
        allowed_gates=SUPPORTED_GATES,
        shots=DEFAULT_SHOTS,
        corr_color=DEFAULT_CORR_COLOR,
        iden_color=DEFAULT_IDEN_COLOR,
        grid_resolution=DEFAULT_GRID_RESOLUTION,
        win_condition={'XI': 0, 'XZ': 0, 'XX': 0, 'ZI': 0, 'ZZ': 0, 'ZX': 0, 'IZ': 0, 'IX': 0}
    )
    return game

def initLevelThirteen():
    game = QuantumGame(
        initialize=[],
        allowed_gates=SUPPORTED_GATES,
        shots=DEFAULT_SHOTS,
        corr_color=DEFAULT_CORR_COLOR,
        iden_color=DEFAULT_IDEN_COLOR,
        grid_resolution=DEFAULT_GRID_RESOLUTION,
        win_condition={'XI': 0, 'XZ': 0, 'XX': 1, 'ZI': 0, 'ZZ': 0, 'ZX': 0, 'IZ': 0, 'IX': 0}
    )
    return game

def initLevelFourteen():
    game = QuantumGame(
        initialize=[],
        allowed_gates=SUPPORTED_GATES,
        shots=DEFAULT_SHOTS,
        corr_color=DEFAULT_CORR_COLOR,
        iden_color=DEFAULT_IDEN_COLOR,
        grid_resolution=DEFAULT_GRID_RESOLUTION,
        win_condition={'XI': 0, 'XZ': 0, 'XX': 0, 'ZI': 0, 'ZZ': 1, 'ZX': 0, 'IZ': 0, 'IX': 0}
    )
    return game

def initLevelFifteen():
    game = QuantumGame(
        initialize=[],
        allowed_gates=SUPPORTED_GATES,
        shots=DEFAULT_SHOTS,
        corr_color=DEFAULT_CORR_COLOR,
        iden_color=DEFAULT_IDEN_COLOR,
        grid_resolution=DEFAULT_GRID_RESOLUTION,
        win_condition={'XI': 0, 'XZ': 0, 'XX': 1, 'ZI': 0, 'ZZ': 1, 'ZX': 0, 'IZ': 0, 'IX': 0}
    )
    return game


def showGame(game): # returns an image of the game inputted into the parameter
    image, win = game.draw_grid() # win is a boolean representing if the user won with this configuration or not
    if win:
        pass # put whatever code to run when the user wins here
    newImage = bytes_to_pygame_image(image)
    screen.blit(newImage, (79,0))
    # STOP - Quantum Method(s) Implementing "game_logic.py"

def save_screen_as_image(screen):
    filename = "screenshot.png"  # Specify the filename here
    pygame.image.save(screen, filename)
    return pygame.image.load(filename)

def colorFinder(screenshot):
    # Define the 8 arbitrary points as (x, y) coordinates
    points = {
        "XI": (242, 240), "XZ": (320, 160), "XX": (400, 80), # X-Row
        "ZI": (320, 322), "ZZ": (400, 240), "ZX": (480, 160), # Z-Row
        "IZ": (480, 324), "IX": (556, 240)                    # I-Row
    }

    # Dictionary to store the colors of the points
    colors = {}
    inclusiveColors = {}

    # Iterate over the points and get the color at each point
    for point, (x, y) in points.items():
        color = screenshot.get_at((x, y))
        #print(color)
        if color == (0, 0, 0):
            inclusiveColors[point] = 1
        elif color[0] > 100 and color[0] < 200:
            inclusiveColors[point] = -1
        else:
            inclusiveColors[point] = 0

    for point, (x, y) in points.items():
        color = screenshot.get_at((x, y))
        if color == (0, 0, 0):
            colors[point] = 1
        else:
            colors[point] = 0



    return colors, inclusiveColors

def winCheck(gameImage, winConditions): # game Image is self explanatory, win conditions is the same dictionary as in the class def.
    if (colorFinder(gameImage)[0] == winConditions): # If the win conditions match what is on the board
        return True
    else:
        return False

def checkWin(game):  # Returns a boolean on whether or not the game has been won
    win = game.check_win()
    return win
# END - METHODS



# START - GAME LOOP
    # Init. Quantum Game Backend
game = initGame()
    # Gameplay Variables and List Init.
gatePossibilitiesList = ['x', 'y', 'z', 'h', 'cz']
hGateLevelList = [4,5,6]  # Levels who's init. gate states should be the 'H' gate
leftGateState = 0  # Init. the state of the left gate selector
rightGateState = 0  # Init. the state of the right gate selector
level = 1  # Variable that indicates the current level the player is on
moveCount = 0  # Variable that holds the number of logic gates the player has enacted onto the circuit
moveCountCapList = ["Placeholder",4,6,4,4,4,6,10,12,15,10,10,10,10,10,10]  # The move cap for each level is state in index order of each level, hence the placeholder in index 0
    # Scoreboard Init.
populateScoreBoardTextList()  # Populates the score board text list so that the scoreboard menu works correctly
    # Pygame Init.
pygame.display.set_icon(gameIcon)  # Changes window icon
displayLogo()  # Displays the QC logo
pygame.display.set_icon(gameIcon)  # Changes window icon
time.sleep(2)
pygame.display.set_icon(gameIcon)  # Changes window icon
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
            if ( state == "scoreBoardAreYouSureMenu"):  # Are you sure menu
                if ( scoreBoardAreYouSureMenuYesButton_click(event)):  # If the yes button is clicked
                    clearUserProgress()  # Clears the user's progress
                    state = "scoreBoardMenu"  # State update
                    displayScoreBoardMenu()  # Displays the scoreboard menu
                    pygame.display.update()  # Update the screen
                    break
                pygame.display.update()  # Update the screen
                if ( scoreBoardAreYouSureMenuNoButton_click(event)):  # If the no button is clicked
                    state = "scoreBoardMenu"  # State update
                    displayScoreBoardMenu()  # Displays the scoreboard menu
                    pygame.display.update()  # Update the screen
                    break



            if ( state == "scoreBoardMenu" ):  # Normal scoreboard menu
                if ( scoreBoardMenuBackButton_click(event) ):  # Back Button On How To Play Menu
                    displayMainMenu()  # Displays the main menu
                    state = "mainMenu"  # State change
                    break
                if ( scoreBoardMenuClearProgressButton_click(event) ):  # Clears the progress of the user
                    displayScoreBoardMenuAreYouSure()  # Displays the are you sure menu
                    pygame.display.update()  # Update the screen
                    state = "scoreBoardAreYouSureMenu"  # State change
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
                if (levelSelectSandboxButton(event)):  # if the sandbox button has been clicked
                    level = "sandbox"
                    displayWhiteScreen()  # Clears screen
                    displayCurrentLevel(level)  # Displays "N/A"
                    displayBlankGameScreen(level)  # Displays gameplay UI
                    leftGateState = 0  # Resets both gate states
                    rightGateState = 0  # ^
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                    displayMovesLeft(level, moveCount)  # Displays the # of moves the user is able to make before losing
                    game = initGame()  # Initializes a blank game
                    showGame(game)  # Displays the qubits
                    state = "gamePlay"
                    break
                if (levelSelectLevel1Button(event)):
                    moveCount = 0
                    leftGateState = 0  # Resets both gate states
                    rightGateState = 0  # ^
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                    displayMovesLeft(level, moveCount)  # Displays the # of moves the user is able to make before losing
                    level = 1
                    game = initGameBasedOnLevel(level)
                    showGame(game)
                    state = "gamePlay"
                    displayGameUIAfterLevelSelectButtonClick()
                    break
                elif (levelSelectLevel2Button(event)):
                    moveCount = 0
                    leftGateState = 0  # Resets both gate states
                    rightGateState = 0  # ^
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                    displayMovesLeft(level, moveCount)  # Displays the # of moves the user is able to make before losing
                    level = 2
                    game = initGameBasedOnLevel(level)
                    showGame(game)  # Displays the qubits
                    state = "gamePlay"
                    displayGameUIAfterLevelSelectButtonClick()
                    break
                elif (levelSelectLevel3Button(event)):
                    moveCount = 0
                    leftGateState = 0  # Resets both gate states
                    rightGateState = 0  # ^
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                    displayMovesLeft(level, moveCount)  # Displays the # of moves the user is able to make before losing
                    level = 3
                    game = initGameBasedOnLevel(level)
                    showGame(game)  # Displays the qubits
                    state = "gamePlay"
                    displayGameUIAfterLevelSelectButtonClick()
                    break
                elif (levelSelectLevel4Button(event)):
                    moveCount = 0
                    leftGateState = 3  # Resets both gate states
                    rightGateState = 3  # ^
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                    displayMovesLeft(level, moveCount)  # Displays the # of moves the user is able to make before losing
                    level = 4
                    game = initGameBasedOnLevel(level)
                    showGame(game)  # Displays the qubits
                    state = "gamePlay"
                    displayGameUIAfterLevelSelectButtonClick()
                    break
                elif (levelSelectLevel5Button(event)):
                    moveCount = 0
                    leftGateState = 3  # Resets both gate states
                    rightGateState = 3  # ^
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                    displayMovesLeft(level, moveCount)  # Displays the # of moves the user is able to make before losing
                    level = 5
                    game = initGameBasedOnLevel(level)
                    showGame(game)  # Displays the qubits
                    state = "gamePlay"
                    displayGameUIAfterLevelSelectButtonClick()
                    break
                elif (levelSelectLevel6Button(event)):
                    moveCount = 0
                    leftGateState = 3  # Resets both gate states
                    rightGateState = 3  # ^
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                    displayMovesLeft(level, moveCount)  # Displays the # of moves the user is able to make before losing
                    level = 6
                    game = initGameBasedOnLevel(level)
                    showGame(game)  # Displays the qubits
                    state = "gamePlay"
                    displayGameUIAfterLevelSelectButtonClick()
                    break
                elif (levelSelectLevel7Button(event)):
                    moveCount = 0
                    leftGateState = 0  # Resets both gate states
                    rightGateState = 0  # ^
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                    displayMovesLeft(level, moveCount)  # Displays the # of moves the user is able to make before losing
                    level = 7
                    game = initGameBasedOnLevel(level)
                    showGame(game)  # Displays the qubits
                    state = "gamePlay"
                    displayGameUIAfterLevelSelectButtonClick()
                    break
                elif (levelSelectLevel8Button(event)):
                    moveCount = 0
                    leftGateState = 0  # Resets both gate states
                    rightGateState = 0  # ^
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                    displayMovesLeft(level, moveCount)  # Displays the # of moves the user is able to make before losing
                    level = 8
                    game = initGameBasedOnLevel(level)
                    showGame(game)  # Displays the qubits
                    state = "gamePlay"
                    displayGameUIAfterLevelSelectButtonClick()
                    break
                elif (levelSelectLevel9Button(event)):
                    moveCount = 0
                    leftGateState = 0  # Resets both gate states
                    rightGateState = 0  # ^
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                    displayMovesLeft(level, moveCount)  # Displays the # of moves the user is able to make before losing
                    level = 9
                    game = initGameBasedOnLevel(level)
                    showGame(game)  # Displays the qubits
                    state = "gamePlay"
                    displayGameUIAfterLevelSelectButtonClick()
                    break
                elif (levelSelectLevel10Button(event)):
                    moveCount = 0
                    leftGateState = 0  # Resets both gate states
                    rightGateState = 0  # ^
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                    displayMovesLeft(level, moveCount)  # Displays the # of moves the user is able to make before losing
                    level = 10
                    game = initGameBasedOnLevel(level)
                    showGame(game)  # Displays the qubits
                    state = "gamePlay"
                    displayGameUIAfterLevelSelectButtonClick()
                    break
                elif (levelSelectLevel11Button(event)):
                    moveCount = 0
                    leftGateState = 0  # Resets both gate states
                    rightGateState = 0  # ^
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                    displayMovesLeft(level, moveCount)  # Displays the # of moves the user is able to make before losing
                    level = 11
                    game = initGameBasedOnLevel(level)
                    showGame(game)  # Displays the qubits
                    state = "gamePlay"
                    displayGameUIAfterLevelSelectButtonClick()
                    break
                elif (levelSelectLevel12Button(event)):
                    moveCount = 0
                    leftGateState = 0  # Resets both gate states
                    rightGateState = 0  # ^
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                    displayMovesLeft(level, moveCount)  # Displays the # of moves the user is able to make before losing
                    level = 12
                    game = initGameBasedOnLevel(level)
                    showGame(game)  # Displays the qubits
                    state = "gamePlay"
                    displayGameUIAfterLevelSelectButtonClick()
                    break
                elif (levelSelectLevel13Button(event)):
                    moveCount = 0
                    leftGateState = 0  # Resets both gate states
                    rightGateState = 0  # ^
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                    displayMovesLeft(level, moveCount)  # Displays the # of moves the user is able to make before losing
                    level = 13
                    game = initGameBasedOnLevel(level)
                    showGame(game)  # Displays the qubits
                    state = "gamePlay"
                    displayGameUIAfterLevelSelectButtonClick()
                    break
                elif (levelSelectLevel14Button(event)):
                    moveCount = 0
                    leftGateState = 0  # Resets both gate states
                    rightGateState = 0  # ^
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                    displayMovesLeft(level, moveCount)  # Displays the # of moves the user is able to make before losing
                    level = 14
                    game = initGameBasedOnLevel(level)
                    showGame(game)  # Displays the qubits
                    state = "gamePlay"
                    displayGameUIAfterLevelSelectButtonClick()
                    break
                elif (levelSelectLevel15Button(event)):
                    moveCount = 0
                    leftGateState = 0  # Resets both gate states
                    rightGateState = 0  # ^
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                    displayMovesLeft(level, moveCount)  # Displays the # of moves the user is able to make before losing
                    level = 15
                    game = initGameBasedOnLevel(level)
                    showGame(game)  # Displays the qubits
                    state = "gamePlay"
                    displayGameUIAfterLevelSelectButtonClick()
                    break

            # Level Select Menu Button Control Flow (from main menu)
            if (state == "levelSelectMenuMain"):
                if (levelSelectMenuMainMenuButton(event) or levelSelectMenuBackButton(event, level)):  # Both the main menu and back button will bring the user back to the main menu, hence why there isn't control flow for both buttons separately
                    displayMainMenu()  # Displays the main menu
                    state = "mainMenu"  # State change
                    break
                if (levelSelectSandboxButton(event)):  # if the sandbox button has been clicked
                    level = "sandbox"
                    displayWhiteScreen()  # Clears screen
                    displayBlankGameScreen(level)  # Displays gameplay UI
                    displayCurrentLevel(level)  # Displays "N/A"
                    leftGateState = 0  # Resets both gate states
                    rightGateState = 0  # ^
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                    displayMovesLeft(level, moveCount)  # Displays the # of moves the user is able to make before losing
                    game = initGame()  # Initializes a blank game
                    showGame(game)  # Displays the qubits
                    state = "gamePlay"
                    break
                if (levelSelectLevel1Button(event)):
                    moveCount = 0
                    leftGateState = 0  # Resets both gate states
                    rightGateState = 0  # ^
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                    displayMovesLeft(level, moveCount)  # Displays the # of moves the user is able to make before losing
                    level = 1
                    game = initGameBasedOnLevel(level)
                    showGame(game)  # Displays the qubits
                    state = "levelExplanation"
                    displayLevelExplanation(level)  # Displays the currently selected level's explanation
                    break
                elif (levelSelectLevel2Button(event)):
                    moveCount = 0
                    leftGateState = 0  # Resets both gate states
                    rightGateState = 0  # ^
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                    displayMovesLeft(level, moveCount)  # Displays the # of moves the user is able to make before losing
                    level = 2
                    game = initGameBasedOnLevel(level)
                    showGame(game)  # Displays the qubits
                    state = "levelExplanation"
                    displayLevelExplanation(level)  # Displays the currently selected level's explanation
                    break
                elif (levelSelectLevel3Button(event)):
                    moveCount = 0
                    leftGateState = 0  # Resets both gate states
                    rightGateState = 0  # ^
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                    displayMovesLeft(level, moveCount)  # Displays the # of moves the user is able to make before losing
                    level = 3
                    game = initGameBasedOnLevel(level)
                    showGame(game)  # Displays the qubits
                    state = "levelExplanation"
                    displayLevelExplanation(level)  # Displays the currently selected level's explanation
                    break
                elif (levelSelectLevel4Button(event)):
                    moveCount = 0
                    leftGateState = 3  # Resets both gate states
                    rightGateState = 3  # ^
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                    displayMovesLeft(level, moveCount)  # Displays the # of moves the user is able to make before losing
                    level = 4
                    game = initGameBasedOnLevel(level)
                    showGame(game)  # Displays the qubits
                    state = "levelExplanation"
                    displayLevelExplanation(level)  # Displays the currently selected level's explanation
                    break
                elif (levelSelectLevel5Button(event)):
                    moveCount = 0
                    leftGateState = 3  # Resets both gate states
                    rightGateState = 3  # ^
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                    displayMovesLeft(level, moveCount)  # Displays the # of moves the user is able to make before losing
                    level = 5
                    game = initGameBasedOnLevel(level)
                    showGame(game)  # Displays the qubits
                    state = "levelExplanation"
                    displayLevelExplanation(level)  # Displays the currently selected level's explanation
                    break
                elif (levelSelectLevel6Button(event)):
                    moveCount = 0
                    leftGateState = 3  # Resets both gate states
                    rightGateState = 3  # ^
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                    displayMovesLeft(level, moveCount)  # Displays the # of moves the user is able to make before losing
                    level = 6
                    game = initGameBasedOnLevel(level)
                    showGame(game)  # Displays the qubits
                    state = "levelExplanation"
                    displayLevelExplanation(level)  # Displays the currently selected level's explanation
                    break
                elif (levelSelectLevel7Button(event)):
                    moveCount = 0
                    leftGateState = 0  # Resets both gate states
                    rightGateState = 0  # ^
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                    displayMovesLeft(level, moveCount)  # Displays the # of moves the user is able to make before losing
                    level = 7
                    game = initGameBasedOnLevel(level)
                    showGame(game)  # Displays the qubits
                    state = "levelExplanation"
                    displayLevelExplanation(level)  # Displays the currently selected level's explanation
                    break
                elif (levelSelectLevel8Button(event)):
                    moveCount = 0
                    leftGateState = 0  # Resets both gate states
                    rightGateState = 0  # ^
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                    displayMovesLeft(level, moveCount)  # Displays the # of moves the user is able to make before losing
                    level = 8
                    game = initGameBasedOnLevel(level)
                    showGame(game)  # Displays the qubits
                    state = "levelExplanation"
                    displayLevelExplanation(level)  # Displays the currently selected level's explanation
                    break
                elif (levelSelectLevel9Button(event)):
                    moveCount = 0
                    leftGateState = 0  # Resets both gate states
                    rightGateState = 0  # ^
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                    displayMovesLeft(level, moveCount)  # Displays the # of moves the user is able to make before losing
                    level = 9
                    game = initGameBasedOnLevel(level)
                    showGame(game)  # Displays the qubits
                    state = "levelExplanation"
                    displayLevelExplanation(level)  # Displays the currently selected level's explanation
                    break
                elif (levelSelectLevel10Button(event)):
                    moveCount = 0
                    leftGateState = 0  # Resets both gate states
                    rightGateState = 0  # ^
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                    displayMovesLeft(level, moveCount)  # Displays the # of moves the user is able to make before losing
                    level = 10
                    game = initGameBasedOnLevel(level)
                    showGame(game)  # Displays the qubits
                    state = "levelExplanation"
                    displayLevelExplanation(level)  # Displays the currently selected level's explanation
                    break
                elif (levelSelectLevel11Button(event)):
                    moveCount = 0
                    leftGateState = 0  # Resets both gate states
                    rightGateState = 0  # ^
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                    displayMovesLeft(level, moveCount)  # Displays the # of moves the user is able to make before losing
                    level = 11
                    game = initGameBasedOnLevel(level)
                    showGame(game)  # Displays the qubits
                    state = "levelExplanation"
                    displayLevelExplanation(level)  # Displays the currently selected level's explanation
                    break
                elif (levelSelectLevel12Button(event)):
                    moveCount = 0
                    leftGateState = 0  # Resets both gate states
                    rightGateState = 0  # ^
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                    displayMovesLeft(level, moveCount)  # Displays the # of moves the user is able to make before losing
                    level = 12
                    game = initGameBasedOnLevel(level)
                    showGame(game)  # Displays the qubits
                    state = "levelExplanation"
                    displayLevelExplanation(level)  # Displays the currently selected level's explanation
                    break
                elif (levelSelectLevel13Button(event)):
                    moveCount = 0
                    leftGateState = 0  # Resets both gate states
                    rightGateState = 0  # ^
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                    displayMovesLeft(level, moveCount)  # Displays the # of moves the user is able to make before losing
                    level = 13
                    game = initGameBasedOnLevel(level)
                    showGame(game)  # Displays the qubits
                    state = "levelExplanation"
                    displayLevelExplanation(level)  # Displays the currently selected level's explanation
                    break
                elif (levelSelectLevel14Button(event)):
                    moveCount = 0
                    leftGateState = 0  # Resets both gate states
                    rightGateState = 0  # ^
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                    displayMovesLeft(level, moveCount)  # Displays the # of moves the user is able to make before losing
                    level = 14
                    game = initGameBasedOnLevel(level)
                    showGame(game)  # Displays the qubits
                    state = "levelExplanation"
                    displayLevelExplanation(level)  # Displays the currently selected level's explanation
                    break
                elif (levelSelectLevel15Button(event)):
                    moveCount = 0
                    leftGateState = 0  # Resets both gate states
                    rightGateState = 0  # ^
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                    displayMovesLeft(level, moveCount)  # Displays the # of moves the user is able to make before losing
                    level = 15
                    game = initGameBasedOnLevel(level)
                    showGame(game)  # Displays the qubits
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
                if (loseWinLevelButton(event)):  # Continue button is clicked
                    state = "mainMenu"  # State change
                    displayWhiteScreen()  # Blanks the screen
                    displayMainMenu()  # Main Menu
                    break
                if (loseWinScreenMainMenuButton(event)):  # Replay level button is clicked
                    state = "gamePlay"  # State change
                    displayWhiteScreen()  # Blanks the screen
                    if (level in hGateLevelList):  # If the level is an 'H' gate level, resets gates to the 'H' gate
                        leftGateState = 3
                        rightGateState = 3
                    else:  # If the level's init. gate orientation is unimportant or if the level in an 'X' gate level
                        leftGateState = 0  # Resets both gate states
                        rightGateState = 0  # ^
                    displayBlankGameScreen(level)
                    displayCurrentLevel(level)  # Displays the current level the player is on
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                    displayMovesLeft(level, moveCount)  # Displays the # of moves the user is able to make before losing
                    game = initGameBasedOnLevel(level)
                    showGame(game)  # Displays the qubits
                    break

            # You Won Screen Button Control Flow
            if (state == "youWonMenu"):
                if (loseWinLevelButton(event)):  # Main menu button is clicked
                    level -= 1 # Sets the level back
                    state = "mainMenu"  # State change
                    displayWhiteScreen()  # Blanks the screen
                    displayMainMenu()  # Main Menu
                    break
                if (loseWinScreenMainMenuButton(event)):  # Next level button is clicked
                    displayWhiteScreen()  # Clears screen
                    moveCount = 0
                    if (level in hGateLevelList):  # If the level is an 'H' gate level, resets gates to the 'H' gate
                        leftGateState = 3
                        rightGateState = 3
                    else:  # If the level's init. gate orientation is unimportant or if the level in an 'X' gate level
                        leftGateState = 0  # Resets both gate states
                        rightGateState = 0  # ^
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                    displayMovesLeft(level, moveCount)  # Displays the # of moves the user is able to make before losing
                    state = "levelExplanation"
                    displayLevelExplanation(level)  # Displays the currently selected level's explanation
                    break
            if (state == "youWonLevel15Menu"):
                if (youWonLevel15MainMenuButton(event)):  # If the main menu button is clicked
                    level = 1  # Sets the level back to one
                    state = "mainMenu"  # State change
                    displayWhiteScreen()  # Blanks the screen
                    displayMainMenu()  # Main Menu
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
                    if (level in hGateLevelList):  # If the level is an 'H' gate level, resets gates to the 'H' gate
                        leftGateState = 3
                        rightGateState = 3
                    else:  # If the level's init. gate orientation is unimportant or if the level in an 'X' gate level
                        leftGateState = 0  # Resets both gate states
                        rightGateState = 0  # ^
                    displayCurrentGates(leftGateState, rightGateState)  # Updates the current gate text
                    displayMovesLeft(level, moveCount)  # Displays the current moves left
                    if (level != "sandbox"):
                        game = initGameBasedOnLevel(level)  # Initializes game based on the current level
                    elif(level == "sandbox"):
                        game = initGame()  # Init. a blank game instance
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

                # WIN CONDITION CONTROL FLOW
                if ( level != "sandbox"):
                    level12WinConditions = {'XI': -1, 'XZ': -1, 'XX': 0, 'ZI': -1, 'ZZ': 0, 'ZX': -1, 'IZ': -1, 'IX': -1}
                    if ( level == 12 and colorFinder(save_screen_as_image(screen))[1] ==  level12WinConditions):  # Doesn't allow the user to use the win con for level 11 to beat level 12
                        displayWinBorder()  # Displays the win border
                        time.sleep(3)  # Pauses for 3 second
                        updateScoreBoardTextFile(level, moveCount)  # Updates the high score of the player
                        displayYouWonScreen(level, moveCount)  # Displays the you won screen
                        displayYouWonScoreInfo(level, moveCount)  # Displays the you won screen score info
                        print("Level " + str(level) + " has been won.")
                        state = "youWonMenu"
                        level += 1
                        game = initGameBasedOnLevel(level)
                        moveCount = 0
                    elif (level != 12 and winCheck(save_screen_as_image(screen), game.getWinConditions())):  # Checks if the level has been won
                        displayWinBorder()  # Displays the win border
                        time.sleep(3)  # Pauses for 3 second
                        if ( level != 15 ):  # If not on the last level
                            updateScoreBoardTextFile(level, moveCount)  # Updates the high score of the player
                            displayYouWonScreen(level, moveCount)  # Displays the you won screen
                            displayYouWonScoreInfo(level, moveCount)  # Displays the you won screen score info
                            print("Level " + str(level) + " has been won.")
                            state = "youWonMenu"
                            level += 1
                            game = initGameBasedOnLevel(level)
                        else:  # If you are on the last level
                            displayWhiteScreen()
                            displayYouWonScreenForLevel15()
                            updateScoreBoardTextFile(level, moveCount)  # Updates the high score of the player
                            displayYouWonScoreInfo(level, moveCount)  # Displays the you won screen score info
                            print("Level " + str(level) + " has been won.")
                            state = "youWonLevel15Menu"
                        # Stuff that should happen either way
                        moveCount = 0

                # MOVE CAP CONTROL FLOW FOR LEVELS (Basically loss detecting control flow)
                if (level == "sandbox"):  # If the user is in sandbox mode reset moveCount to 0 to mitigate bugs
                    moveCount = 0
                if (level == 1 and moveCount == moveCountCapList[level]):  # Checks if the move cap of 1 has been exceeded for level 1
                    displayLoseBorder()  # Displays the lose border
                    time.sleep(2)  # Waits for 3 seconds
                    displayYouLostScreen(level)
                    displayYouLostScoreInfo(level)
                    state = "youLostMenu"
                    moveCount = 0
                if (level == 2 and moveCount == moveCountCapList[level]):  # Checks if the move cap of 2 has been exceeded for level 2
                    displayLoseBorder()  # Displays the lose border
                    time.sleep(2)  # Waits for 3 seconds
                    displayYouLostScreen(level)
                    displayYouLostScoreInfo(level)
                    state = "youLostMenu"
                    moveCount = 0
                if (level == 3 and moveCount == moveCountCapList[level]):  # Checks if the move cap of 2 has been exceeded for level 2
                    displayLoseBorder()  # Displays the lose border
                    time.sleep(2)  # Waits for 3 seconds
                    displayYouLostScreen(level)
                    state = "youLostMenu"
                    moveCount = 0
                if (level == 4 and moveCount == moveCountCapList[level]):  # Checks if the move cap of 2 has been exceeded for level 2
                    displayLoseBorder()  # Displays the lose border
                    time.sleep(2)  # Waits for 3 seconds
                    displayYouLostScreen(level)
                    state = "youLostMenu"
                    moveCount = 0
                if (level == 5 and moveCount == moveCountCapList[level]):  # Checks if the move cap of 2 has been exceeded for level 2
                    displayLoseBorder()  # Displays the lose border
                    time.sleep(2)  # Waits for 3 seconds
                    displayYouLostScreen(level)
                    state = "youLostMenu"
                    moveCount = 0
                if (level == 6 and moveCount == moveCountCapList[level]):  # Checks if the move cap of 1 has been exceeded for level 1
                    displayLoseBorder()  # Displays the lose border
                    time.sleep(2)  # Waits for 3 seconds
                    displayYouLostScreen(level)
                    state = "youLostMenu"
                    moveCount = 0
                if (level == 7 and moveCount == moveCountCapList[level]):  # Checks if the move cap of 2 has been exceeded for level 2
                    displayLoseBorder()  # Displays the lose border
                    time.sleep(2)  # Waits for 3 seconds
                    displayYouLostScreen(level)
                    state = "youLostMenu"
                    moveCount = 0
                if (level == 8 and moveCount == moveCountCapList[level]):  # Checks if the move cap of 2 has been exceeded for level 2
                    displayLoseBorder()  # Displays the lose border
                    time.sleep(2)  # Waits for 3 seconds
                    displayYouLostScreen(level)
                    state = "youLostMenu"
                    moveCount = 0
                if (level == 9 and moveCount == moveCountCapList[level]):  # Checks if the move cap of 2 has been exceeded for level 2
                    displayLoseBorder()  # Displays the lose border
                    time.sleep(2)  # Waits for 3 seconds
                    displayYouLostScreen(level)
                    state = "youLostMenu"
                    moveCount = 0
                if (level == 10 and moveCount == moveCountCapList[level]):  # Checks if the move cap of 2 has been exceeded for level 2
                    displayLoseBorder()  # Displays the lose border
                    time.sleep(2)  # Waits for 3 seconds
                    displayYouLostScreen(level)
                    state = "youLostMenu"
                    moveCount = 0
                if (level == 11 and moveCount == moveCountCapList[level]):  # Checks if the move cap of 1 has been exceeded for level 1
                    displayLoseBorder()  # Displays the lose border
                    time.sleep(2)  # Waits for 3 seconds
                    displayYouLostScreen(level)
                    state = "youLostMenu"
                    moveCount = 0
                if (level == 12 and moveCount == moveCountCapList[level]):  # Checks if the move cap of 2 has been exceeded for level 2
                    displayLoseBorder()  # Displays the lose border
                    time.sleep(2)  # Waits for 3 seconds
                    displayYouLostScreen(level)
                    state = "youLostMenu"
                    moveCount = 0
                if (level == 13 and moveCount == moveCountCapList[level]):  # Checks if the move cap of 2 has been exceeded for level 2
                    displayLoseBorder()  # Displays the lose border
                    time.sleep(2)  # Waits for 3 seconds
                    displayYouLostScreen(level)
                    state = "youLostMenu"
                    moveCount = 0
                if (level == 14 and moveCount == moveCountCapList[level]):  # Checks if the move cap of 2 has been exceeded for level 2
                    displayLoseBorder()  # Displays the lose border
                    time.sleep(2)  # Waits for 3 seconds
                    displayYouLostScreen(level)
                    state = "youLostMenu"
                    moveCount = 0
                if (level == 15 and moveCount == moveCountCapList[level]):  # Checks if the move cap of 2 has been exceeded for level 2
                    displayLoseBorder()  # Displays the lose border
                    time.sleep(2)  # Waits for 3 seconds
                    displayYouLostScreen(level)
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
