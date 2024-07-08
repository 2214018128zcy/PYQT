import sys
from PyQt5.QtWidgets import QApplication, QComboBox, QVBoxLayout, QWidget

def on_selection_changed(index):
    selected_item = combo_box.currentText()
    print("Selected item:", selected_item)

app = QApplication(sys.argv)
window = QWidget()

layout = QVBoxLayout()
combo_box = QComboBox()
combo_box.addItem("Option 1")
combo_box.addItem("Option 2")
combo_box.currentIndexChanged.connect(on_selection_changed)

layout.addWidget(combo_box)
window.setLayout(layout)

window.show()
sys.exit(app.exec_())