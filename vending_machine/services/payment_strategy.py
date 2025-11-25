from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    """
    Абстрактний базовий клас для стратегій оплати.
    Частина патерну проектування Strategy (Стратегія).
    Дозволяє використовувати взаємозамінні алгоритми оплати (Готівка, Картка тощо).
    """
    
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        """
        Обробити оплату вказаної суми.
        Повертає True, якщо успішно, False в іншому випадку.
        """
        pass
