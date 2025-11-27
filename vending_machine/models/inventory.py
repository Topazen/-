from typing import Dict
from .product import Product

class Inventory:
    """
    Керує запасами товарів у торговому автоматі.
    Демонструє Інкапсуляцію та Асоціацію.
    """
    def __init__(self):
        # Мапа product_id до [Product, quantity]
        self._stock: Dict[int, dict] = {}

    def add_product(self, product: Product, quantity: int):
        """Додає товар до інвентарю."""
        if product.product_id in self._stock:
            self._stock[product.product_id]['quantity'] += quantity
        else:
            self._stock[product.product_id] = {
                'product': product,
                'quantity': quantity
            }

    def get_product(self, product_id: int) -> Product:
        """Повертає об'єкт товару, якщо він існує."""
        if product_id in self._stock:
            return self._stock[product_id]['product']
        return None

    def check_stock(self, product_id: int) -> bool:
        """Перевіряє наявність товару на складі."""
        if product_id in self._stock:
            return self._stock[product_id]['quantity'] > 0
        return False

    def dispense_product(self, product_id: int) -> bool:
        """Зменшує запас на 1. Повертає True у разі успіху."""
        if self.check_stock(product_id):
            self._stock[product_id]['quantity'] -= 1
            return True
        return False

    def get_all_products(self):
        """Повертає список всіх товарів з їх кількістю."""
        return self._stock
