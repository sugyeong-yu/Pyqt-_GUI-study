"""
 * Requirements

pip install PyQt5

"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout=QVBoxLayout(self)
        layout.addWidget(QPushButton('button'))

# 상속을 통해서 윚[ㅔㅅ을 분리,?
# Layout 중첩, QWidget 상속
if __name__ == '__main__':
    app = QApplication(sys.argv)

    #window = QWidget()
    window = MainWindow() # 위젯대신 위젯을 상속받은 메인윈도우함수를 사용.
    window.show()

    app.exec_()
