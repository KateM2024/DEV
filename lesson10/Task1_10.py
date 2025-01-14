from abc import ABC, abstractmethod
from typing import List

"""
# Цветочница.

# Определить иерархию и создать несколько цветов.
Собрать букет с использованием аксессуаров с
определением его стоимости.

# Определить время его увядания по среднему времени
жизни всех цветов в букете.

# Позволить сортировку цветов по стоимости.

# Узнать, есть ли цветок в букете.
"""


class Flower(ABC):
    """Абстрактный класс для цветов."""

    def __init__(self, name: str, cost: float, lifespan: int):
        """
        Инициализация цветка.
        :param name: Название цветка.
        :param cost: Стоимость цветка.
        :param lifespan: Время жизни цветка (в часах).
        """
        self.name = name
        self.cost = cost
        self.lifespan = lifespan

    @abstractmethod
    def __str__(self):
        """Возвращает строковое представление цветка."""
        pass

class Rose(Flower):
    def __str__(self):
        return f"Rose {super().__str__()}"


class Tulip(Flower):
    def __str__(self):
        return f"Tulip {super().__str__()}"

class Daisy(Flower):
    def __str__(self):
        return (f"Daisy {super().__str__()}")

class Accessory:
    """Класс для аксессуаров."""

    def __init__(self, name: str, cost: float):
        """
        Инициализация аксессуара.
        :param name: Название аксессуара.
        :param cost: Стоимость аксессуара.
        """
        self.name = name
        self.cost = cost

    def __str__(self):
        return f"Accessory(name={self.name}, cost={self.cost})"

class Bouquet:
    """Класс для букета."""

    def __init__(self):
        self.flowers: List[Flower] = []
        self.accessories: List[Accessory] = []

    def add_flower(self, flower: Flower):
        """Добавить цветок в букет."""
        self.flowers.append(flower)

    def add_accessory(self, accessory: Accessory):
        """Добавить аксессуар в букет."""
        self.accessories.append(accessory)

    def calculate_cost(self) -> float:
        """Рассчитать общую стоимость букета."""
        flower_cost = sum(flower.cost for flower in self.flowers)
        accessory_cost = sum(accessory.cost for accessory in self.accessories)
        return flower_cost + accessory_cost

    def average_lifespan(self) -> float:
        """Определить среднее время увядания букета."""
        if not self.flowers:
            return 0
        return sum(flower.lifespan for flower in self.flowers) / len(self.flowers)

    def sort_by_cost(self):
        """Сортировать цветы в букете по стоимости."""
        self.flowers = sorted(self.flowers, key=lambda flower: flower.cost)

    def contains_flower(self, flower_name: str) -> bool:
        """Проверить, есть ли цветок в букете."""
        return any(flower.name == flower_name for flower in self.flowers)

    def __str__(self):
        bouquet_items = "\n".join(str(flower) for flower in self.flowers)
        accessories = "\n".join(str(accessory) for accessory in self.accessories)
        return f"Bouquet:\nFlowers:\n{bouquet_items}\nAccessories:\n{accessories}"


# Пример использования
if __name__ == "__main__":
    # Создание цветов
    rose = Rose(name="Rose", cost=5.0, lifespan=72)
    tulip = Tulip(name="Tulip", cost=3.0, lifespan=48)
    daisy = Daisy(name="Daisy", cost=2.5, lifespan=36)

    # Создание аксессуаров
    ribbon = Accessory(name="Ribbon", cost=1.0)
    paper = Accessory(name="Wrapping Paper", cost=2.0)

    # Создание букета
    bouquet = Bouquet()
    bouquet.add_flower(rose)
    bouquet.add_flower(tulip)
    bouquet.add_flower(daisy)
    bouquet.add_accessory(ribbon)
    bouquet.add_accessory(paper)

    # Вывод

    print(bouquet)

    # Стоимость букета
    print("\nTotal cost:", bouquet.calculate_cost())

    # Среднее время жизни
    print("Average lifespan (hours):", bouquet.average_lifespan())

    # Сортировка цветов по стоимости
    bouquet.sort_by_cost()
    print("\nBouquet after sorting by cost:")
    print(bouquet)

    # Проверка на наличие цветка
    print("\nContains 'Rose':", bouquet.contains_flower("Rose"))
    print("Contains 'Orchid':", bouquet.contains_flower("Orchid"))
