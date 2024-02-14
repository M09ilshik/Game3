import pygame
import random


pygame.init()

screen_width = 1080
screen_hight = 720

screen = pygame.display.set_mode((screen_width, screen_hight))

font = pygame.font.SysFont("TimesNewRoman", 100)
font2 = pygame.font.SysFont("TimesNewRoman", 30)



score = 0

img = pygame.image.load("img/menukirpichi.jpg")
img_s = pygame.transform.scale(img, (1080, 720))
img1 = pygame.image.load("img/isaak-PhotoRoom.png-PhotoRoom.png")
img1_s = pygame.transform.scale(img1, (100, 100))
img2 = pygame.image.load("img/antiisaak-PhotoRoom.png-PhotoRoom.png")
img2_s = pygame.transform.scale(img2, (100, 100))
img_bullet = pygame.image.load("img/bullet-PhotoRoom.png-PhotoRoom.png")
img_bullet_s = pygame.transform.scale(img_bullet,(50,50))

sound_stop = pygame.mixer.Sound("Sounds/vzryiv-yadernoy-bombyi.mp3")
sound_antihero = pygame.mixer.Sound("Sounds/zombi-boretsya-s-chelovekom-leja-na-zemle-30059.mp3")

speed = 1.0
speed2 = 0.5
img_x = 90
img_y = 70
img_x1 = random.randint(800,980)
img_y1 = -10
x_bull,y_bull = 0, 0
flag_down = False
flag_right = False
flag_left = False
flag_up = False
def hero():
    global img_x
    global img_y
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        img_y -= speed
    if keys[pygame.K_s]:
        img_y += speed
    if keys[pygame.K_a]:
        img_x -= speed
    if keys[pygame.K_d]:
        img_x += speed
    screen.blit(img1_s, (img_x, img_y))

def antihero():
    global img_x1
    global img_y1

    if img_y + 70 < img_y1:
        img_y1 -= speed2
        sound_antihero.play()
    elif img_y > img_y1 + 70:
        img_y1 += speed2
        sound_antihero.play()
    elif img_x + 70 < img_x1:
        img_x1 -= speed2
        sound_antihero.play()
    elif img_x > img_x1 + 70:
        img_x1 += speed2
        sound_antihero.play()
    else:
        sound_antihero.stop()
    screen.blit(img2_s, (img_x1, img_y1))

def bullet():
    global x_bull
    global y_bull
    global flag_down
    global flag_right
    global flag_up
    global flag_left

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        flag_right = True
    if keys[pygame.K_LEFT]:
        flag_left = True
    if keys[pygame.K_UP]:
        flag_up = True
    if keys[pygame.K_DOWN]:
        flag_down = True
    if x_bull >= 1080 or x_bull + 50 <= 0 or y_bull > 720 or y_bull + 50 < 0:
        flag_down = False
        flag_right = False
        flag_left = False
        flag_up = False

    if flag_right == True:
        flag_left = False
        flag_up = False
        flag_down = False
        x_bull += 1
        screen.blit(img_bullet_s, (x_bull, y_bull))
    if flag_left == True:
        flag_right = False
        flag_up = False
        flag_down = False
        x_bull -= 1
        screen.blit(img_bullet_s, (x_bull, y_bull))
    if flag_up == True:
        flag_right = False
        flag_left = False
        flag_down = False
        y_bull -= 1
        screen.blit(img_bullet_s, (x_bull, y_bull))
    if flag_down == True:
        flag_right = False
        flag_up = False
        flag_left = False
        y_bull += 1
        screen.blit(img_bullet_s, (x_bull, y_bull))
    if flag_right != True and flag_left != True and flag_up != True and flag_down != True:
        x_bull = img_x
        y_bull = img_y

while True:
    screen.blit(img_s, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()


    hero()
    bullet()
    antihero()
    
    if img_x1 < img_x + 71 and img_x1 + 71 > img_x and img_y1 < img_y + 71 and img_y1 + 71 > img_y:
        text2 = font.render("Game Over", True, (255,0,0))
        screen.blit(text2, (300, 230))
        speed = 0
        speed2 = 0
        sound_stop.play()

    if img_x1 < x_bull + 70 and img_x1 + 70 > x_bull and img_y1 < y_bull + 70 and img_y1 + 70 > y_bull:
        score += 1
        antihero_spawn = random.randint(300,500)
        antihero_spawn2 = random.randint(1,4)
        if antihero_spawn2 == 1:
            img_x1 = img_x - antihero_spawn
        if antihero_spawn2 == 2:
            img_x1 = img_x + 100 + antihero_spawn
        if antihero_spawn2 == 3:
            img_y1 = img_y - antihero_spawn
        if antihero_spawn2 == 4:
            img_y1 = img_y + 100 + antihero_spawn



    if img_x + 100 > 1080:
        img_x = 1
    elif img_x < 0:
        img_x = 979
    elif img_y + 100 > 720:
        img_y = 1
    elif img_y  < 0:
        img_y = 619

        
    text = font2.render("Score: ", True, (0,255,0))
    screen.blit(text, (0, 0))
    text1 = font2.render(str(score), True, (0, 255, 0))
    screen.blit(text1, (85, 0))

    if score >= 20:
        speed = 0
        speed2 = 0
        text3 = font.render("You Win", True, (0, 0, 255))
        screen.blit(text3, (350, 230))

    pygame.display.update()
