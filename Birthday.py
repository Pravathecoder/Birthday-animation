import pygame
import time

pygame.init() #initialize

WIDTH = 600
HEIGHT = 600
pygame.display.set_caption('Birthday Card')
screen = pygame.display.set_mode((WIDTH,HEIGHT))

img1 = pygame.image.load('images/bg1.jpg') #loding the image
image1 = pygame.transform.scale(img1,(WIDTH,HEIGHT)) #Changing witdh and height

while True:
     #font loading
     font = pygame.font.SysFont('Times New Roman',72)

     #text loading
     text1 = font.render('Happy',True,(0,0,0))
     text2 = font.render('Birthday',True,(0,0,0))

     #showing on screen 
     screen.fill((255,255,255))
     screen.blit(image1,(0,0)) #show image on screen

     #show text on screen 
     screen.blit(text1,(210,180))
     screen.blit(text2,(180,265))

     pygame.display.update()
     time.sleep(2)

     image2 = pygame.image.load('images/bg2.jpg')
     font2 = pygame.font.SysFont('Arial',36)
     text3 = font2.render('Wish you a bright future',True,(0,0,0))

     screen.fill((255,255,255))
     screen.blit(image2,(0,0))

     screen.blit(text3,(30,30))

     pygame.display.update()
     time.sleep(2)

     image3 = pygame.image.load('images/bg3.jpg')
     font3 = pygame.font.SysFont('Georga',36)
     text4 = font3.render('God bless you',True,(0,0,0))

     screen.fill((255,255,255))
     screen.blit(image3,(0,0))

     screen.blit(text4,(30,30))

     pygame.display.update()
     time.sleep(2)

     

     

     