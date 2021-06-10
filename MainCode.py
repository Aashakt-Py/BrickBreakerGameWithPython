# Importing the modules
import pygame
from random import choice
from MenuScreen import MenuScreen as MS

# Intializing pygame
pygame.init()

# Making the Window
HEIGHT = 500
WIDTH = 500
WIN = pygame.display.set_mode((HEIGHT,WIDTH))
pygame.display.set_caption("Brick Breaker By Aashakt")
logo = pygame.image.load("logo.png")
pygame.display.set_icon(logo)

# Some Variables
HitCount = 0

# Making the Brick Class
class Brick:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def Draw(self):
        self.Brick = pygame.draw.rect(WIN,(200,0,255),[self.x,self.y,95,95])           
    def Collision(self,rect,vel):        
        global HitCount
        if rect.colliderect(self.Brick):
            global vel_y
            self.x = 600
            self.y = 600  
            HitCount += 1
            a = open("Coins.txt" ,'r')
            Coins2 = a.read()
            Coins3 = int(Coins2)
            a.close()
            with open("Coins.txt", 'w') as f:
                Coins4 = Coins3 + 1
                f.write(str(Coins4))
            vel_y = abs(vel_y)

def Text(msg,x,y,size):
    font = pygame.font.SysFont("minecraftia20", size, True)
    SurfaceText = font.render(msg, True, (255,255,255))
    WIN.blit(SurfaceText, (x,y))
    
# Main Function
def Main():
    # Gloabling everything
    global vel_y
    global HitCount
    # Some Variables
    run = True
    HitCount = 0
    Player_x = 280
    Player_y = 350
    X_Pos = 225
    vel_x = 0
    X_List = [1,2]
    LoseCheck = False
    # Reading the Velocity File    
    with open("VelocityFile.txt" , 'r') as f:
        VelOcity = f.read()
        vel_y = float(VelOcity)
    # Instanciating the Brick Class
    B1 = Brick(0,0)
    B2 = Brick(100,0)
    B3 = Brick(200,0)
    B4 = Brick(300,0)
    B5 = Brick(400,0)
    B6 = Brick(0,100)
    B7 = Brick(100,100)
    B8 = Brick(200,100)
    B9 = Brick(300,100)
    B10 = Brick(400,100)
    B11 = Brick(0,200)
    B12 = Brick(100,200)
    B13 = Brick(200,200)
    B14 = Brick(300,200)
    B15 = Brick(400,200)
    while run: 
        # Reading the Coin File
        with open("Coins.txt" , 'r') as f:
            Coin = f.read()
            Coins = int(Coin)
        # Reading the Player Color File
        with open("PlayerColor.txt", "r") as f:
            Color1 = f.read()
            PlayerColor = eval(Color1)
        WIN.fill((0,0,0))
        # Making the Striker
        Striker = pygame.draw.rect(WIN, (0,255,0), [X_Pos,450,125,20])
        # Making the Player
        Player = pygame.draw.circle(WIN, PlayerColor, [int(Player_x), int(Player_y)],10)     
        Player_y += vel_y
        Player_x  += vel_x
        # Draw Function
        B1.Draw()
        B2.Draw()
        B3.Draw()
        B4.Draw()
        B5.Draw()
        B6.Draw()
        B7.Draw()
        B8.Draw()
        B9.Draw()
        B10.Draw()
        B11.Draw()
        B12.Draw()
        B13.Draw()
        B14.Draw()
        B15.Draw()
        Text(f"Bricks Destroyed: {HitCount}", 0, 470, 20)
        Text(f"Coins: {Coins}", 370, 470,20)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()          

        B1.Collision(Player,vel_y)    
        B2.Collision(Player,vel_y) 
        B3.Collision(Player,vel_y) 
        B4.Collision(Player,vel_y) 
        B5.Collision(Player,vel_y) 
        B6.Collision(Player,vel_y) 
        B7.Collision(Player,vel_y) 
        B8.Collision(Player,vel_y) 
        B9.Collision(Player,vel_y) 
        B10.Collision(Player,vel_y) 
        B11.Collision(Player,vel_y) 
        B12.Collision(Player,vel_y) 
        B13.Collision(Player,vel_y) 
        B14.Collision(Player,vel_y) 
        B15.Collision(Player,vel_y) 

        # Key Presses for the Striker
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and X_Pos < 375:
            X_Pos += 0.5
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and X_Pos > 0:
            X_Pos -= 0.5   

        # Adding Collisions
        if Striker.colliderect(Player):  
            vel_y = -abs(vel_y)  
            HitVel = choice(X_List)
            if HitVel == 1:
                vel_x = 0.3
            if HitVel == 2:
                vel_x = -0.3   
        if Player_x > 470:
            vel_x = -0.3
        if Player_x < 0:
            vel_x = 0.3 
        if Player_y < 0:
            vel_y = abs(vel_y)
        if Player_y > 450:
            LoseCheck = True
        # Win or Lose
        if HitCount >= 15:
            Win()     
        if LoseCheck:
            Lose()                

def Win():
    run2 = True
    while run2:
        WIN.fill((0,0,0))
        Text("You Win!!", 10,200,70)
        Text("_________",10,280,70)
        Text("Title Screen",160,410,20)
        pygame.draw.rect(WIN, (255,255,255), [150,400,200,50],3)
        pygame.display.update()
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run2 = False
                pygame.quit()
                quit()
        if 150+150 > mouse[0] > 150 and 50+400 > mouse[1] > 400:
            if pygame.mouse.get_pressed()[0]:
                MS(WIN, Text)                

def Lose():
    run2 = True
    while run2:
        WIN.fill((0,0,0))
        Text("You Lose!!", 10,200,70)
        Text("_________",10,280,70)
        Text("Title Screen",160,410,20)
        pygame.draw.rect(WIN, (255,255,255), [150,400,200,50],3)
        pygame.display.update()
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run2 = False
                pygame.quit()
                quit()
        if 150+150 > mouse[0] > 150 and 50+400 > mouse[1] > 400:
            if pygame.mouse.get_pressed()[0]:
                MS(WIN, Text)

MS(WIN, Text)                