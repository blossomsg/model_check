"""Modules to sanity check maya models."""
from typing import List

import maya.app.renderSetup.model.renderSetup  # type: ignore
from maya import cmds, mel

# dictionary to store the values of the statuses
model_check_dict = {}


# Utility Functions
def select_parent_node(checks_dict: List[str]) -> None:
    """This function selects the parent group by splitting
    the name from full path.

    Args:
        checks_dict: (dict): Model check dictionary to fetch list of values
                eg: select_parent_node(model_check_dict["geometry_with_offset_pivot"])
    """
    parent_group = cmds.listRelatives(
        checks_dict,
        fullPath=True,
        parent=True,
    )
    parent_node = parent_group[0].split("|")[1]
    cmds.select(parent_node)


def hierarchy_selection() -> List[str]:
    """This function lists fullpath all descendents of the selection group.

    Returns:
        group_transforms: (List(Any)): List of maya nodes
                     eg: Result: ['|main|group2|group1|pCube1', '|main|group2|group1|pTorus1', ...]

    """
    group_selection: List[str] = cmds.ls(selection=True)
    group_transforms: List[str] = cmds.listRelatives(
        group_selection, allDescendents=True, fullPath=True, type="transform"
    )  # full hierarchy path incase there are name clashes
    return group_transforms


# Constaints Function
def check_constraints() -> None:
    """This function lists the type constraints from the scene and saves the
    values in a dictionary.
    """
    model_check_dict["unwanted_constraints"] = (
            cmds.ls(
                type=[
                    "parentConstraint",
                    "pointConstraint",
                    "orientConstraint",
                    "scaleConstraint",
                    "aimConstraint",
                ]
            )
            or []
    )


def delete_constraints() -> None:
    """This function queries "unwanted_constraints" key, and deletes all the
    constraints from the scene.
    """
    cmds.delete(model_check_dict.get("unwanted_constraints"))


# Master Group Pivot Function
def check_master_group_pivot() -> None:
    """This function checks assets master group pivot position saves the values in a
    dictionary.
    """
    group_selection: List[str] = cmds.ls(selection=True)
    offset_scalepivot_value: List[int] = cmds.xform(
        group_selection, scalePivot=True, query=True
    )
    offset_rotatepivot_value: List[int] = cmds.xform(
        group_selection, rotatePivot=True, query=True
    )
    # centerpivot the geo
    cmds.xform(group_selection, zeroTransformPivots=True, preserve=True)
    # then we take the center pivot value
    centerpivot_scalepivot_pivot: List[int] = cmds.xform(
        group_selection, scalePivot=True, query=True
    )
    centerpivot_rotatepivot_pivot: List[int] = cmds.xform(
        group_selection, rotatePivot=True, query=True
    )
    # set the pivots back to offset position
    # set_offset_scalepivot_vlaue to selected geo
    cmds.xform(group_selection, scalePivot=offset_scalepivot_value)
    # set_offset_rotatepivot_vlaue to selected geo
    cmds.xform(group_selection, rotatePivot=offset_rotatepivot_value)
    # compare the offset and center pivots if not equal save in a list
    model_check_dict["master_group_with_offset_pivot"] = (
        group_selection
        if offset_scalepivot_value != centerpivot_scalepivot_pivot
           or offset_rotatepivot_value != centerpivot_rotatepivot_pivot
        else []
    )


def center_pivot_master_group() -> None:
    """This function center pivots to the object."""
    cmds.xform(
        model_check_dict.get("master_group_with_offset_pivot"),
        zeroTransformPivots=True,
        preserve=True,
    )


