import sys

from PySide2 import QtWidgets


class UiModelCheckWidget(QtWidgets.QWidget):
    """This function initializes the empty ui."""

    def __init__(self):
        super().__init__(parent=None)

        self.check_asset_pushbutton = QtWidgets.QPushButton("Check Asset")
        self.information_plaintextedit = QtWidgets.QPlainTextEdit()
        self.information_clear_pushbutton = QtWidgets.QPushButton("Clear logs")
        self.model_checks_scrollarea = QtWidgets.QScrollArea()
        self.fix_issues_pushbutton = QtWidgets.QPushButton("Fix All Issues")

        self.constraint_checkbox = QtWidgets.QCheckBox("No Constraints")
        self.constraint_button = QtWidgets.QPushButton("Delete All Constraints")
        self.constraint_color_button = QtWidgets.QPushButton()
        self.constraint_color_button.setSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )

        self.center_pivot_points_checkbox = QtWidgets.QCheckBox(
            "Check Pivot points are centered"
        )
        self.center_pivot_points_button = QtWidgets.QPushButton(
            "Center Pivots on all objects"
        )
        self.center_pivot_points_float_precision_button = QtWidgets.QPushButton(
            "Float Precision fix"
        )
        self.center_pivot_color_button = QtWidgets.QPushButton()
        self.center_pivot_color_button.setSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )

        # Scrollarea layout to manage all the checks widgets.
        self.scrollarea_layout = QtWidgets.QGridLayout(self.model_checks_scrollarea)
        self.scrollarea_layout.addWidget(self.constraint_checkbox, 1, 1)
        self.scrollarea_layout.addWidget(self.constraint_button, 1, 2, 1, 2)
        self.scrollarea_layout.addWidget(self.constraint_color_button, 1, 4)
        self.scrollarea_layout.addWidget(self.center_pivot_points_checkbox, 2, 1)
        self.scrollarea_layout.addWidget(self.center_pivot_points_button, 2, 2)
        self.scrollarea_layout.addWidget(
            self.center_pivot_points_float_precision_button, 2, 3
        )
        self.scrollarea_layout.addWidget(self.center_pivot_color_button, 2, 4)

        self.info_verticallayout = QtWidgets.QVBoxLayout()
        self.info_verticallayout.addWidget(self.information_plaintextedit)
        self.info_verticallayout.addWidget(self.information_clear_pushbutton)
        self.checks_info_horizontallayout = QtWidgets.QHBoxLayout()
        self.checks_info_horizontallayout.addWidget(self.model_checks_scrollarea)
        self.checks_info_horizontallayout.addLayout(self.info_verticallayout)

        # Layout all the widgets.
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.check_asset_pushbutton)
        self.layout.addLayout(self.checks_info_horizontallayout)
        self.layout.addWidget(self.fix_issues_pushbutton)
        self.setLayout(self.layout)

        self.setGeometry(200, 100, 400, 300)
        self.setWindowTitle("Model Check v1.0.0")
        self.show()


# Run the program
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = UiModelCheckWidget()
    sys.exit(app.exec_())
