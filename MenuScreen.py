def MenuScreen(win,textFunc):
    import pygame
    from tkinter import Tk
    from tkinter import IntVar
    from tkinter import Radiobutton
    from tkinter import Button
    from MainCode import Main as MA
    from Shop import Shop as SH
    run3 = True
    def TkWindow():
        def setVal():
            if Var1.get() == 1:
                f = open("VelocityFile.txt", 'w')
                f.write("0.5")
                f.close()
            if Var1.get() == 2:
                f = open("VelocityFile.txt", 'w')
                f.write("0.9")
                f.close()
            if Var1.get() == 3:
                f = open("VelocityFile.txt", 'w')
                f.write("1.3")             
                f.close()
        root = Tk()
        root.geometry("50x110")
        root.maxsize(50,110)
        root.minsize(50,110)
        Var1 = IntVar()
        C1 = Radiobutton(root, text=": Easy", variable=Var1,value=1).grid(row=0, column=1)
        C2 = Radiobutton(root, text=": Medium", variable=Var1,value=2).grid(row=1, column=1)
        C3 = Radiobutton(root, text=": Hard", variable=Var1,value=3).grid(row=2, column=1)
        B1 = Button(root, text="Submit", command=setVal).grid(row=3,column=1)
        root.mainloop()
    while run3:
        win.fill((0,0,0))
        textFunc("Brick Breaker Game",20,30,35)
        pygame.draw.rect(win, (255,255,255), [175,175,150,50],2)
        textFunc("Difficulty", 185,185,20)
        pygame.draw.rect(win, (255,255,255), [175,245,150,50],2)
        pygame.draw.rect(win, (255,255,255), [0,0,500,500],8)
        textFunc("Start", 215,255,20)
        pygame.draw.rect(win, (255,255,255), [175,315,150,50],2)
        textFunc("Shop", 220,325,20)
        pygame.display.update()
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run3 = False
                pygame.quit()
                quit()  
        if 175+150 > mouse[0] > 175 and 245+50 > mouse[1] > 245:
            if pygame.mouse.get_pressed()[0]:
                MA()  
        if 175+150 > mouse[0] > 175 and 175+50 > mouse[1] > 175:
            if pygame.mouse.get_pressed()[0]:
                TkWindow() 
        if 175+150 > mouse[0] > 175 and 315+50 > mouse[1] > 315:
            if pygame.mouse.get_pressed()[0]:
                SH(win,textFunc)                            