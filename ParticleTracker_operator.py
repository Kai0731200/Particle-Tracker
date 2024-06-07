import bpy
from bpy.types import Operator

def get_particle_system_index_by_name(obj, particle_system_name):
            particle_systems = obj.particle_systems
            for i, particle_system in enumerate(particle_systems):
                if particle_system.name == particle_system_name:
                    return i
            # 見つからない場合は -1 を返す
            return -1

class ParticleTracker_OT_Operator(Operator):
    bl_idname = "object.particle_tracker_operator"
    bl_label = "Track Particle System"
    bl_description = "Track Particles"
    
    def execute(self, context):
        # アクティブなオブジェクトを取得
        obj = context.active_object
        # アクティブなオブジェクトが存在するか確認
        if obj is None:
            self.report({'ERROR'}, "No active object found. Please select an object.")
            return {'CANCELLED'}
        selected_particle_system_name = context.scene.selected_particle_system_name
        # 選択したパーティクルシステムを取得
        selected_particle_system = obj.particle_systems.get(selected_particle_system_name)
        if selected_particle_system:
            # モディファイアが適用された状態にする
            depsgraph = bpy.context.evaluated_depsgraph_get()
            modified = obj.evaluated_get(depsgraph)
            particle_system_index=get_particle_system_index_by_name(obj, selected_particle_system_name)
            particle_system=modified.particle_systems[particle_system_index]
        else:
            self.report({'ERROR'}, "No particle system found in the active object.")
            return {'CANCELLED'}
        
        frame_start = int(particle_system.settings.frame_start)
        frame_end = int(particle_system.settings.frame_end)

        #パーティクルの位置を取得
        particles = particle_system.particles
        particle_list = [p.location for p in particles]

        # ポイントの作成
        edges = []
        faces = []
        plotDataPoint = bpy.data.meshes.new('plot_data')
        plotDataPoint.from_pydata(particle_list, edges, faces)

        # ポイントからオブジェクトを作成
        tracker_name = particle_system.name+'_Tracker'
        plotDataObject = bpy.data.objects.new(tracker_name, plotDataPoint)
        curScene = bpy.context.scene
        curScene.collection.objects.link(plotDataObject)

        #作成したオブジェクトの頂点情報
        vertices = plotDataPoint.vertices
        #キーフレームの間隔
        frame_interval = 1

        #目標の座標に移動する処理を繰り返す
        for frame_num in range (frame_start, frame_end+1, frame_interval):
            bpy.context.scene.frame_set(frame_num)
            bpy.context.view_layer.update() 
            for i in range(len(particles)):
                if particles[i].alive_state!="UNBORN":
                    vertices[i].co = particles[i].location
                    vertices[i].keyframe_insert(data_path = "co",index = -1)
        
        bpy.context.scene.frame_set(frame_start)
        self.report({'INFO'}, "Particle tracking completed successfully.")
        return {'FINISHED'}


