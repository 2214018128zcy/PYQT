import sys
from PyQt5.QtWidgets import QApplication, QRadioButton, QCheckBox, QVBoxLayout, QWidget

def on_radio_button_toggled(checked):
    if checked:
        print("Radio button checked")

def on_checkbox_toggled(checked):
    if checked:
        print("Checkbox checked")

app = QApplication(sys.argv)
window = QWidget()

layout = QVBoxLayout()

radio_button = QRadioButton("Radio Button")
radio_button.toggled.connect(on_radio_button_toggled)

checkbox = QCheckBox("Checkbox")
checkbox.toggled.connect(on_checkbox_toggled)

layout.addWidget(radio_button)
layout.addWidget(checkbox)

window.setLayout(layout)
window.show()
sys.exit(app.exec_())