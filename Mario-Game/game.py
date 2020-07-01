'''
@author - Sarthak Gupta
'''

import pygame
import sys

# define global variables
LEVEL = 0
SCORE = 0
HIGH_SCORE = 0

# initialize pygame
pygame.init()

# define window
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 600
FPS = 20
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
ADD_NEW_FLAME_RATE = 25

cactus_img = pygame.image.load('E:/Documents/Programs/Python/Mario-Game/resources/Cactus_Bricks.png')
cactus_img_rect = cactus_img.get_rect()
cactus_img_rect.left = 0

fire_img = pygame.image.load('E:/Documents/Programs/Python/Mario-Game/resources/Fire_Bricks.png')
fire_img_rect = fire_img.get_rect()
fire_img_rect.left = 0

CLOCK = pygame.time.Clock()
font = pygame.font.SysFont('forte', 20)

# define canvas
canvas = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Super Mario')

# define dragon class
class Dragon:
    dragon_velocity = 10

    def __init__(self):
        self.dragon_img = pygame.image.load('E:/Documents/Programs/Python/Mario-Game/resources/Dragon.png')
        self.dragon_img_rect = self.dragon_img.get_rect()
        self.dragon_img_rect.width -= 10
        self.dragon_img_rect.height -= 10
        self.dragon_img_rect.top = int(WINDOW_HEIGHT/2)
        self.dragon_img_rect.right = WINDOW_WIDTH
        self.up = True
        self.down = False

    # define method to make Dragon move
    def update(self):
        canvas.blit(self.dragon_img, self.dragon_img_rect)

        # check position of the dragon
        if self.dragon_img_rect.top <= cactus_img_rect.bottom:          # check if its in the top region
            self.up = False
            self.down = True
        elif self.dragon_img_rect.bottom >= fire_img_rect.top:          # check if its in the bottom region
            self.up = True
            self.down = False

        if self.up:                                                     # if in top region, move down
            self.dragon_img_rect.top -= self.dragon_velocity
        elif self.down:                                                 # if in bottom region, move up
            self.dragon_img_rect.top += self.dragon_velocity

dragon = Dragon()

# define the flames class for fireball
class Flames:
    flames_velocity = 20

    def __init__(self):
        self.flames = pygame.image.load('E:/Documents/Programs/Python/Mario-Game/resources/Fireball.png')
        self.flames_img = pygame.transform.scale(self.flames, (20, 20))
        self.flames_img_rect = self.flames_img.get_rect()
        self.flames_img_rect.right = dragon.dragon_img_rect.left
        self.flames_img_rect.top = dragon.dragon_img_rect.top + 30

    # move fireballs on the canvas
    def update(self):
        canvas.blit(self.flames_img, self.flames_img_rect)

        if self.flames_img_rect.left > 0:
            self.flames_img_rect.left -= self.flames_velocity

# define score class
class Topscore:
    def __init__(self):
        self.high_score = 0

    # set top score
    def top_score(self, score):
        if score > self.high_score:
            self.high_score = score

        return self.high_score

# define class variables
topScore = Topscore()
flame = Flames()

# define the mario class
class Mario:
    velocity = 10

    def __init__(self):
        self.mario_img = pygame.image.load('E:/Documents/Programs/Python/Mario-Game/resources/Mario.png')
        self.mario_img_rect = self.mario_img.get_rect()
        self.mario_img_rect.left = 20
        self.mario_img_rect.top = int(WINDOW_HEIGHT/2) - 100
        self.down = True
        self.up = False

    # define method to make Mario move
    def update(self):
        canvas.blit(self.mario_img, self.mario_img_rect)

        if self.mario_img_rect.top <= cactus_img_rect.bottom:           # mario dies - top region
            game_over()
            
            if SCORE > self.mario_score:                                # update score
                self.mario_score = SCORE

        if self.mario_img_rect.bottom >= fire_img_rect.top:             # mario dies - bottom region
            game_over()

            if SCORE > self.mario_score:                                # update score
                self.mario_score = SCORE

        # move mario
        if self.up:                                                     # going up
            self.mario_img_rect.top -= 10
        if self.down:                                                   # going down
            self.mario_img_rect.bottom += 10

mario = Mario()

