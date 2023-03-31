# Author(s): Noah Klaus, London Anderson
# Project: Quantum Checkers (though name has not been decided on as of 2/24/23)
# Common Issue(s): On line 22 (as of 3/3/23), the path to the google chrome app on a normal mac OS is listed. If you have changed the
# location of your chrome instance, you must fix this. If it isn't on line 22, check for "chrome_path" as a variable.
# Known Bugs: None As Of 3/29/23

# *FOR TESTING*
# print("X: " + str(x) + " Y: " + str(y)) # Helps with finding cursor for allocating space for buttons
# *FOR TESTING*

# START - IMPORTS
import time
from io import BytesIO
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
normalScreenRatio = (800,500)  # Screen ratio and game window creation
normalWidth = normalScreenRatio[0]
normalHeight = normalScreenRatio[1]
screen = pygame.display.set_mode(normalScreenRatio)
caption = pygame.display.set_caption("Quantum Checkers")  # Changes window caption
#icon = pygame.display.set_icon(32x32image)  # Changes window icon (NOT IMPLEMENTED YET, MAKE 32x32 SIZED IMAGE)
    # STOP - PYGAME WINDOW INIT.

    # START - SCOREBOARD SCREEN INFORMATION
# List that stores the (x,y) location in a tuple of where each level's score should be put on
scoreTextLocationList = [(190, 140), (190,188), (190,236), (190, 284), (190, 332), (422, 140), (422,188), (422,236), (422, 284), (422, 332), (654, 140), (654,188), (654,236), (654, 284), (654, 332)]
black = (0,0,0)  # The color black in RGB notation
scoreTextBackgroundColor = (239,239,239)  # The color of the score board menu background
scoreTextBackground = pygame.Surface((45,30))  # Makes the shape that will be the background of the score board text
scoreTextBackground.fill(scoreTextBackgroundColor)  # Fills in the background of the surface that was just made
scoreTextFont = pygame.font.SysFont("timesnewroman", 23)  # Stores the font times new roman in size 12 in a variable
    # STOP - SCOREBOARD SCREEN INFORMATION
# END - SCREEN



# START - METHODS
    # START - Display Methods
def displayLevelSelectMenu(): # Displays the level select menu
    # Creation of the level select menu image & placing of image on the screen
    exitGameplayMenu = pygame.image.load('Assets/LevelSelectMenu.png').convert()
    screen.blit(exitGameplayMenu, (0, 0))
    pygame.display.update()

def displayExitGameplayMenu():  # Displays the exit menu for gameplay
    # Creation of the exit gameplay menu image & placing of image on the screen
    exitGameplayMenu = pygame.image.load('Assets/ExitToMainMenuConfirmationMenu.png').convert()
    screen.blit(exitGameplayMenu, (0, 0))
    pygame.display.update()

def displayBlankGameScreen():  # Displays the blank game screen
    # Creation of the blank game screen & placing of image on the screen
    gamePlayBlankScreen = pygame.image.load('Assets/Fourth Iteration of Gameplay UI.png').convert()
    screen.blit(gamePlayBlankScreen, (0,0))
    pygame.display.update()

def displayWhiteScreen(): # Displays a white image on the entire screen
    # Creation of a white image (800x500) & placing the image on the screen
    whiteBackground = pygame.image.load('Assets/800x500WHITE.png').convert()
    screen.blit(whiteBackground, (0,0))
    pygame.display.update()

def displayMainMenu(): # Displays the rough outline of a main menu
    # Creation of the main menu's background & placing of image on the screen
    mainMenuBackground = pygame.image.load('Assets/Main Menu.png').convert()
    screen.blit(mainMenuBackground, (0, 0))
    pygame.display.update()

def displayStartGameMenu(): # Displays the rough outline of the play menu
    # Creation of the play menu's background & placing of image on the screen
    playMenuBackground = pygame.image.load('Assets/Play Menu.png').convert()
    screen.blit(playMenuBackground, (0, 0))
    pygame.display.update()

def displayHowToPlayMenu(): # Displays the rough outline of the how to play menu
    howToPlayMenuBackground = pygame.image.load('Assets/HowToPlay Menu.png').convert()
    screen.blit(howToPlayMenuBackground, (0,0))
    pygame.display.update()

