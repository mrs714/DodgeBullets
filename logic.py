from consts import *
from vec import Vec
from line3d import Line3d
from math import pi

def tryMove(player, dir, entSet):
    
    near = player.nearBullets(playerViewRadius, entSet)
    lines = []

    for ent in near:
        lineDirection = Vec(ent.pos.x, ent.pos.y)
        lineDirection.normalize()
        lineDirection.z = 1/bullet_speed
        lines.append(Line3d(ent.pos, lineDirection))
    
    def calcCost():
        cost = 0
        for i, line in enumerate(lines):
            if tryLine.intersects(line, player_radius + bullet_radius + 1):
                cost += (playerViewRadius - player.pos.distance(near[i].pos))**2
        return cost
    
    def tryAngle():
        nonlocal tryDir, tryLine
        for side in range(-1, 2, 2):
            tryDir = dir.rotation2d(angle*side)
            tryDir.z = 1/player_speed
            tryLine = Line3d(player.pos, tryDir)
            cost = calcCost()
            if cost == 0:
                tryDir.z = 0
                return tryDir
            costs.append((cost, Vec(tryDir.x, tryDir.y)))

    costs = []
    dir.normalize()
    for angle in range(0, pi/3, 2*pi/circular_resolution):
        ret = tryAngle()
        if ret != None:
            return ret
    
    tryDir = Vec(0, 0, 1)
    tryLine = Line3d(player.pos, tryDir)
    costNoMove = calcCost()
    if costNoMove == 0:
        tryDir.z = 0
        return tryDir
    
    for angle in range(pi/3, pi, 2*pi/circular_resolution):
        ret = tryAngle()
        if ret != None:
            return ret
    
    costs.append(costNoMove, Vec(0, 0))

    minCost, minDir = costs[0][0], costs[0][1]
    for c, d in costs:
        if c < minCost:
            minCost = c
            minDir = d
    
    minDir.z = 0
    return minDir



