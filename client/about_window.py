# -*- coding:utf-8 -*-

from PyQt4 import QtCore
from PyQt4 import QtGui


# 关于窗口 继承自消息对话框
class AboutWindow(QtGui.QMessageBox):
    def __init__(self, parent):
        # 初始化Message Box
        QtGui.QMessageBox.__init__(self, parent)

        # 设置消息对话框模态为阻塞整个程序
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        # 设置窗口标记为对话框以及MS下固定对话框大小
        self.setWindowFlags(QtCore.Qt.Dialog
                            | QtCore.Qt.MSWindowsFixedSizeDialogHint)

        # 设置标题
        self.setWindowTitle("About")
        # 设置对话框内容
        self.setText(u'''
        <strong>看什么看</strong>
        <p>就是个填坑中的弹幕小程序</p>
        <p>有什么好看的</p>
        <a href="https://github.com/Frederick-Zhu/danmu">https://github.com/Frederick-Zhu/danmu</a>
        ''')

        # 添加确定键并绑定关闭窗口动作
        self.button_ok = self.addButton(QtGui.QMessageBox.Ok)
        self.button_ok.clicked.connect(self.close)

        # 设置图标 图标来源于父窗口最大的图标
        self.setIconPixmap(parent.windowIcon().pixmap(sorted(self.windowIcon().availableSizes(), key=lambda x: x.width() * x.height())[0]))

        # 显示对话框
        self.show()

    def closeEvent(self, QCloseEvent):
        self.parent().flag_window_about = False
