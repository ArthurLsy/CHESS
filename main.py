import pygame as py
from pygame.locals import *
import sys

liste_pieces = ["Roi", "Dame", "Fou", "Cavalier", "Tour", "Pion"]

class chessboard:

    def __init__(self):

        self.board = []
        self.piece_priseB = []
        self.piece_priseN = []

#Fonction qui permet de créer un plateau vide

    def clear(self):
        self.board = []
        for i in range(8):
            self.board.append([])
            for j in range(8):
                self.board[i].append([])
    
#Fonction pour placer les pièces sur le plateau

    def placement_piece(self):
        self.board[7][4].append(liste_pieces[0])
        self.board[0][4].append(liste_pieces[0])
        self.board[7][3].append(liste_pieces[1])
        self.board[0][3].append(liste_pieces[1])
        self.board[0][2].append(liste_pieces[2])
        self.board[0][5].append(liste_pieces[2])
        self.board[7][2].append(liste_pieces[2])
        self.board[7][5].append(liste_pieces[2])
        self.board[7][6].append(liste_pieces[3])
        self.board[7][1].append(liste_pieces[3])
        self.board[0][6].append(liste_pieces[3])
        self.board[0][1].append(liste_pieces[3])
        self.board[0][7].append(liste_pieces[4])
        self.board[0][0].append(liste_pieces[4])
        self.board[7][7].append(liste_pieces[4])
        self.board[7][0].append(liste_pieces[4])
        for i in range(len(self.board)):
            self.board[6][i].append(liste_pieces[5])
            self.board[1][i].append(liste_pieces[5])
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if i == 7 : 
                    self.board[i][j].append("B")
                if i == 6 : 
                    self.board[i][j].append("B")
                if i == 0 : 
                    self.board[i][j].append("N")
                if i == 1 : 
                    self.board[i][j].append("N")
                
#Fonction qui gère le déplacement des pièces

    def move(self, x, y, x1, y1):
        temp = []
        piece = self.board[x][y][0]
        if piece == liste_pieces[0]:
            if self.move_roi(x, y, x1, y1) == True:         
                self.board[x1][y1].append(self.board[x][y].pop(0))
                self.board[x1][y1].append(self.board[x][y].pop(0))
        if piece == liste_pieces[1]:
            if self.move_dame(x, y, x1, y1) == True:         
                self.board[x1][y1].append(self.board[x][y].pop(0))
                self.board[x1][y1].append(self.board[x][y].pop(0))
        if piece == liste_pieces[2]:
            if self.move_fou(x, y, x1, y1) == True:         
                self.board[x1][y1].append(self.board[x][y].pop(0))
                self.board[x1][y1].append(self.board[x][y].pop(0))
        if piece == liste_pieces[3]:
            if self.move_cavalier(x, y, x1, y1) == True:         
                self.board[x1][y1].append(self.board[x][y].pop(0))
                self.board[x1][y1].append(self.board[x][y].pop(0))
        if piece == liste_pieces[4]:
            if self.move_tour(x, y, x1, y1) == True:         
                self.board[x1][y1].append(self.board[x][y].pop(0))
                self.board[x1][y1].append(self.board[x][y].pop(0))
        if piece == liste_pieces[5]:
            if self.move_pion(x, y, x1, y1) == True:         
                self.board[x1][y1].append(self.board[x][y].pop(0))
                self.board[x1][y1].append(self.board[x][y].pop(0))

