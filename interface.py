import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QHBoxLayout
from PyQt6.QtGui import QAction, QPixmap
from PyQt6.QtCore import Qt
from datetime import datetime  

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
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
        label_date = QLabel(f"{now}")
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

        #region Create button navigator 
        button_navigatot = QPushButton("Навигатор")
        button_navigatot.setStyleSheet("font-size: 24px; font-family: Arial; padding-left: 15px;")
        #endregion

        #region Create button calendar 
        button_date = QPushButton("Выбор даты: календарь")
        button_date.setStyleSheet("font-size: 24px; font-family: Arial; padding-left: 15px;")
        #endregion

        #region Create button doctor 
        button_doctor = QPushButton("Выбор врача: ...v")
        button_doctor.setStyleSheet("font-size: 24px; font-family: Arial; padding-left: 15px;")
        #endregion

        button_navigatot.clicked.connect(self.navigator_click)
        button_date.clicked.connect(self.date_click)
        button_doctor.clicked.connect(self.doctor_click)

        main_h_box_vtoroy.addWidget(button_navigatot)
        main_h_box_vtoroy.addWidget(button_date)
        main_h_box_vtoroy.addWidget(button_doctor)
        
        #endregion

        #region 3 blok

        main_h_box_tretiy = QHBoxLayout()  

        button_pn = QPushButton("Пн")
        button_vt = QPushButton("Вт")
        button_sr = QPushButton("Ср")
        button_cht = QPushButton("Чт")
        button_pt = QPushButton("Пт")
        button_sb = QPushButton("Сб")
        button_vs = QPushButton("Вс")

        button_pn.clicked.connect(lambda: self.zapros_date(1))
        button_vt.clicked.connect(lambda: self.zapros_date(2))
        button_sr.clicked.connect(lambda: self.zapros_date(3))
        button_cht.clicked.connect(lambda: self.zapros_date(4))
        button_pt.clicked.connect(lambda: self.zapros_date(5))
        button_sb.clicked.connect(lambda: self.zapros_date(6))
        button_vs.clicked.connect(lambda: self.zapros_date(7))

        main_h_box_tretiy.addWidget(button_pn)
        main_h_box_tretiy.addWidget(button_vt)
        main_h_box_tretiy.addWidget(button_sr)
        main_h_box_tretiy.addWidget(button_cht)
        main_h_box_tretiy.addWidget(button_pt)
        main_h_box_tretiy.addWidget(button_sb)
        main_h_box_tretiy.addWidget(button_vs)
        
        #endregion

        #region 4 blok

        main_h_box_chetvertuy = QHBoxLayout() 

        for x in range(10):
            label_time = QLabel("09:30", self)
            label_status = QLabel("Свободно", self)
            label_namesurname = QLabel("Иванов Иван")

            main_h_box_chetvertuy.addWidget(label_time)
            main_h_box_chetvertuy.addWidget(label_status)
            main_h_box_chetvertuy.addWidget(label_namesurname)



        
        #endregion 

        # Добавляем все layout в основной вертикальный layout
        main_v_box.addLayout(main_h_box_perviy)
        main_v_box.addLayout(main_h_box_vtoroy)
        main_v_box.addLayout(main_h_box_tretiy)
        main_v_box.addLayout(main_h_box_chetvertuy)
        
        # Устанавливаем layout для центрального виджета
        central_widget.setLayout(main_v_box)

    def navigator_click(self):
        print("CLICK Navigator")
        
    def date_click(self):
        print("CLICK Date")
        
    def doctor_click(self):
        print("CLICK Doctor")

    def zapros_date(self, datte):
        print(f"Запрос даты: {datte}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())