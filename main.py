# Author(s): Noah Klaus
# Project: Quantum Checkers (though name has not been decided on as of 2/24/23)
# Common Issue(s): On line 22 (as of 3/3/23), the path to the google chrome app on a normal mac OS is listed. If you have changed the
# location of your chrome instance, you must fix this. If it isn't on line 22, check for "chrome_path" as a variable.
# Known Bugs: None As Of 2/28/23

# *FOR TESTING*
#print("X: " + str(x) + " Y: " + str(y)) # Helps with finding cursor for allocating space for buttons
# *FOR TESTING*

# START - IMPORTS
import time
import pygame
import webbrowser
# END - IMPORTS



# START - WEB SURFING
gitHubURL = 'https://github.com/cZAlpha/QuantumCheckers' # The project's Github repository
dsuURL = 'https://www.desu.edu/' # DSU's URL
chrome_path = 'open -a /Applications/Google\ Chrome.app %s' # The path to chrome on most Macs
def openGithub(): # Opens github
    webbrowser.get(chrome_path).open(gitHubURL)
def openDSUWebsite(): # Opens DSU's website
    webbrowser.get(chrome_path).open(dsuURL)
# END - WEB SURFING



# START - SCREEN
pygame.init() # Init. Pygame
normalScreenRatio = (800,500) # Screen ratio and game window creation
normalWidth = normalScreenRatio[0]
normalHeight = normalScreenRatio[1]
screen = pygame.display.set_mode(normalScreenRatio)
caption = pygame.display.set_caption("Quantum Checkers") # Changes window caption
# Changes window icon (NOT IMPLEMENTED YET, MAKE 32x32 SIZED IMAGE)
# icon = pygame.display.set_icon(32x32image)

    # START - SCOREBOARD SCREEN INFORMATION
# List that stores the (x,y) location in a tuple of where each level's score should be put on
scoreTextLocationList = [(190, 140), (190,188), (190,236), (190, 284), (190, 332), (422, 140), (422,188), (422,236), (422, 284), (422, 332), (654, 140), (654,188), (654,236), (654, 284), (654, 332)]
black = (0,0,0) # The color black in RGB notation
scoreTextBackgroundColor = (239,239,239) # The color of the score board menu background
scoreTextBackground = pygame.Surface((45,30)) # Makes the shape that will be the background of the score board text
scoreTextBackground.fill(scoreTextBackgroundColor) # Fills in the background of the surface that was just made
scoreTextFont = pygame.font.SysFont("timesnewroman", 23) # Stores the font times new roman in size 12 in a variable
    # START - SCOREBOARD SCREEN INFORMATION
# END - SCREEN



# START - METHODS
    # START - Display Methods
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
    howToPlayMenuBackground = pygame.image.load('Assets/Scoreboard Menu.png').convert()
    screen.blit(howToPlayMenuBackground, (0,0))
    # Placing of the text for the score board background
    for locationTuple in scoreTextLocationList:
        screen.blit(scoreTextBackground, locationTuple)
    scoreTextListIndex = 0
    for locationTuple in scoreTextLocationList:
        scoreText = scoreTextFont.render(str(populateScoreBoardTextList()[scoreTextListIndex]), True, black)
        screen.blit(scoreText, locationTuple)
        scoreTextListIndex += 1 # Increments the scoreTextListIndex every for loop cycle
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
def mainMenuStartGameButton_click(event): # Play Button
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (x > 545 and x < 750) and (y > 45 and y < 93):
            print("Play Button Has Been Clicked")
            return True

def mainMenuHowToPlayButton_click(event): # How To Play Button
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (x > 545 and x < 750) and (y > 140 and y < 190):
           print("Play Button Has Been Clicked")
           return True

def mainMenuScoreBoardButton_click(event): # How To Play Button
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        print("X: " + str(x) + " Y: " + str(y))
        if (x > 545 and x < 750) and (y > 228 and y < 280):
           print("Play Button Has Been Clicked")
           return True

def mainMenuCreditsButton_click(event): # Credits Button
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (x > 545 and x < 750) and (y > 322 and y < 373):
            print("Credits Button Has Been Clicked")
            return True

def mainMenuExitButton_click(event): # Exit Button
    x,y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (x > 545 and x < 750) and (y > 418 and y < 465):
            print("Exit Button Has Been Clicked")
            return True
    # STOP - Main Menu Buttons

    # START - Start Game Menu Buttons
def startGameMenuBackButton_click(event): # Back Button
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
def howToPlayMenuBackButton_click(event): # Back Button
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
def creditsMenuBackButton_click(event): # Exit Button
    x,y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (x > 320 and x < 480) and (y > 410 and y < 462):
            print("Back Button Has Been Clicked")
            return True

