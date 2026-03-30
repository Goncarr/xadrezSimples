from servidor.pieces.piece import Piece
import servidor
class Pawn(Piece):
    def __init__(self,piece:str, current_pos):
        super().__init__(piece,current_pos)
        self.number_of_turns = 0
        self.direction = 0

    def check_available_moves(self,board:list[list]):
        """
        Se turno = 0, move 1 ou 2, adiciona a available
        Se turno > 0, move 1, adiciona available
        Se tem peça nesses espaços, remove espaço do available
        Se peça na diagonal, adiciona a available
        """
        self.available_moves = []
        current_x = self.current_pos[0]
        current_y = int(self.current_pos[1])
        self.available_moves.append([current_x, current_y + 1])
        if self.number_of_turns == 0:
            self.available_moves.append([current_x, current_y + 2])
        for square in self.available_moves:
            if board[8 - square[1]][servidor.col_map[square[0]]] != "  ":
                self.available_moves.remove(square)


    def move(self, piece: Piece, move_requested:str, board:list):
        current_x, current_y = servidor.col_map[self.current_pos[0]], 8 - int(self.current_pos[1])
        move_x, move_y = move_requested[0], int(move_requested[1])
        print(self.available_moves)
        move = [move_x, move_y]
        print(move)
        if move in self.available_moves:
            print("Move in dict")
            move[0] = servidor.col_map[move[0]]
            print(move)
            board[current_y][current_x] = "  "
            board[8 - move[1]][move[0]] = piece
            self.current_pos = move_requested
            self.number_of_turns += 1