def displayScoreBoardMenu(): # Displays the rough outline of the scoreboard menu
    howToPlayMenuBackground = pygame.image.load('Assets/Scoreboard Menu.png').convert()  # Image shit
    screen.blit(howToPlayMenuBackground, (0,0))  # Menu Image Is Put on the Screen
    for locationTuple in scoreTextLocationList:  # Placing of the text for the score board background
        screen.blit(scoreTextBackground, locationTuple)
    scoreTextListIndex = 0
    for locationTuple in scoreTextLocationList:
        scoreText = scoreTextFont.render(str(populateScoreBoardTextList()[scoreTextListIndex]), True, black)
        screen.blit(scoreText, locationTuple)
        scoreTextListIndex += 1  # Increments the scoreTextListIndex every for loop cycle
    pygame.display.update()

def displayCreditsMenu(): # Displays the rough outline of a credits menu
    # Creation of the credit menu's background & placing of image on the screen
    creditsMenuBackground = pygame.image.load('Assets/Credits Menu.png').convert()
    screen.blit(creditsMenuBackground, (0, 0))
    pygame.display.update()

def displayMainMenuExitButtonClicked(): # Method that displays the exit button being clicked (NOT IMPLEMENTED)
    # Creation of the main menu's background with the exit button blacked out & placing of image on the screen
    mainMenuBackground = pygame.image.load('Assets/UnusedAssets/QuantumCheckersMainMenuExitButtonClicked.png').convert()
    screen.blit(mainMenuBackground, (0, 0))
    pygame.display.update()
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
        if (x > 320 and x < 480) and (y > 410 and y < 462):
            print("Back Button Has Been Clicked")
            return True

def startGameMenuGithubButton_click(event):  # Git Hub Button
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (x > 300 and x < 500) and (y > 145 and y < 350):
            print("GitHub Button Has Been Clicked")
            return True
    # STOP - Start Game Menu Buttons

    # START - How To Play Menu Buttons
def howToPlayMenuBackButton_click(event):  # Back Button
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (x > 320 and x < 480) and (y > 410 and y < 462):
            print("Back Button Has Been Clicked")
            return True

def howToPlayMenuGithubButton_click(event):  # Git Hub Button
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (x > 300 and x < 500) and (y > 145 and y < 350):
            print("GitHub Button Has Been Clicked")
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

def resetLevelButton(event, level):  # Resets the level based on whatever level the player is currently on
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
        if (state == "levelSelectMenu"):
            print("X: " + str(x) + " Y: " + str(y))
            if (x > 190 and x < 420) and (y > 412 and y < 465):
                print("Level Select Menu Main Menu Button Has Been Clicked")
                return True

def levelSelectMenuBackButton(event, level):
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (state == "levelSelectMenu"):
            if (x > 444 and x < 605) and (y > 412 and y < 465):
                print("Level Select Menu Back Button Has Been Clicked")
                return True

def levelSelectLevel1Button(event):
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (state == "levelSelectMenu"):
            print("LEVEL 1 SELECTED")
            #if (x > 444 and x < 605) and (y > 412 and y < 465):
            #    print("Level X Button Has Been Clicked")
            #    return True

def levelSelectLevel2Button(event):
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (state == "levelSelectMenu"):
            print("LEVEL 2 SELECTED")
            #if (x > 444 and x < 605) and (y > 412 and y < 465):
            #    print("Level X Button Has Been Clicked")
            #    return True

def levelSelectLevel3Button(event):
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (state == "levelSelectMenu"):
            print("LEVEL 3 SELECTED")
            #if (x > 444 and x < 605) and (y > 412 and y < 465):
            #    print("Level X Button Has Been Clicked")
            #    return True

def levelSelectLevel4Button(event):
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (state == "levelSelectMenu"):
            print("LEVEL 4 SELECTED")
            # if (x > 444 and x < 605) and (y > 412 and y < 465):
            #    print("Level X Button Has Been Clicked")
            #    return True

def levelSelectLevel5Button(event):
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (state == "levelSelectMenu"):
            print("LEVEL 5 SELECTED")
            # if (x > 444 and x < 605) and (y > 412 and y < 465):
            #    print("Level X Button Has Been Clicked")
            #    return True

def levelSelectLevel6Button(event):
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (state == "levelSelectMenu"):
            print("LEVEL 6 SELECTED")
            # if (x > 444 and x < 605) and (y > 412 and y < 465):
            #    print("Level X Button Has Been Clicked")
            #    return True

def levelSelectLevel7Button(event):
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (state == "levelSelectMenu"):
            print("LEVEL 7 SELECTED")
            # if (x > 444 and x < 605) and (y > 412 and y < 465):
            #    print("Level X Button Has Been Clicked")
            #    return True

def levelSelectLevel8Button(event):
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (state == "levelSelectMenu"):
            print("LEVEL 8 SELECTED")
            # if (x > 444 and x < 605) and (y > 412 and y < 465):
            #    print("Level X Button Has Been Clicked")
            #    return True

