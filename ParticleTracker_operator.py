import bpy
from bpy.types import Operator

class ParticleTracker_OT_Operator(Operator):
    bl_idname = "object.particle_tracker_operator"
    bl_label = "Track Particle System"
    bl_description = "Track Particles"
    
    def execute(self, context):
        ps_list=[]
        # アクティブなオブジェクトを取得
        obj = context.active_object
        
        # アクティブなオブジェクトが存在するか確認
        if obj is None:
            self.report({'ERROR'}, "No active object found. Please select an object.")
            return {'CANCELLED'}
        
        # オブジェクトがパーティクルシステムを持っているか確認
        if obj.particle_systems:
            #print(bpy.context.object.name_full)
            # bpy.context.evaluated_depsgraph_get() method はアクティブなオブジェクトではなくシーン全体に依存している
            depsgraph = bpy.context.evaluated_depsgraph_get()
            modified = obj.evaluated_get(depsgraph)
            print("オブジェクト名:", obj.name)
            # オブジェクトごとに存在するパーティクルシステムの情報を取得
            for ps in obj.particle_systems:
                ps_list.append(modified.particle_systems[0])
                #print("　- パーティクルシステム名:", ps.name)
                #print("　　- パーティクル数:", len(ps.particles))
                # 他のパーティクルシステムのプロパティも取得可能
                # 例えば、psys.settings など
        else:
            self.report({'INFO'}, "No particle system found in the active object.")

        if not ps_list:
            self.report({'ERROR'}, "No particle system found in the active object.")
            return {'CANCELLED'}
            
        #print(ps_list)
        ps=ps_list[0]
        #パーティクルの位置を取得
        particles = ps.particles
        p_list = [p.location for p in particles]
        #print(p_list)

        # ポイントの作成
        edges = []
        faces = []
        plotDataPoint = bpy.data.meshes.new('plot_data')
        plotDataPoint.from_pydata(p_list, edges, faces)
        attr = plotDataPoint.attributes.new("p_list", 'FLOAT_VECTOR', 'POINT')
        attr.data.foreach_set("vector", [val for vec in p_list for val in vec])  # ベクトルのリストをフラット化して設定

        plotDataPoint.update()

        # ポイントからオブジェクトを作成
        plotDataObject = bpy.data.objects.new(ps.name+'_Tracker', plotDataPoint)

        curScene = bpy.context.scene
        curScene.collection.objects.link(plotDataObject)

        def my_handler(scene):
            bpy.context.view_layer.update() 
            vts = plotDataPoint.vertices
            for i in range(len(particles)):
                vts[i].co = particles[i].location
            
            bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
            
        bpy.app.handlers.frame_change_pre.clear()
        bpy.app.handlers.frame_change_pre.append(my_handler)
        self.report({'INFO'}, "Particle tracking completed successfully.")
        return {'FINISHED'}


#ハンドラーを削除する関数
def remove_handler(obj):
        handlers_to_remove = []
        for handler in bpy.app.handlers.frame_change_pre:
            if obj in handler.__dict__.values():
                handlers_to_remove.append(handler)
        for handler in handlers_to_remove:
            print(handler)
            bpy.app.handlers.frame_change_pre.remove(handler)

# オブジェクトと今あるハンドラーを全て削除する関数
class ParticleTracker_OT_Delete_Operator(Operator):
    bl_idname = "object.particle_tracker_delete_operator"
    bl_label = "Delete Particle Tracker"
    bl_description = "Remove Particle Tracker and Clear all handler"

    def execute(self, context):
        selected_obj = context.active_object
        if selected_obj:
            bpy.app.handlers.frame_change_pre.clear()
            bpy.data.objects.remove(selected_obj, do_unlink=True)
            self.report({'INFO'}, "Selected object removed.")
        else:
            self.report({'INFO'}, "No active object selected.")
        return {'FINISHED'}


# 今あるハンドラーを全て削除する
class ParticleTracker_OT_Clear_Handler(Operator):
    bl_idname = "object.particle_tracker_clear_handler"
    bl_label = "Delete all handler"
    bl_description = "Remove all handler"

    def execute(self, context):
        # すべてのハンドラーを削除
        bpy.app.handlers.frame_change_pre.clear()
        self.report({'INFO'}, "All handlers have been deleted.")
        return {'FINISHED'}
