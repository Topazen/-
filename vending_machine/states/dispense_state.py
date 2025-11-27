from .base_state import VendingState

class DispenseState(VendingState):
    """
    Стан, що відповідає за видачу товару та повернення решти.
    """
    def select_product(self, context, product_id: int):
        print("Триває видача товару. Зачекайте.")

    def insert_money(self, context, amount: float):
        print("Триває видача товару. Зачекайте.")

    def dispense_product(self, context):
        product_id = context.get_selected_product()
        inventory = context.get_inventory()
        product = inventory.get_product(product_id)
        
        if inventory.dispense_product(product_id):
            print(f"ВИДАЧА: {product.name}")
            
            # Розрахунок решти
            balance = context.get_balance()
            change = balance - product.price
            if change > 0:
                print(f"Повернення решти: {change:.2f} грн")
            
            context.reset_transaction_data()
            
            from .idle_state import IdleState
            context.set_state(IdleState())
        else:
            # Не повинно статися, якщо перевірено в IdleState
            print("Помилка: Товар закінчився під час видачі.")
            context.cancel_transaction() # Повернення коштів

    def cancel_transaction(self, context):
        print("Не можна скасувати під час видачі.")
