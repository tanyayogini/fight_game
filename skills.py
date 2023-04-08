from abc import ABC, abstractmethod


class Skill(ABC):
    user = None
    target = None

    @property
    @abstractmethod
    def skill_name(self):
        pass

    @property
    @abstractmethod
    def skill_damage(self):
        pass

    @property
    @abstractmethod
    def demand_stamina(self):
        pass

    @abstractmethod
    def skill_effect(self) -> str:
        pass

    def _is_stamina_enough(self) -> bool:
        return self.user.stamina >= self.demand_stamina

    def use(self, user, target) -> str:
        self.user = user
        self.target = target
        if self._is_stamina_enough():
            return self.skill_effect()
        return f"{self.user.name} попытался использовать {self.skill_name}, но у него не хватило выносливости."


class FerociousKick(Skill):
    skill_name: str = "Свирепый пинок"
    demand_stamina: int = 6
    skill_damage: int = 12

    def skill_effect(self):
        self.user.stamina -= self.demand_stamina
        self.target.get_damage(self.skill_damage)

        return f"{self.user.name} использует {self.skill_name} и наносит {self.skill_damage} урона сопернику."


class PowerfulThrust(Skill):
    skill_name: str = "Мощный укол"
    demand_stamina: int = 5
    skill_damage: int = 15

    def skill_effect(self):
        self.user.stamina -= self.demand_stamina
        self.target.get_damage(self.skill_damage)

        return f"{self.user.name} использует {self.skill_name} и наносит {self.skill_damage} урона сопернику."
