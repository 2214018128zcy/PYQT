import sys
from PyQt5.QtWidgets import QApplication, QSlider, QProgressBar, QVBoxLayout, QWidget

def on_slider_value_changed(value):
    print("Slider value changed:", value)
    progress_bar.setValue(value)

app = QApplication(sys.argv)
window = QWidget()

layout = QVBoxLayout()
slider = QSlider()
slider.valueChanged.connect(on_slider_value_changed)

progress_bar = QProgressBar()
progress_bar.setRange(0, 100)

layout.addWidget(slider)
layout.addWidget(progress_bar)
window.setLayout(layout)

window.show()
sys.exit(app.exec_())