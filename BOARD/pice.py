class Piece:
    def __init__(self, color):
        self.color = color  # "red", "purple", "gray"
        self.position = None

    def __str__(self):
        return self.color[0].upper()
