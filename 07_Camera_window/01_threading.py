"""
 * Requirements

pip install PyQt5
pip install opencv-python

"""

import sys
import threading

import cv2
from PyQt5 import QtGui
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

form_class = uic.loadUiType('window.ui')[0] # 만들어놓은 ui파일을 가져옴 각 클래스에서 상속하여 사용
class MainWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.label_img.setText #이건아직 ui파일을 불러오기전까진 모르는 거라서 자동완성ㅇ 뜨지 않음.
        self.capture = True
        self.thread = threading.Thread(target=self.video_capture_process)
        self.thread.start() # 스레드가 실행이 될때 동시에 실행할 함수를 지정해주는게 target함수.

    def video_capture_process(self):
        #스레드에 들어갈 target함수.
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)#웹캠을 불러옴

        while self.capture:
            ret, frame = cap.read() # 비디오 캡처
            self.set_image(frame)# frame을 img로 생성. 원래는 cv2.imgshow()로 frame을 띄움 이거랑 비슷한거
        cap.release()# 카메라 해제 
        # 다른 프로그램이 끝나도 얘는 끝나지않을 수 있음 따라서 같이 거지도록 self.capture 변수를 불러오고 실행이되다가 False로 바뀌면 while탈출 후 코드종료
        # 이벤트를 통해서 띄워놓은 창들을 종료했을때 False로 바뀔수 잇도록 처리.  >> closeEvent()

    def set_image(self, frame):
        # 파이큐티가 지원하는 이미지형탤 바꿔주는 함수. (numpy array, width,height, 채널*가로(한줄이 몇픽셀),어떤포맷을가지고있는 파일인지)
        image = QtGui.QImage(frame, frame.shape[1], frame.shape[0], frame.shape[1] * 3, QtGui.QImage.Format_BGR888)
        pixmap = QtGui.QPixmap(image)
        self.label_image.setPixmap(pixmap)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        # 이거는 Qmainwindow가 가지고있는 기본 메소드.
        # 창ㅇ 닫히는 이벤트가 발생하면 이 함수를 실행하도록 하는 이벤트함수.
        self.capture = False # 카메라캡처종료되게끔 False로 변환. 스레드 탈출
        self.thread.join() # 웹캠불러오고 하는게 종료될때까지 창들이 종료되지않을거란 보장이없음. 따라서 동시에되게끔. 스레드가 끝나기까지 메인스레드가 기다려줌


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow() # 이벤트루프시작전 카메라를 띄워오는 그런걸 받아와야함
    window.show()

    app.exec_() # event 류ㅜ프시작
