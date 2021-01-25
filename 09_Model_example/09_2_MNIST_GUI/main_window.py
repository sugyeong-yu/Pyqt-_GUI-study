"""
 * Requirements

pip install PyQt5
pip install opencv-python

https://pytorch.org/

conda install pytorch torchvision torchaudio cudatoolkit=11.0 -c pytorch
or
conda install pytorch torchvision torchaudio cpuonly -c pytorch

"""

import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

from test_tab import TabTest
from train_tab import TabTrain

form_class = uic.loadUiType('ui/main_window.ui')[0]
class MainWindow(QMainWindow, form_class):
    # ㅇ무것도 안들어있는 tab 위젯만 가지고있는 mainwindow
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # tab을 추가하기 >> 따로만든 ui파일을 가지고할거.
        self.tab_train = TabTrain(self.statusBar()) # 다른 파일로 만들어놓음 탭을 이용할떄 status bar를 이용할거므로 전달.
        self.tab_test = TabTest(self.statusBar())

        self.tab_widget.addTab(self.tab_train, "Train") # 탭추가
        self.tab_widget.addTab(self.tab_test, "Test")

        self.tab_widget.setCurrentIndex(0) # 나중에 추가한게 뒤에 ㄴ쌓이는,,? 뭐라는겨


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec_()
