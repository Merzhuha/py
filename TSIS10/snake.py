import pygame
import time
import random
import psycopg2

# Function to initialize database connection
def initialize_db():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="suppliers",
            user="postgres",
            password="6412"
        )
        cur = conn.cursor()
        return conn, cur
    except psycopg2.Error as e:
        print("Error connecting to the database:", e)

# Function to create user and user_score columns if not exists
def create_user_table(cur):
    cur.execute("CREATE TABLE IF NOT EXISTS snake_scores (id SERIAL PRIMARY KEY, username VARCHAR(50) UNIQUE, user_score INTEGER)")

# Function to insert or update user score
def update_user_score(cur, conn, username, scor):
    cur.execute("SELECT * FROM snake_scores WHERE username = %s", (username,))
    user = cur.fetchone()
    if user:
        # Update user's score if user exists
        cur.execute("UPDATE snake_scores SET user_score = %s WHERE username = %s", (scor, username))
    else:
        # Insert new user with score if user doesn't exist
        cur.execute("INSERT INTO snake_scores (username, user_score) VALUES (%s, %s)", (username, scor))
    conn.commit()

# Function to display current user level
def show_user_level(username, cur, conn):
    cur.execute("SELECT user_score FROM snake_scores WHERE username = %s", (username,))
    user_score = cur.fetchone()
    if user_score:
        print(f"Welcome back, {username}! Your current level is {user_score[0]}.")
    else:
        print(f"Welcome, {username}! You are a new player.")
        cur.execute("INSERT INTO snake_scores (username, user_score) VALUES (%s, %s)", (username, 0))
        conn.commit() 

# Initialize database connection and cursor
conn, cur = initialize_db()
create_user_table(cur)

# Get user's username
username = input("Enter your username: ")

# Display user's current level
show_user_level(username, cur, conn)

pygame.init()
size = 600
Snake_size = 25
x, y = random.randrange(0, size, Snake_size), random.randrange(0, size, Snake_size)
apple = random.randrange(0, size, Snake_size), random.randrange(0, size, Snake_size)
bomb = random.randrange(0, size, Snake_size), random.randrange(0, size, Snake_size)
BOMB = pygame.USEREVENT + 1
APPLE = pygame.USEREVENT + 1
lenght = 1
scor=0
level = 0
snake = [(x, y)]
FPS = 10
dx, dy = 0, 0

screen = pygame.display.set_mode([size, size])
clock = pygame.time.Clock()
font_of_score = pygame.font.SysFont('Aarial', 22, bold=True)
font_of_level = pygame.font.SysFont('Aarial', 22, bold=True)
font_of_end = pygame.font.SysFont('Aarial', 70, bold=True)

pygame.time.set_timer(BOMB, 3000)
pygame.time.set_timer(APPLE, 5000)

while True:
    screen.fill(pygame.Color('black'))

    [(pygame.draw.rect(screen, pygame.Color('green'), (i, j, Snake_size - 2, Snake_size - 2))) for i, j in snake]
    pygame.draw.rect(screen, pygame.Color('red'), (*apple, Snake_size, Snake_size))
    pygame.draw.rect(screen, pygame.Color('yellow'), (*bomb, Snake_size, Snake_size))
    render_score = font_of_score.render(f'SCORE: {scor}', True, pygame.Color('yellow'))
    render_level = font_of_level.render(f'LeVeL: {level}', True, pygame.Color('yellow'))
    screen.blit(render_score, (5, 5))
    screen.blit(render_level, (5, 20))
    x += dx * Snake_size
    y += dy * Snake_size
    snake.append((x, y))
    snake = snake[-lenght:]

    if snake[-1] == apple:
        apple = random.randrange(0, size, Snake_size), random.randrange(0, size, Snake_size)
        lenght += 1
        FPS += 0.3
        scor += 1
        if scor % 3 == 0:
            level += 1
            l = [i for i in range(5, 100, 2)]
            for i in l:
                if level == i:
                    FPS += 3.5

    if snake[-1] == bomb:
        while True:
            update_user_score(cur, conn, username, scor)
            render_end = font_of_end.render('GAME OVER', True, pygame.Color('yellow'))
            screen.blit(render_end, (size // 2 - 150, size // 3))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

    # if (x < 0 or x > size - Snake_size or y < 0 or y > size - Snake_size) or (len(snake) != len(set(snake))):
    #     while True:
    #         render_end = font_of_end.render('GAME OVER', True, pygame.Color('yellow'))
    #         screen.blit(render_end, (size // 2 - 150, size // 3))
    #         pygame.display.flip()
    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #                 exit()
    if x < 0: x = size
    if x > size: x = -Snake_size
    if y < 0: y = size
    if y > size: y = -Snake_size
    if len(snake) != len(set(snake)):
        while True:
            update_user_score(cur, conn, username, scor)
            render_end = font_of_end.render('GAME OVER', 1, pygame.Color('yellow'))
            screen.blit(render_end, (size // 2 - 150, size // 3))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
    pygame.display.flip()
    clock.tick(FPS)
    paused=False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == BOMB:
            bomb = random.randrange(0, size, Snake_size), random.randrange(0, size, Snake_size)
        if event.type == APPLE:
            apple = random.randrange(0, size, Snake_size), random.randrange(0, size, Snake_size)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and dx != -1:
                dx, dy = 1, 0
            if event.key == pygame.K_LEFT and dx != 1:
                dx, dy = -1, 0
            if event.key == pygame.K_UP and dy != 1:
                dx, dy = 0, -1
            if event.key == pygame.K_DOWN and dy != -1:
                dx, dy = 0, 1
            #
            if event.key == pygame.K_d and dx != -1:
                dx, dy = 1, 0
            if event.key == pygame.K_a and dx != 1:
                dx, dy = -1, 0
            if event.key == pygame.K_w and dy != 1:
                dx, dy = 0, -1
            if event.key == pygame.K_s and dy != -1:
                dx, dy = 0, 1
            if event.key == pygame.K_SPACE:  # Обработка нажатия клавиши пробела для паузы
                paused = not paused