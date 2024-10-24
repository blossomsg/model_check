"""Modules to create UI"""
import sys

import maya.OpenMayaUI as omui  # type: ignore
from PySide2 import QtCore, QtGui, QtWidgets
from shiboken2 import wrapInstance  # type: ignore

# pylint: disable=import-error
import constants
import model_check_funcs
import model_check_widgets
import utilities

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
        self.information_plaintextedit.setReadOnly(True)
        self.information_plaintextedit.setFont(
            QtGui.QFont(constants.FONT, constants.FONT_POINT_SIZE)
        )
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
        self.vlayout = QtWidgets.QVBoxLayout()
        self.vlayout.addWidget(self.check_asset_pushbutton)
        self.vlayout.addLayout(self.checks_info_horizontallayout)
        self.vlayout.addWidget(self.fix_issues_pushbutton)
        self.setLayout(self.vlayout)

        self.setGeometry(200, 100, 1500, 800)
        self.setWindowTitle("Check Asset v1.0.0")

        self.check_asset_pushbutton.clicked.connect(self.check_asset)
        self.fix_issues_pushbutton.clicked.connect(self.fix_issues)
        self.information_clear_pushbutton.clicked.connect(
            self.information_plaintextedit.clear
        )
        self.show()

    def check_asset(self) -> None:
        """This function checks the asset in the scene by executing -
        clearing plainedit command, empty dictionary, indiviual checks
        widgets list, checks function reference list, checks dictionary
        names list, All the lists are then looped to check if the option
        is checked or unchecked and accordingly execute the checks
        functions. Executes color buttons signals to display
        information's. Lastly executes individual fix functionality.
        """
        self.information_plaintextedit.clear()
        model_check_funcs.model_check_dict = {}
        model_checks_set = [
            self.model_checks.constraint_check_widgets_set,
            self.model_checks.master_group_pivot_origin_widgets_set,
            self.model_checks.center_pivot_points_widgets_set,
            self.model_checks.construction_history_widgets_set,
            self.model_checks.frozen_transforms_widgets_set,
            self.model_checks.no_duplicate_shape_nodes_widgets_set,
            self.model_checks.no_expressions_widgets_set,
            self.model_checks.no_animation_widgets_set,
            self.model_checks.no_render_layers_widgets_set,
            self.model_checks.no_display_layers_widgets_set,
            self.model_checks.no_lights_widgets_set,
            self.model_checks.no_additional_cameras_widgets_set,
            self.model_checks.no_unknown_nodes_widgets_set,
            self.model_checks.viewport_shaded_widgets_set,
            self.model_checks.no_non_manifold_geometry_widgets_set,
            self.model_checks.no_n_sided_faces_widgets_set,
            self.model_checks.no_hidden_geometry_widgets_set,
            self.model_checks.no_uv_in_negative_area_widgets_set,
            self.model_checks.no_namespaces_widgets_set,
        ]
        # Not executing the function, passing function references
        functions = [
            model_check_funcs.check_constraints,
            model_check_funcs.check_master_group_pivot,
            model_check_funcs.check_geometry_center_pivot,
            model_check_funcs.check_construction_histories,
            model_check_funcs.check_all_transforms_are_frozen,
            model_check_funcs.check_duplicate_shape_nodes,
            model_check_funcs.check_expressions,
            model_check_funcs.check_animation_curves,
            model_check_funcs.check_render_layers,
            model_check_funcs.check_display_layers,
            model_check_funcs.check_vray_lights,
            model_check_funcs.check_cameras,
            model_check_funcs.check_unknown_nodes,
            model_check_funcs.check_viewport_shading,
            model_check_funcs.check_nonmanifold_geometry,
            model_check_funcs.check_n_sided_faces,
            model_check_funcs.check_hidden_geometry,
            model_check_funcs.check_uvs_in_negative_space,
            model_check_funcs.check_namespaces,
        ]
        statuses = [
            "unwanted_constraints",
            "master_group_with_offset_pivot",
            "geometry_with_offset_pivot",
            "construction_history_list",
            "freeze_tranform_list",
            "unwanted_multiple_shape_nodes",
            "unwanted_expressions",
            "unwanted_animation_curves",
            "unwanted_rendersetup_layers",
            "unwanted_display_layers",
            "unwanted_vray_lights",
            "unwanted_cameras",
            "unknown_nodes",
            "viewport_shaded",
            "nonmanifold_list",
            "nsided_faces",
            "hidden_geometries",
            "uvs_in_negative_space",
            "unwanted_namespaces",
        ]
        for model_check, model_funcs, status in zip(
            model_checks_set, functions, statuses
        ):
            if model_check.checkbox.isChecked():
                model_funcs()
                if model_check_funcs.model_check_dict.get(status):
                    model_check.buttons[-1].setStyleSheet(constants.RED)
                else:
                    model_check.buttons[-1].setStyleSheet(constants.GREEN)
            else:
                model_check.buttons[-1].setStyleSheet("")
        self.display_check_results()
        self.fix_individual_issues()

    def display_check_results(self) -> None:
        """This function helps to display the dictionary results that are
        saved by all the functions during executions.Results are displayed
        in PlainTextEdit by clicking color buttons.
        """
        self.model_checks.constraint_check_widgets_set.buttons[-1].clicked.connect(
            lambda: self.information_plaintextedit.setPlainText(
                utilities.joinmylist(
                    model_check_funcs.model_check_dict["unwanted_constraints"]
                )
            )
        )

        self.model_checks.master_group_pivot_origin_widgets_set.buttons[
            -1
        ].clicked.connect(
            lambda: self.information_plaintextedit.setPlainText(
                utilities.joinmylist(
                    model_check_funcs.model_check_dict["master_group_with_offset_pivot"]
                )
            )
        )

        self.model_checks.center_pivot_points_widgets_set.buttons[-1].clicked.connect(
            lambda: self.information_plaintextedit.setPlainText(
                utilities.joinmylist(
                    model_check_funcs.model_check_dict["geometry_with_offset_pivot"]
                )
            )
        )

        self.model_checks.construction_history_widgets_set.buttons[-1].clicked.connect(
            lambda: self.information_plaintextedit.setPlainText(
                utilities.joinmylist(
                    model_check_funcs.model_check_dict["construction_history_list"]
                )
            )
        )

        self.model_checks.frozen_transforms_widgets_set.buttons[-1].clicked.connect(
            lambda: self.information_plaintextedit.setPlainText(
                utilities.joinmylist(
                    model_check_funcs.model_check_dict["freeze_tranform_list"]
                )
            )
        )

        self.model_checks.no_duplicate_shape_nodes_widgets_set.buttons[
            -1
        ].clicked.connect(
            lambda: self.information_plaintextedit.setPlainText(
                utilities.joinmylist(
                    model_check_funcs.model_check_dict["unwanted_multiple_shape_nodes"]
                )
            )
        )

        self.model_checks.no_expressions_widgets_set.buttons[-1].clicked.connect(
            lambda: self.information_plaintextedit.setPlainText(
                utilities.joinmylist(
                    model_check_funcs.model_check_dict["unwanted_expressions"]
                )
            )
        )

        self.model_checks.no_animation_widgets_set.buttons[-1].clicked.connect(
            lambda: self.information_plaintextedit.setPlainText(
                utilities.joinmylist(
                    model_check_funcs.model_check_dict["unwanted_animation_curves"]
                )
            )
        )

        self.model_checks.no_render_layers_widgets_set.buttons[-1].clicked.connect(
            lambda: self.information_plaintextedit.setPlainText(
                utilities.joinmylist(
                    model_check_funcs.model_check_dict["unwanted_rendersetup_layers"]
                )
            )
        )

        self.model_checks.no_display_layers_widgets_set.buttons[-1].clicked.connect(
            lambda: self.information_plaintextedit.setPlainText(
                utilities.joinmylist(
                    model_check_funcs.model_check_dict["unwanted_display_layers"]
                )
            )
        )

        self.model_checks.no_lights_widgets_set.buttons[-1].clicked.connect(
            lambda: self.information_plaintextedit.setPlainText(
                utilities.joinmylist(
                    model_check_funcs.model_check_dict["unwanted_vray_lights"]
                )
            )
        )

        self.model_checks.no_additional_cameras_widgets_set.buttons[-1].clicked.connect(
            lambda: self.information_plaintextedit.setPlainText(
                utilities.joinmylist(
                    model_check_funcs.model_check_dict["unwanted_cameras"]
                )
            )
        )

        self.model_checks.no_unknown_nodes_widgets_set.buttons[-1].clicked.connect(
            lambda: self.information_plaintextedit.setPlainText(
                utilities.joinmylist(
                    model_check_funcs.model_check_dict["unknown_nodes"]
                )
            )
        )

        self.model_checks.viewport_shaded_widgets_set.buttons[-1].clicked.connect(
            lambda: self.information_plaintextedit.setPlainText(
                utilities.joinmylist(
                    model_check_funcs.model_check_dict["viewport_shaded"]
                )
            )
        )

        self.model_checks.no_non_manifold_geometry_widgets_set.buttons[
            -1
        ].clicked.connect(
            lambda: self.information_plaintextedit.setPlainText(
                utilities.joinmylist(
                    model_check_funcs.model_check_dict["nonmanifold_list"]
                )
            )
        )

        self.model_checks.no_n_sided_faces_widgets_set.buttons[-1].clicked.connect(
            lambda: self.information_plaintextedit.setPlainText(
                utilities.joinmylist(model_check_funcs.model_check_dict["nsided_faces"])
            )
        )

        self.model_checks.no_hidden_geometry_widgets_set.buttons[-1].clicked.connect(
            lambda: self.information_plaintextedit.setPlainText(
                utilities.joinmylist(
                    model_check_funcs.model_check_dict["hidden_geometries"]
                )
            )
        )

        self.model_checks.no_uv_in_negative_area_widgets_set.buttons[
            -1
        ].clicked.connect(
            lambda: self.information_plaintextedit.setPlainText(
                utilities.joinmylist(
                    model_check_funcs.model_check_dict["uvs_in_negative_space"]
                )
            )
        )

        self.model_checks.no_namespaces_widgets_set.buttons[-1].clicked.connect(
            lambda: self.information_plaintextedit.setPlainText(
                utilities.joinmylist(
                    model_check_funcs.model_check_dict["unwanted_namespaces"]
                )
            )
        )

    def fix_issues(self) -> None:
        """This function fixes all the recorded issues at once and reruns
        the check_asset function."""
        model_check_funcs.delete_constraints()
        model_check_funcs.center_pivot_master_group()
        model_check_funcs.center_pivot_all_objects()
        model_check_funcs.remove_float_precision_issue_nodes()
        model_check_funcs.delete_construction_history()
        model_check_funcs.freeze_transforms()
        model_check_funcs.delete_expressions()
        model_check_funcs.delete_animation_curves()
        model_check_funcs.delete_render_layers()
        model_check_funcs.delete_display_layers()
        model_check_funcs.delete_vray_lights()
        model_check_funcs.delete_unwanted_cameras()
        model_check_funcs.delete_unknown_nodes()
        model_check_funcs.set_viewport_shading()
        model_check_funcs.unhide_geometries()
        model_check_funcs.remove_unwanted_namespaces()
        self.check_asset()

    def fix_individual_issues(self) -> None:
        """This function helps to fix all the recorded issues on individual level."""
        self.model_checks.constraint_check_widgets_set.buttons[0].clicked.connect(
            model_check_funcs.delete_constraints
        )
        self.model_checks.master_group_pivot_origin_widgets_set.buttons[
            0
        ].clicked.connect(model_check_funcs.center_pivot_master_group)
        self.model_checks.center_pivot_points_widgets_set.buttons[0].clicked.connect(
            model_check_funcs.center_pivot_all_objects
        )
        self.model_checks.center_pivot_points_widgets_set.buttons[1].clicked.connect(
            model_check_funcs.remove_float_precision_issue_nodes
        )
        self.model_checks.construction_history_widgets_set.buttons[0].clicked.connect(
            model_check_funcs.delete_construction_history
        )
        self.model_checks.frozen_transforms_widgets_set.buttons[0].clicked.connect(
            model_check_funcs.freeze_transforms
        )
        self.model_checks.no_duplicate_shape_nodes_widgets_set.buttons[
            0
        ].clicked.connect(model_check_funcs.highlight_shapes_with_extra_shape_nodes)
        self.model_checks.no_expressions_widgets_set.buttons[0].clicked.connect(
            model_check_funcs.delete_expressions
        )
        self.model_checks.no_animation_widgets_set.buttons[0].clicked.connect(
            model_check_funcs.delete_animation_curves
        )
        self.model_checks.no_render_layers_widgets_set.buttons[0].clicked.connect(
            model_check_funcs.delete_render_layers
        )
        self.model_checks.no_display_layers_widgets_set.buttons[0].clicked.connect(
            model_check_funcs.delete_display_layers
        )
        self.model_checks.no_lights_widgets_set.buttons[0].clicked.connect(
            model_check_funcs.delete_vray_lights
        )
        self.model_checks.no_additional_cameras_widgets_set.buttons[0].clicked.connect(
            model_check_funcs.delete_unwanted_cameras
        )
        self.model_checks.no_unknown_nodes_widgets_set.buttons[0].clicked.connect(
            model_check_funcs.delete_unknown_nodes
        )
        self.model_checks.viewport_shaded_widgets_set.buttons[0].clicked.connect(
            model_check_funcs.set_viewport_shading
        )
        self.model_checks.no_non_manifold_geometry_widgets_set.buttons[
            0
        ].clicked.connect(model_check_funcs.highlight_nonmanifold_geometry)
        self.model_checks.no_n_sided_faces_widgets_set.buttons[0].clicked.connect(
            model_check_funcs.highlight_n_sided_faces
        )
        self.model_checks.no_hidden_geometry_widgets_set.buttons[0].clicked.connect(
            model_check_funcs.unhide_geometries
        )
        self.model_checks.no_uv_in_negative_area_widgets_set.buttons[0].clicked.connect(
            model_check_funcs.highlight_obj_uvs_in_negative_space
        )
        self.model_checks.no_namespaces_widgets_set.buttons[0].clicked.connect(
            model_check_funcs.remove_unwanted_namespaces
        )


# Run the program
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = UiCheckWidget()
    sys.exit(app.exec_())
