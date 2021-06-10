from pygame import Color


def Shop(win,textFunc):
    import pygame
    from MenuScreen import MenuScreen as MS

    pygame.init()

    # Draw Circle Function
    def DrawCircle(x,y,color):
        pygame.draw.rect(win, color, [x,y,50,50])

    # Mouse Click Function
    def MClick(x,y,mouse,color,coins,coins2):
        if x+50 > mouse[0] > x and y+50 > mouse[1] > y:
            if pygame.mouse.get_pressed()[0]:
                if coins <= coins2: 
                    with open("PlayerColor.txt", 'w') as f:
                        f.write(str(color))
                    with open("Coins.txt", 'r') as f:
                        a = f.read()
                        a2 = int(a)

                    with open("Coins.txt", 'w') as f2:
                        f2.write(str(a2 - coins))
                else:
                    textFunc("Not enough Coins", 100,350,30)        

    run = True
    while run:
        # Reading the Coin File
        with open("Coins.txt", 'r') as f:
            Coin = f.read()
            Coins = int(Coin)
        win.fill((0,0,0))
        pygame.draw.rect(win, (255,255,255), [0,450,150,50],3)
        textFunc("Return",20,460,20)
        textFunc(f"Coins: {Coins}",0,0,30) 
        # Drawing all the Circles
        DrawCircle(100,150,(255,150,0))
        textFunc("100",106,163,15)
        DrawCircle(400,150,(0,0,255))
        textFunc("200",406,163,15)
        DrawCircle(100,300,(50,50,50))
        textFunc("300",106,313,15)
        DrawCircle(400,300,(0,255,255))
        textFunc("400",406,313,15)
        pygame.display.update()
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
        if 0+150 > mouse[0] > 0 and 450+50 > mouse[1] > 450:
            if pygame.mouse.get_pressed()[0]:
                MS(win, textFunc)
        MClick(100,150,mouse,(255,150,0),100,Coins)       
        MClick(400,150,mouse,(0,0,255),200,Coins)   
        MClick(100,300,mouse,(50,50,50),300,Coins)   
        MClick(400,300,mouse,(0,255,255),400,Coins)   
