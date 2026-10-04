import pygame

pygame.init()

WIDTH = 500
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ML PingPong")

clock = pygame.time.Clock()

# -------------------------
# Paddle
# -------------------------

paddle_width = 120
paddle_height = 15

paddle_x = WIDTH // 2 - paddle_width // 2
paddle_y = HEIGHT - 40

paddle_speed = 20

# -------------------------
# Ball
# -------------------------

ball_size = 15

ball_x = WIDTH // 2
ball_y = HEIGHT // 2

ball_speed_x = 5
ball_speed_y = 5

# -------------------------
# Game
# -------------------------

running = True
game_over = False

while running:

    # 1. Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. Update game
    if not game_over:

        # -------------------------
        # Move paddle with keyboard
        # -------------------------

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            paddle_x -= paddle_speed

        if keys[pygame.K_RIGHT]:
            paddle_x += paddle_speed

        # -------------------------
        # Prevent paddle leaving screen
        # -------------------------

        if paddle_x < 0:
            paddle_x = 0

        if paddle_x + paddle_width > WIDTH:
            paddle_x = WIDTH - paddle_width

        # -------------------------
        # Move ball
        # -------------------------

        ball_x += ball_speed_x
        ball_y += ball_speed_y

        # -------------------------
        # Ball hits left wall
        # -------------------------

        if ball_x <= 0:
            ball_x = 0
            ball_speed_x *= -1

        # -------------------------
        # Ball hits right wall
        # -------------------------

        elif ball_x + ball_size >= WIDTH:
            ball_x = WIDTH - ball_size
            ball_speed_x *= -1

        # -------------------------
        # Ball hits top wall
        # -------------------------

        if ball_y <= 0:
            ball_y = 0
            ball_speed_y *= -1

        # -------------------------
        # Create rectangles
        # -------------------------

        ball_rect = pygame.Rect(
            ball_x,
            ball_y,
            ball_size,
            ball_size
        )

        paddle_rect = pygame.Rect(
            paddle_x,
            paddle_y,
            paddle_width,
            paddle_height
        )

        # -------------------------
        # Ball hits paddle
        # -------------------------

        if ball_rect.colliderect(paddle_rect) and ball_speed_y > 0:

            # Put ball directly above paddle
            ball_y = paddle_y - ball_size

            # Bounce upward
            ball_speed_y *= -1

        # -------------------------
        # Ball reaches bottom
        # -------------------------

        if ball_y + ball_size >= HEIGHT:
            game_over = True

    # 3. Draw background
    screen.fill((0, 0, 0))

    # Draw paddle
    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (paddle_x, paddle_y, paddle_width, paddle_height)
    )

    # Draw ball
    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (ball_x, ball_y, ball_size, ball_size)
    )

    # Game over
    if game_over:

        font = pygame.font.Font(None, 60)

        text = font.render(
            "GAME OVER",
            True,
            (255, 255, 255)
        )

        text_rect = text.get_rect(
            center=(WIDTH // 2, HEIGHT // 2)
        )

        screen.blit(text, text_rect)

    # 4. Update display
    pygame.display.flip()

    # 5. 60 FPS
    clock.tick(60)

pygame.quit()