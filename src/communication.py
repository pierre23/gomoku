#!/bin/env python3

import sys
from algo import CAlgo

class CCommunication :

    def read(self) :
        for line in sys.stdin :
            return line

    def write(self, toWrite) :
        print(toWrite)
        sys.stdout.flush()

class CGameProtocol :

    _communication = CCommunication();
    _algo = CAlgo();

    def __init__ (self, name, version, author, country) :
        self.name = name
        self.version = version
        self.author = author
        self.country = country
        self.isRunning = False
        self._commandHandling = {
            "START" : self.startFunction,
            "BEGIN" : self.beginFunction,
            "TURN" : self.turnFunction,
            "ABOUT" : self.aboutFunction,
            "BOARD" : self.boardFunction,
            "INFO" : self.infoFunction,
            "END" : self.endFunction
        }
    
    def debug(self) :
        for x in self.gameBoard :
            print (x)

    def handleCommand(self) :
        self.isRunning = True
        while self.isRunning == True :

            Input = self._communication.read().replace('\n', "", 1)
            splitedInput = Input.split(' ')
            Input = Input.replace(' ', "")
            if splitedInput[0] in self._commandHandling :
                key = splitedInput[0]
                Input = Input.replace(key, "")
                self._commandHandling[key](Input);
            else :
                self._communication.write("UNKNOWN [unknown received command]\n")
            #self.debug()

    def startFunction(self, args) :
        if not args.isdigit() :
            self._communication.write("ERROR message - unsupported size or other error\n")
        else :
            self.size = int(args)
            self.gameBoard = [[0] * self.size for _ in range(self.size)]
            self._communication.write("OK")

    def beginFunction(self, args) :
        self.gameBoard[int(self.size / 2)][int(self.size / 2)] = -1
        self._communication.write(str(int(self.size / 2)) + "," + str(int(self.size / 2)))

    def turnFunction(self, args) :
        coord = args.split(',')
        self.gameBoard[int(coord[0])][int(coord[1])] = -2
        #add algo here
        idx = self._algo.findNextMoove(self.gameBoard, self.size)
        self.gameBoard[int(idx[0])][int(idx[1])] = -1
        self._communication.write(str(int(idx[0])) + "," + str(int(idx[1])))

    def aboutFunction(self, args) :
        self._communication.write("name=\"" + self.name + "\", version=\"" + self.version + "\", author=\"" + self.author + "\", country=\"" + self.country + "\"\n")

    def boardFunction(self, args) :
        Input = self._communication.read().replace('\n', "", 1)
        while Input != "DONE" :
            splitedByComa = Input.split(",")
            if splitedByComa[0].isdigit() and splitedByComa[1].isdigit() :
                self.gameBoard[int(splitedByComa[0])][int(splitedByComa[1])] = 0
            Input = self._communication.read().replace('\n', "", 1)    
        #add algo here
        idx = self._algo.findNextMoove(self.gameBoard, self.size)
        self.gameBoard[int(idx[0])][int(idx[1])] = -1
        self._communication.write(str(int(idx[0])) + "," + str(int(idx[1])))

    def infoFunction(self, args) :
        return

    def endFunction(self, args) :
        self.isRunning = False

try :
    comm = CGameProtocol("PowerGom", "1.0", "SEP", "France");
    comm.handleCommand();
except KeyboardInterrupt :
    exit(1);