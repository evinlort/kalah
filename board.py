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
        if start_name[-1] == "0":
            return False, "Can't take rocks from player's gather hole"
        start_hole = self.ll_hole.get_by_name(start_name)
        rocks_to_scatter = start_hole.take_rocks()
        if not rocks_to_scatter:
            return False, f"No rocks in hole {start_name}"
        working_on_hole = start_hole.linked_hole
        while rocks_to_scatter:
            working_on_hole.add_rock()
            rocks_to_scatter -= 1
            working_on_hole = working_on_hole.linked_hole
        self.check_rules()
        return True, "OK"

    def check_rules(self):
        pass

    def draw(self):
        board_map = [
            ["b6", "b5", "b4", "b3", "b2", "b1"],
            ["b0", "a0"],
            ["a1", "a2", "a3", "a4", "a5", "a6"],
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
