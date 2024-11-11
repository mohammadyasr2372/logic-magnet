from logging import root
import tkinter as tk
from tkinter import messagebox

from BOARD.board import Board
# from BOARD.board import final_board
# from BOARD.board import path
from BOARD.pice import Piece
from BOARD.place import Place
step=-1
idboard=0

grid1=[
        [Place(None,None ), Place(None,None), Place(None,'w'), Place(None,None), Place(None,None)],
        [Place(None,None), Place(None,None),Place(Piece('gray'),None), Place(None,None), Place(None,None)],
        [Place(None,'w'), Place(Piece('gray'),None), Place(None,'w'),Place(Piece('gray'),None), Place(None,'w')],
        [Place(None,None), Place(None,None),Place(Piece('gray'),None), Place(None,None), Place(None,None)],
        [Place(Piece('purple'),None),Place(None,None), Place(None,'w'), Place(None,None),Place(None,None)]
        ]

grid2=[
        [Place(None,None ), Place(None,None),  Place(None,None), Place(None,'w'),Place(None,'w')],
        [Place(None,None), Place(None,None),Place(Piece('gray'),None), Place(None,None), Place(None,None)],
        [Place(Piece('red'),None), Place(None,None),  Place(None,None),Place(None,None),Place(Piece('purple'),None)],
        [Place(None,None), Place(None,None),Place(Piece('gray'),None), Place(None,None), Place(None,None)],
        [Place(None,'w'),Place(None,None),  Place(None,None),Place(None,'w'),Place(None,None)]
        ]

grid3=[
        [Place(None,None ), Place(None,None), Place(None,None),Place(None,None)],
        [Place(None,None), Place(None,'w'),Place(Piece('gray'),None), Place(None,'w')],
        [Place(Piece('purple'),None), Place(None,None),Place(None,None),  Place(None,None)]
        ]
grid4=[
        [Place(None,None ), Place(None,None), Place(None,None),Place(None,'w')],
        [Place(None,None), Place(None,None),Place(Piece('gray'),None), Place(None,None)],
        [Place(Piece('purple'),None), Place(None,None),Place(None,None),  Place(None,'w')]
        ]

boards=[Board(grid4,3,4,3),Board(grid3,3,4,3),Board(grid1,5,5,3),Board(grid2,5,5,3)]

class MagnetGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Magnets Logic Game")
        self.board = boards[idboard]
        self.selected_piece = None
        self.selected_piece_x = None
        self.selected_piece_y = None
        self.create_steps_display()  
        self.create_board_ui()
        # self.show_step()


    def create_board_ui(self):
        # controls = tk.Frame(self.root)
        tk.Button(self.root, text="Solve Bfs", command=self.solve_game_bfs).grid(row=self.board.size + 2, column=0)
        tk.Button(self.root, text="Solve Dfs", command=self.solve_game_dfs).grid(row=self.board.size + 4, column=0)
        self.board_frame = tk.Frame(self.root)
        self.board_frame.grid(row=0, column=0)
        self.buttons = [[None for _ in range(self.board.colom)] for _ in range(self.board.size)]
        for i in range(self.board.size):
            for j in range(self.board.colom):
                btn = tk.Button(self.board_frame, width=8, height=5, command=lambda i=i, j=j: self.select_piece(i, j))
                btn.grid(row=i, column=j)
                self.board.grid[i][j].position=i,j
                self.buttons[i][j] = btn
        self.update_board_ui()

    def create_steps_display(self):
        self.steps_text = tk.Text(self.root, height=10, width=40)
        self.steps_text.grid(row=self.board.size + 3, column=0)
        self.steps_text.insert(tk.END, "Steps to solution will appear here...\n")

    def update_steps_display(self, steps):
        self.steps_text.delete(1.0, tk.END)
        self.steps_text.insert(tk.END, "Steps to solution:\n")
        for step in steps:
            self.steps_text.insert(tk.END, f"{step}\n")

    def select_piece(self, x, y):
        place = self.board.grid[x][y]
        if isinstance(place.piece, Piece):
            if place.piece.color=="gray":
                print('esdv')
            else:
                self.selected_piece = place.piece
                self.selected_piece_x = x
                self.selected_piece_y = y
        else:
            self.move_selected_piece(self.selected_piece_x, self.selected_piece_y, x,y)
    
    def move_selected_piece(self,x1,y1,x2,y2):
        if self.selected_piece:
            self.board.grid=self.board.move_piece(x1,y1,self.selected_piece, x2, y2,self.board.grid)
            self.update_board_ui()

            if self.board.is_solved(self.board.grid):
                        messagebox.showinfo("Congratulations!", "تم حل اللغز")
                        self.root.quit()
                        step=-1
                        global idboard
                        idboard+=1
                        # root = tk.Tk()
                        game = MagnetGameGUI(self.root)
                        self.root.mainloop()

            self.selected_piece = None
    
    def solve_game_bfs(self):
        path = self.board.bfs_solve()
        if path is not None:
            print(path)
            print("Solution found! Steps to solution:")
            self.update_steps_display(path)
            self.update_board_ui()
        else:
            self.update_steps_display("No solution exists.")
            print("No solution exists.")
    
    def solve_game_dfs(self):
        path = self.board.dfs_solve()
        if path is not None:
            print(path)
            print("Solution found! Steps to solution:")
            self.update_steps_display(path)
            self.update_board_ui()
        else:
            self.update_steps_display("No solution exists.")
            print("No solution exists.")

    def show_step(self):
        controls = tk.Frame(self.root)
        # controls.grid(row=self.board.size + 1, column=0)

        tk.Button(self.root, text="Solve", command=self.solve_game).grid(row=self.board.size + 2, column=0)

    def update_board_ui(self):

        # global step
        # step+=1
        # self.show_step()
        # print(step)
        for i in range(self.board.size):
            for j in range(self.board.colom):
                place = self.board.grid[i][j]
                if place:
                    if isinstance(place.piece, Piece) :
                        color = place.piece.color
                        self.buttons[i][j].config(text=place, bg=color)
                    else:
                        color ='white' if isinstance(place.text, str) else "blue"
                        self.buttons[i][j].config(text=str(place), bg=color)

                else:
                    self.buttons[i][j].config(text="", bg="blue")
