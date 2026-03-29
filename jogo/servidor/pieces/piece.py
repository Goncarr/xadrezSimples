class Piece:
    def __init__(self, piece:str, current_pos:str):
        self.current_pos: str = current_pos
        self.available_moves:list = []
        self.piece:str = piece
        self.alive = True