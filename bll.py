import random
from game2048.model import Location
import copy
from game2048.model import Direction

class GameCoreController:

    def __init__(self):
        # self.__map=[
        #     [2,0,4,2],
        #     [2,2,0,0],
        #     [2,0,4,4],
        #     [4,0,0,2]
        # ]
        self.__map=[
            [0]*4,
            [0]*4,
            [0]*4,
            [0]*4,
        ]

        self.__list_merge=[]

        self.__list_empty_location=[]
        self.is_change=False

    @property
    def map(self):
        return self.__map


    def zero_to_end(self):
        for i in range(len(self.__list_merge)-1,-1,-1):
            if self.__list_merge[i]==0:
                del self.__list_merge[i]
                self.__list_merge.append(0)


    def merge(self):
        self.zero_to_end()
        for i in range(len(self.__list_merge)-1):
            if self.__list_merge[i]==self.__list_merge[i+1]:
                self.__list_merge[i]+=self.__list_merge[i+1]
                self.__list_merge[i+1]=0
        self.zero_to_end()


    def move_left(self):
        for r in range(len(self.__map)):
            self.__list_merge[:]=self.__map[r]  #self.__list_merge[:]=[2,0,4,2]
            self.merge()                        #[2,4,2,0]
            self.__map[r][:]=self.__list_merge  #[2,4,2,0]

    def move_right(self):
        for r in range(len(self.__map)):
            self.__list_merge[:]=self.__map[r][::-1] #[2,0,4,2]
            self.merge()                            #[2,4,2,0]
            self.__map[r][::-1]=self.__list_merge   #[0,2,4,2]


    def move_up(self):
        for c in range(4):
            self.__list_merge.clear()
            for r in range(4):
                self.__list_merge.append(self.__map[r][c])      #[2,2,2,4]
            self.merge()                                        #[4,0,2,4] -->[4,2,4,0]
            for r in range(4):                                  #
                self.__map[r][c]=self.__list_merge[r]           #


    def move_down(self):
        for c in range(4):
            self.__list_merge.clear()
            for r in range(3,-1,-1):
                self.__list_merge.append(self.__map[r][c])  #[4,2,2,2]
            self.merge()                                    #[4,4,0,0]
            for r in range(3,-1,-1):
                self.__map[r][c]=self.__list_merge[3-r]

    def __calculate_empty_location(self):
        self.__list_empty_location.clear()
        for r in range(4):
            for c in range(4):
                if self.__map[r][c]==0:
                    loc=Location(r,c)
                    self.__list_empty_location.append(loc)

    def generate_new_number(self):
        self.__calculate_empty_location()
        if len(self.__list_empty_location)==0:
            return
        loc=random.choice(self.__list_empty_location)
        self.__map[loc.r_index][loc.c_index]=4 if random.randint(1,10)==1 else 2
        self.__list_empty_location.remove(loc)


    def is_game_over(self):
        if len(self.__list_empty_location)>0:
            return False

        #2.横向具有相同的元素，游戏不能结束
        for r in range(4):
            for c in range(3):
                if self.__map[r][c]==self.__map[r][c+1]:
                    return False
        #3.竖向具有相同的元素，游戏不能结束
        for r in range(3):
            for c in range(4):
                if self.__map[r][c]==self.__map[r+1][c]:
                    return False

        #2+3
        for r in range(4):
            for c in range(3):
                if self.__map[r][c] == self.__map[r][c + 1] or self.__map[c][r]==self.__map[c+1][r]:
                    return False
        return True


    def move(self,dir):
        self.is_change=False

        original_map=copy.deepcopy(self.__map)

        if dir==Direction.up:
            self.move_up()

        if dir==Direction.down:
            self.move_down()

        if dir==Direction.left:
            self.move_left()

        if dir==Direction.right:
            self.move_right()

        self.is_change=self.__equal_map(original_map)

    def __equal_map(self,original):
        for r in range(4):
            for c in range(4):
                if original[r][c]!=self.__map[r][c]:
                    return True
        return False






def print_map(map):
    print("--------------")
    for r in range(len(map)):
        for c in range(len(map[r])):
            print(map[r][c],end=" ")
        print()
    print("--------------")

if __name__ == '__main__':

    core=GameCoreController()
    print_map(core.map)
    # core.move_up()
    # print_map(core.map)
    # core.move_down()
    # print_map(core.map)
    # core.move_right()
    # print_map(core.map)
    # core.move_left()
    # print_map(core.map)
    core.generate_new_number()
    core.generate_new_number()
    core.generate_new_number()
    print_map(core.map)


