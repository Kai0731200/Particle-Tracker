import bpy
from bpy.types import Panel

class ParticleTracker_PT_Panel(bpy.types.Panel): 
    bl_idname = "PT_PT_particle_tracker"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = "Particle Tracker"
    bl_category = 'Particle Tracker'

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        col = row.column()
        col.operator("object.particle_tracker_operator", text = "Create Particle Tracker")
        col.operator("object.particle_tracker_delete_operator", text = "Delete Particle Tracker")

    