from game2048.bill import GameCoreController


class GameCoreView:
    def __init__(self):
        self.__controller=GameCoreController()
    def main(self):
        self.__start()
        self.update()
    def __start(self):
        self.__controller.add_random_digits()
        self.__controller.add_random_digits()
        self.draw_map()
    def draw_map(self):
        for line in self.__controller.map:
            for item in line:
                print(item,end="\t")
            print()
    def update(self):
        while True:
            dic=input("请输入")
            self.move_map(dic)
            self.__controller.add_random_digits()
            self.draw_map()
            if self.__controller.judgement_game_over():
                print("游戏结束")
                self.__start()

    def move_map(self, dic):
            if dic == "w":
                self.__controller.move_up()
            elif dic == "s":
                self.__controller.move_down()
            elif dic == "a":
                self.__controller.move_left()
            elif dic == "d":
                self.__controller.move_right()