from .base_state import VendingState

class PaymentState(VendingState):
    """
    Стан, коли користувач обрав товар і повинен оплатити.
    """
    def select_product(self, context, product_id: int):
        print("Товар вже обрано. Завершіть транзакцію або скасуйте її.")

    def insert_money(self, context, amount: float):
        context.add_balance(amount)
        current_balance = context.get_balance()
        
        product_id = context.get_selected_product()
        product = context.get_inventory().get_product(product_id)
        
        print(f"Внесено: {amount:.2f} грн. Всього: {current_balance:.2f} грн. Потрібно: {product.price:.2f} грн")
        
        if current_balance >= product.price:
            # Перехід до стану видачі
            from .dispense_state import DispenseState
            context.set_state(DispenseState())
            context.dispense_product() # Викликаємо видачу одразу

    def dispense_product(self, context):
        print("Будь ласка, внесіть достатню суму.")

    def cancel_transaction(self, context):
        print("Транзакцію скасовано. Повернення коштів...")
        balance = context.get_balance()
        if balance > 0:
            print(f"Повернуто: {balance:.2f} грн")
        
        context.reset_transaction_data()
        from .idle_state import IdleState
        context.set_state(IdleState())
