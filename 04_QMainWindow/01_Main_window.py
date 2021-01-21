"""
 * Requirements

pip install PyQt5

"""

import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction, QFileDialog, QPushButton
from PyQt5.QtWidgets import QVBoxLayout


# 기본창을 빈창이 아닌 기능이 포함된 창을 띄우는걸 해볼것이다.
# Qmainwindow는 이미 메뉴를 가지고있는 툴임.
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)

        # Actions
        self.action_load = QAction(QIcon('../images/icons/save.png'), 'Load file', self) # 아이콘이 어떤기능을 수행할 것인지. 어떤메세지, 어떤위젯에 띄울건지
        self.action_load.setShortcut('Ctrl+L') # 단축기 셋팅. action_load가 되도록
        self.action_load.triggered.connect(self.load_event) # 이 액션이 어떤기능을 수행할지는 명시하지 않음. 이를 signal에 slot을 다는거랑 마찬가지. action이 유발됐을대 어던 event가 발생한다.

        self.action_exit = QAction(QIcon('../images/icons/exit.png'), 'Exit', self)
        self.action_exit.setShortcut('ESC')
        self.action_exit.triggered.connect(self.close)

        # Status bar 상태를 볼 수 있는 글자를 넣을 수 잇는 바
        self.status_bar = self.statusBar() # 이미 모듈안에 구현이 다되어있음 status bar라는 객체를 받아와서 사용하면됨.

        # Menu bar
        self.menu_bar = self.menuBar() # 큐메인윈도우의 메뉴바라는 객체를 받아와 사용할 수 있다. 메뉴바에서 수행하는 기능을 컨ㄷ트롤하는 모듈이다.
        self.file_menu = self.menu_bar.addMenu('File')
        self.option_menu = self.menu_bar.addMenu('Options')

        self.file_menu.addAction(self.action_load) # 파일메뉴에 액션을 추가해줌.
        self.file_menu.addAction(self.action_exit)

        # Tool bar 어떠한 기능들이 포함된 아이콘 바
        self.tool_bar = self.addToolBar("Toolbar") # 툴바를 받아온다. addtoolbar로
        self.tool_bar.addAction(self.action_load) # 액션을 바로 추가해주면 툴바에 액션이 적용됨
        self.tool_bar.addAction(self.action_exit)

        # Central Widget 우리가만든 메인위젯들이 들어갈 것.
        window_widget = QWidget()
        window_layout = QVBoxLayout(window_widget)
        window_layout.addWidget(QPushButton("Button"))
        self.setCentralWidget(window_widget) # 큐메인윈도우의 메소드 중 setcen~~ 여기에 윈도우를 넣어주면 내가만들어서 넣은 위젯이 포함이됨.

    def load_event(self):
        self.status_bar.showMessage("Load file..") # 텍스트를 띄워주겠다.
        path = QFileDialog.getOpenFileName(self)
        print(path)
        self.status_bar.clearMessage() # 텍스트를 지운다.


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec_()
