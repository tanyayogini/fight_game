from abc import ABC, abstractmethod
from classes import UnitClass
from equipment import Weapon, Armor
from random import randint


class BaseUnit(ABC):
    def __init__(self, name: str, unit_class: UnitClass):
        self.name = name
        self.unit_class = unit_class
        self.health = unit_class.max_health
        self.stamina = unit_class.max_stamina
        self.weapon = None
        self.armor = None
        self.is_skill_used = False

    @property
    def health_points(self) -> float:
        return round(self.health, 1)

    @property
    def stamina_points(self) -> float:
        return round(self.stamina, 1)

    def create_weapon(self, weapon: Weapon):
        self.weapon = weapon

    def create_armor(self, armor: Armor):
        self.armor = armor

    def _count_damage(self, target) -> float:
        self.stamina -= self.weapon.stamina_per_hit
        damage = self.weapon.count_damage * self.unit_class.attack

        if target.stamina >= target.armor.stamina_per_turn:
            target.stamina -= target.armor.stamina_per_turn
            damage -= target.armor.stamina_per_turn * target.unit_class.stamina

        damage = round(damage, 1)
        target.get_damage(damage)
        return damage

    def get_damage(self, damage: float):
        if damage > 0:
            self.health -= damage

    @abstractmethod
    def hit(self, target) -> str:
        pass

    def use_skill(self, target) -> str:
        if self.is_skill_used:
            return "Навык уже использован."

        result = self.unit_class.skill.use(self, target)
        self.is_skill_used = True
        return result


class PlayerUnit(BaseUnit):
    def hit(self, target: BaseUnit) -> str:
        if self.stamina < self.weapon.stamina_per_hit:
            return (
                f"{self.name} попытался использовать {self.weapon.name}, "
                f"но у него не хватило выносливости.")

        damage = self._count_damage(target)
        if damage > 0:
            return (
                f"{self.name}, используя {self.weapon.name}, "
                f"пробивает {target.armor.name} соперника и наносит {damage} урона."
            )

        return (
            f"{self.name}, используя {self.weapon.name}, наносит удар, "
            f"но {target.armor.name} соперника его останавливает."
        )


class EnemyUnit(BaseUnit):

    def hit(self, target: BaseUnit) -> str:

        if not self.is_skill_used and self.stamina >= self.unit_class.skill.demand_stamina and randint(0, 100) < 10:
            return self.use_skill(target)
        if self.stamina < self.weapon.stamina_per_hit:
            return (
                f"{self.name} попытался использовать {self.weapon.name}, "
                f"но у него не хватило выносливости.")

        damage = self._count_damage(target)
        if damage > 0:
            return (
                f"{self.name}, используя {self.weapon.name}, "
                f"пробивает {target.armor.name} и наносит Вам {damage} урона."
            )

        return (
            f"{self.name}, используя {self.weapon.name}, наносит удар, "
            f"но Ваш(а) {target.armor.name} его останавливает."
        )
