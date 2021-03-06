from __future__ import annotations

from typing import Union


class Hole:
    def __init__(self, player: str, index: Union[str, int], number_of_rocks: int, linked_hole: Hole = None):
        self.player = player.upper()
        self.number_of_rocks = number_of_rocks
        self.name = player + str(index)
        self.linked_hole = linked_hole

    def link_to(self, hole):
        self.linked_hole = hole

    def get_by_name(self, name: str):
        counter = 14
        next_hole = self
        while counter:
            if next_hole.name == name.lower():
                return next_hole
            counter -= 1
            next_hole = next_hole.linked_hole
        raise Exception("No such name found")

    def take_rocks(self):
        rocks = self.number_of_rocks
        self.number_of_rocks = 0
        return rocks

    def add_rock(self):
        self.number_of_rocks += 1

    def set_rocks(self, number: int = 1):
        self.number_of_rocks = number
