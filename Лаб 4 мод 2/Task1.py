if __name__ == "__main__":
    class Car:
        """
        Базовый класс для автомобилей.
        """

        def __init__(self, brand: str, model: str, power: float, max_speed: int) -> None:
            """
            Инициализирует объект автомобиля.
            :param brand: Марка автомобиля
            :param model: Модель автомобиля
            :param power: Мощность двигателя
            :param max_speed: Максимальная скорость
            """
            self._brand = brand  # Инкапсулированный атрибут, так как бренд не должен изменяться после создания объекта
            self._model = model  # Аналогично
            self.power = power
            self.max_speed = max_speed

        def __str__(self) -> str:
            """
            Возвращает строковое представление автомобиля для пользователя.
            """
            return f"Автомобиль {self._brand} {self._model} ({self.power}) - {self.max_speed}"

        def __repr__(self) -> str:
            """
            Возвращает строковое представление объекта для разработчика.
            """
            return f"{self.__class__.__name__}({self._brand}, {self._model}, {self.power}, {self.max_speed})"

        @property
        def brand(self) -> str:
            """
            Возвращает марку автомобиля.
            """
            return self._brand

        @property
        def model(self) -> str:
            """
            Возвращает модель автомобиля.
            """
            return self._model

        @property
        def power(self) -> float:
            return self._power

        @power.setter
        def power(self, new_power: float) -> None:
            if not isinstance(new_power, (float, int)):
                raise TypeError("Мощность двигателя должна являться float или int")
            if new_power < 0:
                raise ValueError("Мощность двигателя должна быть положительным числом")
            self._power = new_power

        @property
        def max_speed(self) -> int:
            return self._max_speed

        @max_speed.setter
        def max_speed(self, new_max_speed: int) -> None:
            if not isinstance(new_max_speed, int):
                raise TypeError("Максимальная скорость должна являться int")
            if new_max_speed < 0:
                raise ValueError("Максимальная скорость должна быть положительным числом")
            self._max_speed = new_max_speed

        def drive(self) -> str:
            """
            Симулирует движение автомобиля.
            """
            return "Автомобиль движется."


    class PassengerCar(Car):
        """
        Класс для легковых автомобилей.
        """

        def __init__(self, brand: str, model: str, power: float, max_speed: int, convenience: int) -> None:
            """
            Инициализирует объект легкового автомобиля.
            :param convenience: Оценка по 10 балльной шкале удобства автомобиля
            """
            super().__init__(brand, model, power, max_speed)
            self.convenience = convenience

        @property
        def convenience(self) -> int:
            return self._convenience

        @convenience.setter
        def convenience(self, new_convenience: int) -> None:
            if not isinstance(new_convenience, int):
                raise TypeError("Удобство автомобиля должно быть int")
            if new_convenience < 1 or new_convenience > 10:
                raise  ValueError("Удобство автомобиля должно быть целым числом от 1 до 10")
            self._convenience = new_convenience

        def __str__(self) -> str:
            """
            Возвращает строковое представление легкового автомобиля.
            """
            return f"{super().__str__()} - {self.convenience} /10 комфорта"

        def __repr__(self) -> str:
            """
            Возвращает строковое представление объекта для разработчика.
            """
            return f"{self.__class__.__name__}({self._brand}, {self._model}, {self.power}, {self.max_speed}, {self.convenience})"

        def drive(self) -> str:
            """
            Перегруженный метод движения автомобиля. В легковом автомобиле акцент на комфорте.
            """
            return "Легковой автомобиль движется плавно, но быстро."


    class Truck(Car):
        """
        Класс для грузовых автомобилей.
        """

        def __init__(self, brand: str, model: str, power: float, max_speed: int, load_capacity: float) -> None:
            """
            Инициализирует объект грузового автомобиля.
            :param load_capacity: Грузоподъемность
            """
            super().__init__(brand, model, power, max_speed)
            self.load_capacity = load_capacity

        @property
        def load_capacity(self) -> float:
            return self._load_capacity

        @load_capacity.setter
        def load_capacity(self, new_load_capacity: float) -> None:
            if not isinstance(new_load_capacity, (float, int)):
                raise TypeError("Грузоподъёмность должна быть float или int")
            if new_load_capacity < 0:
                raise ValueError("Грузоподъёмность должна быть положительным числом")
            self._load_capacity = new_load_capacity

        def __str__(self) -> str:
            """
            Возвращает строковое представление грузового автомобиля.
            """
            return f"{super().__str__()} - грузоподъемность {self.load_capacity}"

        def __repr__(self) -> str:
            """
            Возвращает строковое представление объекта для разработчика.
            """
            return f"{self.__class__.__name__}({self._brand}, {self._model}, {self.power}, {self.max_speed}, {self.load_capacity})"

        def drive(self) -> str:
            """
            Перегруженный метод движения автомобиля. В грузовике акцент на мощности и грузоподъемности.
            """
            return "Грузовик движется мощно, перевозя тяжелые грузы."
    pass
