import pygame
import  random
WIDTH = 1000
HEIGHT = 600
class Player:
    def __init__(self, x, y, size, color, speed,name ):
        self.hitbox = pygame.Rect(x, y, size, size)
        self.color = color
        self.speed = speed
        self.name = name
        self.x = x
        self.y = y
    def draw(self, window):
        pygame.draw.rect(window, self.color, self.hitbox)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.x += self.speed


class Food:
    def __init__(self, size, x, y, color):
        self.hitbox = pygame.Rect(x, y, size, size)
        self.color = color
        self.x = x
        self.y = y
    def draw(self, window):
        pygame.draw.rect(window, self.color, self.hitbox)
pygame.init()

window = pygame.display.set_mode([WIDTH, HEIGHT])

clock = pygame.time.Clock()
foods = [ ]
for i in range(300):
    food = Food(20,
                 random.randint(-2000, 2000),
                 random.randint(-2000, 2000),
                 [random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)])
    foods.append(food)
andriy = Player(WIDTH/2, HEIGHT/2, 50, [255, 0, 0], 3, "любомир")
while 1==1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    window.fill([255, 255, 255])
    andriy.draw(window)
    andriy.update()

    for food in foods:
        food.draw(window)
        
    pygame.display.flip()

    clock.tick(60)