# Center Pivots Functions
def check_geometry_center_pivot() -> None:
    """This function checks assets(geo) pivot position.
    Maya docs page for reference
    https://knowledge.autodesk.com/support/maya-lt/learn-explore/caas/CloudHelp/cloudhelp/2015/ENU/MayaLT/files/FAQ-How-can-I-get-an-objects-pivot-point-in-world-space-htm.html
    """
    geo_with_offset = []
    group_transforms = hierarchy_selection()
    for transform in group_transforms:
        # we are taking the offset value
        offset_scalepivot_value = cmds.xform(transform, scalePivot=True, query=True)
        offset_rotatepivot_value = cmds.xform(transform, rotatePivot=True, query=True)
        # centerpivot the geo
        cmds.xform(transform, centerPivots=True, preserve=True)
        # then we take the center pivot value
        centerpivot_scalepivot_pivot = cmds.xform(
            transform, scalePivot=True, query=True
        )
        centerpivot_rotatepivot_pivot = cmds.xform(
            transform, rotatePivot=True, query=True
        )
        # set the pivots back to offset position
        # set_offset_scalepivot_vlaue to selected geo
        cmds.xform(transform, scalePivot=offset_scalepivot_value)
        # set_offset_rotatepivot_vlaue to selected geo
        cmds.xform(transform, rotatePivot=offset_rotatepivot_value)
        # compare the offset and center pivots if not equal save in a list
        if (
                offset_scalepivot_value != centerpivot_scalepivot_pivot
                or offset_rotatepivot_value != centerpivot_rotatepivot_pivot
        ):
            geo_with_offset.append(transform)

    model_check_dict["geometry_with_offset_pivot"] = geo_with_offset


def center_pivot_all_objects() -> None:
    """This function center pivots the assets(geo)."""
    if model_check_dict.get("geometry_with_offset_pivot"):
        for geo in model_check_dict["geometry_with_offset_pivot"]:
            cmds.xform(geo, centerPivots=True, preserve=True)
        select_parent_node(model_check_dict["geometry_with_offset_pivot"])


def remove_float_precision_issue_nodes() -> None:
    """This function is only to be used if center_pivot_all function fails.
    Reason this was created becauseoffset and center pivot when compared
    showed difference in 10th place decimal values.
    """
    model_check_dict["geometry_with_offset_pivot"] = []


# Construction History Functions
def check_construction_histories() -> None:
    """This function checks the history on geometries.
    Maya docs page for reference.
    https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=__Nodes_polyBase_html
    """
    geo_with_history = []
    group_transforms = hierarchy_selection()
    for transform in group_transforms:
        shapes = cmds.listRelatives(transform, fullPath=True, shapes=True)
        if shapes:
            if cmds.listConnections(shapes[0], type="polyBase"):
                geo_with_history.append(shapes[0])

    model_check_dict["construction_history_list"] = geo_with_history


def delete_construction_history() -> None:
    """This function deletes the histories of the geometries."""
    if model_check_dict.get("construction_history_list"):
        for geo in model_check_dict["construction_history_list"]:
            cmds.delete(geo, constructionHistory=True)
        select_parent_node(model_check_dict["construction_history_list"])


# Freeze Transform Functions
def check_all_transforms_are_frozen() -> None:
    """This function checks the geometries transform values."""
    geo_with_values = []
    group_transforms = hierarchy_selection()
    value = [0.0, 0.0, 0.0]
    scale_relative_value = [1.0, 1.0, 1.0]
    for transform in group_transforms:
        translate = cmds.xform(transform, translation=True, query=True)
        rotation = cmds.xform(transform, rotation=True, query=True)
        scale = cmds.xform(transform, scale=True, query=True, relative=True)
        if translate != value or rotation != value or scale != scale_relative_value:
            geo_with_values.append(transform)

    model_check_dict["freeze_tranform_list"] = geo_with_values


def freeze_transforms() -> None:
    """This function freezes the transforms of the assets(geo)"""
    if model_check_dict.get("freeze_tranform_list"):
        for geo in model_check_dict["freeze_tranform_list"]:
            cmds.makeIdentity(geo, apply=True)
        select_parent_node(model_check_dict["freeze_tranform_list"])


# Duplicate Shapes Functions
def check_duplicate_shape_nodes() -> None:
    """This function checks the geometries shapes."""
    geo_with_more_shapes = []
    group_selection = cmds.ls(selection=True)
    group_transforms = cmds.ls(group_selection, dagObjects=True, type="transform")
    for child in group_transforms:
        shapes = cmds.listRelatives(child, shapes=True, noIntermediate=True)
        if shapes:
            if len(shapes) > 1:
                geo_with_more_shapes.append(child)
    model_check_dict["unwanted_multiple_shape_nodes"] = geo_with_more_shapes


def highlight_shapes_with_extra_shape_nodes() -> None:
    """This function highlights geo with extra shapes."""
    cmds.select(model_check_dict.get("unwanted_multiple_shape_nodes"))


# Check Expressions functions
def check_expressions() -> None:
    """This function lists the expression nodes from the scene."""
    model_check_dict["unwanted_expressions"] = cmds.ls(type="expression") or []


