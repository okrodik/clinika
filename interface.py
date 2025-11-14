import sys
from PyQt6.QtWidgets import QApplication, QComboBox, QMessageBox, QDialog, QLineEdit, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QDateEdit
from PyQt6.QtGui import QAction, QPixmap
from PyQt6.QtCore import Qt, QDate
from datetime import datetime  
import main


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.idDoctor = 1  # Сначала инициализируем атрибуты
        self.DatePriem = None
        self.initializeUI()

    def initializeUI(self):
        self.DatePriem = f"{datetime.now().strftime('%Y-%m-%d')}"
        self.setMinimumSize(350, 250)
        self.setWindowTitle("Stacked Layout")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        # Создаем центральный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_v_box = QVBoxLayout()

        #region PERVUY BLOK
        main_h_box_perviy = QHBoxLayout()

        logo_image = "nolic.png"  # Убедитесь, что файл существует
  
        #region Create Logotype
        logo_label = QLabel()
        try:
            logo_pixmap = QPixmap(logo_image)
            if not logo_pixmap.isNull():
                logo_pixmap = logo_pixmap.scaled(30, 30)
                logo_label.setPixmap(logo_pixmap)
        except:
            pass  # Если логотип не загружается, просто продолжаем

        logo_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        #endregion

        #region Create name 
        label_name = QLabel("Клиника Доктора Мыреева")
        label_name.setAlignment(Qt.AlignmentFlag.AlignLeft)
        label_name.setStyleSheet("font-size: 24px; font-family: Arial; padding-left: 15px;")
        #endregion

        #region DATe label
        now = datetime.now() 
        label_date = QLabel(f"{now.strftime('%d.%m.%Y')}")
        label_date.setAlignment(Qt.AlignmentFlag.AlignRight)
        label_date.setStyleSheet("font-size: 24px; font-family: Arial;")
        #endregion

        # Контейнер для логотипа и названия (слева)
        left_layout_logo_name = QHBoxLayout()
        right_layout_date = QHBoxLayout()

        # Создаем контейнерные виджеты для layout'ов
        left_container = QWidget()
        right_container = QWidget()

        # Добавляем виджеты в левый layout
        left_layout_logo_name.addWidget(logo_label)
        left_layout_logo_name.addWidget(label_name)
        left_layout_logo_name.setContentsMargins(0, 0, 0, 0)  # Убираем отступы

        # Добавляем виджеты в правый layout
        right_layout_date.addWidget(label_date)
        right_layout_date.setContentsMargins(0, 0, 0, 0)  # Убираем отступы

        # Устанавливаем layout'ы для контейнерных виджетов
        left_container.setLayout(left_layout_logo_name)
        right_container.setLayout(right_layout_date)

        # Добавляем контейнеры в основной layout
        main_h_box_perviy.addWidget(left_container)
        main_h_box_perviy.addStretch()  # Растягивающее пространство между левой и правой частью
        main_h_box_perviy.addWidget(right_container)

        #endregion

        #region VTOROY BLOK
        
        main_h_box_vtoroy = QHBoxLayout()  


        #region Create button calendar 
        date_edit = QDateEdit()
        date_edit.setCalendarPopup(True)  # Включаем выпадающий календарь
        date_edit.setDate(QDate.currentDate())
        date_edit.setDisplayFormat("yyyy-MM-dd")
        date_edit.setStyleSheet("font-size: 24px; font-family: Arial; padding-left: 15px;")
        date_edit.dateChanged.connect(self.on_date_changed)
        #endregion



        combo_doctor = QComboBox(self)
        combo_doctor.addItems(main.getDoctorName())
        combo_doctor.textActivated.connect(self.onActivated)
        combo_doctor.setStyleSheet("font-size: 24px; font-family: Arial; padding-left: 15px;")

        #date_edit.clicked.connect(self.date_click)

        main_h_box_vtoroy.addWidget(date_edit)
        main_h_box_vtoroy.addWidget(combo_doctor)
            
        #endregion

        #region 4 BLOK - Простое расписание
        main_v_box_chetvertuy = QVBoxLayout()

        # Заголовок
        label_title = QLabel("Расписание")

        label_title.setStyleSheet("font-size: 16px; font-weight: bold;")
        main_v_box_chetvertuy.addWidget(label_title)

        self.schedule_layout = main_v_box_chetvertuy  # Сохраняем ссылку
        self.update_schedule(self.idDoctor, self.DatePriem)
       
        
        #endregion 
            
        #region 5 blok 

        main_h_box_pyatuy = QHBoxLayout()

        button_newPriem = QPushButton("Новый прием", self)
        button_patient = QPushButton("Пациент", self)
        button_setting = QPushButton("Настройки", self)

        button_newPriem.clicked.connect(self.newPriem)
        button_patient.clicked.connect(self.newPatient)
        button_setting.clicked.connect(self.setting)

        main_h_box_pyatuy.addWidget(button_newPriem)
        main_h_box_pyatuy.addWidget(button_patient)
        main_h_box_pyatuy.addWidget(button_setting)

        #endregion

        # Добавляем все layout в основной вертикальный layout
        main_v_box.addLayout(main_h_box_perviy)
        main_v_box.addLayout(main_h_box_vtoroy)
        main_v_box.addLayout(main_v_box_chetvertuy)
        main_v_box.addLayout(main_h_box_pyatuy)
        
        # Устанавливаем layout для центрального виджета
        central_widget.setLayout(main_v_box)

