import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.execute_command)

    def execute_command(self):
        # 获取 LineEdit 中的文本
        command = self.lineEdit.text()

        # 在 TextBrowser 中输出命令
        self.textBrowser.append(f"执行命令: {command}")

        # 清空 LineEdit
        self.lineEdit.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())