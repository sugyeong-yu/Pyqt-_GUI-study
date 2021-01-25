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
#학습된 모델을 불러와서동작하고싶을때. >> ex)얼굴검출
# 추가된 부분은 #####으로 구분되어있음.
form_class = uic.loadUiType('ui/window.ui')[0]
class MainWindow(QMainWindow, form_class):
    pixmap_change_signal = pyqtSignal(np.ndarray)

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        ################################################################################################################
        self.detector = cv2.CascadeClassifier('model/haarcascade_frontalface_default.xml') # 얼굴검출기 초기화
        ################################################################################################################

        self.video_thread = VideoThread()
        self.video_thread.set_detector(self.detector) # 다른 클래스에 detector를 전달해줌.
        self.video_thread.image_change_signal.connect(self.set_image)
        self.video_thread.start()

    @pyqtSlot(np.ndarray)
    def set_image(self, frame):
        image = QtGui.QImage(frame, frame.shape[1], frame.shape[0], frame.shape[1] * 3, QtGui.QImage.Format_BGR888)
        pixmap = QtGui.QPixmap(image)
        self.label_image.setPixmap(pixmap)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.video_thread.capture = False
        self.video_thread.wait()


class VideoThread(QThread):
    image_change_signal = pyqtSignal(np.ndarray)

    def set_detector(self, detector):
        self.detector = detector

    def run(self):
        self.capture = True
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

        while self.capture:
            ret, frame = cap.read()
            if ret:
                ########################################################################################################
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # 처리과정 추가. 컬러이미지-> 흑백영상전환-> 위치검출->
                faces = self.detector.detectMultiScale(gray, 1.3, 5) # 1.3, 5 는 민감도를 설정하는거 지금 몰라도됨 >> 얼굴정보가 return됨
                for (x, y, w, h) in faces:
                    sx = x
                    sy = y
                    ex = x + w
                    ey = y + h
                    cv2.rectangle(frame, (sx, sy), (ex, ey), (0, 255, 0), 3) # bbox를 그림
                ########################################################################################################
                self.image_change_signal.emit(frame) # 윈도우에 띄움


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec_()
