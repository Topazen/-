from .base_state import VendingState
# Local imports to avoid circular dependency issues at module level
# We will import transition targets inside methods

class IdleState(VendingState):
    """
    Стан очікування взаємодії з користувачем.
    """
    def select_product(self, context, product_id: int):
        # Перевірка наявності товару
        inventory = context.get_inventory()
        product = inventory.get_product(product_id)
        
        if not product:
            print("Невірний ID товару.")
            return
            
        if not inventory.check_stock(product_id):
            print("Товар закінчився.")
            return

        print(f"Обрано: {product.name} - {product.price:.2f} грн")
        context.set_selected_product(product_id)
        
        # Перехід до стану оплати
        from .payment_state import PaymentState
        context.set_state(PaymentState())

    def insert_money(self, context, amount: float):
        print("Будь ласка, спочатку оберіть товар.")

    def dispense_product(self, context):
        print("Спочатку оберіть товар та оплатіть.")

    def cancel_transaction(self, context):
        print("Нічого скасовувати.")
