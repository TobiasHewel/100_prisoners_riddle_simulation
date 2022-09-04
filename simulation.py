from asyncio import constants
import random


instances = []


class Prisoner:
    def __init__(self):
        self.id = 1

    def random_tactic(boxes):
        print("RANDOM TACTIC!")


class Instance:
    def __init__(self):
        self.prisoners = []
        self.boxes = {}
        self.survived = None

        for i in range(0, 9):
            self.prisoners.append(Prisoner())

        box_numbers = list(range(0, 9))
        random.shuffle(box_numbers)

        for i in range(0, 9):
            self.boxes[i] = box_numbers[i]

    def run(self, tactic):
        print(tactic)
        match tactic:
            case "random":
                print(self.prisoners.id)
                # self.prisoners[0].random_tactic(self.boxes)


instances.append(Instance())
instance1 = Instance()

instance1.run(tactic="random")
