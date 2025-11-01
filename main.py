import pyodbc

# Подключение к SQL Server
conn = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=MSI;'                    # Server name
    'DATABASE=clinika;'                  # Database name
    'Trusted_Connection=yes;'        # Windows Authentication
    'TrustServerCertificate=yes;'    # Trust server certificate
)
cursor = conn.cursor()



cursor.execute("""
SELECT 
    p.surname,
    p.name, 
    a.date,
    a.time,
    t.tooth_number,
    t.status
FROM Patients p
INNER JOIN Appointments a ON p.id = a.patient_id
INNER JOIN Teeth t ON p.id = t.patient_id
WHERE p.id = 1
ORDER BY t.tooth_number
""")

results = cursor.fetchall()

# Вывести результаты
for row in results:
    print(row)

# Закрыть соединение
cursor.close()
conn.close()