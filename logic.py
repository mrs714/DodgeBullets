from consts import *
from vec import Vec
from line3d import Line3d
from math import pi, radians as rad

def calcCost(player, tryLine, near, lines):
    cost = 0
    for i, line in enumerate(lines):
        alti = tryLine.closestAltitude(line)
        if alti > 0:
            dist = tryLine.horizontalDistance(line, alti)      
            if dist < player_radius + bullet_radius+7:
                cost -= alti
    return cost

def tryAngle(player, dir, angle, costs, near, lines):
    for side in range(-1, 2, 2):
        tryDir = dir.rotation2d(angle*side)

        if (player.pos + (tryDir*(player_speed/ticksPS))).outside(player_radius):
            continue

        tryDir.z = 1/player_speed
        tryLine = Line3d(player.pos, tryDir)
        cost = calcCost(player, tryLine, near, lines)
        if cost == 0:
            tryDir.z = 0
            return tryDir
        costs.append((cost, Vec(tryDir.x, tryDir.y)))

def tryMove(player, dir, bList):
    
    near = player.nearBullets(playerViewRadius, bList) 
    #near = [b for b in near if player.mayCollide(b, 0)]
    lines = []

    #lines creation
    for ent in near:
        lineDirection = Vec(ent.pos.x, ent.pos.y)
        lineDirection.normalize()
        lineDirection.z = 1/bullet_speed
        lines.append(Line3d(ent.pos, lineDirection))
    
    costs = []
    #first part
    dir.normalize()
    for a in range(0, 60, circular_step):
        angle = rad(a)
        ret = tryAngle(player, dir, angle, costs, near, lines)
        if ret != None:
            print("ez")
            return ret

    #middle
    tryDir = Vec(0, 0, 1)
    tryLine = Line3d(player.pos, tryDir)
    costNoMove = calcCost(player, tryLine, near, lines)
    if costNoMove == 0:
        tryDir.z = 0
        print("ez")
        return tryDir
    
    #second part
    for a in range(60, 179, circular_step):
        angle = rad(a)
        ret = tryAngle(player, dir, angle, costs, near, lines)
        if ret != None:
            print("ez")
            return ret
    
    
    costs.append((costNoMove, Vec(0, 0)))

    minCost, minDir = costs[0][0], costs[0][1]
    for c, d in costs:
        if c < minCost:
            minCost = c
            minDir = d
    print("not ez: ", minCost)
    minDir.z = 0
    return minDir

def shootPlayer(player, targetId, pList, bullets, tickCounter):
    target = pList[targetId]
    dir = Vec(target.pos.x - player.pos.x, target.pos.y - player.pos.y)
    player.shoot(dir, bullets, tickCounter)

