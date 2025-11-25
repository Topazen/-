from .payment_strategy import PaymentStrategy

class CashPayment(PaymentStrategy):
    def process_payment(self, amount: float) -> bool:
        print(f"Обробка оплати готівкою: {amount:.2f} грн...")
        # Готівка завжди приймається
        return True

class CardPayment(PaymentStrategy):
    def process_payment(self, amount: float) -> bool:
        print(f"Обробка оплати карткою: {amount:.2f} грн...")
        # Симуляція перевірки картки
        print("З'єднання з банком... Схвалено.")
        return True
