# vim:ts=4:et
# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# <pep8 compliant>

try:
    import bpy
except ModuleNotFoundError:
    pass
else:
    from .collection import util_collection
    from .object import set_transform, create_data_object
    from .object import collect_objects, collect_collections
    from .object import collect_hierarchy_objects
    from .object import collect_armature_modifiers, collect_modifiers
    from .transform import translate, rotate, scale
from .utils import swapyz, swizzleq, strip_nnn, vector_str
