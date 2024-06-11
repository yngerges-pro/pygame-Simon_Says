import pygame
import random
import time
# import clock
from button import Button # By importing Button we can access methods from
#the Button class
pygame.init()
clock = pygame.time.Clock()

class main:
    def __init__(self):
        # Constants
        SCREEN_WIDTH = 500
        SCREEN_HEIGHT = 500
        self.SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.GREEN_ON = (0, 255, 0)
        self.GREEN_OFF = (0, 180, 0)
        self.RED_ON = (255, 0, 0)
        self.RED_OFF = (180, 0, 0)
        self.BLUE_ON = (0, 0, 255)
        self.BLUE_OFF = (0, 0, 150)
        self.YELLOW_ON = (255, 255, 0)
        self.YELLOW_OFF = (227, 227, 0)
        # Pass in respective sounds for each color
        self.GREEN_SOUND = pygame.mixer.Sound("bell1.mp3") # bell1
        self.RED_SOUND = pygame.mixer.Sound("bell2.mp3") # bell2
        self.BLUE_SOUND = pygame.mixer.Sound("bell3.mp3") # bell3
        self.YELLOW_SOUND = pygame.mixer.Sound("bell4.mp3") # bell4
        
        self.green = Button(self.GREEN_ON, self.GREEN_OFF, self.GREEN_SOUND, 0, 0)
        self.red = Button(self.RED_ON, self.RED_OFF, self.RED_SOUND, 0, 250)
        self.blue = Button(self.BLUE_ON, self.BLUE_OFF, self.BLUE_SOUND, 250, 0)
        self.yellow = Button(self.YELLOW_ON, self.YELLOW_OFF, self.YELLOW_SOUND, 250, 250)

        self.colors = ["green","red","blue", "yellow"]

        self.__cpu_sequence = []
        self.__players_sequence = []
        '''
        Draws game board
        '''
    def draw_board(self):
        # Call the draw method on all four button objects
        # Button Sprite Objects

        green = Button(self.GREEN_OFF, self.GREEN_OFF, self.GREEN_SOUND, 0, 0)
        red = Button(self.RED_OFF, self.RED_OFF, self.RED_SOUND, 0, 250)
        blue = Button(self.BLUE_OFF, self.BLUE_OFF, self.BLUE_SOUND, 250, 0)
        yellow = Button(self.YELLOW_OFF, self.YELLOW_OFF, self.YELLOW_SOUND, 250, 250)
        
        green.draw(self.SCREEN,0,0)
        red.draw(self.SCREEN,0,250)
        blue.draw(self.SCREEN,250,0)
        yellow.draw(self.SCREEN,250,250)

        '''
        Chooses a random color and appends to cpu_sequence.
        Illuminates randomly chosen color.
        '''

    
    def cpu_turn(self):
        choice = str(random.choice(self.colors)) # pick random color
        print("The choice is", choice)
        self.__cpu_sequence.append(choice) # update cpu sequence
        if choice == "green":
            self.green.update(self.SCREEN)
        elif choice == "red":
            self.red.update(self.SCREEN)
        elif choice == "blue":
            self.blue.update(self.SCREEN)
        elif choice == "yellow":
            self.yellow.update(self.SCREEN)
        else:
            print("Wrong Color")
        # Check other three color options

        print(self.__cpu_sequence)
        '''
        Plays pattern sequence that is being tracked by cpu_sequence
    '''

    def repeat_cpu_sequence(self):
        if(len(self.__cpu_sequence) != 0):
            for color in self.__cpu_sequence:
                if color == "green":
                    self.green.update(self.SCREEN)
                elif color == "red":
                    self.red.update(self.SCREEN)
                elif color == "blue":
                    self.blue.update(self.SCREEN)
                else:
                    self.yellow.update(self.SCREEN)
                pygame.time.wait(2000)

        '''
        After cpu sequence is repeated the player must attempt to copy the same
        pattern sequence.

        L12-6 Final Project.md 11/30/2021

        4 / 5

        The player is given 3 seconds to select a color and checks if the selected
        color matches the cpu pattern sequence.
        If player is unable to select a color within 3 seconds then the game is
        over and the pygame window closes.
        '''

    def game_over():
        pygame.quit()
        quit()
    
    
    def player_turn(self):
        turn_time = time.time()
        while time.time() <= turn_time + 3 and len(self.__players_sequence) <= len(self.__cpu_sequence):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:

                    # button click occured
                    # Grab the current position of mouse here
                    pos = list(pygame.mouse.get_pos())
                    
                    if self.green.selected(pos): # green button was selected
                        self.green.update(self.SCREEN) # illuminate button
                        self.__players_sequence.append("green") # add to player
                    elif self.red.selected(pos): # red button was selected
                        self.red.update(self.SCREEN) # illuminate button
                        self.__players_sequence.append("red") # add to player
                    elif self.yellow.selected(pos): # yellow button was selected
                        self.yellow.update(self.SCREEN) # illuminate button
                        self.__players_sequence.append("yellow") # add to player
                    elif self.blue.selected(pos): # blue button was selected
                        self.blue.update(self.SCREEN) # illuminate button
                        self.__players_sequence.append("blue") # add to player

                    print("player's list", self.__players_sequence)
                    mobj = main()
                    mobj.check_sequence(self.__players_sequence) # check if player
                        # choice was correct
                    turn_time = time.time() # reset timer
        # Check other three options
        # If player does not select a button within 3 seconds then the game
        # closes
        if not time.time() <= turn_time + 3:
            mobj = main()
            mobj.check_sequence(self.__players_sequence)

    '''
    Checks if player's move matches the cpu pattern sequence
    '''

    def check_sequence(self, players_sequence):
        if self.__players_sequence[:len(self.__players_sequence)] != self.__cpu_sequence[:len(self.__players_sequence)]:
            pygame.quit()
            quit()




    '''
    Quits game and closes pygame window
    '''

     
# Game Loop
run = True
while run:

    mainobj = main()# draws buttons onto pygame screen
    mainobj.draw_board()
    mainobj.repeat_cpu_sequence() # repeats cpu sequence if it's not empty
    mainobj.cpu_turn() # cpu randomly chooses a new color
    mainobj.player_turn() # player tries to recreate cpu sequence


    # pygame.time.wait(5000) # waits one second before repeating cpu
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.display.quit()
            pygame.quit()
            quit()
    pygame.display.update()

    