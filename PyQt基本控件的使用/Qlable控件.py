import sys
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QFont

app = QApplication(sys.argv)
window = QWidget()

layout = QVBoxLayout()
label = QLabel("Hello, PyQt!")
label.setFont(QFont("Arial", 16))

layout.addWidget(label)
window.setLayout(layout)

window.show()
sys.exit(app.exec_())