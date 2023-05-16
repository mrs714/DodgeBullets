import pygame
from consts import *
from player import Player
from bullet import Bullet
from logic import tryMove, shootPlayer
from vec import Vec

tickCounter = 0
collisions = 0

bullets = {}
players = {}


player1 = Player(Vec(200, 200))
player2 = Player(Vec(800, 800))
player3 = Player(Vec(200, 800))
player4 = Player(Vec(800, 200))
#player5 = Player(Vec(200, 500))
#player6 = Player(Vec(800, 500))

player0 = Player(Vec(350, 350))

players[player0.id] = player0
players[player1.id] = player1
players[player2.id] = player2
players[player3.id] = player3
players[player4.id] = player4
#players[player5.id] = player5
#players[player6.id] = player6

id_main_player = player0.id

pygame.init()

win = pygame.display.set_mode((map_size, map_size))
pygame.display.set_caption("The game")

clock = pygame.time.Clock()

dirs = [Vec(1, 0), Vec(1, 1), Vec(0, 1), Vec(-1, 1), Vec(-1, 0), Vec(-1, -1), Vec(0, -1), Vec(1, -1)]
positions = [Vec(350, 350), Vec(350, 650), Vec(650, 650), Vec(650, 350)]

def update():
    for player in players.values():
        player.move(player_speed)
        if player.id == id_main_player:
            player.dir = tryMove(player, dirs[2*(int(tickCounter/100)%4)], bullets)
        else:
            shootPlayer(player, id_main_player, players, bullets, tickCounter)
    
    delids = []
    for bullet in bullets.values():
        if bullet.pos.outside(2):
            delids.append(bullet.id)
            continue
        bullet.move(bullet_speed)
    for id in delids:
        del bullets[id]


    #check for collisions
    for bullet in bullets.values():
        for player in players.values():
            if player.pos.distance(bullet.pos) < player_radius and player.id != bullet.owner.id and player.id != id_main_player:
                collisions += 1
                print("Collisions: " + str(collisions))
                

    
def draw():
    update()

    win.fill((0, 0, 0))

    for player in players.values():
        if player.id == id_main_player:
            pygame.draw.circle(win, (0, 255, 0), (int(player.pos.x), int(player.pos.y)), player_radius)
        else:
            pygame.draw.circle(win, (255, 0, 0), (int(player.pos.x), int(player.pos.y)), player_radius)
    
    for bullet in bullets.values():
        pygame.draw.circle(win, (255, 255, 255), (int(bullet.pos.x), int(bullet.pos.y)), bullet_radius)

run = True
while run:
    clock.tick(ticksPS)
    tickCounter += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        run = False
    
    draw()

    pygame.display.update()