#TODO ДОБАВИТЬ ЗАПИСЬ НА ПРИЕМ
    def newPriem(self, s):
        print("click", s)

        dlg = CustomDialog()
        if dlg.exec():
            print("Success!")
        else:
            print("Cancel!")

    def newPatient(self):
        pass
    
    def setting(self):
        pass  

        
    def date_click(self):
        print("CLICK Date")
        
    def doctor_click(self):
        print("CLICK Doctor")

    def zapros_date(self, datte):
        print(f"Запрос даты: {datte}")

    def onActivated(self, text):
        if (text == "Доктор Иванов"):
            self.idDoctor = 1
        if(text == "Доктор Петрова"):
            self.idDoctor = 2
        if (text == "Доктор Сидоров"):
            self.idDoctor = 3

        self.update_schedule(self.idDoctor, self.DatePriem)


    def update_schedule(self, doctor_id, datePriem):
        # Очищаем существующее расписание (кроме заголовка)
        if self.schedule_layout:
            while self.schedule_layout.count() > 1:
                item = self.schedule_layout.takeAt(1)
                if item.widget():
                    item.widget().deleteLater()
                elif item.layout():
                    # Если это layout, рекурсивно удаляем его содержимое
                    self.clear_layout(item.layout())
    
        appointments = main.getAppointments(doctor_id, datePriem)

        # Данные для таблицы
        if appointments:
            for time, name, service, notes, status in appointments:
                h_box = QHBoxLayout()
                
                time_label = QLabel(time)
                time_label.setStyleSheet("font-weight: bold; min-width: 50px;")
                
                name_label = QLabel(name)
                type_label = QLabel(service)
                notes_label = QLabel(notes)
                status_label = QLabel(status) 
                
                for label in [name_label, type_label, notes_label, status_label]:
                    label.setStyleSheet("background: Light sea green; padding: 5px; margin: 2px;")
                
                h_box.addWidget(time_label)
                h_box.addWidget(name_label)
                h_box.addWidget(type_label)
                h_box.addWidget(notes_label)
                h_box.addWidget(status_label)
                
                self.schedule_layout.addLayout(h_box)
        else:
            # Если записей нет, показываем сообщение
            no_appointments_label = QLabel("Записей на прием нет")
            no_appointments_label.setStyleSheet("font-style: italic; color: gray;")
            self.schedule_layout.addWidget(no_appointments_label)
        
        # Принудительно обновляем интерфейс
        self.schedule_layout.update()

    # Вспомогательный метод для очистки layout
    def clear_layout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clear_layout(item.layout())

    def on_date_changed(self, date):
        self.DatePriem = date.toString("yyyy-MM-dd")
        self.update_schedule(self.idDoctor, self.DatePriem)

