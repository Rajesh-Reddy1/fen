import pygame as p
import fen
import os
g=fen.game()
p.init()
p.display.set_caption('CHESS')
Width = 800
Height = Width
screen = p.display.set_mode((Width,Height))

class chessboard():

    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.dim = 8
        self.size = self.height // self.dim
        self.images = {}

    def loadImages(self):
        pieces = ['r','n','b','k','q','p','P','R','N','B','K','Q']
        for piece in pieces:
            
            self.images[piece] = p.transform.scale(p.image.load(os.path.normcase('IMAGES/'+piece+'.png')),(self.size,self.size))

    def drawImages(self):
        for r in range(self.dim):
            for c in range(self.dim):
                piece = g.board[r][c]
                if piece != '-':
                    screen.blit(self.images[piece],p.Rect(c*self.size,r*self.size,self.size,self.size))
    
    def drawingboard(self):
        colors = [p.Color('pink'),p.Color('gray')]
        screen.fill(p.Color("dark green"))

        for r in range(self.dim):
            for c in range(self.dim):
                color = colors[(r+c)%2]
                p.draw.rect(screen,color,p.Rect(r*self.size,c*self.size,self.size,self.size))

    def main(self): 
        chessboard.loadImages(self)
        clock = p.time.Clock()
        done = False
        Sqselected = ()
        PlayerClicks = []
        global movemade
        movemade = False
        

        while not done:  
            for event in p.event.get():

                if event.type == p.QUIT:  
                    done = True

            clock.tick(15)
            chessboard.drawingboard(self)
            chessboard.drawImages(self)
            p.display.flip()

q=chessboard(Width,Height)
q.main()