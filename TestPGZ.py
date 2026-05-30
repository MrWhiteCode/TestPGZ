import pgzrun
import pygame
import random
import time

WIDTH = 600
HEIGHT = 400
FPS = 60

player = Actor("player") #type: ignore
floor = Actor("floor") #type: ignore
coins = []
score = 0

new_size = (int(WIDTH * 1.5), int(HEIGHT * 1.5))
floor._surf = pygame.transform.scale(floor._surf, new_size)

floor._rect = floor._surf.get_rect()

floor.bottom = HEIGHT  
floor.left = 0

player.bottom = floor.top
player.x = WIDTH // 2

player.x = 300 
player.y = 200


def draw():
    screen.clear() #type: ignore
    floor.draw()
    player.draw()
    for coin in coins:
        coin.draw() #type: ignore
    screen.draw.text(f"Score: {score}", (20, 20), color="white", fontsize=30) #type: ignore
    if score == 75:
        screen.fill("black") #type: ignore
        screen.draw.text("Win!", center=(WIDTH // 2, HEIGHT // 2), color="white", fontsize=30) #type: ignore

def update():
    global score

    if keyboard.left: #type: ignore
        player.x -= 4
    
    if keyboard.right: #type: ignore
        player.x += 4
    
    if keyboard.up: #type: ignore
        player.y -= 4
    
    if keyboard.down: #type: ignore
        player.y += 4

    for coin in coins:
        if player.colliderect(coin):
            coins.remove(coin)
            score += random.randint(1, 4)
            break



def spawn_coins():
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    coin = Actor("coin", (x, y)) #type: ignore
    coin._surf = pygame.transform.scale(coin._surf, (30, 30))
    coin._rect = coin._surf.get_rect() 
    coin.pos = (x, y)
    coins.append(coin)

clock.schedule_interval(spawn_coins, 2.0) #type: ignore

pgzrun.go()