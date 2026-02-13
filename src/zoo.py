"""Класс Zoo, демонстрирующий композицию и управление коллекцией."""

from typing import List, Optional
from src.animal import Animal


class Zoo:
    """
    Класс Zoo, управляющий коллекцией животных.
    """

    def __init__(self, name: str, location: str) -> None:
        """
        Инициализация зоопарка.
        
        Аргументы:
            name: Название зоопарка
            location: Локация зоопарка
        """
        self._name = name
        self._location = location
        self._animals: List[Animal] = []

    # Здесь можно добавить нужные методы для управления животными в зоопарке (нужно чтобы тесты проходили)

    @property
    def name(self) -> str:
        return self._name

    @property
    def location(self) -> str:
        return self._location

    @property
    def animals(self) -> List[Animal]:
        return self._animals.copy()

    def add_animal(self, animal: Animal) -> None:
        self._animals.append(animal)

    def remove_animal(self, animal: Animal) -> bool:
        if animal in self._animals:
            self._animals.remove(animal)
            return True
        return False

    def find_animal_by_name(self, name: str) -> Optional[Animal]:
        for animal in self._animals:
            if animal.name == name:
                return animal
        return None

    def get_animal_count(self) -> int:
        return len(self._animals)

    def get_species_count(self, species: str) -> int:
        return sum(1 for a in self._animals if a.__class__.__name__ == species)

    def get_all_sounds(self) -> List[str]:
        return [a.make_sound() for a in self._animals]

    def feed_all(self) -> None:
        for animal in self._animals:
            animal.eat("food")

    def exercise_all(self, minutes: int = 10) -> None:
        for animal in self._animals:
            exercise = getattr(animal, "exercise", None)
            if callable(exercise):
                exercise(minutes)
            else:
                animal.make_sound()

    def display_animals(self) -> None:
        for animal in self._animals:
            print(animal)