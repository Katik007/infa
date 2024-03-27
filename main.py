import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QPalette
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QTimer
import random


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Моя программа")
        self.setGeometry(400, 300, 450, 350)
        layout = QVBoxLayout()
        self.label = QLabel("Нажми кнопку!", self)
        layout.addWidget(self.label, alignment=Qt.AlignmentFlag.AlignCenter)
        self.button1 = QPushButton("Кнопка", self)
        self.button1.clicked.connect(self.moveButton)
        layout.addWidget(self.button1, alignment=Qt.AlignmentFlag.AlignCenter)
        self.button2 = QPushButton("Счётчик: 0", self)
        self.button2.clicked.connect(self.updateCounter)
        layout.addWidget(self.button2, alignment=Qt.AlignmentFlag.AlignCenter)
        self.button3 = QPushButton("Жмак", self)
        self.button3.clicked.connect(self.changeColor)
        self.button3.setGeometry(375, 315, 55, 25)
        self.button4 = QPushButton("Изменить фон", self)
        self.button4.clicked.connect(self.changeColorfone)
        self.button4.setGeometry(348, 280, 97, 25)
        self.button5 = QPushButton("Показать котика", self)
        self.button5.clicked.connect(self.showCat)
        self.button5.setGeometry(177, 310, 97, 25)
        self.timer = QTimer(self)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.hideCat)
        self.label = QLabel("Ничего не выбрано")
        layout.addWidget(self.label)
        self.yes_button = QPushButton("ДА")
        self.yes_button.clicked.connect(self.button_clicked)
        layout.addWidget(self.yes_button, alignment=Qt.AlignmentFlag.AlignLeft)
        self.no_button = QPushButton("НЕТ")
        self.no_button.clicked.connect(self.button_clicked)
        layout.addWidget(self.no_button, alignment=Qt.AlignmentFlag.AlignLeft)
        self.setLayout(layout)
        self.counter = 0

    def button_clicked(self):
        sender_button = self.sender()
        if sender_button == self.yes_button:
            self.label.setText("Выбрано: ДА")
        elif sender_button == self.no_button:
            self.label.setText("Выбрано: НЕТ")

    def showCat(self):
        pixmap = QPixmap("cat.jpg")
        self.label.setPixmap(pixmap)
        self.timer.start(1300)

    def hideCat(self):
        self.label.clear()

    def changeColorfone(self):
        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.setStyleSheet(f"background-color: {color.name()}")

    def changeColor(self):
        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.button3.setStyleSheet(f"background-color: {color.name()}")

    def moveButton(self):
        pos = self.button1.pos()
        if pos.x() < self.width() / 2:
            self.button1.move(self.width() - self.button1.width(), pos.y())
        else:
            self.button1.move(0, pos.y())

    def updateCounter(self):
        self.counter += 1
        self.button2.setText(f"Счётчик: {self.counter}")


app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())
