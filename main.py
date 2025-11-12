import sqlite3

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('klinika.db')
cursor = connection.cursor()


def getDoctor():
    connection = sqlite3.connect('klinika.db')
    cursor = connection.cursor()
    
    cursor.execute('SELECT name FROM doctors')
    names = cursor.fetchall()
    
    connection.close()  # Закрываем соединение после выполнения
    
    return [name[0] for name in names]
    
def getAppointments(doctor_id, datePriem):
    connection = sqlite3.connect('klinika.db')
    cursor = connection.cursor()
    
    cursor.execute('''
        SELECT 
            a.time, 
            p.fullName as patient_name, 
            a.service_type, 
            a.notes, 
            a.status 
        FROM appointments a
        LEFT JOIN patients p ON a.patient_id = p.id
        WHERE a.doctor_id = ? AND a.date = ?
    ''', (doctor_id, datePriem))
    
    appointments = cursor.fetchall()
    connection.close()
    
    return appointments

def getDoctorName():
    connection = sqlite3.connect('klinika.db')
    cursor = connection.cursor()
    
    cursor.execute('''
        SELECT name FROM doctors
    ''')
    
    nameDoctor = [row[0] for row in cursor.fetchall()]  # Извлекаем только имена
    connection.close()
    
    return nameDoctor


# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()