import pygame
import time
import random
pygame.init()
white = [255,255,255]
red = [255,0,0]
black = [0,0,0]
img = pygame.image.load('1.jpg')
screen = pygame.display.set_mode((800,900))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None,23)
direction = "right"


def text_objects(msg,color):
    textsurface = font.render(msg, True, color)
    return textsurface, textsurface.get_rect()

def trap_massage(msg,color):
    text_surface, text_rect = text_objects(msg, color)
    #screen_text = font.render(msg, True, color)
    #screen.blit(screen_text, [400,450])
    text_rect.center = 400, 450
    screen.blit(text_surface, text_rect)
def snake(snakeList):
    if direction == "right":
        head = pygame.transform.rotate(img, 90)
    if direction == "left":
        head = pygame.transform.rotate(img, 270)
    if direction == "up":
        head = pygame.transform.rotate(img, 180)
    if direction == "down":
        head = pygame.transform.rotate(img, 0)
    
    screen.blit(head, (snakeList[-1][0],snakeList[-1][1]))
    for XnY in snakeList[:-1]:
        
        pygame.draw.rect(screen,black,[XnY[0],XnY[1],10,10])
def game_loop():
    global direction
    lead_x = 300
    lead_y = 300
    t = False
    gameOver = False
    lead_x_change = 10
    lead_y_change = 0
    Random_rangeX = round(random.randrange(0,800)/10.0)*10.0
    Random_rangeY = round(random.randrange(0,900)/10.0)*10.0
    snakeList = []
    snakeLength = 0
    
    while not t:
        while gameOver == True:
            screen.fill(white)
            trap_massage("press C to play Q to quit",red)
            pygame.display.flip()

            
            for event in pygame.event.get():
                
                if event.type == pygame.KEYDOWN:
                    
                    if event.key == pygame.K_q:
                        t = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        game_loop()
        for m in pygame.event.get():
           if m.type == pygame.QUIT:
               t = True


           if m.type == pygame.KEYDOWN:
               if m.key == pygame.K_LEFT:
                   direction = "left"
                   
                   lead_x_change = -10
                   lead_y_change = 0
               if m.key == pygame.K_RIGHT:
                   direction = "right"
                   lead_x_change = +10
                   lead_y_change = 0
               if m.key == pygame.K_UP:
                   direction = "up"
                   lead_y_change = -10
                   lead_x_change = 0
               if m.key == pygame.K_DOWN:
                   direction = "down"
                   lead_y_change = +10
                   lead_x_change = 0
                
          # if m.type == pygame.KEYUP:
          #      if m.key == pygame.K_LEFT or m.key == pygame.K_RIGHT:
          #         lead_x_change = 0 
        lead_x += lead_x_change
        lead_y += lead_y_change
        screen.fill(white)
        if lead_x >= 800 or lead_y >= 900 or lead_x <= 0 or lead_y <= 0:
            gameOver = True
        pygame.draw.rect(screen,red,[Random_rangeX,Random_rangeY,10,10])
        
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)
        snake(snakeList)
        for snakeSegment in snakeList[:-1]:
            if snakeHead == snakeSegment:
                gameOver = True
        if len(snakeList)>snakeLength:
            del snakeList[0]
        pygame.display.update()
        
        clock.tick(10)
        if lead_x == Random_rangeX and lead_y == Random_rangeY:
            Random_rangeX = round(random.randrange(0,800)/10.0)*10.0
            Random_rangeY = round(random.randrange(0,900)/10.0)*10.0
            snakeLength += 1
  
    pygame.quit()
    quit()

game_loop()

