class ConiferousTree:
    """
    Базовый класс для хвойных деревьев.
    """

    def __init__(self, name: str, height: float) -> None:
        """
        Инициализация хвойного дерева.

        :param name: Название дерева
        :param height: Высота дерева в метрах
        """
        self._name = name  # Инкапсулирую название, так как доступ к нему нужен только через методы
        self.height = height

    def __str__(self) -> str:
        return f"Хвойное дерево: {self._name}, Высота: {self.height} м"

    def __repr__(self) -> str:
        return f"ConiferousTree(name={self._name!r}, height={self.height!r})"

    def produce_cones(self) -> str:
        """
        Метод, который должен быть переопределён в дочерних классах.
        """
        return "Производит шишки"

    def get_name(self) -> str:
        """
        Возвращает название дерева.
        """
        return self._name


class Spruce(ConiferousTree):
    """
    Дочерний класс, представляющий ель.
    """

    def __init__(self, name: str, height: float, needle_length: float) -> None:
        """
        Инициализация ели.

        :param name: Название ели
        :param height: Высота ели
        :param needle_length: Длина иголок в сантиметрах
        """
        super().__init__(name, height)  # Наследую конструктор базового класса
        self.needle_length = needle_length

    def __str__(self) -> str:
        return f"Ель: {self._name}, Высота: {self.height} м, Длина иголок: {self.needle_length} см"

    def __repr__(self) -> str:
        return f"Spruce(name={self._name!r}, height={self.height!r}, needle_length={self.needle_length!r})"

    def produce_cones(self) -> str:
        """
        Переопределённый метод производства шишек для ели.
        Теперь метод указывает, что ель производит удлинённые шишки.
        """
        return "Ель производит удлинённые шишки"

    def provide_shelter(self) -> str:
        """
        Метод, показывающий, что ель может служить укрытием для животных.
        """
        return f"{self._name} предоставляет укрытие птицам и мелким животным"


class Pine(ConiferousTree):
    """
    Дочерний класс, представляющий сосну.
    """

    def __init__(self, name: str, height: float, needle_length: float) -> None:
        """
        Инициализация сосны.

        :param name: Название сосны
        :param height: Высота сосны
        :param needle_length: Длина иголок в сантиметрах
        """
        super().__init__(name, height)  # Наследую конструктор базового класса
        self.needle_length = needle_length

    def __str__(self) -> str:
        return f"Сосна: {self._name}, Высота: {self.height} м, Длина иголок: {self.needle_length} см"

    def __repr__(self) -> str:
        return f"Pine(name={self._name!r}, height={self.height!r}, needle_length={self.needle_length!r})"

    def produce_cones(self) -> str:
        """
        Переопределённый метод производства шишек для сосны.
        Теперь метод указывает, что сосна производит круглые шишки.
        """
        return "Сосна производит круглые шишки"


if __name__ == "__main__":
    spruce = Spruce("Ель обыкновенная", 30.0, 2.5)
    pine = Pine("Сосна обыкновенная", 35.0, 5.0)

    print(spruce)
    print(spruce.produce_cones())
    print(spruce.provide_shelter())

    print(pine)
    print(pine.produce_cones())

