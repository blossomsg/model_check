"""Modules to create UI"""
import sys
from typing import List

import maya.OpenMayaUI as omui  # type: ignore
from PySide2 import QtCore, QtWidgets
from shiboken2 import wrapInstance  # type: ignore

ptr = omui.MQtUtil.mainWindow()
ptr_instance = wrapInstance(int(ptr), QtWidgets.QWidget)


class UiButtonCheckbox(QtWidgets.QWidget):
    """This class creates buttons and checkboxes"""

    def __init__(
        self, checkbox: QtWidgets.QCheckBox, *buttons: QtWidgets.QPushButton
    ) -> None:
        """This function initializes checkbox and buttons in fixed size policy for last button.

        Args:
            checkbox (QtWidgets.QCheckBox): A checkbox to toggle sanity checks
            *buttons (QtWidgets.QPushButton): Multiple Buttons
                to do sanity checks and display color status
        """
        super().__init__()
        self.checkbox = checkbox
        self.buttons = buttons
        # Making the last button Fixed size policy
        self.buttons[-1].setSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )


# pylint: disable=too-many-instance-attributes
class UiModelCheckWidget(QtWidgets.QWidget):
    """This function initializes the ui."""

    def __init__(self) -> None:
        super().__init__(parent=None)

        # Parent to Maya UI
        self.setParent(ptr_instance)
        self.setWindowFlags(QtCore.Qt.Window)

        self.check_asset_pushbutton = QtWidgets.QPushButton("Check Asset")
        self.model_checks_scrollarea = QtWidgets.QScrollArea()
        self.information_plaintextedit = QtWidgets.QPlainTextEdit()
        self.information_clear_pushbutton = QtWidgets.QPushButton("Clear logs")
        self.fix_issues_pushbutton = QtWidgets.QPushButton("Fix All Issues")

        # Constraint Widgets Set
        self.constraint_check_widgets_set = UiButtonCheckbox(
            QtWidgets.QCheckBox("No Constraints"),
            QtWidgets.QPushButton("Delete All Constraints"),
            QtWidgets.QPushButton(),
        )

        # Master Pivot Origin Widgets Set
        self.master_group_pivot_origin_widgets_set = UiButtonCheckbox(
            QtWidgets.QCheckBox("Master group pivot is at origin"),
            QtWidgets.QPushButton("Reset master group pivot"),
            QtWidgets.QPushButton(),
        )

        # Center Pivot Widgets Set
        self.center_pivot_points_widgets_set = UiButtonCheckbox(
            QtWidgets.QCheckBox("Check Pivot points are centered"),
            QtWidgets.QPushButton("Center Pivots on all objects"),
            QtWidgets.QPushButton("Float Precision fix"),
            QtWidgets.QPushButton(),
        )

        # Construction History Widgets Set
        self.construction_history_widgets_set = UiButtonCheckbox(
            QtWidgets.QCheckBox("Check Construction History"),
            QtWidgets.QPushButton("Delete Construction History"),
            QtWidgets.QPushButton(),
        )

        # Frozen Transforms Widgets Set
        self.frozen_transforms_widgets_set = UiButtonCheckbox(
            QtWidgets.QCheckBox("All Transforms are frozen"),
            QtWidgets.QPushButton("Freeze Transforms on all Objects"),
            QtWidgets.QPushButton(),
        )

        # No Duplicate Shape Nodes Widgets Set
        self.no_duplicate_shape_nodes_widgets_set = UiButtonCheckbox(
            QtWidgets.QCheckBox("No Duplicate Shape Nodes"),
            QtWidgets.QPushButton("Highlight nodes with extra shape nodes"),
            QtWidgets.QPushButton(),
        )

        # No Expressions Widgets Set
        self.no_expressions_widgets_set = UiButtonCheckbox(
            QtWidgets.QCheckBox("No Expressions"),
            QtWidgets.QPushButton("Delete All expressions"),
            QtWidgets.QPushButton(),
        )

        # No Animation Widgets Set
        self.no_animation_widgets_set = UiButtonCheckbox(
            QtWidgets.QCheckBox("No Animation"),
            QtWidgets.QPushButton("Delete All Animations"),
            QtWidgets.QPushButton(),
        )

        # No Render Layers Widgets Set
        self.no_render_layers_widgets_set = UiButtonCheckbox(
            QtWidgets.QCheckBox("No Render Layers"),
            QtWidgets.QPushButton("Delete Render Layers"),
            QtWidgets.QPushButton(),
        )

        # No Display Layers Widgets Set
        self.no_display_layers_widgets_set = UiButtonCheckbox(
            QtWidgets.QCheckBox("No Display Layers"),
            QtWidgets.QPushButton("Delete Display Layers"),
            QtWidgets.QPushButton(),
        )

        # No Lights Widgets Set
        self.no_lights_widgets_set = UiButtonCheckbox(
            QtWidgets.QCheckBox("No Lights"),
            QtWidgets.QPushButton("Delete Lights"),
            QtWidgets.QPushButton(),
        )

        # No Additional Cameras Widgets Set
        self.no_additional_cameras_widgets_set = UiButtonCheckbox(
            QtWidgets.QCheckBox("No Additional Cameras"),
            QtWidgets.QPushButton("Delete all Additional Cameras"),
            QtWidgets.QPushButton(),
        )

        # No Unknown Nodes Widgets Set
        self.no_unknown_nodes_widgets_set = UiButtonCheckbox(
            QtWidgets.QCheckBox("No Unknown Nodes"),
            QtWidgets.QPushButton("Delete Unknown Nodes"),
            QtWidgets.QPushButton(),
        )

        # Viewport Set to Shaded, No Wireframe Widgets set
        self.viewport_shaded_widgets_set = UiButtonCheckbox(
            QtWidgets.QCheckBox("Viewport Set to Shaded"),
            QtWidgets.QPushButton("Set Viewport to Shaded"),
            QtWidgets.QPushButton(),
        )

        # No Non-Mainfold Widgets set
        self.no_non_mainfold_geometry_widgets_set = UiButtonCheckbox(
            QtWidgets.QCheckBox("No Non-Mainfold Geometry"),
            QtWidgets.QPushButton("Highlight Mainfold Geometry"),
            QtWidgets.QPushButton(),
        )

        # No N-Sided Faces Widgets set
        self.no_n_sided_faces_widgets_set = UiButtonCheckbox(
            QtWidgets.QCheckBox("No N-Sided Faces"),
            QtWidgets.QPushButton("Highlight N-Sided Faces"),
            QtWidgets.QPushButton(),
        )

        # No UV's in Negative Areas Widgets set
        self.no_uv_in_negative_area_widgets_set = UiButtonCheckbox(
            QtWidgets.QCheckBox("No UV's in Negative Areas"),
            QtWidgets.QPushButton("Highlight Objects"),
            QtWidgets.QPushButton(),
        )

        # No Hidden Geometry Widgets set
        self.no_hidden_geometry_widgets_set = UiButtonCheckbox(
            QtWidgets.QCheckBox("No Hidden Geometry"),
            QtWidgets.QPushButton("Unhide All Objects"),
            QtWidgets.QPushButton(),
        )

        # No Namespaces Widgets Set
        self.no_namespaces_widgets_set = UiButtonCheckbox(
            QtWidgets.QCheckBox("No Namespaces"),
            QtWidgets.QPushButton("Delete All Namespaces"),
            QtWidgets.QPushButton(),
        )

        # Splitting Scrollarea and Information Box
        self.splitter = QtWidgets.QSplitter()
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.addWidget(self.model_checks_scrollarea)

        self.scrollarea_layout = QtWidgets.QGridLayout(self.model_checks_scrollarea)
        self.add_widgets_set_to_scrollarea()

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

    def add_widgets_set_to_scrollarea(self) -> None:
        """This function is to isolate widget sets(checkbox and button) and add in scrollarea."""

        checks_widgets_sets = [
            self.constraint_check_widgets_set,
            self.master_group_pivot_origin_widgets_set,
            self.center_pivot_points_widgets_set,
            self.construction_history_widgets_set,
            self.frozen_transforms_widgets_set,
            self.no_duplicate_shape_nodes_widgets_set,
            self.no_expressions_widgets_set,
            self.no_render_layers_widgets_set,
            self.no_display_layers_widgets_set,
            self.no_lights_widgets_set,
            self.no_additional_cameras_widgets_set,
            self.no_unknown_nodes_widgets_set,
            self.viewport_shaded_widgets_set,
            self.no_non_mainfold_geometry_widgets_set,
            self.no_n_sided_faces_widgets_set,
            self.no_uv_in_negative_area_widgets_set,
            self.no_hidden_geometry_widgets_set,
            self.no_namespaces_widgets_set,
        ]
        self._add_widgets_sets_to_scrollarea(widgets_sets=checks_widgets_sets)

    def _add_widgets_sets_to_scrollarea(
        self, widgets_sets: List[UiButtonCheckbox]
    ) -> None:
        """Helper function to add widget sets(checkbox and widget) to scrollarea"""
        for idx, widgets in enumerate(widgets_sets):
            self.scrollarea_layout.addWidget(widgets.checkbox, idx, 1)
            if len(widgets.buttons) == 2:
                self.scrollarea_layout.addWidget(widgets.buttons[0], idx, 2, 1, 2)
                self.scrollarea_layout.addWidget(widgets.buttons[1], idx, 4)
            else:
                self.scrollarea_layout.addWidget(widgets.buttons[0], idx, 2)
                self.scrollarea_layout.addWidget(widgets.buttons[1], idx, 3)
                self.scrollarea_layout.addWidget(widgets.buttons[2], idx, 4)


# Run the program
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = UiModelCheckWidget()
    sys.exit(app.exec_())
