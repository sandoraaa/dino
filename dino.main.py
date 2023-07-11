import pygame
#import random

pygame.init()
bg=pygame.image.load('dino.bg.jpg')
dinoimg=pygame.image.load('dino (1).png')
stoneimg=pygame.image.load('cactys (1).png')
cloudimg=pygame.image.load('cloud.png')
cloud2img=pygame.image.load('cloud2.png')
appleimg=pygame.image.load('apple.png')
lifeimg=pygame.image.load('life.png')


x=50
y=255

w=80
h=80

sx=580
sy=285

c2x=400
c2y=60

cx=230
cy=45

ax=300
ay=280

#lx=10
#ly=10



sspeed=15
cspeed=2
c2speed=1
aspeed=10

width=600
height =500

life=3



font=pygame.font.SysFont("verdana",100)
font2=pygame.font.SysFont("verdana",30)

text=font2.render('Game over!', True, pygame.Color("black"))
text2=font2.render('press Space to', True, pygame.Color("black"))
text3=font2.render('continue', True, pygame.Color("black"))


def jump():
    global make_jump, y, jump_count
    if jump_count>=-30:
        y-=jump_count/2
        jump_count-=3

    else:
        jump_count=30
        make_jump=False


jump_count=30
make_jump=False

size_window = (width, height)
window = pygame.display.set_mode(size_window)
pygame.display.set_caption('Game')


run=True

lose=False

game_state='run'

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP and game_state=='run':
                make_jump=True

            #if event.key==pygame.K_SPACE:

    window.fill ('green')
    window.blit(bg,(0,0))
    lx=10
    for i in range (life):
        window.blit(lifeimg, (lx, 10))
        lx+=35

    #window.blit(lifeimg, (lx, 10))


    window.blit(dinoimg,(x,y))

    window.blit(stoneimg, (sx, sy))
    window.blit(cloudimg, (cx, cy))
    window.blit(cloud2img, (c2x, c2y))
    window.blit(appleimg, (ax,ay))

    sx-=sspeed
    cx-=cspeed
    c2x-=c2speed
    ax-=aspeed
    if c2x<-80:
        c2x=585
    if cx<-40:
        cx=580
    if sx<-55:
        sx=570
    if ax<-20:
        ax=1500
    if make_jump:
        jump()
    keys = pygame.key.get_pressed()



    if x <= sx <= x+w and y <= sy <= y+h:
        print('ewewew')
        #text_image = font.render('Boom', True, pygame.Color("white"))
        #window.blit(text_image,(250,250))
        sx=width
        life-=1
        print(life)
        if life==0:
            sspeed=0
            cspeed=0
            c2speed=0
            aspeed=0
            window.fill('white')
            window.blit(text,(200,170))
            window.blit(text2, (180, 200))
            window.blit(text3, (220, 230))
            game_state='lose'
            pygame.time.delay(100)

    if keys[pygame.K_SPACE] and game_state !='run':
        print('end')
        game_state = 'run'
        sspeed = 15
        cspeed = 2
        c2speed = 1
        aspeed=10
        sx = 580
        life=3






    pygame.time.delay(50)
    pygame.display.update()



pygame.quit()