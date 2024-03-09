
import pygame

screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Chess")
#pygame.transform.scale(calculator, (int(calculator.get_width() * 0.75), int(calculator.get_height() * 0.75)))
board = pygame.image.load("chess_board.png")
board = pygame.transform.scale(board, (700, 700))
#white pieces:
white_king = pygame.image.load("white_pieces/chess_king_white.png")
#black pieces
black_king = pygame.image.load("black_pieces/chess_king_black.png")

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
    screen.blit(white_king, (140, 400))

    pygame.display.flip()
