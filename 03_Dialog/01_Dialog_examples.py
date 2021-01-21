"""
 * Requirements

pip install PyQt5

"""

import sys

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QVBoxLayout, QPushButton, QLabel
from PyQt5.QtWidgets import QInputDialog, QMessageBox, QFileDialog
from PyQt5.QtGui import QPixmap
# 메세지 박스

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(500, 500)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Message box
        self.button_message_box = QPushButton('Message box')
        self.layout.addWidget(self.button_message_box)
        self.button_message_box.clicked.connect(self.message_box_event) # 버튼을 눌렀을때 메세지박스라는 이벤트가 발생.

        # Input dialog
        self.button_input_dialog = QPushButton('Input dialog')
        self.label_text = QLabel()
        self.layout.addWidget(self.button_input_dialog)
        self.layout.addWidget(self.label_text)
        self.button_input_dialog.clicked.connect(self.input_dialog_event)

        # File dialog
        self.button_file_dialog = QPushButton('File dialog')
        self.label_image = QLabel()
        self.pixmap = QPixmap()
        self.layout.addWidget(self.button_file_dialog)
        self.layout.addWidget(self.label_image)
        self.button_file_dialog.clicked.connect(self.file_dialog_event)

    def message_box_event(self):
        # 한단락이 하나의 메세지박스를 띄우는 방법이 제시되어있음.
        # 단순한 정보전달 about
        QMessageBox.about(self, 'About box', 'Message') # 어떤 위젯에 추가된 메세지박스인지를알리기 위함 (어떤위젯에, 메세지창 제목, 메세지창 내용)

        #  information이면 정보를 알려주기위함(!)
        ret = QMessageBox.information(self, 'Information box', 'Message', QMessageBox.Ok | QMessageBox.Cancel, QMessageBox.Ok) # 맨 마지막파라미터는 ok를 누르면 informatio박스가 떴을때 엔터를 눌렀을때 ok로 넘어갈 수 있도록,,,기본버튼 설정
        # 어떤버튼이 눌려서 종료가 되었는지를 return하고 이가 ret에 담김 >> 메세지박스를 가지고 분기를 설정할수있다.
        if ret == QMessageBox.Ok:
            print('Information box : ok')
        elif ret == QMessageBox.Cancel:
            print('Information box : cancel')
        # warning
        ret = QMessageBox.warning(self, 'Warning box', 'Message', QMessageBox.Discard | QMessageBox.Cancel, QMessageBox.Discard)
        if ret == QMessageBox.Discard:
            print('Warning box : Discard')
        elif ret == QMessageBox.Cancel:
            print('Warning box : cancel')
        # 질문을하거나 동의를 구해야할때 question
        ret = QMessageBox.question(self, 'Question box', 'Message', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if ret == QMessageBox.Yes:
            print('Question box : yes')
        elif ret == QMessageBox.No:
            print('Question box : no')
        # 안된다고 막거나 경고표시 critical
        ret = QMessageBox.critical(self, 'Critical box', 'Message', QMessageBox.Discard | QMessageBox.Cancel, QMessageBox.Cancel)
        if ret == QMessageBox.Discard:
            print('Warning box : Discard')
        elif ret == QMessageBox.Cancel:
            print('Warning box : cancel')

    def input_dialog_event(self):
        # 메인윈도우에서보면 버튼을 누르면 (input_dialog란) 입력받을 수 있는 input_dialog 박스가 뜬다.
        # 어떤 텍스트를 받아오겠다. (어떤위젯?, 다이아로그창 이름, 어떤메세지?) 입력을 받을 수 잇는 창이다.
        text, ret = QInputDialog.getText(self, 'Input dialog', 'input : ')
        # return값은 입력된 텍스트, 어떤버튼이 눌렸는지 를 return한다.
        if ret:
            self.label_text.setText(text)

    def file_dialog_event(self):
        # 파일불러오기가능.
        ret = QFileDialog.getOpenFileName(self, 'Select file')# 어떤형시긍로 받아올지를 결정 getopen~~ (어떤위젯?, 어던메세지) > 파일이름정도 받아올때,
        # 폴더를 받아오고 싶을때 getexisting~~~~
        # return은 파일을 제대로 선택했으면 파일으ㅣ 이름이 return 안됐으면 없을것. ex)이미지파일 선택시 이미지파일의 path가 받아와질것.
        print(ret)

        path = ret[0]
        self.pixmap.load(path) # 이미지파일의 경로받아와서 pixmap을 통해 라벨에 띄우는 코드.
        self.label_image.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec_()
