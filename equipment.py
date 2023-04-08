from random import uniform
import json
from dataclasses import dataclass
from typing import Optional
import marshmallow_dataclass
import os

FILEPATH = os.path.abspath("./data/equipment.json")


@dataclass
class Weapon:
    id: int
    name: str
    min_damage: float
    max_damage: float
    stamina_per_hit: float

    @property
    def count_damage(self) -> float:
        return round(uniform(self.min_damage, self.max_damage), 1)


@dataclass
class Armor:
    id: int
    name: str
    defence: float
    stamina_per_turn: float


class EquipmentData:
    weapons: list[Weapon]
    armors: list[Armor]


class Equipment:

    def __init__(self):
        self.equipment = self._create_equipment()

    def get_weapon(self, weapon_name: str) -> Optional[Weapon]:
        for weapon in self.equipment.weapons:
            if weapon.name == weapon_name:
                return weapon
        return None

    def get_armor(self, armor_name: str) -> Optional[Armor]:
        for armor in self.equipment.armors:
            if armor.name == armor_name:
                return armor
        return None

    def get_weapon_names(self) -> list:
        return [weapon.name for weapon in self.equipment.weapons]

    def get_armor_names(self) -> list:
        return [armor.name for armor in self.equipment.armors]

    @staticmethod
    def _create_equipment() -> EquipmentData:
        with open(FILEPATH, "r", encoding="utf-8") as f:
            data = json.load(f)
            equipment_schema = marshmallow_dataclass.class_schema(EquipmentData)
            return equipment_schema().load(data)
