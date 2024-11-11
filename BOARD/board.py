

from BOARD.pice import Piece
from BOARD.place import Place
import copy
from queue import deque
# step=-1
# range_step=2


class Board:
    def __init__(self,grid,row,colom,range_step):
        self.grid = grid
        self.colom=colom
        self.size = row
        self.range_step = range_step


    def move_piece(self,x1,y1, piece, new_x, new_y,gr1):
            grid=copy.deepcopy(gr1)
            grid[x1][y1].piece = None
            grid[new_x][new_y].piece = piece
            piece.position = (new_x, new_y)
            if(piece.color=='purple'):
                for i in range(self.size):
                    place = grid[i][new_y]
                    if place:
                        if isinstance(place.piece, Piece) :
                            if(i>new_x):
                                if( i<(self.size-1)):
                                    if(grid[i+1][new_y].piece==None):
                                        self.move_auto_piece(i,new_y,place.piece, (i+1),new_y ,grid)
                            if(i<new_x):
                                if(i>0):
                                    if(grid[i-1][new_y].piece==None):
                                        self.move_auto_piece(i,new_y,place.piece, (i-1),new_y,grid )

                for j in range(self.colom):
                    place = grid[new_x][j]
                    if place:
                        if isinstance(place.piece, Piece) :
                            if(j>new_y):
                                if( j<(self.colom-1)):
                                    if(grid[new_x][j+1].piece==None):
                                        self.move_auto_piece(new_x,j,place.piece, new_x,j+1,grid )
                                        break
                            if(j<new_y):
                                if(j>0):
                                    if(grid[new_x][j-1].piece==None):
                                        self.move_auto_piece(new_x,j,place.piece, new_x,j-1 ,grid)

            else:
                for i in range(self.size):
                    place = grid[i][new_y]
                    if place:
                        if isinstance(place.piece, Piece) :
                            if(i<(new_x)):
                                # if( i<(self.size-1)):
                                    if(grid[i+1][new_y].piece==None):
                                        self.move_auto_piece(i,new_y,place.piece, (i+1),new_y ,grid)
                            if(i>(new_x)):
                                # if(i>0):
                                    if(grid[i-1][new_y].piece==None):
                                        self.move_auto_piece(i,new_y,place.piece, (i-1),new_y ,grid)

                for j in range(self.colom):
                    place = grid[new_x][j]
                    if place:
                        if isinstance(place.piece, Piece) :
                            if(j<new_y):
                                # if( j<(colom-1)):
                                    if(grid[new_x][j+1].piece==None):
                                        self.move_auto_piece(new_x,j,place.piece, new_x,j+1,grid )
                            if(j>new_y):
                                # if(j>0):
                                    if(grid[new_x][j-1].piece==None):
                                        self.move_auto_piece(new_x,j,place.piece, new_x,j-1,grid )
            self.is_solved(grid)
            return grid

    def move_auto_piece(self,x1,y1, piece, new_x, new_y,grid):
            grid[x1][y1].piece = None
            grid[new_x][new_y].piece = piece
            piece.position = (new_x, new_y)


    def is_solved(self,grid):
        # item =self.history_queue.get
        # print(item)
        for i in range(self.size):
            for j in range(self.colom):
                place = grid[i][j]
                if place:
                    if(place.text =='w'):
                        if place.piece is None :
                            return False
        return True

    def is_solvedAlgori(self,path,piece,grid):
        # print(path)
        temp=path[0]
        for item in path:
            (x1,y1)=temp
            (new_x,new_y)=item
            self.grid=self.move_piece(x1,y1,piece,new_x,new_y,grid)
            temp=item

        if self.is_solved(grid)==False:
            print('w4etrythrgef')
            grid[new_x][new_y].piece = None
        else:
            for item in path:
                    (x1,y1)=temp
                    (new_x,new_y)=item
                    self.grid= self.move_piece(x1,y1,piece,new_x,new_y,self.grid)
                    temp=item
        return self.is_solved(grid)

    def get_neighbors(self,node):
        (row,col)=node
        neighbors=[]
        for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            new_row,new_col=row+dr,col+dc
            if 0<=new_row<self.size and 0<=new_col<(self.colom-1):
                neighbors.append((new_row,new_col))
        # print(neighbors)
        return neighbors
    

    def bfs_solve(self):
        queue = []
        visited=[]
        pieces=[]
        piece=self.returnMagnets()
        for place in piece:
            queue.append(place.position)
            visited.append(place.position)
            pieces.append(place.piece)
            start=place

        grid=copy.deepcopy(self.grid)
        parent={start.position:None}
        print(parent)
        queueGrid = [self.grid]
        visitedGird =[self.grid]
        while queueGrid:
            node=queue.pop(0)
            grid=queueGrid.pop(0)
            nodde=node
            path=[]
            for nodde in parent:
                path.append(nodde)
                print(parent)
            print(path[::-1])

            if self.is_solvedAlgori(path[::-1],pieces[0],grid):
                    return path[::-1]

            for neighbors in self.get_neighbors(node):
                (x1,y1)=node
                (new_x,new_y)=neighbors
                gridNew=(self.move_piece(x1,y1,pieces[0],new_x,new_y,self.grid))

                if (gridNew not in visitedGird):
                    queueGrid.append(gridNew)
                    visitedGird.append(gridNew)
                    queue.append(neighbors)
                    visited.append(neighbors)
                    parent[neighbors]=node
        return None
    
    def dfs_solve(self):
        stack = []
        visited=[]
        pieces=[]
        piece=self.returnMagnets()
        for place in piece:
            stack.append(place.position)
            visited.append(place.position)
            pieces.append(place.piece)
            start=place

        grid=copy.deepcopy(self.grid)
        parent={start.position:None}
        print(parent)
        stackGrid = [self.grid]
        visitedGird =[self.grid]
        while stackGrid:
            node=stack.pop()
            grid=stackGrid.pop()
            nodde=node
            path=[]
            for nodde in parent:
                path.append(nodde)
                print(parent)
            print(path[::-1])

            if self.is_solvedAlgori(path[::-1],pieces[0],grid):
                    return path[::-1]

            for neighbors in self.get_neighbors(node):
                (x1,y1)=node
                (new_x,new_y)=neighbors
                gridNew=(self.move_piece(x1,y1,pieces[0],new_x,new_y,self.grid))

                if (gridNew not in visitedGird):
                    stackGrid.append(gridNew)
                    visitedGird.append(gridNew)
                    stack.append(neighbors)
                    visited.append(neighbors)
                    parent[neighbors]=node
        return None
    
    def returnMagnets(self):
        piece=[]
        for i in range(self.size):
            for j in range(self.colom):
                place = self.grid[i][j]
                if place:
                    if isinstance(place.piece, Piece) :
                        if (place.piece.color =='red' or place.piece.color =='purple'):
                            piece.append(place)
        return piece