class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Добавить пациента!")

        message = QLabel("Выберите дату записи")
        message.setStyleSheet("font-weight: bold; min-width: 50px;")
        
        #region Create button calendar 
        dateZapis = QDateEdit()
        dateZapis.setCalendarPopup(True)  # Включаем выпадающий календарь
        dateZapis.setDate(QDate.currentDate())
        dateZapis.setDisplayFormat("yyyy-MM-dd")
        dateZapis.setStyleSheet("font-size: 20px; font-family: Arial; padding-left: 15px;")
        dateZapis.setFixedWidth(200)
        #endregion

        message2 = QLabel("Выберите дату записи")
        message2.setStyleSheet("font-weight: bold; min-width: 50px;")

        vremaZapis = QComboBox()
        vremaZapis.addItems(["09:00", "09:30", "10:00", "10:30", "11:00", "11:30", "12:00", "12:30", "13:00", "13:30", "14:00", "14:30", "15:00", "15:30", "16:00"])
        vremaZapis.setStyleSheet("font-size: 20px; font-family: Arial; padding-left: 15px;")
        vremaZapis.setFixedWidth(200)

        message3 = QLabel("Выбрать врача")
        message3.setStyleSheet("font-weight: bold; min-width: 50px;")

        viborVrach = QComboBox()
        viborVrach.addItems(["Доктор Иванов", "Доктор Петрова", "Доктор Сидоров"])
        viborVrach.setStyleSheet("font-size: 20px; font-family: Arial; padding-left: 15px;")
        viborVrach.setFixedWidth(200)

        message4 = QLabel("Какая услуга?")
        message4.setStyleSheet("font-weight: bold; min-width: 50px;")

        uslugeType = QComboBox()
        uslugeType.addItems(["Осмотр", "Консультация", "Лечение"])
        uslugeType.setStyleSheet("font-size: 20px; font-family: Arial; padding-left: 15px;")
        uslugeType.setFixedWidth(200)

        message5 = QLabel("Описание")
        message5.setStyleSheet("font-weight: bold; min-width: 50px;")

        textNotes = QLineEdit()
        textNotes.setStyleSheet("font-size: 20px; font-family: Arial; padding-left: 15px;")
        textNotes.setFixedWidth(200)

        self.VerLayoutDate = QVBoxLayout()
        self.VerLayoutVrema = QVBoxLayout()
        self.VerLayoutDoctor = QVBoxLayout()
        self.VerLayoutSerType = QVBoxLayout()
        self.VerLayoutNotes = QVBoxLayout()

        self.layout = QHBoxLayout()
        self.VertLayout = QVBoxLayout()
        self.ButtonLayout = QHBoxLayout()

        buttonExit = QPushButton("Выйти", self)
        buttonSave = QPushButton("Сохранить", self)

        buttonExit.clicked.connect(self.ClickExit)
        buttonSave.clicked.connect(self.ClickSave)

        self.VerLayoutDate.addWidget(message)
        self.VerLayoutDate.addWidget(dateZapis)

        self.VerLayoutVrema.addWidget(message2)
        self.VerLayoutVrema.addWidget(vremaZapis)

        self.VerLayoutDoctor.addWidget(message3)
        self.VerLayoutDoctor.addWidget(viborVrach)

        self.VerLayoutSerType.addWidget(message4)
        self.VerLayoutSerType.addWidget(uslugeType)

        self.VerLayoutNotes.addWidget(message5)
        self.VerLayoutNotes.addWidget(textNotes)

        self.ButtonLayout.addWidget(buttonExit)
        self.ButtonLayout.addWidget(buttonSave)

        self.layout.addLayout(self.VerLayoutDate)
        self.layout.addLayout(self.VerLayoutVrema)
        self.layout.addLayout(self.VerLayoutDoctor)
        self.layout.addLayout(self.VerLayoutSerType)
        self.layout.addLayout(self.VerLayoutNotes)

        self.VertLayout.addLayout(self.layout)
        self.VertLayout.addLayout(self.ButtonLayout)

        self.setLayout(self.VertLayout)

    def ClickExit(self):
        self.close()


    def ClickSave(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())