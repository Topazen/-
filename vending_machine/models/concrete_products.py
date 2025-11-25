from .product import Product

class Drink(Product):
    """
    Конкретна реалізація напою.
    """
    def __init__(self, name: str, price: float, product_id: int, volume_ml: int):
        super().__init__(name, price, product_id)
        self._volume_ml = volume_ml

    def get_description(self) -> str:
        return f"{self.name} ({self._volume_ml} мл) - {self.price:.2f} грн"

class Snack(Product):
    """
    Конкретна реалізація снеку.
    """
    def __init__(self, name: str, price: float, product_id: int, weight_g: int):
        super().__init__(name, price, product_id)
        self._weight_g = weight_g

    def get_description(self) -> str:
        return f"{self.name} ({self._weight_g} г) - {self.price:.2f} грн"
