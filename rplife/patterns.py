from typing import Set, Tuple
from dataclasses import dataclass

@dataclass
class Pattern:
    name: str
    alive_cells: Set[Tuple[int, int]]
