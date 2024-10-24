"""Modules to create model checks"""
from typing import List

from PySide2 import QtGui, QtWidgets

# pylint: disable=import-error
import constants
import ui_check_base


# pylint: disable=too-many-instance-attributes
class ModelCheckWidgets(QtWidgets.QWidget):
    """A class that creates and holds model check widgets for the UI."""

    def __init__(self) -> None:
        super().__init__()
        self.grid_layout = QtWidgets.QGridLayout()

        # Constraint Widgets Set
        self.constraint_check_widgets_set = ui_check_base.UiCheckBase(
            QtWidgets.QCheckBox("No Constraints"),
            QtWidgets.QPushButton("Delete All Constraints"),
            QtWidgets.QPushButton(),
            font=QtGui.QFont(constants.FONT, constants.FONT_POINT_SIZE),
        )

        # Master Pivot Origin Widgets Set
        self.master_group_pivot_origin_widgets_set = ui_check_base.UiCheckBase(
            QtWidgets.QCheckBox("Master group pivot is at origin"),
            QtWidgets.QPushButton("Reset master group pivot"),
            QtWidgets.QPushButton(),
            font=QtGui.QFont(constants.FONT, constants.FONT_POINT_SIZE),
        )

        # Center Pivot Widgets Set
        self.center_pivot_points_widgets_set = ui_check_base.UiCheckBase(
            QtWidgets.QCheckBox("Check Pivot points are centered"),
            QtWidgets.QPushButton("Center Pivots on all objects"),
            QtWidgets.QPushButton("Float Precision fix"),
            QtWidgets.QPushButton(),
            font=QtGui.QFont(constants.FONT, constants.FONT_POINT_SIZE),
        )

        # Construction History Widgets Set
        self.construction_history_widgets_set = ui_check_base.UiCheckBase(
            QtWidgets.QCheckBox("Check Construction History"),
            QtWidgets.QPushButton("Delete Construction History"),
            QtWidgets.QPushButton(),
            font=QtGui.QFont(constants.FONT, constants.FONT_POINT_SIZE),
        )

        # Frozen Transforms Widgets Set
        self.frozen_transforms_widgets_set = ui_check_base.UiCheckBase(
            QtWidgets.QCheckBox("All Transforms are frozen"),
            QtWidgets.QPushButton("Freeze Transforms on all Objects"),
            QtWidgets.QPushButton(),
            font=QtGui.QFont(constants.FONT, constants.FONT_POINT_SIZE),
        )

        # No Duplicate Shape Nodes Widgets Set
        self.no_duplicate_shape_nodes_widgets_set = ui_check_base.UiCheckBase(
            QtWidgets.QCheckBox("No Duplicate Shape Nodes"),
            QtWidgets.QPushButton("Highlight nodes with extra shape nodes"),
            QtWidgets.QPushButton(),
            font=QtGui.QFont(constants.FONT, constants.FONT_POINT_SIZE),
        )

        # No Expressions Widgets Set
        self.no_expressions_widgets_set = ui_check_base.UiCheckBase(
            QtWidgets.QCheckBox("No Expressions"),
            QtWidgets.QPushButton("Delete All expressions"),
            QtWidgets.QPushButton(),
            font=QtGui.QFont(constants.FONT, constants.FONT_POINT_SIZE),
        )

        # No Animation Widgets Set
        self.no_animation_widgets_set = ui_check_base.UiCheckBase(
            QtWidgets.QCheckBox("No Animation"),
            QtWidgets.QPushButton("Delete All Animations"),
            QtWidgets.QPushButton(),
            font=QtGui.QFont(constants.FONT, constants.FONT_POINT_SIZE),
        )

        # No Render Layers Widgets Set
        self.no_render_layers_widgets_set = ui_check_base.UiCheckBase(
            QtWidgets.QCheckBox("No Render Layers"),
            QtWidgets.QPushButton("Delete Render Layers"),
            QtWidgets.QPushButton(),
            font=QtGui.QFont(constants.FONT, constants.FONT_POINT_SIZE),
        )

        # No Display Layers Widgets Set
        self.no_display_layers_widgets_set = ui_check_base.UiCheckBase(
            QtWidgets.QCheckBox("No Display Layers"),
            QtWidgets.QPushButton("Delete Display Layers"),
            QtWidgets.QPushButton(),
            font=QtGui.QFont(constants.FONT, constants.FONT_POINT_SIZE),
        )

        # No Lights Widgets Set
        self.no_lights_widgets_set = ui_check_base.UiCheckBase(
            QtWidgets.QCheckBox("No Lights"),
            QtWidgets.QPushButton("Delete Lights"),
            QtWidgets.QPushButton(),
            font=QtGui.QFont(constants.FONT, constants.FONT_POINT_SIZE),
        )

        # No Additional Cameras Widgets Set
        self.no_additional_cameras_widgets_set = ui_check_base.UiCheckBase(
            QtWidgets.QCheckBox("No Additional Cameras"),
            QtWidgets.QPushButton("Delete all Additional Cameras"),
            QtWidgets.QPushButton(),
            font=QtGui.QFont(constants.FONT, constants.FONT_POINT_SIZE),
        )

        # No Unknown Nodes Widgets Set
        self.no_unknown_nodes_widgets_set = ui_check_base.UiCheckBase(
            QtWidgets.QCheckBox("No Unknown Nodes"),
            QtWidgets.QPushButton("Delete Unknown Nodes"),
            QtWidgets.QPushButton(),
            font=QtGui.QFont(constants.FONT, constants.FONT_POINT_SIZE),
        )

        # Viewport Set to Shaded, No Wireframe Widgets set
        self.viewport_shaded_widgets_set = ui_check_base.UiCheckBase(
            QtWidgets.QCheckBox("Viewport Set to Shaded"),
            QtWidgets.QPushButton("Set Viewport to Shaded"),
            QtWidgets.QPushButton(),
            font=QtGui.QFont(constants.FONT, constants.FONT_POINT_SIZE),
        )

        # No Non-Manifold Widgets set
        self.no_non_manifold_geometry_widgets_set = ui_check_base.UiCheckBase(
            QtWidgets.QCheckBox("No Non-Manifold Geometry"),
            QtWidgets.QPushButton("Highlight Manifold Geometry"),
            QtWidgets.QPushButton(),
            font=QtGui.QFont(constants.FONT, constants.FONT_POINT_SIZE),
        )

        # No N-Sided Faces Widgets set
        self.no_n_sided_faces_widgets_set = ui_check_base.UiCheckBase(
            QtWidgets.QCheckBox("No N-Sided Faces"),
            QtWidgets.QPushButton("Highlight N-Sided Faces"),
            QtWidgets.QPushButton(),
            font=QtGui.QFont(constants.FONT, constants.FONT_POINT_SIZE),
        )

        # No UV's in Negative Areas Widgets set
        self.no_uv_in_negative_area_widgets_set = ui_check_base.UiCheckBase(
            QtWidgets.QCheckBox("No UV's in Negative Areas"),
            QtWidgets.QPushButton("Highlight Objects"),
            QtWidgets.QPushButton(),
            font=QtGui.QFont(constants.FONT, constants.FONT_POINT_SIZE),
        )

        # No Hidden Geometry Widgets set
        self.no_hidden_geometry_widgets_set = ui_check_base.UiCheckBase(
            QtWidgets.QCheckBox("No Hidden Geometry"),
            QtWidgets.QPushButton("Unhide All Objects"),
            QtWidgets.QPushButton(),
            font=QtGui.QFont(constants.FONT, constants.FONT_POINT_SIZE),
        )

        # No Namespaces Widgets Set
        self.no_namespaces_widgets_set = ui_check_base.UiCheckBase(
            QtWidgets.QCheckBox("No Namespaces"),
            QtWidgets.QPushButton("Delete All Namespaces"),
            QtWidgets.QPushButton(),
            font=QtGui.QFont(constants.FONT, constants.FONT_POINT_SIZE),
        )

        self.add_widgets_set_to_layout()
        self.enable_all_checkboxes()
        self.setLayout(self.grid_layout)

    def add_widgets_set_to_layout(self) -> None:
        """This function is to isolate widget sets(checkbox and button) and add in scrollarea."""

        checks_widgets_sets = [
            self.constraint_check_widgets_set,
            self.master_group_pivot_origin_widgets_set,
            self.center_pivot_points_widgets_set,
            self.construction_history_widgets_set,
            self.frozen_transforms_widgets_set,
            self.no_duplicate_shape_nodes_widgets_set,
            self.no_expressions_widgets_set,
            self.no_animation_widgets_set,
            self.no_render_layers_widgets_set,
            self.no_display_layers_widgets_set,
            self.no_lights_widgets_set,
            self.no_additional_cameras_widgets_set,
            self.no_unknown_nodes_widgets_set,
            self.viewport_shaded_widgets_set,
            self.no_non_manifold_geometry_widgets_set,
            self.no_n_sided_faces_widgets_set,
            self.no_uv_in_negative_area_widgets_set,
            self.no_hidden_geometry_widgets_set,
            self.no_namespaces_widgets_set,
        ]
        self._add_widgets_sets_to_layout(widgets_sets=checks_widgets_sets)

    def enable_all_checkboxes(self) -> None:
        """This function is to enable all the model checks checkboxes."""

        checks_widgets_sets = [
            self.constraint_check_widgets_set.checkbox,
            self.master_group_pivot_origin_widgets_set.checkbox,
            self.center_pivot_points_widgets_set.checkbox,
            self.construction_history_widgets_set.checkbox,
            self.frozen_transforms_widgets_set.checkbox,
            self.no_duplicate_shape_nodes_widgets_set.checkbox,
            self.no_animation_widgets_set.checkbox,
            self.no_expressions_widgets_set.checkbox,
            self.no_render_layers_widgets_set.checkbox,
            self.no_display_layers_widgets_set.checkbox,
            self.no_lights_widgets_set.checkbox,
            self.no_additional_cameras_widgets_set.checkbox,
            self.no_unknown_nodes_widgets_set.checkbox,
            self.viewport_shaded_widgets_set.checkbox,
            self.no_non_manifold_geometry_widgets_set.checkbox,
            self.no_n_sided_faces_widgets_set.checkbox,
            self.no_uv_in_negative_area_widgets_set.checkbox,
            self.no_hidden_geometry_widgets_set.checkbox,
            self.no_namespaces_widgets_set.checkbox,
        ]

        self._set_all_checkboxes(checkboxes=checks_widgets_sets, state=True)

    def _add_widgets_sets_to_layout(
        self, widgets_sets: List[ui_check_base.UiCheckBase]
    ) -> None:
        """Helper function to add widget sets(checkbox and widget) to scrollarea"""
        for idx, widgets in enumerate(widgets_sets):
            self.grid_layout.addWidget(widgets.checkbox, idx, 1)
            if len(widgets.buttons) == 2:
                self.grid_layout.addWidget(widgets.buttons[0], idx, 2, 1, 2)
                self.grid_layout.addWidget(widgets.buttons[1], idx, 4)
            else:
                self.grid_layout.addWidget(widgets.buttons[0], idx, 2)
                self.grid_layout.addWidget(widgets.buttons[1], idx, 3)
                self.grid_layout.addWidget(widgets.buttons[2], idx, 4)

    @staticmethod
    def _set_all_checkboxes(
        checkboxes: List[ui_check_base.UiCheckBase], state: bool
    ) -> None:
        """Helper function to set the state of all the checkboxes.
        Args:
            checkbox List[ui_check_base.UiCheckBase.checkbox]: Checkboxes widgets of all the checks
            state (bool): Update Checkbox state with boolean
        """
        for checks in checkboxes:
            checks.setChecked(state)
