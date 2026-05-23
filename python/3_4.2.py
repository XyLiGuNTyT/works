class VideoCard:
    # Атрибуты класса
    manufacturer: str = "Unknown"
    interface: str = "PCIe 4.0"

    def __init__(self, model: str, vram: int, core_clock: int, power_consumption: int, color: str) -> None:
        """
        Инициализация объекта видеокарты.

        :param model: Модель видеокарты
        :param vram: Объем видеопамяти в ГБ
        :param core_clock: Тактовая частота ядра в МГц
        :param power_consumption: Энергопотребление в ваттах (TDP)
        :param color: Цвет кожуха или подсветки
        """
        self.model = model
        self.vram = vram
        self.core_clock = core_clock
        self.power_consumption = power_consumption
        self.color = color

    def __str__(self) -> str:
        """Магический метод: строковое представление видеокарты."""
        return (f"{self.manufacturer} {self.model} ({self.color}) – "
                f"{self.vram}GB VRAM, {self.core_clock}MHz core clock, "
                f"{self.power_consumption}W TDP, Interface: {self.interface}")

    def check_vram(self, required_vram: int) -> bool:
        """
        Проверяет, достаточно ли видеопамяти для запуска игры или приложения.

        :param required_vram: Требуемый объем видеопамяти в ГБ
        :return: True, если памяти хватает, иначе False
        """
        return required_vram <= self.vram

    def overclock_core(self, additional_mhz: int) -> None:
        """Увеличивает тактовую частоту ядра (разгон)."""
        if additional_mhz > 0:
            self.core_clock += additional_mhz
            print(f"Частота ядра увеличена на {additional_mhz} МГц. Теперь частота = {self.core_clock} МГц")
        else:
            print("Некорректное значение для увеличения частоты")

    def estimate_power_consumption(self, load_percent: float) -> float:
        """
        Оценивает энергопотребление видеокарты при заданной нагрузке.

        :param load_percent: Нагрузка в процентах (0–100)
        :return: Оценочное энергопотребление в ваттах
        """
        if load_percent < 0 or load_percent > 100:
            raise ValueError("Нагрузка должна быть в пределах от 0 до 100 %")
        return self.power_consumption * (load_percent / 100.0)

    def update_color(self, new_color: str) -> None:
        """Меняет цвет кожуха/подсветки видеокарты."""
        self.color = new_color
        print(f"Цвет изменён на {new_color}")

    @classmethod
    def change_interface(cls, new_interface: str) -> None:
        """Изменяет интерфейс подключения для всех видеокарт (атрибут класса)."""
        cls.interface = new_interface
        print(f"Интерфейс для всех видеокарт изменён на {new_interface}")


# Создание трёх видеокарт
gpu1 = VideoCard("RTX 4080", 16, 2205, 320, "Black")
gpu2 = VideoCard("RX 7900 XT", 20, 2100, 315, "Silver")
gpu3 = VideoCard("Arc A770", 16, 2400, 225, "Blue")

print(gpu1)
print(gpu2)
print(gpu3)

print("\n--- Проверка методов ---")

required_vram = 12
if gpu1.check_vram(required_vram):
    print(f"На {gpu1.model} хватит видеопамяти ({required_vram} ГБ)")
else:
    print(f"На {gpu1.model} недостаточно видеопамяти ({required_vram} ГБ)")

gpu2.overclock_core(150)

try:
    load = 75
    estimated_power = gpu3.estimate_power_consumption(load)
    print(f"При нагрузке {load}% {gpu3.model} будет потреблять около {estimated_power:.1f} Вт")
except ValueError as e:
    print(e)

gpu1.update_color("Red")

VideoCard.change_interface("PCIe 5.0")

print("\n--- После изменений ---")
print(gpu1)
print(gpu2)
print(gpu3)