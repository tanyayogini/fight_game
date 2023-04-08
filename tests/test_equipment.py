import pytest
from equipment import Equipment
equipment = Equipment()


class TestEquipment:
    def test_get_weapon(self):
        assert equipment.get_weapon("топорик") is not None
        assert equipment.get_weapon("test_eq") is None

    def test_get_weapon_name(self):
        assert equipment.get_weapon_names() == ["топорик", "ножик", "ладошки"]