def levelSelectLevel9Button(event):
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (state == "levelSelectMenu"):
            print("LEVEL 9 SELECTED")
            # if (x > 444 and x < 605) and (y > 412 and y < 465):
            #    print("Level X Button Has Been Clicked")
            #    return True

def levelSelectLevel10Button(event):
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (state == "levelSelectMenu"):
            print("LEVEL 10 SELECTED")
            # if (x > 444 and x < 605) and (y > 412 and y < 465):
            #    print("Level X Button Has Been Clicked")
            #    return True

def levelSelectLevel11Button(event):
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (state == "levelSelectMenu"):
            print("LEVEL 11 SELECTED")
            # if (x > 444 and x < 605) and (y > 412 and y < 465):
            #    print("Level X Button Has Been Clicked")
            #    return True

def levelSelectLevel12Button(event):
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (state == "levelSelectMenu"):
            print("LEVEL 12 SELECTED")
            # if (x > 444 and x < 605) and (y > 412 and y < 465):
            #    print("Level X Button Has Been Clicked")
            #    return True

def levelSelectLevel13Button(event):
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (state == "levelSelectMenu"):
            print("LEVEL 13 SELECTED")
            # if (x > 444 and x < 605) and (y > 412 and y < 465):
            #    print("Level X Button Has Been Clicked")
            #    return True

def levelSelectLevel14Button(event):
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (state == "levelSelectMenu"):
            print("LEVEL 14 SELECTED")
            # if (x > 444 and x < 605) and (y > 412 and y < 465):
            #    print("Level X Button Has Been Clicked")
            #    return True

def levelSelectLevel15Button(event):
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (state == "levelSelectMenu"):
            print("LEVEL 15 SELECTED")
            # if (x > 444 and x < 605) and (y > 412 and y < 465):
            #    print("Level X Button Has Been Clicked")
            #    return True
    # STOP - Level Select Menu Buttons

    # START - IMAGE CONVERSION
def bytes_to_pygame_image(bytes_io):
    image_bytes = bytes_io.getvalue()  # Read the bytes from the BytesIO object
    surface = pygame.image.load(BytesIO(image_bytes))  # Load the image from the bytes into a pygame Surface
    image = surface.convert()  # Convert the surface to a pygame compatible image
    return image
    # END - IMAGE CONVERSION

    # START - Quantum Method(s) Implementing "game_logic.py"
def initBlankGame():
    game = QuantumGame(
        initialize=[],
        allowed_gates=SUPPORTED_GATES,
        shots=1024,
        corr_color=(60, 120, 216),
        iden_color=(17, 85, 204),
        grid_resolution=(799, 499),
        rectangle_length=10,
        circle_radius=1
    )
    image = game.draw_grid()
    newImage = bytes_to_pygame_image(image)
    return newImage
    # STOP - Quantum Method(s) Implementing "game_logic.py"
# END - METHODS



# START - GAME LOOP
    # Gameplay Variables and List Init.
