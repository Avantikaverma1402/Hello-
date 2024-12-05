#hello.py
import sys
#importing PyQt6 PACKAGE
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit
app= QApplication([])
window= QWidget()
window.setWindowTitle("Welcome Note")
window.setGeometry(100,100,280,100)
helloMsg= QLabel("<h1>Hello, World!</h1>",parent=window)
helloMsg.move(60,40)
window.show()

sys.exit(app.exec())


