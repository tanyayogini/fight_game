import pytest
from arena import Arena
from classes import Warrior, Thief
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

arena = Arena()
arena.player = hero1
arena.enemy = hero2

hero1.stamina = 8
hero2.stamina = 8.5

class TestArena:
    def test_stamina_regeneration(self):
        arena._stamina_regeneration()
        assert hero1.stamina == 8.9
        assert hero2.stamina == 9.6

