from typing import Union

from hole import Hole


class PlayerHole(Hole):
    def __init__(self, player: str, index: Union[str, int], number_of_rocks, linked_hole=None):
        super().__init__(player, index, number_of_rocks, linked_hole)
        self.number_of_rocks = 11

    def take_rocks(self, name=None):
        hole = self.get_by_name(name)
        return hole.number_of_rocks
