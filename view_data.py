import sqlite3
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box
from datetime import datetime

console = Console()

def show_database_beautiful():
    connection = sqlite3.connect('klinika.db')
    cursor = connection.cursor()
    
    # ТАБЛИЦА DOCTORS
    cursor.execute("SELECT * FROM doctors")
    doctors = cursor.fetchall()
    
    doctors_table = Table(
        title="👨‍⚕️ ВРАЧИ",
        show_header=True,
        header_style="bold cyan",
        box=box.DOUBLE_EDGE,
        title_style="bold green"
    )
    
    doctors_table.add_column("ID", style="dim", width=4)
    doctors_table.add_column("Имя врача", style="bold white", width=20)
    doctors_table.add_column("Специализация", style="magenta", width=15)
    
    for doc in doctors:
        doctors_table.add_row(str(doc[0]), doc[1], doc[2])
    
    console.print(doctors_table)
    
    # ТАБЛИЦА PATIENTS
    cursor.execute("SELECT * FROM patients")
    patients = cursor.fetchall()
    
    patients_table = Table(
        title="👥 ПАЦИЕНТЫ",
        show_header=True,
        header_style="bold blue",
        box=box.ROUNDED,
        title_style="bold yellow"
    )
    
    patients_table.add_column("ID", style="dim", width=4)
    patients_table.add_column("ФИО", style="bold white", width=20)
    patients_table.add_column("Телефон", style="green", width=15)
    patients_table.add_column("Email", style="cyan", width=25)
    
    for patient in patients:
        patients_table.add_row(str(patient[0]), patient[1], patient[2], patient[3])
    
    console.print(patients_table)
    
    # ТАБЛИЦА APPOINTMENTS с JOIN
    cursor.execute('''
        SELECT 
            a.id, a.date, a.time, 
            d.name as doctor_name, d.specialization,
            p.fullName as patient_name, p.phone,
            a.status, a.service_type, a.duration, a.notes
        FROM appointments a
        LEFT JOIN doctors d ON a.doctor_id = d.id
        LEFT JOIN patients p ON a.patient_id = p.id
        ORDER BY a.date, a.time
    ''')
    
    appointments = cursor.fetchall()
    
    appointments_table = Table(
        title="📅 ЗАПИСИ НА ПРИЕМ",
        show_header=True,
        header_style="bold magenta",
        box=box.MINIMAL_HEAVY_HEAD,
        title_style="bold red",
        width=120
    )
    
    appointments_table.add_column("ID", style="dim", width=4)
    appointments_table.add_column("Дата", style="yellow", width=12)
    appointments_table.add_column("Время", style="yellow", width=8)
    appointments_table.add_column("Врач", style="cyan", width=18)
    appointments_table.add_column("Пациент", style="green", width=18)
    appointments_table.add_column("Услуга", style="white", width=15)
    appointments_table.add_column("Статус", style="bold", width=12)
    appointments_table.add_column("Длит.", style="dim", width=6)
    
    for app in appointments:
        # Форматируем статус
        status_text = app[7]
        status_style = "green" if app[7] == 'confirmed' else "yellow" if app[7] == 'free' else "red"
        
        # Форматируем пациента
        patient_name = app[5] if app[5] else "[dim]Свободно[/dim]"
        
        appointments_table.add_row(
            str(app[0]),
            app[1],
            app[2],
            f"{app[3]}\n[dim]{app[4]}[/dim]",
            patient_name,
            app[8],
            f"[{status_style}]{status_text}[/{status_style}]",
            f"{app[9]}мин"
        )
    
    console.print(appointments_table)
    
    # СТАТИСТИКА
    cursor.execute("SELECT COUNT(*) FROM doctors")
    doctors_count = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM patients")
    patients_count = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM appointments")
    appointments_count = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM appointments WHERE status = 'confirmed'")
    confirmed_count = cursor.fetchone()[0]
    
    stats_panel = Panel(
        f"[bold]👨‍⚕️ Врачи:[/bold] {doctors_count}\n"
        f"[bold]👥 Пациенты:[/bold] {patients_count}\n"
        f"[bold]📅 Всего записей:[/bold] {appointments_count}\n"
        f"[bold]✅ Подтвержденных:[/bold] {confirmed_count}\n"
        f"[bold]📊 Заполненность:[/bold] {confirmed_count}/{appointments_count}",
        title="📈 СТАТИСТИКА БАЗЫ ДАННЫХ",
        style="bold blue",
        box=box.DOUBLE
    )
    
    console.print(stats_panel)
    
    connection.close()

# Запускаем красивый вывод
show_database_beautiful()