#Fonction pour gérer les conditions pour le déplacement et la prise de pièce

    def move_roi(self, x, y, x1, y1):
        if self.board[x1][y1] != [] :
            if self.board[x1][y1][1]=='B'and self.board[x][y][1]=='N':
                self.piece_priseB.append(self.board[x1][y1])
                self.board[x1][y1]=[]
            elif self.board[x1][y1][1]=='N'and self.board[x][y][1]=='B':
                self.piece_priseN.append(self.board[x1][y1])
                self.board[x1][y1]=[]
            elif self.board[x1][y1][1] == self.board[x][y][1]:
                print("Place occupée")
                return False
        if abs(x - x1) == 1 :
            if abs(y - y1) == 1  or abs(y - y1) == 0:
                return True
        if abs(y - y1) == 1 :
            if abs(x - x1) == 1  or abs(x - x1) == 0:
                return True
        print('Mouvement impossible')
        return False

    def move_dame(self, x, y, x1, y1):
        if self.board[x1][y1] != [] :
            if self.board[x1][y1][1]=='B'and self.board[x][y][1]=='N':
                self.piece_priseB.append(self.board[x1][y1])
                self.board[x1][y1]=[]
            elif self.board[x1][y1][1]=='N'and self.board[x][y][1]=='B':
                self.piece_priseN.append(self.board[x1][y1])
                self.board[x1][y1]=[]
            elif self.board[x1][y1][1] == self.board[x][y][1]:
                print("Place occupée")
                return False
        if abs(x1 - x) != 0 and abs(y1 - y) == 0 :
            if x < x1 : 
                min = x
                max = x1
            else :
                min = x1
                max = x
            for i in range(min+1,max):
                if self.board[i][y] != [] :
                    print('Il y a un pièce sur le chemin')
                    return False
            return True
        if abs(y1 - y) != 0 and abs(x1 - x) == 0 :
            if y < y1 : 
                min = y
                max = y1
            else :
                min = y1
                max = y
            for i in range(min+1,max):
                if self.board[x][i] != [] :
                    print('Il y a un pièce sur le chemin')
                    return False
            return True
        if abs(x1 - x) == abs(y1 - y) :
            if x > x1 and y > y1 :
                Xmax = x
                Xmin = x1
                Ymax = y
                Ymin = y1
                for i in range(Xmin+1,Xmax):
                    for j in range(Ymin,Ymax):
                        if self.board[i][j] != [] :
                            print('Il y a un pièce sur le chemin')
                            return False
            if x > x1 and y < y1 :
                Xmax = x
                Xmin = x1 
                Ymax = y1
                Ymin = y
                for i in range(Xmin+1,Xmax):
                    for j in range(Ymin,Ymax):
                        if self.board[i][j] != [] :
                            print('Il y a un pièce sur le chemin')
                            return False
            if x < x1 and y > y1 :
                Xmax = x1
                Xmin = x
                Ymax = y
                Ymin = y1
                for i in range(Xmin+1,Xmax):
                    for j in range(Ymin,Ymax):
                        if self.board[i][j] != [] :
                            print('Il y a un pièce sur le chemin')
                            return False
            if x < x1 and y < y1 :
                Xmax = x1
                Xmin = x 
                Ymax = y1
                Ymin = y
                for i in range(Xmin+1,Xmax):
                    for j in range(Ymin,Ymax):
                        if self.board[i][j] != [] :
                            print('Il y a un pièce sur le chemin')
                            return False
            return True
        print('Mouvement impossible')
        return False

    def move_fou(self, x, y, x1, y1):
        if self.board[x1][y1] != [] :
            if self.board[x1][y1][1]=='B'and self.board[x][y][1]=='N':
                self.piece_priseB.append(self.board[x1][y1])
                self.board[x1][y1]=[]
            elif self.board[x1][y1][1]=='N'and self.board[x][y][1]=='B':
                self.piece_priseN.append(self.board[x1][y1])
                self.board[x1][y1]=[]
            elif self.board[x1][y1][1] == self.board[x][y][1]:
                print("Place occupée")
                return False
        if abs(x1 - x) == abs(y1 - y) :
            if x > x1 and y > y1 :
                Xmax = x
                Xmin = x1
                Ymax = y
                Ymin = y1
                for i in range(Xmin+1,Xmax):
                    for j in range(Ymin,Ymax):
                        if self.board[i][j] != [] :
                            print('Il y a un pièce sur le chemin')
                            return False
            if x > x1 and y < y1 :
                Xmax = x
                Xmin = x1 
                Ymax = y1
                Ymin = y
                for i in range(Xmin+1,Xmax):
                    for j in range(Ymin,Ymax):
                        if self.board[i][j] != [] :
                            print('Il y a un pièce sur le chemin')
                            return False
            if x < x1 and y > y1 :
                Xmax = x1
                Xmin = x
                Ymax = y
                Ymin = y1
                for i in range(Xmin+1,Xmax):
                    for j in range(Ymin,Ymax):
                        if self.board[i][j] != [] :
                            print('Il y a un pièce sur le chemin')
                            return False
            if x < x1 and y < y1 :
                Xmax = x1
                Xmin = x 
                Ymax = y1
                Ymin = y
                for i in range(Xmin+1,Xmax):
                    for j in range(Ymin,Ymax):
                        if self.board[i][j] != [] :
                            print('Il y a un pièce sur le chemin')
                            return False
            return True
        print('Mouvement impossible')
        return False

    def move_cavalier(self, x, y, x1, y1):
        if self.board[x1][y1] != [] :
            if self.board[x1][y1][1]=='B'and self.board[x][y][1]=='N':
                self.piece_priseB.append(self.board[x1][y1])
                self.board[x1][y1]=[]
            elif self.board[x1][y1][1]=='N'and self.board[x][y][1]=='B':
                self.piece_priseN.append(self.board[x1][y1])
                self.board[x1][y1]=[]
            elif self.board[x1][y1][1] == self.board[x][y][1]:
                print("Place occupée")
                return False
        if abs(x1-x) == 1 and abs(y1-y) == 2 :
            return True
        if abs(x1-x) == 2 and abs(y1-y) == 1 :
            return True
        print('Mouvement impossible')
        return False

    def move_tour(self, x, y, x1, y1):
        if self.board[x1][y1] != [] :
            if self.board[x1][y1][1]=='B'and self.board[x][y][1]=='N':
                self.piece_priseB.append(self.board[x1][y1])
                self.board[x1][y1]=[]
            elif self.board[x1][y1][1]=='N'and self.board[x][y][1]=='B':
                self.piece_priseN.append(self.board[x1][y1])
                self.board[x1][y1]=[]
            elif self.board[x1][y1][1] == self.board[x][y][1]:
                print("Place occupée")
                return False
        if abs(x1 - x) != 0 and abs(y1 - y) == 0 :
            if x < x1 : 
                min = x
                max = x1
            else :
                min = x1
                max = x
            for i in range(min+1,max):
                if self.board[i][y] != [] :
                    print('Il y a un pièce sur le chemin')
                    return False
            return True
        if abs(y1 - y) != 0 and abs(x1 - x) == 0 :
            if y < y1 : 
                min = y
                max = y1
            else :
                min = y1
                max = y
            for i in range(min+1,max):
                if self.board[x][i] != [] :
                    print('Il y a un pièce sur le chemin')
                    return False
            return True
        print('Mouvement impossible')
        return False

    def move_pion(self, x, y, x1, y1):
        if y==y1 and self.board[x1][y1] != [] :
            print("Place occupée")
            return False
        if y!=y1 and self.board[x1][y1] != [] :
            if self.board[x][y][1] == 'N' and x1-x==1 and self.board[x1][y1][1] == 'B':
                if y1==y+1 or y1==y-1:
                    self.piece_priseB.append(self.board[x1][y1])
                    self.board[x1][y1]=[]
                    return True
            if self.board[x][y][1] == 'B' and x-x1==1 and self.board[x1][y1][1] == 'N':
                if y1==y+1 or y1==y-1:
                    self.piece_priseN.append(self.board[x1][y1])
                    self.board[x1][y1]=[]
                    return True
        if abs(y1-y) != 0 :
            print('Mouvement impossible')
            return False
        if self.board[x][y][1] == 'B' and x == 6 and x-x1 == 2 :
            if self.board[x-1][y] != [] :
                print('Il y a un pièce sur le chemin')
                return False
            return True
        if self.board[x][y][1] == 'N' and x == 1 and x1-x == 2 :
            if self.board[x+1][y] != [] :
                print('Il y a un pièce sur le chemin')
                return False
            return True
        if self.board[x][y][1] == 'B' and x-x1 == 1 :
            return True
        if self.board[x][y][1] == 'N' and x1-x == 1 :
            return True
        print('Mouvement impossible')
        return False

