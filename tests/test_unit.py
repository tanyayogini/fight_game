import pytest

from classes import Thief, Warrior
from equipment import Weapon, Armor
from unit import PlayerUnit, EnemyUnit

hero1 = PlayerUnit(name='test_unit1', unit_class=Warrior)
hero1.stamina = 10
hero1.unit_class.stamina = 0.9
hero1.unit_class.attack = 1.1
hero1.create_weapon(Weapon(10, 'test_weapon', 2.4, 2.4, 2))

hero2 = EnemyUnit(name='test_unit2', unit_class=Thief)
hero2.stamina = 10
hero2.health = 10
hero2.unit_class.stamina = 1.1
hero2.unit_class.armor = 0.8
hero2.create_armor(Armor(10, 'test_armor', 2, 1.5))

hero3 = EnemyUnit(name='test_unit3', unit_class=Thief)
hero3.stamina = 0.8
hero3.health = 10
hero3.unit_class.stamina = 1.1
hero3.unit_class.armor = 0.8
hero3.create_armor(Armor(10, 'test_armor', 2, 1.5))

class TestBaseUnit:
    def test_count_damage(self):
        assert hero1._count_damage(hero2) == 1.0
        assert hero1.stamina == 8
        assert hero2.stamina == 8.5

        hero1.stamina = 10
        assert hero1._count_damage(hero3) == 2.6
        assert hero1.stamina == 8
        assert hero3.stamina == 0.8

    def test_get_damage(self):
        assert hero2.health == 9
        assert hero3.health == 7.4

