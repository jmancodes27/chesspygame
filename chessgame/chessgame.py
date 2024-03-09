
import pygame

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
# piece convention: 0 = nil, 1,2 = pawn, 3,4 = knight, 5,6 = bishop, 7,8 = rook, 9,10 = queen, 11,12 = king, white is odd, black even
chess_board = [
    [8, 4, 6, 10, 12, 6, 4, 8],
    [2, 2, 2, 2, 2, 2, 2, 2],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [7, 3, 5, 9, 11, 5, 3, 7],
    ]

t_space = 87
y_space = 405
first_space = -208
pygame.init()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()


    if pygame.mouse.get_pressed()[0] and not mouse_was_pressed:
        print("mouse pressed")
        mouse_was_pressed = True
    if not pygame.mouse.get_pressed()[0]:
        mouse_was_pressed = False

    
    screen.fill((0, 0, 0)) 
    screen.blit(board, (0, 0))
    screen.blit(white_king, (first_space + t_space * 4, y_space))
    screen.blit(white_bishop, (first_space + t_space * 5, y_space))
    screen.blit(white_knight, (first_space + t_space * 6, y_space))
    screen.blit(white_rook, (first_space + t_space * 7, y_space))
    screen.blit(white_queen, (first_space + t_space * 3, y_space))
    screen.blit(white_bishop, (first_space + t_space * 2, y_space))
    screen.blit(white_knight, (first_space + t_space * 1, y_space))
    screen.blit(white_rook, (first_space, y_space))
    for z in range(7):
        for i in range(8):
            screen.blit(white_pawn, (first_space + t_space * i, y_space - t_space * (z + 1)))
    pygame.display.flip()
