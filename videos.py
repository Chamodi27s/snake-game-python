import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 20
FPS = 10

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 35)

def draw_snake(snake):
    for x, y in snake:
        pygame.draw.rect(win, (0, 255, 0), (x, y, BLOCK_SIZE, BLOCK_SIZE))
        
def message(text, color):
    msg = font.render(text, True, color)
    win.blit(msg, [WIDTH//6, HEIGHT//3])

def game_loop():
    x, y = WIDTH // 2, HEIGHT // 2
    dx, dy = 0, 0
    snake = [(x, y)]
    length = 1
    food = (random.randrange(0, WIDTH, BLOCK_SIZE), random.randrange(0, HEIGHT, BLOCK_SIZE))

    run = True
    game_over = False

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT: dx, dy = -BLOCK_SIZE, 0
                elif event.key == pygame.K_RIGHT: dx, dy = BLOCK_SIZE, 0
                elif event.key == pygame.K_UP: dx, dy = 0, -BLOCK_SIZE
                elif event.key == pygame.K_DOWN: dx, dy = 0, BLOCK_SIZE
                elif game_over and event.key == pygame.K_r:
                    game_loop()
                    return
                elif game_over and event.key == pygame.K_q:
                    run = False

        if not game_over:
            x += dx
            y += dy
            snake.append((x, y))
            if len(snake) > length:
                del snake[0]

            # Check collision with walls or self
            if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT or len(snake) != len(set(snake)):
                game_over = True

            # Check collision with food
            if (x, y) == food:
                food = (random.randrange(0, WIDTH, BLOCK_SIZE), random.randrange(0, HEIGHT, BLOCK_SIZE))
                length += 1

            win.fill((0, 0, 0))
            pygame.draw.rect(win, (255, 0, 0), (*food, BLOCK_SIZE, BLOCK_SIZE))
            draw_snake(snake)
            pygame.display.update()
            clock.tick(FPS)
        else:
            win.fill((0, 0, 0))
            message("Game Over! Press R to Restart or Q to Quit", (255, 255, 255))
            pygame.display.update()

    pygame.quit()


game_loop()
