# This program is free software; you can redistribute it and/or modify!
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "ParticleTracker",
    "author" : "Kai0731200",
    "description" : "",
    "blender" : (4, 10, 0),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "Generic"
}

if "bpy" in locals():
    import imaplib
    imaplib.reload(ParticleTracker_operator)
    imaplib.reload(ParticleTracker_ui)
else:
    from . import ParticleTracker_operator
    from . import ParticleTracker_ui

import bpy

# 関数の定義
# パーティクルシステムの名前一覧を取得する関数
def get_particle_system_names(self, context) -> list:
    obj = context.object
    particle_systems = obj.particle_systems
    particle_system_names = [(ps.name, ps.name, "") for ps in particle_systems]

    return particle_system_names

classes = (
    ParticleTracker_operator.ParticleTracker_OT_Operator,
    ParticleTracker_ui.ParticleTracker_PT_Panel
)

def register():
    for c in classes:
        bpy.utils.register_class(c)
    bpy.types.Scene.selected_particle_system_name = bpy.props.EnumProperty(items=[], name="Selected Particle System Name")
    # パーティクルシステムの名前一覧を更新
    bpy.types.Scene.selected_particle_system_name = bpy.props.EnumProperty(
        items=get_particle_system_names,
        name="Selected Particle System Name"
    )

def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)
    del bpy.types.Scene.selected_particle_system_name

if __name__ == "__main__":
    register()
