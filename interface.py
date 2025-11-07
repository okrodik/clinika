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

        #region PERVUY BLOK
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_v_box = QVBoxLayout(central_widget)

        logo_image = "nolic.png"
        
        # Создаем горизонтальный контейнер для всей верхней строки
        top_layout = QHBoxLayout()
        
        # Контейнер для логотипа и названия (слева)
        left_layout_logo_name = QHBoxLayout()
        rigth_layout_date = QHBoxLayout()
        
        #region Create Logotype
        logo_label = QLabel()
        logo_pixmap = QPixmap(logo_image)
        logo_pixmap = logo_pixmap.scaled(30, 30)
        logo_label.setPixmap(logo_pixmap)
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

        left_layout_logo_name.addWidget(logo_label)
        left_layout_logo_name.addWidget(label_name)

        rigth_layout_date.addWidget(label_date)
        
        left_widget = QWidget()
        left_widget.setLayout(left_layout_logo_name)

        rigth_widget = QWidget()
        rigth_widget.setLayout(rigth_layout_date)

        # Добавляем левую часть и дату в верхний layout
        top_layout.addWidget(left_widget)
        top_layout.addStretch()  # Растягивающее пространство между левой и правой частью
        top_layout.addWidget(rigth_widget)

        #endregion

        #region VTOROY BLOK
        main_h_box_vtoroy = QHBoxLayout()  

        #region Create button navigator 
        button_navigatot = QPushButton("Навигатор", self)
        button_navigatot.setStyleSheet("font-size: 24px; font-family: Arial; padding-left: 15px;")
        #endregion

        #region Create button calendar 
        button_date = QPushButton("Выбор даты: календарь", self)
        button_date.setStyleSheet("font-size: 24px; font-family: Arial; padding-left: 15px;")
        #endregion

        #region Create button doctor 
        button_doctor = QPushButton("Выбор врача: ...v", self)
        button_doctor.setStyleSheet("font-size: 24px; font-family: Arial; padding-left: 15px;")
        #endregion

        main_h_box_vtoroy.addWidget(button_navigatot)
        main_h_box_vtoroy.addWidget(button_date)
        main_h_box_vtoroy.addWidget(button_doctor)

        main_h_box_vtoroy.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Добавляем верхний layout в основной вертикальный layout
        main_v_box.addLayout(top_layout)
        main_v_box.addLayout(main_h_box_vtoroy)


app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec())