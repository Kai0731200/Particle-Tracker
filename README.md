# Particle Tracker for Blender

Particle Tracker is a free add-on for Blender that allows you to track each particle by creating points from particles in a particle system in your scene. Fully compatible with Blender 4.1 and above, supports particle position tracking and animation.

The first version was created in 2024.


# DEMO
Create and track points at the particle position  
![スクリーンショット 2024-05-11 012537](https://github.com/Kai0731200/Particle-Tracker/assets/74250530/7ce743ab-1e34-4a9f-8e68-269b26de7471)

UI  
![スクリーンショット 2024-05-11 013257](https://github.com/Kai0731200/Particle-Tracker/assets/74250530/b7fe6f32-cf4d-4b57-a81a-e24195ae0ce4)

# Features

By using Particle Tracker, you can access particle information in particle systems that cannot be accessed directly with the current blender (4.1).
This add-on doesn't just create points at the particle's location; it also tracks the particle's position and moves the point each frame.
Additionally, since points are created, particle positions can be accessed from geometry nodes, allowing for various applications that are synchronized with particle systems.

This addon uses handlers.
In addition, Blender's particle system is realized using modifier functions, and it is not possible to directly access the position of each particle.
Therefore
bpy.context.evaluated_depsgraph_get(), ob.evaluated_get(depsgraph)
to get the position from the mesh when the modifier is applied.

# Requirement

Blender 4.1 or later

# Installation

1. Download Particle Tracker for Blender from [main](https://github.com/Kai0731200/Particle-Tracker/archive/refs/heads/main.zip)(best), or the latest release.
2. In Blender from the **File** menu open **User Preferences** .
3. Go to the **Add-ons** tab .
4. Look for any old version of TexTools currently installed and uninstall it.
5. Hit **Install Addon-on from File...** and Select the zip file.
6. Enable the Particle Tracker Addon.
7. In 3D view press N. You'll find new buttons **Particle Tracker panel** tab in the Side Bar.

# Usage
- **Create Particle Tracker** button will create one object **Particle Tracker** corresponding to the top particle system of the active object's slot.
The name of the object will be **"Particle System name" _Tracker**. Hereafter it is called **Particle Tracker**.
- The created **Particle Tracker** is an object consisting of (multiple) points, whose number and position correspond to the particles of the particle system.
- As you move the frame, the **Particle Tracker** moves to the same position as each particle in the particle system and tracks the particles.

- **Delete Particle Tracker and Clear All Handlers** deletes the selected object and clears all handlers currently in the scene. Mainly used to delete **Particle Tracker**.

- **Clear All Handlers** removes all handlers that are currently in the scene. This stops particle tracking.

**Hint:**
- The current version only supports the particle system at the top of the object's slot.
- As an internal process, if you press the **Delete Particle Tracker and Clear all handler** button, all handlers existing in the scene will be deleted.
We are currently working on this as other handlers will also be deleted.

# Note
We are currently developing the following features  
・Behavior when reopening the file  
・Behavior when there are multiple particle systems  
・Delete any Tracker corresponding to a particle system  
・Delete only the intended handler when executing **Delete Particle Tracker and Clear all handler**  



# Author
* Kai0731200
* akanekaiii731@gmail.com
