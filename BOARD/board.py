

from BOARD.pice import Piece
from BOARD.place import Place

# row =5
# colom =5
# step=-1
# range_step=2




class Board:
    def __init__(self,grid,row,colom,range_step):
        self.grid = grid
        self.colom=colom
        self.size = row
        self.range_step = range_step


    def swap_piece(self,x1,y1, piece, new_x, new_y):
            self.grid[x1][y1].piece = None
            self.grid[new_x][new_y].piece = piece
            piece.position = (new_x, new_y)
            if(piece.color=='purple'):
                for i in range(self.size):
                    place = self.grid[i][new_y]
                    if place:
                        if isinstance(place.piece, Piece) :
                            if(i>new_x):
                                if( i<(self.size-1)):
                                    if(self.grid[i+1][new_y].piece==None):
                                        self.swap_auto_piece(i,new_y,place.piece, (i+1),new_y )
                            if(i<new_x):
                                if(i>0):
                                    if(self.grid[i-1][new_y].piece==None):
                                        self.swap_auto_piece(i,new_y,place.piece, (i-1),new_y )

                for j in range(self.colom):
                    place = self.grid[new_x][j]
                    if place:
                        if isinstance(place.piece, Piece) :
                            if(j>new_y):
                                if( j<(self.colom-1)):
                                    if(self.grid[new_x][j+1].piece==None):
                                        self.swap_auto_piece(new_x,j,place.piece, new_x,j+1 )
                                        break
                            if(j<new_y):
                                if(j>0):
                                    if(self.grid[new_x][j-1].piece==None):
                                        self.swap_auto_piece(new_x,j,place.piece, new_x,j-1 )

            else:
                for i in range(self.size):
                    place = self.grid[i][new_y]
                    if place:
                        if isinstance(place.piece, Piece) :
                            if(i<(new_x)):
                                # if( i<(self.size-1)):
                                    if(self.grid[i+1][new_y].piece==None):
                                        self.swap_auto_piece(i,new_y,place.piece, (i+1),new_y )
                            if(i>(new_x)):
                                # if(i>0):
                                    if(self.grid[i-1][new_y].piece==None):
                                        self.swap_auto_piece(i,new_y,place.piece, (i-1),new_y )

                for j in range(self.colom):
                    place = self.grid[new_x][j]
                    if place:
                        if isinstance(place.piece, Piece) :
                            if(j<new_y):
                                # if( j<(colom-1)):
                                    if(self.grid[new_x][j+1].piece==None):
                                        self.swap_auto_piece(new_x,j,place.piece, new_x,j+1 )
                            if(j>new_y):
                                # if(j>0):
                                    if(self.grid[new_x][j-1].piece==None):
                                        self.swap_auto_piece(new_x,j,place.piece, new_x,j-1 )

    def swap_auto_piece(self,x1,y1, piece, new_x, new_y):
            self.grid[x1][y1].piece = None
            self.grid[new_x][new_y].piece = piece
            piece.position = (new_x, new_y)


    def is_solved(self):
        for i in range(self.size):
            for j in range(self.colom):
                place = self.grid[i][j]
                if place:
                    if isinstance(place.piece, Piece) :
                        if(place.text !='w'):
                            return False
        return True
