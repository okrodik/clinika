import sqlite3
from tabulate import tabulate

def show_table(table_name):
    connection = sqlite3.connect('klinika.db')
    cursor = connection.cursor()
    
    # Получаем данные
    cursor.execute(f"SELECT * FROM {table_name}")
    data = cursor.fetchall()
    
    # Получаем названия колонок
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = [column[1] for column in cursor.fetchall()]
    
    # Выводим таблицу
    print(f"\n📊 ТАБЛИЦА: {table_name.upper()}")
    print("=" * 80)
    print(tabulate(data, headers=columns, tablefmt="pretty"))
    print(f"Всего записей: {len(data)}")
    
    connection.close()

# Выводим все таблицы
show_table("doctors")
show_table("patients")
show_table("appointments")