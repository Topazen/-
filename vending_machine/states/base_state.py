from abc import ABC, abstractmethod

class VendingState(ABC):
    """
    Абстрактний базовий клас для станів торгового автомата.
    Частина патерну проектування State (Стан).
    Дозволяє автомату змінювати свою поведінку при зміні внутрішнього стану.
    """

    @abstractmethod
    def select_product(self, context, product_id: int):
        """Handle product selection."""
        pass

    @abstractmethod
    def insert_money(self, context, amount: float):
        """Handle money insertion."""
        pass

    @abstractmethod
    def dispense_product(self, context):
        """Handle dispensing the product."""
        pass

    @abstractmethod
    def cancel_transaction(self, context):
        """Handle cancellation of the current transaction."""
        pass
