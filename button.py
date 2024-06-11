import random
import time
import pygame

pygame.init()

class Button():
    pygame.sprite.Sprite
    def __init__(self, color_on, color_off, color_sound, num1,num2): # Add given properties as parameters
        pygame.sprite.Sprite.__init__(self)
        # Initialize properties here
        self.color_on = color_on
        self.color_off = color_off
        self.color_sound = color_sound
        self.num1 = num1
        self.num2 = num2

        #initalize image and rect
        self.image = pygame.Surface((250, 250))
        self.image.fill(self.color_off)
        self.rect = self.image.get_rect()

        # Assign x, y coordinates to the top left of the sprite
        self.rect.topleft = (self.num1, self.num2)
        
        
                
    
    # Draws button sprite onto pygame window when called
    def draw(self, screen, x, y):
        # blit image here

        pygame.display.update()
        
        screen.blit(self.image, (x, y))
        
        # pygame.time.wait(500)
        pygame.display.update()

        '''
        Used to check if given button is clicked/selected by player
        '''

    def selected(self, mouse_pos):
        # Check if button was selected. Pass in mouse_pos.
        '''
        Illuminates button selected and plays corresponding sound.
        Sets button color back to default color after being illuminated.
        '''

        #click check
        self.clicked = False
        # for e in pygame.event.get():
        
        
        if self.rect.collidepoint(mouse_pos):
            self.clicked = True
            print("Clicked?", self.clicked)
            pygame.display.update()
            #illuminates button
            self.image.fill(self.color_on)
            # self.screen            
            # self.color_on.update(self.screen)
            # pygame.time.wait(500)
            #plays sound
            pygame.mixer.Sound.play(self.color_sound)
            #shows default color
            self.image.fill(self.color_off)
            pygame.display.update()

        return self.clicked
            

            # L12-6 Final Project.md 11/30/2021

        # 2 / 5

    def update(self, screen):
        # Illuminate button by filling color here
        # blit the image here so it is visible to the player
        # Play sound
        pygame.display.update()
        self.image.fill(self.color_on)
        self.screen = screen.blit(self.image, (self.rect.x, self.rect.y))
        # pygame.time.wait(500)
        self.image.fill(self.color_off)
        self.screen
        pygame.time.wait(500)
        pygame.display.update()
        # pygame.time.wait(1000)