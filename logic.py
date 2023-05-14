from consts import *
from vec import Vec
from line3d import Line3d
from math import pi, radians as rad

def calcCost(player, tryLine, near, lines):
    cost = 0
    len_no = 0
    for i, line in enumerate(lines):
        dist = tryLine.distance(line)
        if dist < player_radius*2:
            cost += (playerViewRadius - player.pos.distance(near[i].pos))**2
    return cost

def tryAngle(player, dir, angle, costs, near, lines):
    for side in range(-1, 2, 2):
        tryDir = dir.rotation2d(angle*side)

        if (player.pos + (tryDir*(player_speed/ticksPS))).outside(player_radius):
            continue

        tryDir.z = 100000/player_speed
        tryLine = Line3d(player.pos, tryDir)
        cost = calcCost(player, tryLine, near, lines)
        if cost == 0:
            tryDir.z = 0
            return tryDir
        costs.append((cost, Vec(tryDir.x, tryDir.y)))

def tryMove(player, dir, bList):
    
    near = player.nearBullets(playerViewRadius, bList)
    lines = []

    #lines creation
    for ent in near:
        lineDirection = Vec(ent.pos.x, ent.pos.y)
        lineDirection.normalize()
        lineDirection.z = 100000/bullet_speed
        lines.append(Line3d(ent.pos, lineDirection))
    
    costs = []
    #first part
    dir.normalize()
    for a in range(0, 60, circular_step):
        angle = rad(a)
        ret = tryAngle(player, dir, angle, costs, near, lines)
        if ret != None:
            return ret
    
    #middle
    tryDir = Vec(0, 0, 1)
    tryLine = Line3d(player.pos, tryDir)
    costNoMove = calcCost(player, tryLine, near, lines)
    if costNoMove == 0:
        tryDir.z = 0
        return tryDir
    
    #second part
    for a in range(60, 179, circular_step):
        angle = rad(a)
        ret = tryAngle(player, dir, angle, costs, near, lines)
        if ret != None:
            return ret
    
    costs.append((costNoMove, Vec(0, 0)))

    minCost, minDir = costs[0][0], costs[0][1]
    for c, d in costs:
        if c < minCost:
            minCost = c
            minDir = d

    minDir.z = 0
    return minDir

def shootPlayer(player, targetId, pList, bullets, tickCounter):
    target = pList[targetId]
    dir = Vec(target.pos.x - player.pos.x, target.pos.y - player.pos.y)
    player.shoot(dir, bullets, tickCounter)

