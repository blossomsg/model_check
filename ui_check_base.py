from PySide2 import QtGui, QtWidgets


class UiCheckBase(QtWidgets.QWidget):
    """This class creates buttons and checkboxes"""

    def __init__(
            self, checkbox: QtWidgets.QCheckBox, *buttons: QtWidgets.QPushButton, font: QtGui.QFont
    ) -> None:
        """This function initializes checkbox and buttons. Sets the fonts, font size and fixed size policy
        for last button.

        Args:
            checkbox (QtWidgets.QCheckBox): A checkbox to toggle sanity checks
            *buttons (QtWidgets.QPushButton): Multiple Buttons
                to do sanity checks and display color status
            font (QtGui.QFont): Set font for Checkbox and Buttons
        """
        super().__init__()
        self.checkbox = checkbox
        self.buttons = buttons
        self.checkbox.setFont(font)
        for button in self.buttons:
            button.setFont(font)
        # Making the last button Fixed size policy
        self.buttons[-1].setSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
