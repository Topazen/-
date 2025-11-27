from abc import ABC, abstractmethod

class VendingState(ABC):
    """
    Абстрактний базовий клас для станів торгового автомата.
    Частина патерну проектування State (Стан).
    Дозволяє автомату змінювати свою поведінку при зміні внутрішнього стану.
    """

    @abstractmethod
    def select_product(self, context, product_id: int):
        """Обробка вибору товару."""
        pass

    @abstractmethod
    def insert_money(self, context, amount: float):
        """Обробка внесення коштів."""
        pass

    @abstractmethod
    def dispense_product(self, context):
        """Обробка видачі товару."""
        pass

    @abstractmethod
    def cancel_transaction(self, context):
        """Обробка скасування поточної транзакції."""
        pass
