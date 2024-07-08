import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget

def on_button_click():
    print("Button clicked!")

app = QApplication(sys.argv)
window = QWidget()

layout = QVBoxLayout()
button = QPushButton("Click Me!")
button.clicked.connect(on_button_click)

layout.addWidget(button)
window.setLayout(layout)

window.show()
sys.exit(app.exec_())