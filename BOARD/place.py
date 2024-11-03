
class Place:
    def __init__(self, piece,text):
        self.piece = piece
        self.text = text  # "W", none"
        self.position = None

    def __str__(self):
        return  self.text[0].upper() if isinstance( self.text, str) else ""
