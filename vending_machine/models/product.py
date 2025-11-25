from abc import ABC, abstractmethod

class Product(ABC):
    """
    Абстрактний базовий клас для всіх продуктів у торговому автоматі.
    Демонструє Абстракцію та Інкапсуляцію.
    """
    def __init__(self, name: str, price: float, product_id: int):
        self._name = name
        self._price = price
        self._product_id = product_id

    @property
    def name(self) -> str:
        return self._name

    @property
    def price(self) -> float:
        return self._price

    @property
    def product_id(self) -> int:
        return self._product_id

    @abstractmethod
    def get_description(self) -> str:
        """Returns a description of the product."""
        pass

    def __str__(self):
        return f"[{self._product_id}] {self._name} - {self._price:.2f} грн"
