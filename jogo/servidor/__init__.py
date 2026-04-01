# dicionário com as coordenadas das peças brancas
from servidor.pieces.pawn import Pawn
from servidor.pieces.king import King
from servidor.pieces.rook import Rook
from servidor.pieces.bishop import Bishop
from servidor.pieces.queen import Queen
from servidor.pieces.knight import Knight

wpawn = Pawn("wP", "a2")
wpawn2 = Pawn("wP", "b2")
wpawn3 = Pawn("wP", "c2")
wpawn4 = Pawn("wP", "d2")
wpawn5 = Pawn("wP", "e2")
wpawn6 = Pawn("wP", "f2")
wpawn7 = Pawn("wP", "g2")
wpawn8 = Pawn("wP", "h2")
wking = King("wK", "e1")
wrook1 = Rook("wR", "a1")
wrook2 = Rook("wR", "h1")
wbishop1 = Bishop("wB", "f1")
wbishop2 = Bishop("wB", "c1")
wqueen = Queen("wQ", "d1")
wknight1 = Knight("wT", "b1")
wknight2 = Knight("wT", "g1")
DEFAULT_WHITE_BOARD_MAP = {
    "wP": [wpawn, wpawn2, wpawn3, wpawn4, wpawn5, wpawn6, wpawn7, wpawn8],
    "wK": [wking],
    "wR": [wrook1, wrook2],
    "wB": [wbishop1, wbishop2],
    "wQ": [wqueen],
    "wT": [wknight1,wknight2]
}

bpawn = Pawn("wP", "a7")
bpawn2 = Pawn("wP", "b7")
bpawn3 = Pawn("wP", "c7")
bpawn4 = Pawn("wP", "d7")
bpawn5 = Pawn("wP", "e7")
bpawn6 = Pawn("wP", "f7")
bpawn7 = Pawn("wP", "g7")
bpawn8 = Pawn("wP", "h7")
bking = King("wK", "e8")
brook1 = Rook("wR", "a8")
brook2 = Rook("wR", "h8")
bbishop1 = Bishop("wB", "f8")
bbishop2 = Bishop("wB", "c8")
bqueen = Queen("wQ", "d8")
bknight1 = Knight("wT", "b8")
bknight2 = Knight("wT", "g8")
DEFAULT_BLACK_BOARD_MAP = {
    "wP": [bpawn, bpawn2, bpawn3, bpawn4, bpawn5, bpawn6, bpawn7, bpawn8],
    "wK": [bking],
    "wR": [brook1, brook2],
    "wB": [bbishop1, bbishop2],
    "wQ": [bqueen],
    "wT": [bknight1,bknight2]
}

"""
DEFAULT_WHITE_BOARD_MAP = {
    "wP": ["a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1"],
    "wN": ["b0", "g0"],
    "wB": ["c0", "f0"],
    "wR": ["a0", "h0"],
    "wQ": ["d0"],
    "wK": ["e0"],
}
"""

"""
# dicionário com as coordenadas das peças pretas
DEFAULT_BLACK_BOARD_MAP = {
    "bP": ["a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6"],
    "bN": ["b7", "f7"],
    "bB": ["c7", "g7"],
    "bR": ["a7", "h7"],
    "bQ": ["d7"],
    "bK": ["e7"],
}
"""

"""
col_map = {
    "a":0,
    "b":1,
    "c":2,
    "d":3,
    "e":4,
    "f":5,
    "g":6,
    "h":7,
}
"""

letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

COMMAND_SIZE = 9
INT_SIZE = 8
ADD_OP = "add      "
OBJ_OP = "obj_obj  "
SYM_OP = "sym      "
SUB_OP = "sub      "
BYE_OP = "bye      "
END_OP = "stop     "
PORT = 35000
SERVER_ADDRESS = "localhost"