def delete_expressions() -> None:
    """This function deletes all the expressions from the scene."""
    cmds.delete(model_check_dict.get("unwanted_expressions"))


# check animation curves functions
def check_animation_curves() -> None:
    """This function lists the anim curves nodes from the scene."""
    model_check_dict["unwanted_animation_curves"] = (
            cmds.ls(type=["animCurveTL", "animCurveTA", "animCurveTU"]) or []
    )


def delete_animation_curves() -> None:
    """This function deletes all the anim curves nodes from the scene."""
    cmds.delete(model_check_dict.get("unwanted_animation_curves"))


# check render setup layers functions
def check_render_layers() -> None:
    """This function lists the render setups layers from the scene"""
    model_check_dict["unwanted_rendersetup_layers"] = (
            cmds.ls(type="renderSetupLayer") or []
    )


def delete_render_layers() -> None:
    """This function deletes all the rendersetup layers from the scene"""
    if model_check_dict.get("unwanted_rendersetup_layers"):
        rs = maya.app.renderSetup.model.renderSetup.instance()
        rs.clearAll()


# Display Layers Functions
def check_display_layers() -> None:
    """This function lists the display layers from the scene."""
    default_layers = ["defaultLayer"]
    list_display_layers = cmds.ls(type="displayLayer")
    model_check_dict["unwanted_display_layers"] = [
                                                      layers for layers in list_display_layers if
                                                      layers not in default_layers
                                                  ] or []


def delete_display_layers() -> None:
    """This function deletes all the display layers from the scene."""
    cmds.delete(model_check_dict.get("unwanted_display_layers"))


# Vray Light Functions
def check_vray_lights() -> None:
    """This function lists the vray lights from the scene."""
    model_check_dict["unwanted_vray_lights"] = (
            cmds.ls(
                type=[
                    "VRayLightRectShape",
                    "VRayLightDomeShape",
                    "VRayLightIESShape",
                    "VRayLightSphereShape",
                    "VRaySunTarget",
                ]
            )
            or []
    )


def delete_vray_lights() -> None:
    """This function deletes all the vray lights from the scene."""
    cmds.delete(
        cmds.listRelatives(model_check_dict.get("unwanted_vray_lights"), parent=True)
    )


# cameras functions
def check_cameras() -> None:
    """This function lists the cameras from the scene."""
    default_cameras = ["frontShape", "perspShape", "sideShape", "topShape"]
    list_cameras = cmds.ls(type="camera")
    unwanted_cameras = [cam for cam in list_cameras if cam not in default_cameras]
    model_check_dict["unwanted_cameras"] = [
                                               cmds.listRelatives(parents, allParents=True)[0] for parents in
                                               unwanted_cameras
                                           ] or []


def delete_unwanted_cameras() -> None:
    """This function deletes all the unwanted cameras from the scene."""
    cmds.delete(model_check_dict.get("unwanted_cameras"))


# Unknown Functions
def check_unknown_nodes() -> None:
    """This function lists the unknown nodes from the scene."""
    model_check_dict["unknown_nodes"] = cmds.ls(type="unknown") or []


def delete_unknown_nodes() -> None:
    """This function deletes all the unknown nodes from the scene."""
    cmds.delete(model_check_dict.get("unknown_nodes"))


# Shaded Viewport Functions
def check_viewport_shading() -> None:
    """This function checks the viewport for wireframe shading."""
    model_check_dict["viewport_shaded"] = [] if cmds.modelEditor("modelPanel4", query=True,
                                                                 wireframeOnShaded=True) else [
        "Not Shaded with Wireframe"]


def set_viewport_shading() -> None:
    """This function sets the viewport to wireframe shading."""
    cmds.modelEditor("modelPanel4", edit=True, wireframeOnShaded=True)


# Viewport Display Smoothness
def viewport_smoothness() -> None:
    """This function sets the scene geo smoothness."""
    cmds.displaySmoothness(
        divisionsU=0, divisionsV=0, pointsWire=4, pointsShaded=1, polygonObject=1
    )


