import pygame
import time
import random

pygame.init()

screen = pygame.display.set_mode((500,800))
pygame.display.set_caption("Pygame Flappy Bird")
pygame.display.set_icon(pygame.image.load("favicon.ico"))
clock = pygame.time.Clock()
running = True

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images =  [pygame.image.load('sprites/yellowbird-upflap.png').convert_alpha(),
                        pygame.image.load('sprites/yellowbird-midflap.png').convert_alpha(),
                        pygame.image.load('sprites/yellowbird-downflap.png').convert_alpha()]
        self.current_image = 0
        self.cor_x = 120
        self.cor_y = 400
        self.height = 35
        self.width = 50
        self.image = pygame.image.load("sprites/yellowbird-midflap.png") 
        self.vel = 10
        
    def draw(self,screen):
        self.current_image = (self.current_image + 1) % 3
        self.image = self.images[self.current_image]
       
        screen.blit(pygame.transform.scale(self.image, (self.width,self.height)), (self.cor_x, self.cor_y))

    def action(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            
            
            self.cor_y -= self.vel
            
        else:
             
            
            self.cor_y +=7
        

class Ground():
    def __init__(self) -> None:
        self.cor_x = 0
        self.cor_y = 700
        self.height = 100
        self.width = 800
        self.vel = 2
        self.image = pygame.image.load("sprites/ground.png")
    
    def draw(self):
        
        screen.blit(pygame.transform.scale(self.image, (self.width,self.height)), (self.cor_x, self.cor_y))
        self.cor_x -=self.vel
        if self.cor_x <= -55:
            
            self.cor_x = 0

class Pipe():
    def __init__(self,cor_y, cor_x) -> None:
        self.cor_x = cor_x
        self.cor_y = cor_y
        self.downcor_y = 0

        self.width = 90
        self.height = 400
        self.image = pygame.image.load("sprites/pipe-green.png")
        self.image_up = pygame.transform.rotate(self.image, 180)
        
        self.vel = 3

    def draw(self):
        self.cor_x -=self.vel
        
        screen.blit(pygame.transform.scale(self.image_up, (self.width,self.height)), (self.cor_x, self.cor_y))    
        screen.blit(pygame.transform.scale(self.image, (self.width,self.height)), (self.cor_x, self.cor_y +self.height +200))

class Score():
    def __init__(self) -> None:
        self.score = 0
        self.cor_x = 250
        self.cor_y = 50
        
        self.height = 50
        self.width = 50
        
    def draw(self):
        
        
        if self.score ==  10:
            score_greater_10.score += 1
            self.score = 0
  
        image = pygame.image.load(f"sprites/{self.score}.png")
      
        screen.blit(pygame.transform.scale(image, (self.width,self.height)), (self.cor_x, self.cor_y))



background_image = pygame.image.load("sprites/background-day.png")
background_image = pygame.transform.scale(background_image, (500, 800))


start_image = pygame.image.load("sprites/message.png")
start_image = pygame.transform.scale(start_image, (200,300))

bird = Bird()
ground = Ground()
score = Score()
score_greater_10 = Score()


pipe = Pipe(cor_y=-150, cor_x=1000)
pipe_2 = Pipe(cor_y=-200, cor_x=1500 )
pipe_3 = Pipe(cor_y=-250, cor_x=2000)
pipe_4 = Pipe(cor_y= -300, cor_x=2500)


wing_sound = pygame.mixer.Sound("sounds/wing.ogg")
score_sound = pygame.mixer.Sound("sounds/point.ogg")
wing_sound.set_volume(0.7)
score_sound.set_volume(0.5)

start = False
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_SPACE :
                start = True
                wing_sound.play() 
    screen.fill((0,0,0))
    screen.blit(background_image,(0,0))
    screen.blit(start_image, (150,150))
    if start == True:
        start_image.fill((0, 0, 0, 0))
        pipe.draw()
        pipe_2.draw()
        pipe_3.draw()
        pipe_4.draw()
        score.draw()


        #collision     self.cor_y +self.height +200


        if (pipe.cor_x > bird.cor_x and pipe.cor_x < bird.cor_x + bird.width) and ((pipe.cor_y  < bird.cor_y and pipe.cor_y + pipe.height > bird.cor_y + bird.width) or (pipe.cor_y +pipe.height +200  < bird.cor_y + bird.width and pipe.cor_y +pipe.height +200 + 400>bird.cor_y + bird.width)) :
            print("collide")
        
        # if (pipe.cor_x > bird.cor_x and pipe.cor_x < bird.cor_x + bird.width) and (pipe.cor_y +pipe.height +200  < bird.cor_y + bird.width and pipe.cor_y +pipe.height +200 + 400>bird.cor_y + bird.width) :
        #     print("hello")
        



        if  pipe.cor_x > 120 and pipe.cor_x < 123:
                score_sound.play()
                score.score +=1
                score.draw()
    
        if  pipe_2.cor_x > 120 and pipe_2.cor_x < 125:
                score_sound.play()
                score.score +=1
                score.draw()
        
        if  pipe_3.cor_x > 120 and pipe_3.cor_x < 123:
                score_sound.play()
                score.score +=1
                score.draw()
        
        if  pipe_4.cor_x > 120 and pipe_4 .cor_x < 123:
                score_sound.play()
                score.score +=1
                score.draw()
        
        score_greater_10.draw()
        if score.score == 0:
            score_greater_10.cor_x = 200
            score_greater_10.draw()
    
        if pipe.cor_x < -100:
            
            pipe.cor_x = 1000
        
        
                
                
        if pipe_2.cor_x < -100:
            
            pipe_2.cor_x = 1500
        
        if pipe_3.cor_x < -100:
            pipe_3.cor_x = 2000
        
        if pipe_4.cor_x < -100:
            pipe_4.cor_x = 2500
        bird.action()
    
    ground.draw()
    
    bird.draw(screen)
    # pygame.display.flip()
    clock.tick(65)
    pygame.display.update()
    
pygame.quit()