gatePossibilitiesList = ['x', 'y', 'z', 'h', 'cz']
leftGateState = 0  # Init. the state of the left gate selector
rightGateState = 0  # Init. the state of the right gate selector
level = 0  # Variable that indicates the current level the player is on
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
        if event.type == pygame.constants.MOUSEBUTTONDOWN:  # If the mouse has been clicked
            if event.button == 1:  # If the left click of the mouse was clicked
                # Main Menu Button Control Flow
                if ( state == "mainMenu" ):
                    if ( mainMenuStartGameButton_click(event) ):  # If the start game button is clicked
                        # TESTING ONLY START
                        state = "gamePlay"
                        displayBlankGameScreen()
                        # TESTING ONLY STOP
                        # What should be implemented here after testing code is removed:
                            # 1) change the state to "levelSelectMenu"
                            # 2) use the displayLevelSelectMenu() method
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

                # How To Play Menu Button Control Flow
                if ( state == "howToPlayMenu" ):
                    if ( howToPlayMenuBackButton_click(event) ):  # Back Button On How To Play Menu
                        displayMainMenu()  # Displays the main menu
                        state = "mainMenu"  # State change
                        break
                    if (  howToPlayMenuGithubButton_click(event) ):  # Github Button
                        openGithub()
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
                        displayBlankGameScreen() # REPLACE WITH CODE THAT RETURNS TO THE PREVIOUS GAME STATE

                # Level Select Menu Button Control Flow
                if ( state == "levelSelectMenu" ):
                    if ( levelSelectMenuMainMenuButton(event) ): # Main menu button
                        state = "mainMenu"
                        displayMainMenu()
                    if ( levelSelectMenuBackButton(event, level) ): # Back Button
                        state = "gamePlay"
                        displayBlankGameScreen()
                        # IMPLEMENT GOING BACK TO WHATEVER LEVEL YOU WERE JUST AT!!!

                # Gameplay Button Control Flow
                if (state == "gamePlay"):
                    # LEVEL SELECT BUTTON
                    if ( levelSelectButton(event) ):  # Level Select Button
                        state = "levelSelectMenu"  # THIS SHOULD EVENTUALLY BE MIGRATED TO AN ACTUAL LEVEL SELECT MENU
                        displayLevelSelectMenu()
                        break
                    # LEFT GATE BUTTONS
                    if ( leftGateUpButton(event) ):  # Left Gate Up Button (MOVING UP MEANS GOING LEFT IN THE LIST, SUBTRACTING)
                        if ( leftGateState == 0 ):
                            leftGateState = len(gatePossibilitiesList) - 1  # Makes the left gate state loop back to end of list
                        elif ( leftGateState != 0 and leftGateState > 0):
                            leftGateState -= 1  # De-increments the leftGateState
                        # FOR TESTING ONLY
                        print("Gate After Click: " + gatePossibilitiesList[leftGateState])  # Prints the state after button click of left gate selector
                        # FOR TESTING ONLY
                    if ( leftGateDownButton(event) ):  # Left Gate Down Button (MOVING DOWN MEANS GOING RIGHT IN THE LIST, ADDING)
                        if (leftGateState == len(gatePossibilitiesList) - 1):
                            leftGateState = 0  # Makes the left gate state loop back to end of list
                        elif (leftGateState != len(gatePossibilitiesList) - 1 and leftGateState < len(gatePossibilitiesList) - 1):
                            leftGateState += 1  # De-increments the leftGateState
                        # FOR TESTING ONLY
                        print("Gate After Click: " + gatePossibilitiesList[leftGateState])  # Prints the state after button click of left gate selector
                        # FOR TESTING ONLY
                    if ( leftGateSelectButton(event) ):  # Left Gate Select Button
                        print(" --> Not implemented yet")
                        # This will cause the image of the Qubits to change given the current logic gate selected

                    # RESET LEVEL BUTTON
                    if ( resetLevelButton(event, level) ):  # Reset Level Button
                        # IMPLEMENT RESETTING THE ACTUAL IMAGE OF THE QUBITS BASED ON THE LEVEL THE PLAYER IS ON
                        leftGateState  = 0  # Resets both gate states
                        rightGateState = 0
                        # TESTING ONLY BELOW
                        screen.blit(initBlankGame(), (100,0))
                        # TESTING ONLY ABOVE

                    # RIGHT GATE BUTTONS
                    if ( rightGateUpButton(event) ):  # Left Gate Up Button (MOVING UP MEANS GOING LEFT IN THE LIST, SUBTRACTING)
                        if (leftGateState == 0):
                            leftGateState = len(gatePossibilitiesList) - 1  # Makes the left gate state loop back to end of list
                        elif (leftGateState != 0 and leftGateState > 0):
                            leftGateState -= 1  # De-increments the leftGateState
                        # FOR TESTING ONLY
                        print("Gate After Click: " + gatePossibilitiesList[
                            leftGateState])  # Prints the state after button click of left gate selector
                        # FOR TESTING ONLY
                    if ( rightGateDownButton(event) ):  # Left Gate Down Button (MOVING DOWN MEANS GOING RIGHT IN THE LIST, ADDING)
                        if (leftGateState == len(gatePossibilitiesList) - 1):
                            leftGateState = 0  # Makes the left gate state loop back to end of list
                        elif (leftGateState != len(gatePossibilitiesList) - 1 and leftGateState < len(
                                gatePossibilitiesList) - 1):
                            leftGateState += 1  # De-increments the leftGateState
                        # FOR TESTING ONLY
                        print("Gate After Click: " + gatePossibilitiesList[leftGateState])  # Prints the state after button click of left gate selector
                        # FOR TESTING ONLY
                    if ( rightGateSelectButton(event) ):  # Left Gate Select Button
                        print(" --> Not implemented yet")
                        # NOT IMPLEMENTED YET: This will cause the image of the Qubits to change given the current logic gate selected

                    # EXIT LEVEL BUTTON
                    if ( exitGameplayButton(event) ): # If the exit level button has been clicked
                        displayExitGameplayMenu()
                        state = "exitGameplayMenu"
            #
            # STOP - BUTTON CONTROL FLOW

    pygame.display.update() # Update the screen
    clock.tick(60) # Sets the frame rate to 60
# END - GAME LOOP
