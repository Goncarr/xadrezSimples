class Piece:
    def __init__(self, piece:str, current_pos:list):
        self.current_pos: list = current_pos
        self.available_moves:list = []
        self.piece:str = piece
        self.alive = True