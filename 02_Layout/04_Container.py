"""
 * Requirements

pip install PyQt5

"""

import sys

from PyQt5.QtWidgets import QApplication, QGroupBox, QVBoxLayout, QScrollArea, QWidget, \
    QHBoxLayout, QTabWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
# 위젯을 배치하는데 테두리에 선을 그어놓고 그룹의 이름을 명시해줄 수 있는 형식. 얘네는 레이아웃은아닉 위젯,(다른위젯을 포함하되 디자인요소나 새로운 기능을 사용할수있도록한거)
if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = QWidget()
    window.resize(400, 400)
    window.show()

    main_layout = QHBoxLayout()
    window.setLayout(main_layout)

    # Group box 그룹이름을 명시하고 어떤특징을 가지고있는지 알려줄수있는 디자인요소 (수직방향의 박스)
    group_box = QGroupBox('Group name')
    group_layout = QVBoxLayout(group_box) # 레이아웃을 위젯에 셋팅 버티칼,,? 박스레이아웃 > 아래방향으로 하나씩 쌓임 , QH는 옆으로.
    group_layout.addWidget(QPushButton('Group box button'))# 임의의 버튼하나가 생성됨
    group_layout.addWidget(QPushButton('Group box button'))
    group_layout.addWidget(QPushButton('Group box button'))
    main_layout.addWidget(group_box)

    # Scroll area 스크롤을 사용하고싶을때
    scroll_area = QScrollArea() # scroll area를 만들고
    label = QLabel("a\nb\nc\nd\ne\nf\ng\nh\ni\nj\nk\nl\nm\nn\no\np\nq\nr\ns\nt\nu\nv\nw\nx\ny\nz") # 만들고싶은 라벨을 만들고
    scroll_area.setWidget(label) # scroll area에 라벨을 셋팅해주고
    main_layout.addWidget(scroll_area) #  scroll을 레이아웃에 셋팅해주기.
    # main_layout.addWidget(label)

    # Tab : 다른위젯들을 번갈아보고싶을때 쓰는기능
    tab_widget = QTabWidget() # 위젯을 임의로 만들어서 addtab이라는 명령어를 통해서 tab을 추가해주면 익 추가된 widget이 뜨는것.
    tab1 = QPushButton('Tab1 button')
    tab_widget.addTab(tab1, 'Tab 1') # 버튼을 tab1에 추가되는 것.

    tab2 = QWidget()
    tab_layout = QVBoxLayout(tab2)
    tab_layout.addWidget(QLabel('Tab2 label')) # 라벨을 넣ㅇ주고
    tab_layout.addWidget(QPushButton('Tab2 button'))# 버튼을 넣은 탭을 만들 수 있음.
    tab_widget.addTab(tab2, 'Tab 2')

    main_layout.addWidget(tab_widget)

    app.exec_()
