import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_window1 import Ui_mainWindow as Ui_Window1
from ui_window2 import Ui_MainWindow as Ui_Window2

class Window1(QMainWindow, Ui_Window1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.dakai.clicked.connect(self.open_window2)
        self.guanbi.clicked.connect(self.close)
    def open_window2(self):
        self.window2 = Window2()
        self.window2.show()


class Window2(QMainWindow, Ui_Window2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.close)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window1 = Window1()
    window1.show()
    sys.exit(app.exec_())