# Non-Mainfold Functions
def check_nonmanifold_geometry() -> None:
    """This function checks the geometries non-manifold faces in the selected group."""
    list_of_vertices_and_faces = []
    group_transforms = hierarchy_selection()
    for transform in group_transforms:
        if cmds.polyInfo(transform, nonManifoldVertices=True, laminaFaces=True):
            list_of_vertices_and_faces.append(
                cmds.polyInfo(transform, nonManifoldVertices=True, laminaFaces=True)
            )
    flatten_list = [
        each for vertex_face in list_of_vertices_and_faces for each in vertex_face
    ]
    model_check_dict["nonmanifold_list"] = flatten_list or []


def highlight_nonmanifold_geometry() -> None:
    """This function selects the non-manifold faces from dictionary which is
    higlighted in viewport."""
    cmds.select(model_check_dict.get("nonmanifold_list"))


# N-Sided Faces Functions
def check_n_sided_faces() -> None:
    """This function checks the geometries n-sided faces in the selected group."""
    group_selection = cmds.ls(selection=True)
    # pylint: disable=line-too-long
    ngons_list = mel.eval(
        'polyCleanupArgList 4 { "0","2","0","0","1","0","0","0","0","1e-05","0","1e-05","0","1e-05","0","-1","0",'
        '"0" };'
    )
    cmds.select(group_selection)
    model_check_dict["nsided_faces"] = ngons_list or []


def highlight_n_sided_faces() -> None:
    """This function selects the n-sided faces from dictionary which is higlighted in viewport."""
    cmds.select(model_check_dict.get("nsided_faces"))


# Hidden Geometries Functions
def check_hidden_geometry() -> None:
    """This function checks the hidden geometries in the scene."""
    hidden_items = []
    group_transforms = hierarchy_selection()
    for transform in group_transforms:
        if not cmds.getAttr(f"{transform}.visibility"):
            hidden_items.append(transform)
    model_check_dict["hidden_geometries"] = hidden_items


def unhide_geometries() -> None:
    """This function unhides the hidden geo in the scene."""
    if model_check_dict.get("hidden_geometries"):
        for geo in model_check_dict["hidden_geometries"]:
            cmds.setAttr(f"{geo}.visibility", 1)
        select_parent_node(model_check_dict["hidden_geometries"])


# UVS in Negative Spaces Functions
def check_uvs_in_negative_space() -> None:
    """
    This function checks the uv's are in x 0.0 and y 0.0 positive space for geometry.
    """
    geo_in_negative_space = []
    group_transforms = hierarchy_selection()
    for transform in group_transforms:
        boundingbox_evaluate = cmds.polyEvaluate(transform, boundingBox2d=True)
        try:
            value_u1 = boundingbox_evaluate[0][0]
            if value_u1 < 0.0:
                geo_in_negative_space.append(transform)
        except TypeError:
            pass
        try:
            value_v1 = boundingbox_evaluate[1][0]
            if value_v1 < 0.0:
                geo_in_negative_space.append(transform)
        except TypeError:
            pass
    model_check_dict["uvs_in_negative_space"] = geo_in_negative_space


def highlight_obj_uvs_in_negative_space() -> None:
    """This function highlights the uv's in negative space in viewport."""
    cmds.select(model_check_dict.get("uvs_in_negative_space"))


# Namespaces Functions
def check_namespaces() -> None:
    """This function lists the namespaces in the scene."""
    default_namespace = ["UI", "shared"]
    all_namespaces = cmds.namespaceInfo(listOnlyNamespaces=True)
    model_check_dict["unwanted_namespaces"] = [
                                                  names for names in all_namespaces if names not in default_namespace
                                              ] or []


def remove_unwanted_namespaces() -> None:
    """This function deletes the namespaces from the scene."""
    unwanted_namespaces = model_check_dict["unwanted_namespaces"]
    for names in unwanted_namespaces:
        try:
            cmds.namespace(removeNamespace=f"{names}", mergeNamespaceWithRoot=True)
        except RuntimeError:
            cmds.namespace(removeNamespace=f"{names}")


def assign_lambert1() -> None:
    """This function assigns the default lambert shader to every geo in the group."""
    group_selection = cmds.ls(selection=True)
    group_shape = cmds.listRelatives(
        group_selection, allDescendents=True, fullPath=True, type="shape"
    )
    for shape in group_shape:
        cmds.sets(shape, forceElement="initialShadingGroup", edit=True)


def delete_unused_shader_nodes() -> None:
    """Delete unused shader nodes in the scene file."""
    mel.eval('hyperShadePanelMenuCommand("hyperShadePanel1", "deleteUnusedNodes")')