#initialisation du jeu

jeu = chessboard()
jeu.clear()
jeu.placement_piece()

#Initialisation de Pygame (non terminée)

py.init()
Blanc = (255,255,255)
Noir = (0,0,0)
Size = 100
ecran = py.display.set_mode((Size*8,Size*8))

RoiBlanc = py.image.load('sprite/RB.png').convert_alpha()
RoiBlanc = py.transform.scale(RoiBlanc,(100,100))

running = True
while running:
    for event in py.event.get():
        if event.type == QUIT:
            running = False
    ecran.fill((150,150,150))
    for i in range(8):
        for j in range(8):
            if j%2==0:
                if i%2==0:
                    py.draw.rect(ecran, Blanc, Rect(i*Size, j*Size, Size, Size))
                else :
                    py.draw.rect(ecran, Noir, Rect(i*Size, j*Size, Size, Size))
            if j%2==1:
                if i%2==1:
                    py.draw.rect(ecran, Blanc, Rect(i*Size, j*Size, Size, Size))
                else :
                    py.draw.rect(ecran, Noir, Rect(i*Size, j*Size, Size, Size))
    for i in range(8):
        for j in range(8):
            if jeu.board[i][j] != [] :
                if jeu.board[i][j][0] == 'Roi':
                    if jeu.board[i][j][1] == 'B':
                        ecran.blit(RoiBlanc,(j*100,i*100))

    if event.type == py.MOUSEBUTTONDOWN and event.button == 1:
                    posx = event.pos[0]/100-(event.pos[0]%100)/100
                    posy = event.pos[1]/100-(event.pos[1]%100)/100
                     
    py.display.flip()

py.quit()