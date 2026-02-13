"""Основные тесты для проекта OOP."""

import unittest
from src.animals import Dog, Cat, Bird
from src.zoo import Zoo


class TestAnimal(unittest.TestCase):
    """Тесты для классов животных."""

    def setUp(self) -> None:
        """Set up test fixtures."""
        self.dog = Dog("Max", 3, "Labrador")
        self.cat = Cat("Luna", 2, "Gray")
        self.bird = Bird("Polly", 1, "Parrot")

    def test_dog_initialization(self) -> None:
        """Тестирование инициализации собаки."""
        self.assertEqual(self.dog.name, "Max")
        self.assertEqual(self.dog.age, 3)
        self.assertEqual(self.dog.breed, "Labrador")

    def test_dog_sound(self) -> None:
        """Тестирование звука собаки."""
        self.assertIn("Woof", self.dog.make_sound())

    def test_dog_tricks(self) -> None:
        """Тестирование обучения трюкам."""
        self.dog.teach_trick("Fetch")
        self.assertIn("performed", self.dog.perform_trick("Fetch"))

    def test_cat_sound(self) -> None:
        """Тестирование звука кота."""
        self.assertIn("Meow", self.cat.make_sound())

    def test_cat_eat(self) -> None:
        """Тестирование коконмления кота."""
        self.cat.exercise(20)  # Уменьшить энергию
        initial_energy = self.cat.energy
        self.cat.eat("fish")
        self.assertGreater(self.cat.energy, initial_energy)

    def test_bird_fly(self) -> None:
        """Тестирование полета птицы."""
        result = self.bird.fly(50)
        self.assertIn("flew", result)
        self.assertEqual(self.bird.altitude, 50)

    def test_bird_cannot_fly(self) -> None:
        """Тестирование нелетающей птицы."""
        penguin = Bird("Pingu", 5, "Penguin", can_fly=False)
        result = penguin.fly(100)
        self.assertIn("cannot fly", result)

    def test_sleep(self) -> None:
        """Тестирование функции сна."""
        self.dog.energy  # Store reference
        self.dog.exercise(30)  # Reduce energy
        self.dog.sleep(2)  # Restore energy
        self.assertGreater(self.dog.energy, 40)

    def test_info_string(self) -> None:
        """Тестирование генерации строки информации."""
        info = self.dog.get_info()
        self.assertIn("Max", info)
        self.assertIn("Dog", info)


class TestZoo(unittest.TestCase):
    """Тесты для класса Zoo."""

    def setUp(self) -> None:
        """Подготовка тестовых ресурсов."""
        self.zoo = Zoo("Test Zoo", "TestCity")
        self.dog = Dog("Buddy", 4, "Beagle")
        self.cat = Cat("Mittens", 1, "White")

    def test_zoo_initialization(self) -> None:
        """Тестирование инициализации зоопарка."""
        self.assertEqual(self.zoo.name, "Test Zoo")
        self.assertEqual(self.zoo.location, "TestCity")
        self.assertEqual(self.zoo.get_animal_count(), 0)

    def test_add_animal(self) -> None:
        """Тестирование добавления животных."""
        self.zoo.add_animal(self.dog)
        self.assertEqual(self.zoo.get_animal_count(), 1)

    def test_remove_animal(self) -> None:
        """Тестирование от удаления животных."""
        self.zoo.add_animal(self.dog)
        result = self.zoo.remove_animal(self.dog)
        self.assertTrue(result)
        self.assertEqual(self.zoo.get_animal_count(), 0)

    def test_find_animal_by_name(self) -> None:
        """Тестирование поиска животного по имени."""
        self.zoo.add_animal(self.dog)
        found = self.zoo.find_animal_by_name("Buddy")
        self.assertEqual(found, self.dog)

    def test_species_count(self) -> None:
        """Тестирование посчета видов."""
        self.zoo.add_animal(self.dog)
        self.zoo.add_animal(self.cat)
        self.assertEqual(self.zoo.get_species_count("Dog"), 1)
        self.assertEqual(self.zoo.get_species_count("Cat"), 1)

    def test_get_all_sounds(self) -> None:
        """Тестирование получения всех звуков."""
        self.zoo.add_animal(self.dog)
        self.zoo.add_animal(self.cat)
        sounds = self.zoo.get_all_sounds()
        self.assertEqual(len(sounds), 2)

    def test_animals_property(self) -> None:
        """Тестирование тоже свойство возвращает копию."""
        self.zoo.add_animal(self.dog)
        animals_copy = self.zoo.animals
        self.assertEqual(len(animals_copy), 1)
        # Проверить, что это копия, а не исходный список
        animals_copy.append(self.cat)
        self.assertEqual(self.zoo.get_animal_count(), 1)


if __name__ == "__main__":
    unittest.main()