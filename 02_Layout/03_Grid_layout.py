"""
 * Requirements

pip install PyQt5

"""

import sys

from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QSizePolicy

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = QWidget()
    window.resize(500, 500)
    # 박스가 위에서부터 쌓는 형식이였다면 그리드는 네모칸들을 나누어놓고 레이아웃을 배치하는 형식.
    layout = QGridLayout(window)
    window.setLayout(layout) # 레이아웃 윈도우에 셋팅
    # 라벨만들기
    label1 = QLabel("label1", window)
    label2 = QLabel("label2", window)
    label3 = QLabel("label3", window)

    label1.setStyleSheet("background-color:red")
    label2.setStyleSheet("background-color:orange")
    label3.setStyleSheet("background-color:yellow")
    # 박스레이아웃은 순차적이기 때문에 순서명시가 필요업었는데 얘는 순서를 명시해줘야함 (행,열)
    layout.addWidget(label1, 0, 0)
    layout.addWidget(label2, 0, 1)
    layout.addWidget(label3, 1, 0,1,2) #(행,열,행방향으로 몇칸, 열방향으로 몇칸)

    window.show()

    app.exec_()
