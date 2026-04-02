from servidor.pieces.piece import Piece
import servidor

class King(Piece):
    def __init__(self,piece:str, current_pos):
        super().__init__(piece,current_pos)

    def check_available_moves(self, board: list[list]):
        self.available_moves = []
        current_x = servidor.letter.index(self.current_pos[0])
        current_y = 8 - int(self.current_pos[1])

        for target_y in range(current_y - 1, current_y + 2):
            for target_x in range(current_x - 1, current_x + 2):

                if 0 <= target_x < 8 and 0 <= target_y < 8:
                    if target_x == current_x and target_y == current_y:
                        continue
                    target_square = board[target_y][target_x]
                    if target_square == "  ":
                        self.available_moves.append([servidor.letter[target_x], 8 - target_y])
                    else:
                        if self.piece[0] != target_square.piece[0]:
                            self.available_moves.append([servidor.letter[target_x], 8 - target_y])


    def is_checked(self, board: list[list]):
        current_x = servidor.letter.index(self.current_pos[0])
        current_y = 8 - int(self.current_pos[1])

        king_moves = False
        checked = False
        pieces_that_can_attack = []
        defend = False

        if not self.available_moves:
            king_moves = True

        for line in board :
            for piece in line:
                if piece == "  " or self.piece[0] == piece.piece[0]:
                    continue
                for move in piece.available_moves:
                    if move in self.available_moves:
                        self.available_moves.remove(move)
                    if move == self.current_pos:
                        checked = True
                        pieces_that_can_attack.append(piece)
        count = 0
        for line in board:
            for square in line:
                if square == "  " or self.piece[0] != square.piece[0]:
                    continue
                for piece in pieces_that_can_attack:
                    for move in square.available_moves:
                        if move == piece.current_pos:
                            count += 1
                            continue

        if checked:
            if king_moves or defend:
                print("check")
            else:
                print("checkmate")
                exit(0)


        """
        pegar os movimentos que atacam o rei (peça)
        for piece in pieces_that_can_attack:
            
            
            if a == b and c != d:
                if c > d:
                    c, d = d, c
                for i in range(a + 1, b):
                    moves_need_defend.append()
        
        """


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

