import sqlite3

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('klinika.db')
cursor = connection.cursor()

doctors_data = [
    ('Доктор Иванов', 'Терапевт'),
    ('Доктор Петрова', 'Хирург'),
    ('Доктор Сидоров', 'Кардиолог')
]

patients_data = [
    ('Иван Сергеев', '+79990001122', 'ivan@mail.ru'),
    ('Мария Петрова', '+79990003344', 'maria@mail.ru'),
    ('Алексей Козлов', '+79990005566', 'alex@mail.ru')
]

appointments_data = [
    ('2024-01-15', '09:00', 1, 1, 'confirmed', 'Консультация', 30, 'Первичный прием'),
    ('2024-01-15', '10:00', 2, 2, 'confirmed', 'Осмотр', 45, 'Послеоперационный осмотр'),
    ('2024-01-16', '11:00', 1, None, 'free', 'Консультация', 30, None)
]

cursor.executemany('INSERT INTO doctors (name, specialization) VALUES (?, ?)', doctors_data)
cursor.executemany('INSERT INTO patients (fullName, phone, email) VALUES (?, ?, ?)', patients_data)
cursor.executemany('''
    INSERT INTO appointments (date, time, doctor_id, patient_id, status, service_type, duration, notes) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
''', appointments_data)

# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()