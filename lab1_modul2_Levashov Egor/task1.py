import doctest

class Car:
    """
    Класс, представляющий автомобиль.
    """

    def __init__(self, brand: str, year: int):
        if year <= 1885:
            raise ValueError("Год выпуска должен быть после 1885 года.")

        self.brand = brand
        self.year = year

    def start_engine(self) -> str:
        """
        Запустить двигатель автомобиля.

        Returns:
            str: Сообщение о запуске двигателя.

        Example:
            >>> car = Car("Toyota", 2020)
            >>> car.start_engine()
            'Двигатель Toyota запущен.'
        """
        return f"Двигатель {self.brand} запущен."

    def stop_engine(self) -> str:
        """
        Остановить двигатель автомобиля.

        Returns:
            str: Сообщение об остановке двигателя.

        Example:
            >>> car = Car("Toyota", 2020)
            >>> car.stop_engine()
            'Двигатель Toyota остановлен.'
        """
        return f"Двигатель {self.brand} остановлен."


class Human:
    """
    Класс, представляющий человека.
    """

    def __init__(self, name: str, age: int):
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным.")

        self.name = name
        self.age = age

    def greet(self) -> str:
        """
        Поздороваться с человеком.

        Returns:
            str: Приветственное сообщение.

        Example:
            >>> human = Human("Егор", 18)
            >>> human.greet()
            'Привет, меня зовут Егор.'
        """
        return f"Привет, меня зовут {self.name}."

    def have_birthday(self):
        """
        Увеличить возраст человека на один год.

        Example:
            >>> human = Human("Егор", 18)
            >>> human.have_birthday()
            >>> human.age
            19
        """
        self.age += 1


class Computer:
    """
    Класс, представляющий компьютер.
    """

    def __init__(self, model: str, ram: int):
        if ram <= 0:
            raise ValueError("Объем RAM должен быть положительным числом.")

        self.model = model
        self.ram = ram

    def boot_up(self) -> str:
        """
        Загрузить операционную систему.

        Returns:
            str: Сообщение о загрузке.

        Example:
            >>> pc = Computer("ASER", 16)
            >>> pc.boot_up()
            'Компьютер ASER загружается.'
        """
        return f"Компьютер {self.model} загружается."

    def shut_down(self) -> str:
        """
        Выключить компьютер.

        Returns:
            str: Сообщение об отключении.

        Example:
            >>> pc = Computer("ASER", 16)
            >>> pc.shut_down()
            'Компьютер ASER выключается.'
        """
        return f"Компьютер {self.model} выключается."


if __name__ == "__main__":
    doctest.testmod()

