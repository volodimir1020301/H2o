import json
import socket
import threading
import time

import pygame
import  random
WIDTH = 1000
HEIGHT = 600
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("2.tcp.eu.ngrok.io", 15132))

player_id = client.recv(1024). decode()
other_players_data = {}

def receiv_data():
    global  other_players_data
    while True:
        try:
            data = client.recv(4096).decode()
            if data:
                other_players_data = json.loads(data)
        except:
            break
threading.Thread(target=receiv_data, daemon=True).start()
class Player:
    def __init__(self, x, y, size, color, speed,name ):
        self.hitbox = pygame.Rect(x, y, size, size)
        self.color = color
        self.speed = speed
        self.name = name
        self.x = x
        self.y = y
        self.size = size
    def draw(self, window, scale=1):
        draw_x = int(WIDTH // 2 - (self.size * scale) //2)
        draw_y = int(HEIGHT // 2 - (self.size * scale) // 2)
        self.hitbox = pygame.Rect(draw_x, draw_y, self.size * scale, self.size * scale)
        pygame.draw.rect(window, self.color, self.hitbox)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.x += self.speed
        if keys[pygame.K_s]:
            self.y += self.speed
        if keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_w]:
            self.y -= self.speed


class Food:
    def __init__(self, size, x, y, color):
        self.hitbox = pygame.Rect(x, y, size, size)
        self.color = color
        self.x = x
        self.y = y
        self.size = size
    def draw(self, window, player_x, player_y, scale):
        draw_x = int((self.x - player_x) * scale + WIDTH // 2)
        draw_y = int((self.y - player_y) * scale + HEIGHT // 2)
        self.hitbox = pygame.Rect(draw_x, draw_y, self.size * scale, self.size * scale)
        pygame.draw.rect(window, self.color, self.hitbox)
pygame.init()
pygame.display.set_caption("Надпис на екрані")
fon = pygame.font. SysFont("ARial",36 )
text = fon.render("H2o ", True, (0, 0, 0))
window = pygame.display.set_mode([WIDTH, HEIGHT])

clock = pygame.time.Clock()
foods = [ ]
for i in range(400):
    food = Food(20,
                 random.randint(-2000, 2000),
                 random.randint(-2000, 2000),
                 [random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)])
    foods.append(food)
    scale = 1
andriy = Player(WIDTH/2, HEIGHT/2, 50, [0, 0, 0], 5, "любомир")
last_send_time = 0
while 1==1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    scale = max(0.3, min(60 / andriy.size, 1.5))
    for food in foods:
        if andriy.hitbox.colliderect(food.hitbox):
            food.x = random.randint(-2000, 2000)
            food.y = random.randint(-2000, 2000)
            andriy.size += 2
    window.fill([255, 255, 255])
    andriy.draw(window, scale)
    window.blit(text, (0, 0))
    andriy.update()
    if time.time() - last_send_time > 0.1 :
        try:
            players_data = json.dumps({
                "x" : andriy.x,
                "y" : andriy.y,
                "size" : andriy.size,
                "color" : andriy.color,
                "name" : andriy.name,
                "speed": andriy.speed
            })
            client.send(players_data.encode())
        except Exception as e:
            print("Connection lost:", e)
            running = False
        pass

    for pid, pdata in other_players_data.items():
        draw_x = int((pdata["x"] - andriy.x) * scale + WIDTH // 2 )
        draw_y = int((pdata["y"] - andriy.y) * scale + HEIGHT // 2)
        size = pdata["size"] * scale
        pygame.draw.rect(window, pdata["color"], pygame.Rect(draw_x, draw_y, size, size))


    for food in foods:
        food.draw(window, andriy.x, andriy.y, scale)
        
    pygame.display.flip()

    clock.tick(60)