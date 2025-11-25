from .models.concrete_products import Drink, Snack
from .services.machine_context import VendingMachineContext

def setup_machine(machine: VendingMachineContext):
    """
    Ініціалізує торговий автомат товарами.
    """
    # Створення продуктів
    coke = Drink("Кока-Кола", 15.00, 1, 500)
    snickers = Snack("Snickers", 12.50, 2, 50)
    water = Drink("Вода", 8.00, 3, 500)
    
    # Додавання до інвентарю
    machine.get_inventory().add_product(coke, 10)
    machine.get_inventory().add_product(snickers, 8)
    machine.get_inventory().add_product(water, 15)

    print("Система: Автомат ініціалізовано товарами.")
