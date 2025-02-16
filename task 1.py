class ConiferousTree:
    """
    Хвойные деревья - базовый класс.
    """

    def __init__(self, species: str, height: float, age: int) -> None:
        """
        Инициализация хвойного дерева.

        :param species: Вид дерева.
        :param height: Высота дерева в метрах.
        :param age: Возраст дерева в годах.
        """
        self.species = species
        self.height = height
        self.age = age

    def grow(self, years: int) -> None:
        """
        Увеличивает высоту дерева на 1 метр за каждый год роста.

        :param years: Количество лет, которое дерево растет.
        """
        self.height += years

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.
        """
        return f"{self.species} (Height: {self.height}m, Age: {self.age} years)"

    def __repr__(self) -> str:
        """
        Возвращает представление объекта для отладки.
        """
        return f"ConiferousTree(species='{self.species}', height={self.height}, age={self.age})"


class Pine(ConiferousTree):
    """
    Сосна - дочерний класс.
    """

    def __init__(self, species: str, height: float, age: int, cone_size: float) -> None:
        """
        Инициализация сосны.

        :param species: Вид сосны.
        :param height: Высота сосны в метрах.
        :param age: Возраст сосны в годах.
        :param cone_size: Размер шишек в сантиметрах.
        """
        super().__init__(species, height, age)
        self.__cone_size = cone_size  # Инкапсуляция, чтобы защитить размер шишек

    def grow(self, years: int) -> None:
        """
        Увеличивает высоту сосны на 1 метр за каждый год роста.

        :param years: Количество лет, которое сосна растет.
        """
        super().grow(years)

    def __str__(self) -> str:
        """
        Возвращает строковое представление сосны.
        """
        return f"{self.species} (Height: {self.height}m, Age: {self.age} years, Cone Size: {self.__cone_size}cm)"

    def __repr__(self) -> str:
        """
        Возвращает представление объекта для отладки.
        """
        return f"Pine(species='{self.species}', height={self.height}, age={self.age}, cone_size={self.__cone_size})"

if __name__ == "__main__":
    pine_tree = Pine("Scots Pine", 5.0, 10, 5.0)
    print(pine_tree)  # Вывод информации о сосне
    pine_tree.grow(2)  # Дерево растет на 2 года
    print(pine_tree)  # Вывод информации о сосне после роста