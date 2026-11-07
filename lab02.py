
from abc import ABC, abstractmethod


class GameObject:
    def __init__(self, object_id, name, x, y):
        self._id = object_id
        self._name = name
        self._x = x
        self._y = y

    def getId(self):
        return self._id

    def getName(self):
        return self._name

    def getX(self):
        return self._x

    def getY(self):
        return self._y


class Attacker(ABC):
    @abstractmethod
    def attack(self, unit):
        pass


class Moveable(ABC):
    @abstractmethod
    def move(self, x, y):
        pass


class Unit(GameObject):
    def __init__(self, object_id, name, x, y, hp):
        super().__init__(object_id, name, x, y)
        self._hp = float(hp)

    def isAlive(self):
        return self._hp > 0

    def getHp(self):
        return self._hp

    def receiveDamage(self, damage):
        if damage < 0:
            raise ValueError("Damage cannot be negative")
        self._hp = max(0.0, self._hp - damage)


class Archer(Unit, Attacker, Moveable):
    def attack(self, unit):
        if not isinstance(unit, Unit):
            raise TypeError("Target must be a Unit")
        if self.isAlive() and unit.isAlive():
            unit.receiveDamage(20)

    def move(self, x, y):
        if self.isAlive():
            self._x = x
            self._y = y


class Building(GameObject):
    def __init__(self, object_id, name, x, y, built=False):
        super().__init__(object_id, name, x, y)
        self._built = built

    def isBuilt(self):
        return self._built


class Fort(Building, Attacker):
    def attack(self, unit):
        if not isinstance(unit, Unit):
            raise TypeError("Target must be a Unit")
        if self.isBuilt() and unit.isAlive():
            unit.receiveDamage(30)


class MobileHouse(Building, Moveable):
    def move(self, x, y):
        self._x = x
        self._y = y


if __name__ == "__main__":
    archer1 = Archer(1, "Archer 1", 0, 0, 100)
    archer2 = Archer(2, "Archer 2", 5, 5, 100)
    fort = Fort(3, "Fort", 10, 10, True)
    house = MobileHouse(4, "Mobile house", 2, 2, True)

    archer1.attack(archer2)
    print("Archer 2 HP:", archer2.getHp())

    fort.attack(archer1)
    print("Archer 1 HP:", archer1.getHp())

    archer1.move(3, 4)
    house.move(7, 8)

    print("Archer 1 position:", archer1.getX(), archer1.getY())
    print("Mobile house position:", house.getX(), house.getY())
