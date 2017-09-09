# -*- coding:utf-8 -*-

import sys

from PyQt4 import QtCore
from PyQt4 import QtGui

from client.system_tray import SystemTray
from client.about_window import AboutWindow


class MainWindow(QtGui.QWidget):
    def __init__(self):
        # 初始化QWidget
        QtGui.QWidget.__init__(self)

        # 初始化系统托盘图标
        self.system_tray = SystemTray(self)

        # 创建根布局
        layout = QtGui.QVBoxLayout(self)

        # 创建第一行布局
        h_box_layout = QtGui.QHBoxLayout()
        h_box_layout.addWidget(QtGui.QLabel('Server: '))
        self.line_edit_server = QtGui.QLineEdit()
        self.line_edit_server.setText('')
        h_box_layout.addWidget(self.line_edit_server)
        layout.addLayout(h_box_layout)

        # 创建第二行布局
        h_box_layout = QtGui.QHBoxLayout()
        h_box_layout.addWidget(QtGui.QLabel('Password: '))
        self.line_edit_password = QtGui.QLineEdit()
        self.line_edit_password.setText('')
        h_box_layout.addWidget(self.line_edit_password)
        layout.addLayout(h_box_layout)

        # 创建第三行布局（Button行）
        h_box_layout = QtGui.QHBoxLayout()
        self.button_hide = QtGui.QPushButton('&Hide')
        self.button_config = QtGui.QPushButton('&Config')
        self.button_about = QtGui.QPushButton('&About')
        self.button_about.clicked.connect(self.on_button_about_clicked)
        self.button_hide.clicked.connect(self.on_button_hide_clicked)
        h_box_layout.addWidget(self.button_hide)
        h_box_layout.addWidget(self.button_config)
        h_box_layout.addWidget(self.button_about)
        layout.addLayout(h_box_layout)

        # 创建第四行布局
        h_box_layout = QtGui.QHBoxLayout()
        self.button_start = QtGui.QPushButton('&Start')
        h_box_layout.addWidget(self.button_start)
        layout.addLayout(h_box_layout)

        # 设置窗口只能关闭和最小化
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint
                            | QtCore.Qt.WindowMinimizeButtonHint)
        # 设置窗口大小
        self.setFixedSize(600, 225)
        # 设置窗口标题
        self.setWindowTitle('Main Window')
        # 设定图标
        self.setWindowIcon(QtGui.QIcon('icon\\icon.png'))
        # 设置根布局
        self.setLayout(layout)

        # 显示窗口
        self.show()

    @QtCore.pyqtSlot()
    def on_button_hide_clicked(self):
        self.hide()

    @QtCore.pyqtSlot()
    def on_button_about_clicked(self):
        # QtGui.QMessageBox.information(self, 'About', 'About')
        AboutWindow(self)


if __name__ == '__main__':
    # 初始化主程序
    app = QtGui.QApplication(sys.argv)

    # 新建主窗口
    main_window = MainWindow()

    # 运行主程序
    sys.exit(app.exec_())