def creditsMenuGithubButton_click(event): # Git Hub Button
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
        # Takes "level" and "score" as perameters, "level" denotes what line of the file should be changed, which also denotes
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
        # Initializes a list to hold the scores of the user for the various levels in the game
        scoreBoardTextList = []
        # Loops thru each line in the file
        for line in f:
            # Appends the text from the file into a list to be used in order to display the scoreboard
            scoreBoardTextList.append(line.strip())
    return scoreBoardTextList
    # STOP - Scoreboard File Reading Methods
# END - METHODS



# START - GAME LOOP
# Populates the score board text list so that the scoreboard menu works correctly
populateScoreBoardTextList()
# Places the main menu screen on the game window to initialize the game
displayMainMenu()
# Initializing the FSM in the "mainMenu" state because the game starts on the main menu
state = "mainMenu"
# Clock (used in game loop to limit frame rate)
clock = pygame.time.Clock()
# Init. loop variable
running = True
while running:
    for event in pygame.event.get(): # For loop to check for user input (events)
        if event.type == pygame.QUIT: # If the "quit" button is clicked in the mac os's game window
            running = False
            pygame.quit()
            quit()

        # START - BUTTON CONTROL FLOW
        #
        if event.type == pygame.constants.MOUSEBUTTONDOWN: # If the mouse has been clicked
            if event.button == 1: # If the left click of the mouse was clicked
                # Main Menu Button Control Flow
                if ( state == "mainMenu" ):
                    if ( mainMenuStartGameButton_click(event) ): # If the start game button is clicked
                        displayStartGameMenu() # Displays the start game menu
                        state = "startGameMenu" # State change
                        break
                    if ( mainMenuHowToPlayButton_click(event) ):
                        displayHowToPlayMenu() # Displays the how to play menu
                        state = "howToPlayMenu" # State change
                        break
                    if ( mainMenuScoreBoardButton_click(event) ):
                        displayScoreBoardMenu() # Displays the scoreboard menu
                        state = "scoreBoardMenu" # State change
                        # UPDATES THE LIST HOLDING THE SCORE BOARD TEXT VALUES
                        # INSERT FUNCTION CALL THAT READS THE TEXT FILE THAT HOLDS THE SCOREBOARD TEXT
                        break
                    if ( mainMenuCreditsButton_click(event) ): # If the credits button is clicked
                        displayCreditsMenu() # Displays the credits menu
                        state = "creditsMenu" # State change
                        break
                    if (mainMenuExitButton_click(event)):  # If the exit game button is clicked
                        running = False
                        pygame.quit()
                        quit()
                        break

                # Start Game Menu Button Control Flow
                if ( state == "startGameMenu" ):
                    if ( startGameMenuBackButton_click(event) ): # Back Button On Start Game Menu
                        displayMainMenu()  # Displays the main menu
                        state = "mainMenu"  # State change
                        break
                    if ( startGameMenuGithubButton_click(event) ): # Github Button On Start Game Menu
                        openGithub() # Opens the project's Github repository in a native google chrome instance
                        break

                # How To Play Menu Button Control Flow
                if ( state == "howToPlayMenu" ):
                    if ( howToPlayMenuBackButton_click(event) ): # Back Button On How To Play Menu
                        displayMainMenu()  # Displays the main menu
                        state = "mainMenu"  # State change
                        break
                    if (  howToPlayMenuGithubButton_click(event) ): # Github Button
                        openGithub()
                        break

                # Scoreboard Menu Button Control Flow
                if ( state == "scoreBoardMenu" ):
                    if ( scoreBoardMenuBackButton_click(event) ): # Back Button On How To Play Menu
                        displayMainMenu()  # Displays the main menu
                        state = "mainMenu"  # State change
                        break

                # Credits Menu Button Control Flow
                if ( state == "creditsMenu" ):
                    if ( creditsMenuBackButton_click(event) ): # Back Button
                        displayMainMenu() # Displays the main menu
                        state = "mainMenu" # State change
                        break
                    if ( creditsMenuGithubButton_click(event) ): # Github Hypertext-lookalike Button
                        openGithub() # Opens the project's Github repository in a native google chrome instance
                        break
                    if ( creditsMenuDSUButton_click(event) ): # DSU Hypertext-lookalike Button
                        openDSUWebsite() # Opens DSU's website
                        break
            #
            # STOP - BUTTON CONTROL FLOW

    # Update the screen
    pygame.display.update()
    # Clock: Sets the frame rate to 60
    clock.tick(60)
# END - GAME LOOP