# define the game over function
def game_over():
    pygame.mixer.music.stop()
    music = pygame.mixer.Sound('E:/Documents/Programs/Python/Mario-Game/resources/Mario_Dies.wav')
    music.play()

    topScore.top_score(SCORE)
    
    game_over_img = pygame.image.load('E:/Documents/Programs/Python/Mario-Game/resources/End.png')
    game_over_img_rect = game_over_img.get_rect()
    game_over_img_rect.center = (int(WINDOW_WIDTH/2), int(WINDOW_HEIGHT/2))
    
    canvas.blit(game_over_img, game_over_img_rect)
    
    while True:
        for event in pygame.event.get():
            # exit game window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # restart game
            if event.type == pygame.KEYDOWN:
                # quit if 'esc' pressed
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                music.stop()
                game_loop()

        pygame.display.update()

# define the start game method
def start_game():
    canvas.fill(BLACK)

    start_img = pygame.image.load('E:/Documents/Programs/Python/Mario-Game/resources/Start.png')
    start_img_rect = start_img.get_rect()
    start_img_rect.center = (int(WINDOW_WIDTH/2), int(WINDOW_HEIGHT/2))
    
    canvas.blit(start_img, start_img_rect)
    
    while True:
        for event in pygame.event.get():
            # exit game window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # restart game
            if event.type == pygame.KEYDOWN:
                # quit if 'esc' pressed
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                game_loop()

        pygame.display.update()

# define method to state the difficulty level
def check_level(SCORE):
    global LEVEL

    # level - 1
    if SCORE in range(0, 100):
        cactus_img_rect.bottom = 50
        fire_img_rect.top = WINDOW_HEIGHT - 50
        LEVEL = 1

    # level - 2
    elif SCORE in range(100, 200):
        cactus_img_rect.bottom = 100
        fire_img_rect.top = WINDOW_HEIGHT - 100
        LEVEL = 2

    # level - 3
    elif SCORE in range(200, 300):
        cactus_img_rect.bottom = 150
        fire_img_rect.top = WINDOW_HEIGHT - 150
        LEVEL = 3
    
    # level - 4
    elif SCORE > 300:
        cactus_img_rect.bottom = 200
        fire_img_rect.top = WINDOW_HEIGHT - 200
        LEVEL = 4

# define the main game loop
def game_loop():
    global SCORE
    while True:
        add_new_flame_counter = 0
        flames_list = []

        pygame.mixer.music.load('E:/Documents/Programs/Python/Mario-Game/resources/Mario_Themes.wav')
        pygame.mixer.music.play(-1, 0.0)
        
        while True:
            canvas.fill(BLACK)
            check_level(SCORE)
            
            dragon.update()
            
            add_new_flame_counter += 1

            if add_new_flame_counter == ADD_NEW_FLAME_RATE:
                add_new_flame_counter = 0
                new_flame = Flames()
                flames_list.append(new_flame)
            
            for f in flames_list:
                if f.flames_img_rect.left <= 0:
                    flames_list.remove(f)
                    SCORE += 10

                f.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        mario.up = True
                        mario.down = False
                    elif event.key == pygame.K_DOWN:
                        mario.down = True
                        mario.up = False
                
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        mario.up = False
                        mario.down = True
                    elif event.key == pygame.K_DOWN:
                        mario.down = True
                        mario.up = False

            # display score
            score_font = font.render('Score:'+str(SCORE), True, GREEN)
            score_font_rect = score_font.get_rect()
            score_font_rect.center = (200, cactus_img_rect.bottom + int(score_font_rect.height/2))
            canvas.blit(score_font, score_font_rect)

            # display level
            level_font = font.render('Level:'+str(LEVEL), True, GREEN)
            level_font_rect = level_font.get_rect()
            level_font_rect.center = (500, cactus_img_rect.bottom + int(score_font_rect.height/2))
            canvas.blit(level_font, level_font_rect)

            # display top score
            top_score_font = font.render('Top Score:'+str(topScore.high_score),True,GREEN)
            top_score_font_rect = top_score_font.get_rect()
            top_score_font_rect.center = (800, cactus_img_rect.bottom + int(score_font_rect.height/2))
            canvas.blit(top_score_font, top_score_font_rect)

            canvas.blit(cactus_img, cactus_img_rect)
            canvas.blit(fire_img, fire_img_rect)
            
            # update game
            mario.update()
            
            for f in flames_list:
                if f.flames_img_rect.colliderect(mario.mario_img_rect):
                    game_over()
                    
                    if SCORE > mario.mario_score:
                        mario.mario_score = SCORE
            
            pygame.display.update()
            CLOCK.tick(FPS)

# start the game
start_game()
