"""
 * Requirements

pip install PyQt5

"""

import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        main_layout=QVBoxLayout(self)
        layout=QHBoxLayout()
        label1 = QLabel("label1")
        label2 = QLabel("label2")
        label3 = QLabel("label3")
        # 배경색을 각각 지정함.
        label1.setStyleSheet("background-color:red")
        label2.setStyleSheet("background-color:orange")
        label3.setStyleSheet("background-color:yellow")
        # # 아래로 순차로 쌓이는 경우
        # main_layout.addWidget(label1)
        # main_layout.addWidget(label2)
        # main_layout.addWidget(label3)

        # 처음은 아래로 나머지 둘은 가로로 쌓고싶을때 레이앙ㅅ에 레이아웃 중첩
        main_layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)
        main_layout.addLayout(layout)

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#
#     window = QWidget()
#     window.resize(500, 500)
#     # 주의 : 레이아웃은 위젯은 아님. 따라서 레이아웃자체가 위젯에 셋팅이되게됨. 위젯의 기본레이아웃으로 설정이되면 위젯안에 원하는 방식대로 쌓이게 되는것
#     layout = QHBoxLayout(window) # linear layout이랑 같은거. 위젯안에 위젯들을 집어넣는데 위치를 지정해주는게아닌 순차적으로 쌓는.
#     window.setLayout(layout) # 레이아웃을 위젯에 셋팅을해줌. 위젯내부에 다른 위젯이 합쳐지는 방식은 박스레이아웃의 방식을 따른다.
#     # 라벨을 3개만듬. window에 추가할것이므로 명시
#     label1 = QLabel("label1",window)
#     label2 = QLabel("label2",window)
#     label3 = QLabel("label3",window)
#     # 배경색을 각각 지정함.
#     label1.setStyleSheet("background-color:red")
#     label2.setStyleSheet("background-color:orange")
#     label3.setStyleSheet("background-color:yellow")
#
#     # 위젯에 연결
#     layout.addWidget(label1)
#     layout.addWidget(label2)
#     layout.addWidget(label3)
#     # 위젯에는 3개의 라벨이 추가된 상태로 나오게됨.
#     window.show()
#
#     app.exec_()

 if __name__ == '__main__':
     app = QApplication(sys.argv)

     window = MainWindow()  # 위젯대신 위젯을 상속받은 메인윈도우함수를 사용.
     window.show()

     app.exec_()
