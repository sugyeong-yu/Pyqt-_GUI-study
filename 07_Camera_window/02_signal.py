"""
 * Requirements

pip install PyQt5
pip install opencv-python

"""
import sys

import cv2
import numpy as np
from PyQt5 import QtGui
from PyQt5 import uic
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow


form_class = uic.loadUiType('window.ui')[0]
class MainWindow(QMainWindow, form_class):
    pixmap_change_signal = pyqtSignal(np.ndarray)

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.video_thread = VideoThread()# 만든스레드
        # 시그널이 발생했을때 set_image를 실행하겠다.>> 이미지를 불러오고 시그널발생 후 setimage실행 > numpy array배열을 인자로 받음, 그리고 프레임을 띄움
        self.video_thread.image_change_signal.connect(self.set_image) # 이미지가 바뀌는시그널이 발생할경우 set_image라는 이벤트발생
        self.video_thread.start()

    @pyqtSlot(np.ndarray) # 아래의 함수가 슬롯의 역할을 한다는 함수. 이거 굳이없어도 실행은 됨. 꾸며주는역할로써도 문제없다 뭐 언제쓰라는겨
    def set_image(self, frame):
        image = QtGui.QImage(frame, frame.shape[1], frame.shape[0], frame.shape[1] * 3, QtGui.QImage.Format_BGR888)
        pixmap = QtGui.QPixmap(image)
        self.label_image.setPixmap(pixmap)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.video_thread.capture = False
        self.video_thread.wait()


class VideoThread(QThread):
    #파이선에서 제공하는 스레드말고 파이큐티에서 제공하는 스레드 방식.(QThread)
    image_change_signal = pyqtSignal(np.ndarray)# 시그널이 발생했을때 시그널을 발생시키는 곳에서 인자를 넘겨받음.
    # 스레드가 start되면 run이라는 함수가 자동으로 실행됨
    def run(self):
        self.capture = True
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

        while self.capture:
            ret, frame = cap.read()
            if ret:
                # 이미지가 발생하면 이 시그널이 계속해서 발생함
                self.image_change_signal.emit(frame) #이미지 띄우는부분.> pyqt에서제공하는 signal  , emit은 시그널이 발생하도록 하는 명령어어

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec_()
