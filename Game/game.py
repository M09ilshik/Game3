import pygame
import random


pygame.init()

screen_width = 1080
screen_hight = 720

screen = pygame.display.set_mode((screen_width, screen_hight))

font = pygame.font.SysFont("Goudy Stout обычный", 50)
font2 = pygame.font.SysFont("TimesNewRoman", 30)

img = pygame.image.load("img/menu.jpg")
img_s = pygame.transform.scale(img, (1080, 720))
img1 = pygame.image.load("img/zmeya.png")
img1_s = pygame.transform.scale(img1, (100, 100))
img2 = pygame.image.load("img/demon.png")
img2_s = pygame.transform.scale(img2, (100, 100))
img_bullet = pygame.image.load("img/bullet.png")
img_bullet_s = pygame.transform.scale(img_bullet,(300,300))

sound_stop = pygame.mixer.Sound("Sounds/vzryiv-yadernoy-bombyi.mp3")
sound_antihero = pygame.mixer.Sound("Sounds/zombi-boretsya-s-chelovekom-leja-na-zemle-30059.mp3")

speed = 1.0
speed2 = 0.5
img_x = 90
img_y = 70
img_x1 = random.randint(800,980)
img_y1 = -10
img_bullet_x = -100
img_bullet_y = -100

def hero():
    global img_x
    global img_y
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        img_y -= speed
    elif keys[pygame.K_s]:
        img_y += speed
    elif keys[pygame.K_a]:
        img_x -= speed
    elif keys[pygame.K_d]:
        img_x += speed
    screen.blit(img1_s, (img_x, img_y))

# def antihero():
#     global img_x1
#     global img_y1
#
#     if img_y1 + 100 >= 620:
#         img_y1 -= speed2
#         sound_antihero.play()
#     elif img_y1 <= 0:
#         img_y1 += speed2
#         sound_antihero.play()
#     else:
#         sound_antihero.stop()
#     screen.blit(img2_s, (img_x1, img_y1))

# def bullet():
#     global img_bullet_x
#     global img_bullet_y
#
#     i


while True:
    screen.blit(img_s, (0, 0))
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif keys[pygame.K_SPACE]:

            screen.blit(img_bullet_s,(img_x, img_y))



    hero()
    # antihero()
    
    if img_x + 100  > img_x1 and img_x < img_x1 + 100 and img_y + 100 > img_y1 and img_y < img_y1 + 100:
        speed = 0
        speed2 = 0
        sound_stop.play()
    else:
        pass

    if img_x + 100 > 1080:
        img_x = 1
    elif img_x < 0:
        img_x = 979
    elif img_y + 100 > 720:
        img_y = 1
    elif img_y  < 0:
        img_y = 619
        
    text = font2.render("Start", True, (0,0,225))
    screen.blit(text, (500, 320))
    text = font.render("Welcome", True, (0, 255, 0))
    screen.blit(text, (455, 200))
    text = font2.render("Options", True, (0,0,255))
    screen.blit(text, (480, 350))
    text = font2.render("Exit", True, (255, 0, 0))
    screen.blit(text, (505, 380))

    pygame.display.update()
