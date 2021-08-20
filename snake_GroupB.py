import pygame
import random
import sys

pygame.init()

white = (255, 255, 255)
maroon = (220,20,60)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Ukuran Screen
SCREEN_width = 600
SCREEN_height = 400
SCREEN = pygame.display.set_mode((SCREEN_width, SCREEN_height))
pygame.display.set_caption('Jungle Snack by Group B') 
clock = pygame.time.Clock()

# Gambar Background dan Penutup 
bg_surface = pygame.image.load('assets/Base-snakee.png').convert_alpha()
init_surface = pygame.image.load('assets/Logo.png').convert_alpha()
init_rect = init_surface.get_rect(center = (300,200))

# Ukuran dan Kecepatan Gerak Ular
snake_block = 10
snake_speed = 15

# Font tulisan yang dipakai 
font_style = pygame.font.SysFont("bahnschrift", 20)
score_font = pygame.font.SysFont("timesnewroman", 20)
keyboard_font = pygame.font.SysFont("timesnewroman",15)

# Sound
eat_food = pygame.mixer.Sound('sounds/eat_food.wav')
crash = pygame.mixer.Sound('sounds/crash_.wav')
crash.set_volume(1)
background_music = pygame.mixer.Sound('sounds/Jazz.mp3')
background_music.set_volume(0.5)
background_music.play(loops = -1)

# Mendefinisikan Kata Kata yang di perlukan
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, white)
    SCREEN.blit(value, [20, 0])

def message(msg, color): 
    mesg = font_style.render(msg, True, color) 
    SCREEN.blit(mesg, [SCREEN_width / 3.5, SCREEN_height / 1.1])

def message1(msg, color): 
    mesg = font_style.render(msg, True, color) 
    SCREEN.blit(mesg, [SCREEN_width / 2.3, SCREEN_height / 1.17]) 

def keyboardmsg(msg,color):
    mesg = keyboard_font.render(msg,True,color)
    SCREEN.blit(mesg,[SCREEN_width / 3.9, SCREEN_height / 1.06]) 

# Mendefinisikan bentuk Ular
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(SCREEN, black, [x[0], x[1], snake_block, snake_block])

# Pengulangan Permainan 
def gameLoop():
    game_over = False
    game_close = False
 
    x1 = SCREEN_width / 2
    y1 = SCREEN_height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1

    # Posisi Makanan
    foodx = round(random.randrange(20, 550) / 10.0) * 10.0
    foody = round(random.randrange(20, 350) / 10.0) * 10.0
    
    
    while not game_over:
        
        while game_close == True:

            # Detail saat Kalah
            SCREEN.fill(black)
            SCREEN.blit(init_surface, init_rect)
            message1("You Lost!", white)
            message("Press P-Play Again or Q-Quit", white)

            Your_score(Length_of_snake - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p:
                        gameLoop()

        # Mengatur pergerakan Snake menggunakan panah atau WASD
        for event in pygame.event.get():       
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
                elif event.key == pygame.K_a:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_d:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_w:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_s:
                    y1_change = snake_block
                    x1_change = 0
            
        # Membuat batas tembok
        if x1 >= 580 or x1 < 30 or y1 >= 380 or y1 < 15:
            crash.play()
            game_close = True
            
        x1 += x1_change
        y1 += y1_change
        SCREEN.blit(bg_surface,(0,0))
    
        pygame.draw.rect(SCREEN, maroon, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
            
        
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                crash.play()
                game_close = True
 
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
         
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(20, 550) / 10.0) * 10.0
            foody = round(random.randrange(20, 350) / 10.0) * 10.0
            Length_of_snake += 1
            eat_food.play()
        keyboardmsg ("Use ← = Left, ↑ = Up, , → = Right, ↓ = Down", white)        

        pygame.display.update()
        clock.tick(snake_speed)


    pygame.quit()
    quit()

gameLoop()
