import bpy
from bpy.types import Operator

class ParticleTracker_OT_Operator(Operator):
    bl_idname = "object.particle_tracker_operator"
    bl_label = "Track Particle System"
    bl_description = "Track Particles"
    
    def execute(self, context):
        ps_list=[]
        # シーン内のすべてのオブジェクトを走査
        for obj in bpy.context.scene.objects:
            # オブジェクトがパーティクルシステムを持っているか確認
            if obj.particle_systems:
                #print(bpy.context.object.name_full)
                # bpy.context.evaluated_depsgraph_get() method don't depend on activeobject but whole sene
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
        print(ps_list)
        ps=ps_list[0]
        #パーティクルの位置を取得
        particles = ps.particles
        p_list = [p.location for p in particles]
        print(p_list)

        # make mesh
        edges = []
        faces = []
        plotDataMesh = bpy.data.meshes.new('plot_data')
        plotDataMesh.from_pydata(p_list, edges, faces)
        attr = plotDataMesh.attributes.new("p_list", 'FLOAT_VECTOR', 'POINT')
        attr.data.foreach_set("vector", [val for vec in p_list for val in vec])  # ベクトルのリストをフラット化して設定

        plotDataMesh.update()

        # make object from mesh
        plotDataObject = bpy.data.objects.new('plot_data_object', plotDataMesh)

        curScene = bpy.context.scene
        curScene.collection.objects.link(plotDataObject)

        def my_handler(scene):
            bpy.context.view_layer.update() 
            vts = plotDataMesh.vertices
            for i in range(len(particles)):
                vts[i].co = particles[i].location
            
            bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
            
        bpy.app.handlers.frame_change_pre.clear()
        bpy.app.handlers.frame_change_pre.append(my_handler)
        return {'FINISHED'}
    
class ParticleTracker_OT_Delete_Operator(Operator):
    bl_idname = "object.particle_tracker_delete_operator"
    bl_label = "Delete Particle Tracker"
    bl_description = "Remove Particle Tracker"
    
    def execute(self, context):
        # 削除したいオブジェクトの名前を指定
        object_name= "plot_data_object"
        # オブジェクトが存在するかチェック
        if object_name in bpy.data.objects:
            # オブジェクトを取得して削除
            bpy.data.objects.remove(bpy.data.objects[object_name], do_unlink=True)
            bpy.app.handlers.frame_change_pre.clear()
        return {'FINISHED'}
        

        