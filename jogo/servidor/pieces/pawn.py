from servidor.pieces.piece import Piece
import servidor
class Pawn(Piece):
    def __init__(self,piece:str, current_pos):
        super().__init__(piece,current_pos)
        self.number_of_turns = 0
        self.direction = 1 if "w" in self.piece else -1
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
        if board[8 - current_y + 1][servidor.letter.index(current_x)] != "  ":
            self.available_moves.append([current_x, current_y + 1 * self.direction])
            if self.number_of_turns == 0 :
                self.available_moves.append([current_x, current_y + 2 * self.direction])

        # Attack moves
        current_x = servidor.letter.index(current_x)
        diagonal_left = servidor.letter[current_x - 1]

        if self.direction == 1:
            square_diag_left = board[current_y ][servidor.letter.index(diagonal_left)]
        else:
            square_diag_left = board[current_y - 2][servidor.letter.index(diagonal_left)]

        if square_diag_left != "  " and diagonal_left != "h":
            self.available_moves.append([diagonal_left,current_y + 1 * self.direction])

        try:
            diagonal_right = servidor.letter[current_x + 1]

            if self.direction == 1:
                square_diag_right = board[current_y][servidor.letter.index(diagonal_right)]
            else:
                square_diag_right = board[current_y - 2][servidor.letter.index(diagonal_right)]

            if square_diag_right != "  ":
                self.available_moves.append([diagonal_right, current_y + 1 * self.direction])
        except IndexError:
            print("Not a valid Move")



    def move(self, piece: Piece, move_requested:str, board:list):
        current_x, current_y = servidor.letter.index(self.current_pos[0]), 8 - int(self.current_pos[1])
        move_x, move_y = move_requested[0], int(move_requested[1])
        print(self.available_moves)
        move = [move_x, move_y]
        print(move)
        if move in self.available_moves:
            print("Move in dict")
            move[0] = servidor.letter.index(move[0])
            print(move)
            board[current_y][current_x] = "  "
            board[8 - move[1]][move[0]] = piece
            self.current_pos = move_requested
            self.number_of_turns += 1