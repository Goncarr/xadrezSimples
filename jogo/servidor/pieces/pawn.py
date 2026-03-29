from servidor.pieces.piece import Piece
import servidor
class Pawn(Piece):
    def __init__(self,piece:str, current_pos):
        super().__init__(piece,current_pos)
        self.number_of_turns = 0

    def check_available_moves(self,board:list[list]):
        """
        Se turno = 0, move 1 ou 2, adiciona a available
        Se turno > 0, move 1, adiciona available
        Se tem peça nesses espaços, remove espaço do available
        Se peça na diagonal, adiciona a available
        """
        self.available_moves = []
        current_x, current_y = servidor.col_map(self.current_pos[0]), int(self.current_pos[1])
        if self.number_of_turns == 0:
            self.available_moves.append([current_x, current_y + 1])
            self.available_moves.append([current_x, current_y + 2])
        else:
            self.available_moves.append([current_x, current_y + 1])
        print(self.available_moves)


    def move_pawn(self,move:list, board:list[list[str,str]]):
        if move in self.available_moves:
            board[self.current_pos[0]][self.current_pos[1]] = "  "
            board[move[0]][move[1]] = self.piece
            self.current_pos = move

