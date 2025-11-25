from typing import Dict
from .product import Product

class Inventory:
    """
    Керує запасами товарів у торговому автоматі.
    Демонструє Інкапсуляцію та Асоціацію.
    """
    def __init__(self):
        # Maps product_id to [Product, quantity]
        self._stock: Dict[int, dict] = {}

    def add_product(self, product: Product, quantity: int):
        """Adds a product to the inventory."""
        if product.product_id in self._stock:
            self._stock[product.product_id]['quantity'] += quantity
        else:
            self._stock[product.product_id] = {
                'product': product,
                'quantity': quantity
            }

    def get_product(self, product_id: int) -> Product:
        """Returns the product object if it exists."""
        if product_id in self._stock:
            return self._stock[product_id]['product']
        return None

    def check_stock(self, product_id: int) -> bool:
        """Checks if a product is in stock."""
        if product_id in self._stock:
            return self._stock[product_id]['quantity'] > 0
        return False

    def dispense_product(self, product_id: int) -> bool:
        """Reduces stock by 1. Returns True if successful."""
        if self.check_stock(product_id):
            self._stock[product_id]['quantity'] -= 1
            return True
        return False

    def get_all_products(self):
        """Returns a list of all products with their quantities."""
        return self._stock
