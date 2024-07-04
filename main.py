#python3 main.py 2>&1 | sed '/Secure coding is not enabled for restorable state!/d'
import pygame
import random
import sys

WIDTH = 800
HEIGHT = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#Display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

#Paddles
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
paddle_speed = 5
paddle1 = pygame.Rect(30, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle2 = pygame.Rect(WIDTH - 30 - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)

#Ball
BALL_SIZE = 20
ball_speed_x = 3
ball_speed_y = 3
ball = pygame.Rect(WIDTH//2 - BALL_SIZE//2, HEIGHT//2 - BALL_SIZE//2, BALL_SIZE, BALL_SIZE)

#Score and Winner
player1_score = 0
player2_score = 0
font = pygame.font.Font(None, 74)

#Running the game until winner
loop_game = True
while loop_game:
    for game in pygame.event.get():
        if game.type == pygame.QUIT:
            loop_game = False
            # pygame.quit()
            # sys.exit()
    
    #Keys to control paddles
    arrow_keys = pygame.key.get_pressed()
    if arrow_keys[pygame.K_w] and paddle1.top > 0:
        paddle1.y -= paddle_speed
    if arrow_keys[pygame.K_s] and paddle1.bottom < HEIGHT:
        paddle1.y += paddle_speed
    if arrow_keys[pygame.K_UP] and paddle2.top > 0:
        paddle2.y -= paddle_speed
    if arrow_keys[pygame.K_DOWN] and paddle2.bottom < HEIGHT:
        paddle2.y += paddle_speed

    #Ball movement
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    #Ball collision with paddles
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_speed_x *= -1

    #Ball collision with top and bottom walls
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    #Ball collision with left and right walls --> Scoring
    if ball.left <= 0:
        player2_score += 1
        ball.x = WIDTH//2 - BALL_SIZE//2
        ball.y = HEIGHT//2 - BALL_SIZE//2
        ball_speed_x *= random.choice((1, -1))
        ball_speed_y *= random.choice((1, -1))
    if ball.right >= WIDTH:
        player1_score += 1
        ball.x = WIDTH//2 - BALL_SIZE//2
        ball.y = HEIGHT//2 - BALL_SIZE//2
        ball_speed_x *= random.choice((1, -1))
        ball_speed_y *= random.choice((1, -1))

    #Drawing the game
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, paddle1)
    pygame.draw.rect(screen, WHITE, paddle2)
    pygame.draw.ellipse(screen, WHITE, ball)

    #Score
    player1_text = font.render(str(player1_score), True, WHITE)
    player2_text = font.render(str(player2_score), True, WHITE)
    screen.blit(player1_text, (WIDTH//2 - 100, 50))
    screen.blit(player2_text, (WIDTH//2 + 50, 50))
    pygame.display.flip()
    pygame.time.delay(30)

    #Winner
    if player1_score == 5 or player2_score == 5:
        if player1_score == 5:
            winner = "Player 1"  
        else:
            winner = "Player 2"
        text = font.render(f"{winner} wins!", True, WHITE)
        text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//2))
        screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.delay(200)

#Quit game
pygame.quit()
sys.exit()