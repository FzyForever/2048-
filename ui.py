from game2048.bll import GameCoreController
from game2048.model import Direction
import os

class GameView:
    def __init__(self):
        self.__core=GameCoreController()

    def start(self):
        self.__core.generate_new_number()
        self.__core.generate_new_number()
        self.print_map()

    def print_map(self):
        #os.system("clear")
        for r in range(len(self.__core.map)):
            for c in range(len(self.__core.map[r])):
                print(self.__core.map[r][c], end="\t")
            print()



    def update(self):
        while True:
            self.move_map()
            if self.__core.is_change:
                self.__core.generate_new_number()
                self.print_map()
                if self.__core.is_game_over():
                    print("游戏结束")
                    break

    def move_map(self):
        dir=input("请输入wsad:")
        if dir=="w":
            self.__core.move(Direction.up)

        if dir=="s":
            self.__core.move(Direction.down)

        if dir=="a":
            self.__core.move(Direction.left)

        if dir=="d":
            self.__core.move(Direction.right)



