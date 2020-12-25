"""
    2048游戏核心算法
"""
import random
class GameCoreController:
    def __init__(self):
        self.list_merge=None
        self.__map = [[0, 0, 0, 0],
                     [0, 0, 0, 0 ],
                     [0, 0, 0, 0 ],
                     [0, 0, 0, 0]]
        self.__list_blank_location=[]
    @property
    def map(self):
        return self.__map
    def __zero_to_end(self):
        for i in self.list_merge[::-1]:
            if i == 0:
                self.list_merge.remove(i)
                self.list_merge.append(0)

    def __merge_element(self):
        self.__zero_to_end()
        for m in range(len(self.list_merge) - 1):
            if self.list_merge[m] == self.list_merge[m + 1]:
                self.list_merge[m] = self.list_merge[m] * 2
                del self.list_merge[m + 1]
                self.list_merge.append(0)

    def move_left(self):
        for line in self.map:
            self.list_merge = line
            self.__merge_element()

    def move_right(self):
        for line in self.__map:
            self.list_merge = line[::-1]
            self.__merge_element()
            line[::-1] = self.list_merge

    def __transpose(self):
        for c in range(0, 3):
            for i in range(c + 1, 4):
                self.map[i][c], self.map[c][i] = self.map[c][i], self.map[i][c]

    def move_up(self):
        self.__transpose()
        self.move_left()
        self.__transpose()

    def move_down(self):
        self.__transpose()
        self.move_right()
        self.__transpose()

    def random_digits(self,a,b):
        return random.randint(a,b)

    def add_random_digits(self):
        self.__list_blank_location.clear()
        self.calculate_blank(self.__list_blank_location)
        number=self.random_digits(0,len(self.__list_blank_location)-1)
        number01=self.__list_blank_location[number][0]
        number02=self.__list_blank_location[number][1]
        self.map[number01][number02]=self.craet_random_number()

    def calculate_blank(self,list_zero):
        for i in range(len(self.map)):
            for c in range(len(self.map)):
                if self.map[i][c] == 0:
                    list_zero.append((i, c))

    def craet_random_number(self):
        number=self.random_digits(1,10)
        if 0<number<10:
            return 2
        else:
            return 4

    def judgement_game_over(self):
        if len(self.__list_blank_location):return False
        for i in range(4):
            for c in range(3):
                if self.map[i][c]==self.map[i][c+1]or self.map[c][i]==self.map[c+1][i]:
                    return False
        return True








