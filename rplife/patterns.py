from typing import Set, Tuple
from dataclasses import dataclass

@dataclass
class Pattern:
    name: str
    alive_cells: Set[Tuple[int, int]]

    @classmethod
    def from_toml(cls, name, toml_data):
        return cls(
            name,
            alive_cells = {tuple(cell) for cell in toml_data["alive_cells"]},
        )
