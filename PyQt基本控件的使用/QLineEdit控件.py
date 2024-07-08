import sys
from PyQt5.QtWidgets import QApplication, QLineEdit, QVBoxLayout, QWidget

def on_text_changed(text):
    print("Text changed:", text)

app = QApplication(sys.argv)
window = QWidget()

layout = QVBoxLayout()
line_edit = QLineEdit()
line_edit.textChanged.connect(on_text_changed)

layout.addWidget(line_edit)
window.setLayout(layout)

window.show()
sys.exit(app.exec_())