"""Modules to create UI"""
import sys

import maya.OpenMayaUI as omui  # type: ignore
from PySide2 import QtCore, QtGui, QtWidgets
from shiboken2 import wrapInstance  # type: ignore

# pylint: disable=import-error
import constants
import model_check_widgets

ptr = omui.MQtUtil.mainWindow()
ptr_instance = wrapInstance(int(ptr), QtWidgets.QWidget)


# pylint: disable=too-many-instance-attributes
# pylint: disable=too-many-statements
class UiCheckWidget(QtWidgets.QWidget):
    """This function initializes the ui."""

    def __init__(self) -> None:
        super().__init__(parent=None)

        # Parent to Maya UI
        self.setParent(ptr_instance)
        self.setWindowFlags(QtCore.Qt.Window)

        self.check_asset_pushbutton = QtWidgets.QPushButton("Check Asset")
        self.check_asset_pushbutton.setFont(
            QtGui.QFont(constants.FONT, constants.FONT_POINT_SIZE)
        )

        self.checks_scrollarea = QtWidgets.QScrollArea()
        self.checks_scrollarea.setWidgetResizable(True)
        self.model_checks = model_check_widgets.ModelCheckWidgets()
        self.checks_scrollarea.setWidget(self.model_checks)

        self.information_plaintextedit = QtWidgets.QPlainTextEdit()
        self.information_clear_pushbutton = QtWidgets.QPushButton("Clear logs")
        self.information_clear_pushbutton.setFont(
            QtGui.QFont(constants.FONT, constants.FONT_POINT_SIZE)
        )
        self.fix_issues_pushbutton = QtWidgets.QPushButton("Fix All Issues")
        self.fix_issues_pushbutton.setFont(
            QtGui.QFont(constants.FONT, constants.FONT_POINT_SIZE)
        )

        # Splitting Scrollarea and Information Box
        self.splitter = QtWidgets.QSplitter()
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.addWidget(self.checks_scrollarea)

        self.information_frame = QtWidgets.QFrame(self.splitter)
        self.information_verticallayout = QtWidgets.QVBoxLayout(self.information_frame)
        self.information_verticallayout.addWidget(self.information_plaintextedit)
        self.information_verticallayout.addWidget(self.information_clear_pushbutton)
        self.information_verticallayout.setContentsMargins(1, 1, 1, 1)

        self.checks_info_horizontallayout = QtWidgets.QHBoxLayout()
        self.checks_info_horizontallayout.addWidget(self.splitter)

        # Layout all the widgets.
        self.layout = QtWidgets.QVBoxLayout()  # type: ignore[method-assign]
        self.layout.addWidget(self.check_asset_pushbutton)
        self.layout.addLayout(self.checks_info_horizontallayout)
        self.layout.addWidget(self.fix_issues_pushbutton)
        self.setLayout(self.layout)

        self.setGeometry(200, 100, 1500, 800)
        self.setWindowTitle("Model Check v1.0.0")
        self.show()


# Run the program
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = UiCheckWidget()
    sys.exit(app.exec_())
