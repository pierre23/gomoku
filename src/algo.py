#!/bin/env python3

class CAlgo :

    def __init__(self) :
        self.around = {
            (0,1),
            (0,-1),
            (1,0),
            (-1,0),
            (1,1),
            (-1,-1),
            (1,-1),
            (-1,1)
        }

    def debug(self) :
        for x in self.gameBoard :
            print (x)

    def findNextMoove(self, gameBoard, size) :
        self.gameBoard = gameBoard
        self.size = size
        for x in range(0, size) :
            for y in range(0, size) :
                for around in self.around :
                    if x + around[0] < self.size and y + around[1] < self.size and x + around[0] >= 0 and y + around[1] >= 0 and self.gameBoard[x + around[0]][y + around[1]] < 0 and self.gameBoard[x][y] >= 0 :
                        value = self.findPath((x + around[0], y + around[1]), around, 1)
                        if value > self.gameBoard[x][y] :
                            self.gameBoard[x][y] = value
        return self.idxFinding()

    def idxFinding(self) :
        maxValue = 0
        maxX = 0
        maxY = 0
        for x in range(0, self.size) :
            for y in range(0, self.size) :
                if self.gameBoard[x][y] > 0 and self.gameBoard[x][y] >= maxValue :
                    maxValue = self.gameBoard[x][y] - int('0')
                    maxX = x
                    maxY = y
        return (maxX,maxY)


    def findPath(self, pos, sens, nbr) :
        if pos[0] + sens[0] < self.size and pos[1] + sens[1] < self.size and pos[0] + sens[0] >= 0 and pos[1] + sens[1] > 0 :
            if self.gameBoard[pos[0] + sens[0]][pos[1] + sens[1]] == self.gameBoard[pos[0]][pos[1]] :
                nbr += 1
                return self.findPath((pos[0] + sens[0], pos[1] + sens[1]), sens, nbr)
        return nbr
