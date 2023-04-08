import pytest

from classes import Warrior, Thief
from unit import PlayerUnit
from skills import FerociousKick

hero1 = PlayerUnit(name='test_unit1', unit_class=Warrior)
hero2 = PlayerUnit(name='test_unit2', unit_class=Thief)
skill = FerociousKick()


class TestFerociousKick:
    def test_is_stamina_enough(self):
        skill.user = hero1
        assert skill._is_stamina_enough() is True
        skill.demand_stamina = 31
        assert skill._is_stamina_enough() is False
        skill.demand_stamina = 6

    def test_skill_effect(self):
        skill.user = hero1
        skill.target = hero2
        assert skill.skill_effect() == "test_unit1 использует Свирепый пинок и наносит 12 урона сопернику."

    def test_use(self):
        assert skill.use(user=hero1, target=hero2) == "test_unit1 использует Свирепый пинок и наносит 12 урона сопернику."
        skill.demand_stamina = 31
        assert skill.use(user=hero1, target=hero2) == "test_unit1 попытался использовать Свирепый пинок, но у него не хватило выносливости."

