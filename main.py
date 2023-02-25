# Author(s): Noah Klaus
# Project: Quantum Checkers (though name has not been decided on as of 2/24/23)
# Known Bugs: The only known bug is that if you click in the middle of the 'credits' button on the main menu,
# it will click through into the Github access button. This is due to Pygame not registering singular mouse
# button clicks but rather many despite the button only being pressed once.

# START - IMPORTS
import time
import pygame
import webbrowser
# END - IMPORTS



# START - WEB SURFING
gitHubURL = 'https://github.com/cZAlpha/QuantumCheckers'
chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
def openGithub(): # Opens github
    webbrowser.get(chrome_path).open(gitHubURL)
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
# END - SCREEN



# START - METHODS
def displayMainMenu(): # Displays the rough outline of a main menu
    # Creation of the main menu's background & placing of image on the screen
    mainMenuBackground = pygame.image.load('Assets/QuantumCheckersMainMenu.png').convert()
    screen.blit(mainMenuBackground, (0, 0))

def displayPlayMenu(): # Displays the rough outline of the play menu
    # Creation of the play menu's background & placing of image on the screen
    playMenuBackground = pygame.image.load('Assets/QuantumCheckersPlayMenu.png').convert()
    screen.blit(playMenuBackground, (0, 0))

def displayCreditsMenu(): # Displays the rough outline of a credits menu
    # Creation of the credit menu's background & placing of image on the screen
    creditsMenuBackground = pygame.image.load('Assets/QuantumCheckersCreditsMenu.png').convert()
    screen.blit(creditsMenuBackground, (0, 0))

def displayMainMenuExitButtonClicked(): # Method that displays the exit button being clicked (NOT IMPLEMENTED)
    # Creation of the main menu's background with the exit button blacked out & placing of image on the screen
    mainMenuBackground = pygame.image.load('Assets/QuantumCheckersMainMenuExitButtonClicked.png').convert()
    screen.blit(mainMenuBackground, (0, 0))
    pygame.display.update()

def mainMenuPlayButton_click(event): # Play Button
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (x > 280 and x < 520) and (y > 164 and y < 244):
            print("Play Button Has Been Clicked")
            return True

def mainMenuCreditsButton_click(event): # Credits Button
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (x > 280 and x < 520) and (y > 265 and y < 347):
            print("Credits Button Has Been Clicked")
            return True

def mainMenuExitButton_click(event): # Exit Button
    x,y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (x > 280 and x < 520) and (y > 368 and y < 448):
            print("Exit Button Has Been Clicked")
            return True

def creditsMenuBackButton_click(event): # Exit Button
    x,y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (x > 280 and x < 520) and (y > 368 and y < 448):
            print("Back Button Has Been Clicked")
            return True

def creditsMenuGithubButton_click(event): # Git Hub Button
    x,y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if ( state == "creditsMenu" ):
            if (x > 354 and x < 440) and (y > 270 and y < 350):
                print("GitHub Button Has Been Clicked")
                return True
# END - METHODS



# START - GAME LOOP
# Places the main menu screen on the game window to initialize the game
displayMainMenu()
# Testing
state = "mainMenu"
# Clock (used in game loop to limit framerate)
clock = pygame.time.Clock()
# Init. loop variable
running = True
while running:
    #Check for user input
        # Check for event if user has pushed
        # any event in queue
    for event in pygame.event.get():
        # if event is of type quit then set running bool to false
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            quit()

        # START - BUTTON LOGIC CONTROL FLOW
        if ( state == "mainMenu"): # Main Menu Button Logic
            if ( mainMenuPlayButton_click(event) == True ): # If play button is hit while on main menu
                displayPlayMenu() # Change screen
                state = "playMenu" # Change state
            elif ( mainMenuCreditsButton_click(event) == True ):
                displayCreditsMenu() # Change screen
                state = "creditsMenu" # Change state
            elif ( mainMenuExitButton_click(event) == True ): # If exit button is clicked, exit pygame window
                displayMainMenuExitButtonClicked() # Change screen
                time.sleep(0.2) # Wait
                pygame.quit() # Quit game

        if ( state == "creditsMenu" ): # Credits Menu Button Logic
            if ( creditsMenuGithubButton_click(event) == True ):
                openGithub()
            elif ( creditsMenuBackButton_click(event) == True ):
                state = "mainMenu"
                displayMainMenu()
        # STOP - BUTTON LOGIC CONTROL FLOW



    # Step 2: Update the screen
    pygame.display.update()

    # Clock: Sets the framerate to 60
    clock.tick(60)
# END - GAME LOOP
