# -*- coding:utf-8 -*-
import types

from PyQt4 import QtCore
from PyQt4 import QtGui

# 系统托盘类
class SystemTray(QtGui.QSystemTrayIcon):
    def __init__(self, parent, *args):
        # 初始化QSystemTrayIcon
        QtGui.QSystemTrayIcon.__init__(self, parent, *args)

        # 设置系统托盘图标
        self.setIcon(QtGui.QIcon('icon\\icon.png'))

        # 建立系统托盘图标菜单
        menu = QtGui.QMenu(parent)

        self.action_show = QtGui.QAction('Show Main Window', menu)
        menu.addAction(self.action_show)

        # 设置系统托盘图标菜单
        self.setContextMenu(menu)

        # 系统托盘图标被激活
        self.activated.connect(self.on_activated)

        # 显示系统托盘图标
        self.show()

    @QtCore.pyqtSlot(QtGui.QSystemTrayIcon.ActivationReason)
    def on_activated(self, reason):
        if reason == QtGui.QSystemTrayIcon.DoubleClick:
            if not isinstance(self.parent(), types.NoneType):
                if self.parent().isVisible():
                    self.parent().hide()
                else:
                    self.parent().show()