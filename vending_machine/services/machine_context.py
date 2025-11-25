from ..models.inventory import Inventory
from ..states.base_state import VendingState
from ..states.idle_state import IdleState # We will create this next
from ..services.payment_strategy import PaymentStrategy

class VendingMachineContext:
    """
    Клас Context для патерну State.
    Він підтримує посилання на екземпляр підкласу VendingState,
    який представляє поточний стан торгового автомата.
    """
    def __init__(self):
        self._inventory = Inventory()
        self._state: VendingState = None
        self._current_amount = 0.0
        self._selected_product_id = None
        self._payment_strategy: PaymentStrategy = None
        
        # Ініціалізація стану (уникнення циклічних імпортів)
        self.set_state(IdleState())

    def set_state(self, state: VendingState):
        """Перехід до нового стану."""
        self._state = state
        print(f"\n[Система] Перехід до {type(state).__name__}") # Дебаг режим увімкнено

    def get_inventory(self) -> Inventory:
        return self._inventory

    def select_product(self, product_id: int):
        self._state.select_product(self, product_id)

    def insert_money(self, amount: float):
        self._state.insert_money(self, amount)

    def dispense_product(self):
        self._state.dispense_product(self)

    def cancel_transaction(self):
        self._state.cancel_transaction(self)

    # Context Data Management
    def set_selected_product(self, product_id: int):
        self._selected_product_id = product_id

    def get_selected_product(self) -> int:
        return self._selected_product_id

    def add_balance(self, amount: float):
        self._current_amount += amount

    def get_balance(self) -> float:
        return self._current_amount

    def reset_transaction_data(self):
        self._current_amount = 0.0
        self._selected_product_id = None
