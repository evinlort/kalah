from hole import Hole, PlayerHole


class Board:
    def __init__(self, rocks=3):
        self.ll_hole = self.build_holes(rocks)

    def __iter__(self):
        return self

    def __next__(self):
        self.ll_hole = self.ll_hole.linked_hole
        return self.ll_hole

    @staticmethod
    def build_holes(rocks) -> Hole:
        start_hole = None
        prev_hole = None
        for i in range(14, 0, -1):
            if i // 8:
                player = "b"
            else:
                player = "a"
            index = i % 7
            if index == 0:
                hole = PlayerHole(player, index, rocks, prev_hole)
            else:
                hole = Hole(player, index, rocks, prev_hole)
            if i == 14:
                start_hole = hole
            prev_hole = hole
        start_hole.link_to(prev_hole)
        return start_hole

    def scatter(self, start_name):
        pass

    def draw(self):
        board_map = [
            ["a1", "a2", "a3", "a4", "a5", "a6"],
            ["b0", "a0"],
            ["b1", "b2", "b3", "b4", "b5", "b6"]
        ]
        for line in board_map:
            if len(line) == 2:
                print(str(self.ll_hole.get_by_name(line[0]).number_of_rocks).ljust(2),
                      "  " * 7,
                      str(self.ll_hole.get_by_name(line[1]).number_of_rocks).rjust(2))
            else:
                print("  ", end="")
                for pos in line:
                    print(self.ll_hole.get_by_name(pos).number_of_rocks, end="  ")
                print()
