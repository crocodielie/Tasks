from __future__ import annotations

class Car:
    """
    Класс Car представляет автомобиль с определённой мощностью двигателя и объёмом топливного бака.

    Атрибуты:
    - engine_power (int): Мощность двигателя автомобиля.
    - fuel_volume (int): Объём топливного бака.
    - current_fuel (int): Текущее количество топлива в баке.

    Методы:
    - refilling(volume: int): Заправка автомобиля.
    - engine_upgrade(delta_power: int): Улучшение мощности двигателя.
    """
    def __init__(self, engine_power: int, fuel_volume: int):
        self.engine_power = engine_power
        self.fuel_volume = fuel_volume
        self.current_fuel = 0

    def refilling(self, volume: int):
        """
        Заправляет автомобиль топливом.

        Аргументы:
            volume (int): Объём топлива для заправки.

        Raises:
            TypeError: Если объём топлива не является целым числом.
            ValueError: Если объём топлива отрицательный или превышает допустимый объём.

        >>> car = Car(150, 50)
        >>> car.refilling(20)
        >>> car.current_fuel
        20
        >>> car.refilling(40)
        Traceback (most recent call last):
            ...
        ValueError: The amount of fuel must not exceed the permissible amount
        """
        if not isinstance(volume, int):
            raise TypeError("The volume of refueled fuel must be int")
        if volume < 0:
            raise ValueError("The volume of refueled fuel must be positive")
        if self.current_fuel + volume > self.fuel_volume:
            raise ValueError("The amount of fuel must not exceed the permissible amount")
        else:
            self.current_fuel += volume

    def engine_upgrade(self, delta_power: int):
        """
        Улучшает мощность двигателя.

        Аргументы:
            delta_power (int): На сколько увеличить мощность двигателя.

        Raises:
            TypeError: Если delta_power не является целым числом.

        >>> car = Car(150, 50)
        >>> car.engine_upgrade(20)
        >>> car.engine_power
        170
        """
        if not isinstance(delta_power, int):
            raise TypeError("The delta power must be int")
        self.engine_power += delta_power


class Person:
    """
    Класс Person представляет человека с именем, возрастом и семейным статусом.

    Атрибуты:
    - name (str): Имя человека.
    - age (int): Возраст человека.
    - marital_status (int): Семейный статус (0 - одинок, 1 - в браке, 2 - влюблён, 3 - встречается).
    - partner_name (str | None): Имя партнёра.

    Методы:
    - set_marital_status(status: int): Устанавливает семейный статус.
    - set_partner_name(name: str): Устанавливает имя партнёра.
    """
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.marital_status = 0
        self.partner_name = None

    def set_marital_status(self, status: int):
        """
        Устанавливает семейный статус.

        Аргументы:
            status (int): Новый статус.

        Raises:
            TypeError: Если статус не является целым числом.

        >>> person = Person("Alice", 25)
        >>> person.set_marital_status(1)
        >>> person.marital_status
        1
        """
        if not isinstance(status, int):
            raise TypeError("The status must be int")
        if status not in (0, 1):
            raise ValueError("Marital status must be 0 or 1")
        self.marital_status = status

    def set_partner_name(self, name: str):
        """
        Устанавливает имя партнёра.

        Аргументы:
            name (str): Имя партнёра.

        Raises:
            TypeError: Если имя партнёра не является строкой.
            ValueError: Если семейный статус равен 0 (одинок(ая)).

        >>> person = Person("Alice", 25)
        >>> person.set_marital_status(1)
        >>> person.set_partner_name("Bob")
        >>> person.partner_name
        'Bob'
        """
        if not isinstance(name, str):
            raise TypeError("The name must be str")
        if self.marital_status == 0:
            raise ValueError("Person hasn't got a partner if he/she is lonely")
        self.partner_name = name


class Water:
    """
    Класс Water представляет воду с массой и температурой.

    Атрибуты:
    - mass (int): Масса воды.
    - temperature (int): Температура воды.

    Методы:
    - change_temperature(delta: int): Изменяет температуру воды.
    - adding_water(another_water: Water): Добавляет другую воду.
    """
    def __init__(self, mass: int, temperature: int):
        self.mass = mass
        self.temperature = temperature

    def change_temperature(self, delta: int):
        """
        Изменяет температуру воды.

        Аргументы:
            delta (int): Изменение температуры.

        Raises:
            TypeError: Если delta не является целым числом.

        >>> water = Water(1000, 20)
        >>> water.change_temperature(10)
        >>> water.temperature
        30
        """
        if not isinstance(delta, int):
            raise TypeError("The delta temperature must be int")
        self.temperature += delta

    def adding_water(self, another_water: Water):
        """
        Добавляет другую воду, изменяя массу и температуру.

        Аргументы:
            another_water (Water): Вода для добавления.

        Raises:
            TypeError: Если another_water не является экземпляром Water.

        >>> water1 = Water(1000, 20)
        >>> water2 = Water(500, 40)
        >>> water1.adding_water(water2)
        >>> water1.mass
        1500
        >>> water1.temperature
        26
        """
        if not isinstance(another_water, Water):
            raise TypeError("To stack, the water must be of the appropriate class")
        total_mass = self.mass + another_water.mass
        self.temperature = (self.mass * self.temperature + another_water.mass * another_water.temperature) // total_mass
        self.mass = total_mass


if __name__ == "__main__":
    import doctest
    doctest.testmod()