
import pygame
from math import trunc

def find_legal_pawn(pawn_x, pawn_y, targ_x, targ_y, targ_piece, pawn_piece):
    if pawn_piece % 2 == 0:
        print("black's piece")
        if (pawn_x == targ_x and pawn_y == targ_y + 2 and pawn_y == 6) or (pawn_x == targ_x and pawn_y == targ_y + 1):
            return True
        elif  targ_piece % 2 == 1 and (pawn_x == targ_x + 1 or pawn_x == targ_x - 1) and pawn_y == targ_y + 1: #normally would need targ piece check but not because of %
            return True
    else:
        print("white piece")
        if (pawn_x == targ_x and pawn_y == targ_y - 2 and pawn_y == 1) or (pawn_x == targ_x and pawn_y == targ_y - 1):
            return True
        elif  targ_piece % 2 == 0 and not targ_piece == 0 and (pawn_x == targ_x + 1 or pawn_x == targ_x - 1) and pawn_y == targ_y - 1:
            return True
    print("invalid pawn move")
    return False
def find_legal_knight(knight_x, knight_y, targ_x, targ_y):
    print(knight_moves)
    for i in range(8):
        if knight_x - targ_x == knight_moves[i][0] and knight_y - targ_y == knight_moves[i][1]:
            return True
    print("invalid knight move")
    return False



screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Chess")
#pygame.transform.scale(calculator, (int(calculator.get_width() * 0.75), int(calculator.get_height() * 0.75)))
board = pygame.image.load("chess_board.png")
board = pygame.transform.scale(board, (700, 700))
#white pieces:
white_king = pygame.image.load("white_pieces/chess_king_white.png")
white_queen = pygame.image.load("white_pieces/chess_queen_white.png")
white_rook = pygame.image.load("white_pieces/chess_rook_white.png")
white_bishop = pygame.image.load("white_pieces/chess_bishop_white.png")
white_knight = pygame.image.load("white_pieces/chess_knight_white.png")
white_pawn = pygame.image.load("white_pieces/chess_pawn_white.png")
#black pieces
black_king = pygame.image.load("black_pieces/chess_king_black.png")
black_queen = pygame.image.load("black_pieces/chess_queen_black.png")
black_rook = pygame.image.load("black_pieces/chess_rook_black.png")
black_bishop = pygame.image.load("black_pieces/chess_bishop_black.png")
black_knight = pygame.image.load("black_pieces/chess_knight_black.png")
black_pawn = pygame.image.load("black_pieces/chess_pawn_black.png")
#current inefficiency 
#blank_png = pygame.image.load("blank.png")
# piece convention: 0 = nil, 1,2 = pawn, 3,4 = knight, 5,6 = bishop, 7,8 = rook, 9,10 = queen, 11,12 = king, white is even, black odd
chess_board = [
  
    [7, 3, 5, 9, 11, 5, 3, 7],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 2, 2, 2, 2, 2],
    [8, 4, 6, 10, 12, 6, 4, 8]
    ]
num_to_surf = {0: None, 1: white_pawn, 2: black_pawn, 3: white_knight, 4: black_knight, 5: white_bishop, 6: black_bishop, 7: white_rook, 8: black_rook, 9: white_queen, 10: black_queen, 11: white_king, 12: black_king}
mirror_fix = {0: 7, 1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6:1, 7: 0}
pawn_moves = [[0, 1], [0, 2]]
global knight_moves
knight_moves = [[-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]]
legal_move_dicts_list = []
t_space = 87
y_offset = 405
x_offset = -208
mouse_column = 0
mouse_row = 0
click1_cord = (None, None)
click2_cord = (None, None)
tempvar = None
pygame.init()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
    mouse_column = trunc(mouse_pos_x / 88)
    mouse_row = trunc(mouse_pos_y / 88)
    

    if pygame.mouse.get_pressed()[0] and not mouse_was_pressed:
        if click1_cord == (None, None):
            click1_cord = (mirror_fix[mouse_row], mouse_column)
        else:
            click2_cord = (mirror_fix[mouse_row], mouse_column) # fix for mirror
            print(click1_cord)
            print(click2_cord)
            if chess_board[click1_cord[0]][click1_cord[1]] == 0:
                print("invalid null piece move")
            elif chess_board[click1_cord[0]][click1_cord[1]] == 1 or chess_board[click1_cord[0]][click1_cord[1]] == 2: # optomise with dict, check if pawn
                if  find_legal_pawn(click1_cord[1], click1_cord[0], click2_cord[1], click2_cord[0], chess_board[click2_cord[0]][click2_cord[1]], chess_board[click1_cord[0]][click1_cord[1]]):
                    chess_board[click2_cord[0]][click2_cord[1]] = chess_board[click1_cord[0]][click1_cord[1]]
                    chess_board[click1_cord[0]][click1_cord[1]] = 0
            elif chess_board[click1_cord[0]][click1_cord[1]] == 3 or chess_board[click1_cord[0]][click1_cord[1]] == 4:
                if find_legal_knight(click1_cord[1], click1_cord[0], click2_cord[1], click2_cord[0]):
                    chess_board[click2_cord[0]][click2_cord[1]] = chess_board[click1_cord[0]][click1_cord[1]]
                    chess_board[click1_cord[0]][click1_cord[1]] = 0
            else:
                chess_board[click2_cord[0]][click2_cord[1]] = chess_board[click1_cord[0]][click1_cord[1]]
                chess_board[click1_cord[0]][click1_cord[1]] = 0
            click1_cord = (None, None)
            click2_cord = (None, None)

        mouse_was_pressed = True
    if not pygame.mouse.get_pressed()[0]:
        mouse_was_pressed = False

    
    screen.fill((0, 0, 0)) 
    screen.blit(board, (0, 0))

    for y in range(8):
        for x in range(8):
            if not chess_board[y][x] == 0:
                screen.blit(num_to_surf[chess_board[y][x]], ((x_offset + t_space * x, y_offset - t_space * y)))
    pygame.display.flip()
