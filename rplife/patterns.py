from typing import Set, Tuple
from dataclasses import dataclass
from pathlib import Path
import tomllib  # needs python > 3.11

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

PATTERNS_FILE = Path(__file__).parent / "patterns.toml"

def get_pattern(name, filename=PATTERNS_FILE):
    data = tomllib.loads(filename.read_text(encoding="utf-8"))
    return Pattern.from_toml(name, toml_data=data[name])

def get_all_patterns(filename=PATTERNS_FILE):
    data = tomllib.loads(filename.read_text(encoding="utf-8"))
    return [
        Pattern.from_toml(name, toml_data) for name, toml_data in data.items()
    ]
    
