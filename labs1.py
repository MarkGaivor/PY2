import doctest


class Can:
    def __init__(self, capacity_volume: float, occupied_volume: float):
        """
        Создание и подготовка к работе объекта "Стакан"

        :param capacity_volume: Объем стакана
        :param occupied_volume: Объем занимаемой жидкости

        Примеры:
        >>> can = Can(500, 0)  # инициализация экземпляра класса
        """
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Объем бидона должен быть типа int или float")
        if capacity_volume <= 0:
            raise ValueError("Объем бидона должен быть положительным числом")
        self.capacity_volume = capacity_volume

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Количество жидкости должно быть int или float")
        if occupied_volume < 0:
            raise ValueError("Количество жидкости не может быть отрицательным числом")
        self.occupied_volume = occupied_volume

    def is_empty_can(self) -> bool:

        >>> can = Can(500, 0)
        >>> can.is_empty_Can()

        ...

    def add_water_to_can(self, water: float) -> None:

        Добавление воды в стакан.
        :param water: Объем добавляемой жидкости

        :raise ValueError: Если количество добавляемой жидкости превышает свободное место в бидоне, то вызываем ошибку

        Примеры:
        >>> can = Can(500, 0)
        >>> can.add_water_to_can(200)
        """
        if not isinstance(water, (int, float)):
            raise TypeError("Добавляемая жидкость должна быть типа int или float")
        if water < 0:
            raise ValueError("Добавляемая жидкость должна положительным числом")
        ...

    def remove_water_from_can(self, estimate_water: float) -> None:
        """
        Извлечение воды из бидона.

        :param estimate_water: Объем извлекаемой жидкости
        :raise ValueError: Если количество извлекаемой жидкости превышает количество воды в бидоне,
        то возвращается ошибка.

        :return: Объем реально извлеченной жидкости

        Примеры:
        >>> can = Can(500, 500)
        >>> can.remove_water_from_can(200)

        ...
class Chair:
    def __init__(self, capacity_volume: float, occupied_volume: float):
       
        >>> chair = Chair(500, 0)  # инициализация экземпляра класса
        
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Прочность стула должен быть типа int или float")
        if capacity_volume <= 0:
            raise ValueError("Прочность стула должен быть положительным числом")
        self.capacity_volume = capacity_volume

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Нагрузка стула должно быть int или float")
        if occupied_volume < 0:
            raise ValueError("Нагрузка стула не может быть отрицательным числом")
        self.occupied_volume = occupied_volume
    def chair_is_broken(self, capacity_volume: float, occupied_volume: float):
        if capacity_volume < occupied_volume:
            print('стул сломан')
    def add_object_on_chair(self):
        ...
class Hermitage:
    def __init__(self, capacity_volume: float, occupied_volume: float):



        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Объём музея должен быть типа int или float")
        if capacity_volume <= 0:
            raise ValueError("Объем музея должен быть положительным числом")
        self.capacity_volume = capacity_volume

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Заполненность должно быть int или float")
        if occupied_volume < 0:
            raise ValueError("Заполненность не может быть отрицательным числом")
        self.occupied_volume = occupied_volume

    def Hermitage_is_empty(self, capacity_volume: float, occupied_volume: float):
        if capacity_volume < occupied_volume:
            print('музей пуст')

    def add_object_on_Hermitage(self):
        ...
    
        
        




if __name__ == "__main__":

    doctest.testmod()