import pygame as pg

pg.init()

#loading graphics
#images
btn=pg.image.load('graphics/buttons/btn.png')
bar=pg.image.load('graphics/bars/bar.png')
#fonts

#sounds



def mainGame():
    screen= pg.display.set_mode((1200,600))
    pg.display.set_caption("dice&dots")
    on=True
    while on:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                on=False
        
        screen.fill("white")

        screen.blit(bar,(120,111))
        for i in range(120,720,120):
            for j in range(120,600,120):
                btn_rct=btn.get_rect(center=(i,j))
                screen.blit(btn,btn_rct)
        pg.display.update()

def boxCheck():
    pass

def turns():
    pass

def winCheck():
    pass


if __name__=='__main__':
    mainGame()