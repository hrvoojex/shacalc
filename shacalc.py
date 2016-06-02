#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Calculates a password hash in Linux, located in /etc/shadow.
You need to enter salt (eg. $6$xxxxxxxx) and your
password (eg. my_password).
"""

import sys
import crypt
from PySide.QtGui import *


class MyApp(QMainWindow):
    """
    This class presents main application window
    """
    def __init__(self, parent=None):
        super(MyApp, self).__init__(parent)

        # main window size, title and icon
        self.setMinimumSize(800, 150)
        self.setWindowTitle("Calculate a password hash in Linux")
        self.setWindowIcon(QIcon("lock.ico"))

        # lines for entering data
        self.saltLabel = QLabel("Salt:")
        self.saltLine = QLineEdit()
        self.saltLine.setPlaceholderText("e.g. $6$xxxxxxxx")
        self.passwordLabel = QLabel("Password:")
        self.passwordLine = QLineEdit()
        self.hashLabel = QLabel("Hash")
        self.hashSunkenLabel = QLabel()
        self.hashSunkenLabel.setFrameStyle(QFrame.Box | QFrame.Sunken)
        self.resultButton = QPushButton("&Calculate", self)
        self.resultButton.setMaximumSize(100, 50)

        # set layout
        grid = QGridLayout()
        grid.addWidget(self.passwordLabel, 0, 0)
        grid.addWidget(self.passwordLine, 0, 1)
        grid.addWidget(self.saltLabel, 1, 0)
        grid.addWidget(self.saltLine, 1, 1)
        grid.addWidget(self.hashLabel, 3, 0)
        grid.addWidget(self.hashSunkenLabel, 3, 1)
        grid.addWidget(self.resultButton, 2, 1)

        #  set central widget in QMainWindow
        widget = QWidget()
        widget.setLayout(grid)
        self.setCentralWidget(widget)

        #  This happens when button is clicked
        self.resultButton.clicked.connect(self.logic)

        #  Shows a widget
        self.show()

    def logic(self):
        """
        Calculates hash from salt and password
        """
        salt = self.saltLine.text()
        password = self.passwordLine.text()
        resulting_hash = crypt.crypt(password, salt)
        self.hashSunkenLabel.setText(resulting_hash)


def main():
    app = QApplication(sys.argv)
    instance = MyApp()
    instance.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
