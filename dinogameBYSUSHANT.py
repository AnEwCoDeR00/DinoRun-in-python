import pygame
import random
import math
#physics
gamespeed = 1
dinofallspeed = 1
jumpspeed = 250
score = 0
pygame.init()
over_font = pygame.font.Font('freesansbold.ttf', 32)
sc = pygame.font.Font('freesansbold.ttf', 25)

screen = pygame.display.set_mode((800, 600))
#player
player = pygame.image.load('player.png')
player = pygame.transform.scale(player, (100,100))
playerx = 100
playery = 350
def play():
    screen.blit(player, (playerx, playery))
#jump music
jump = pygame.mixer.music.load('jump.wav')
def jum():
    pygame.mixer.music.play()

#bird
bird = pygame.image.load('bird.png')
bird = pygame.transform.scale(bird, (30,30))
birdx = random.randint(600, 2000)
birdy = 100
def birddraw():
    screen.blit(bird, (birdx, birdy))
   
#background
bg = pygame.image.load('ground.png')
bg = pygame.transform.scale(bg, (2500,60))
bgx = 0
bgy = 400
def bgdraw():
    screen.blit(bg, (bgx, bgy))    
#cactus
bg1 = pygame.image.load('cactus.png')
bg1 = pygame.transform.scale(bg1, (60,60))
bg1x = 600
bg1y = 370
def cactus():
    screen.blit(bg1, (bg1x, bg1y))
#highscore
highscore = open('highscore.txt', "r").read()
int(highscore)
   

#game over text and score display
def game_over_text():
    over_text = over_font.render("GAME OVER", True, (0, 0, 0))
    screen.blit(over_text, (500,200))
def scorex():
    scoret = sc.render('Score: '+ str(score) + ' Highscore: ' + str(highscore), True, (0, 0, 0))
    screen.blit(scoret, (400, 50))

def checkscore(score,highscore):
     int(score)
     int(highscore)
     if score > int(highscore):
            int(score)
            int(highscore)
            highscore = score
            open('highscore.txt', "w").write(str(score))
#see if user wants to play so i maked a state
gamestate = 'ready'
#main game
running = True
while running:
    def isCollision(bg1x, bg1y,playerx, playery):#collison test functions cactus and bird
       distance = math.sqrt(math.pow(bg1x - playerx, 2) + (math.pow(bg1y - playery, 2)))
       if distance < 70:
            return True
       else:
            return False
    def birdCollision(birdx, birdy,playerx, playery):
       distance = math.sqrt(math.pow(birdx - playerx, 2) + (math.pow(birdy - playery, 2)))
       if distance < 30:
          return True
       else:
          return False
    screen.fill((255, 255, 255))#white screen
    #this code excutes when game is not started
    if gamestate == 'ready':
        scoredis = over_font.render("Press anything to play ", True, (0, 0, 0))#display the score
        higscor =  over_font.render("High score: "+ str(highscore), True, (0, 0, 0))
        screen.blit(scoredis, (200,200))
        screen.blit(higscor, (300,400))
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
                running= False
          if event.type == pygame.KEYDOWN:#if user press any button start game
              gamestate = 'play'    
    #game starts when any key is pressed  
    if gamestate == 'play':
        checkscore(score,highscore)#highscore
        gamestate = 'play'#always game state will be in play
        gamespeed += 0.0005#speeds
        dinofallspeed += 0.00025
        birdx -= 1#bird will always fly
        if birdx <= 0:#if bird reachs 0 x then move it to random x
          birdx = random.randint(600, 2000)
        for e in pygame.event.get(): 
            if e.type == pygame.QUIT:#window closing
                running= False
            if e.type == pygame.KEYDOWN:                             
                if e.key == pygame.K_SPACE:#if users press space then make the dino jump
                    if playery == 350:
                       playery -= jumpspeed
                       jum()
            
        #this code sees if dino is in air if yes then it makes the dino come down       
        if playery != 350:
           playery += dinofallspeed
        if playery >= 350:#if dino is on the ground its y position will be 350
           playery = 350
        #draws everything
        bgdraw()#draws the ground
        play()#draws the player
        cactus()#draws the cactus
        birddraw()#draws the bird
        scorex()#display the score
        #makes the ground move BUT I DONT NEED THIS XD
        bgx -= 1
        bg1x -= gamespeed#makes the cactus move gamespeed is increased every time while loop is ran
        if bgx == -500:#sees if ground is far then makes it come back
         bgx = -50 
        if bg1x <  0 :#checks if cactus has reached end if yes then add scores and makes the cactus to a new pos 
           bg1x = random.randint(750,1000)
           score += 10
        colison = isCollision(bg1x, bg1y,playerx, playery)
        if colison: #checks if collison      
           game_over_text()
           running = False
        plbir = birdCollision(birdx, birdy,playerx, playery)
        if plbir:           
           game_over_text()
           running= False
    #nice mess of code
    #i am a new coder and i am 12 year old so plz dont say my game badXD
    
    
       

    pygame.display.update()