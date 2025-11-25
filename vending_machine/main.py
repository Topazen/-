import sys
import os
import io

# Примусове кодування UTF-8 для консолі Windows
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Додавання кореневої папки проекту до шляху для імпорту пакету 'vending_machine'
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
if project_root not in sys.path:
    sys.path.append(project_root)

from vending_machine.services.machine_context import VendingMachineContext
from vending_machine.config import setup_machine
from vending_machine.utils.logger import Logger

def main():
    Logger.log("Запуск системи торгового автомата...")
    
    machine = VendingMachineContext()
    setup_machine(machine)

    while True:
        print("\n" + "="*30)
        print(" ІНТЕРФЕЙС ТОРГОВОГО АВТОМАТА")
        print("="*30)
        
        # Відображення інвентарю
        print("Доступні товари:")
        inventory = machine.get_inventory().get_all_products()
        for pid, data in inventory.items():
            prod = data['product']
            qty = data['quantity']
            if qty > 0:
                print(f" [{pid}] {prod.name} - ₴{prod.price:.2f} | Кількість: {qty}")
            else:
                print(f" [{pid}] {prod.name} - НЕМАЄ В НАЯВНОСТІ")
        print("="*30)

        print("\nОпції:")
        print("1. Обрати товар")
        print("2. Внести кошти")
        print("3. Скасувати транзакцію")
        print("4. Адмін-меню (Вихід/Поповнення)")
        
        choice = input("\nВаш вибір: ")

        try:
            if choice == '1':
                print("\n--- Доступні товари ---")
                inventory = machine.get_inventory().get_all_products()
                for pid, data in inventory.items():
                    prod = data['product']
                    qty = data['quantity']
                    if qty > 0:
                        print(f" [{pid}] {prod.name} - ₴{prod.price:.2f} | Кількість: {qty}")
                    else:
                        print(f" [{pid}] {prod.name} - НЕМАЄ В НАЯВНОСТІ")
                print("-" * 30)
                pid = int(input("Введіть ID товару: "))
                machine.select_product(pid)
            elif choice == '2':
                amount = float(input("Введіть суму для внесення: ₴"))
                machine.insert_money(amount)
            elif choice == '3':
                machine.cancel_transaction()
            elif choice == '4':
                admin_pass = input("Введіть пароль адміністратора (admin): ")
                if admin_pass == "admin":
                    print("\n--- АДМІН МЕНЮ ---")
                    print("1. Поповнити товар")
                    print("2. Вимкнути систему")
                    admin_choice = input("Вибір: ")
                    
                    if admin_choice == '1':
                        pid = int(input("ID товару: "))
                        qty = int(input("Кількість: "))
                        prod = machine.get_inventory().get_product(pid)
                        if prod:
                            machine.get_inventory().add_product(prod, qty)
                            Logger.log(f"Адмін поповнив товар {pid} на {qty} шт.")
                        else:
                            print("Товар не знайдено.")
                    elif admin_choice == '2':
                        Logger.log("Вимкнення системи.")
                        break
                else:
                    print("Невірний пароль.")
            else:
                print("Невірний вибір.")
        except ValueError:
            print("Невірний ввід. Будь ласка, введіть число.")
        except Exception as e:
            Logger.log(f"Помилка: {e}")

if __name__ == "__main__":
    main()
