# Particle Tracker for Blender version 1.1.0 released !

Particle Tracker is a free add-on for Blender that allows you to track each particle by creating points from particles in a particle system in your scene. Fully compatible with Blender 4.1 and above, supports particle position tracking and animation.

version 1.1.0 was created in 2024.06.07.

The main improvements are
- Significantly improved usability with key frame method
・Support for multiple particle systems
・Improved robustness, such as no problems occurring even if the file is reopened
is.

# DEMO
Create and track points at the particle position  
![スクリーンショット 2024-05-11 012537](https://github.com/Kai0731200/Particle-Tracker/assets/74250530/71382067-9e55-4d9a-80c8-a1b3add19413)

DEMO VIDEO  
![Particle Tracker demo short](https://github.com/Kai0731200/Particle-Tracker/assets/74250530/1172dd16-5c82-4935-a218-49ac88dec5ae)  
Full version → https://youtu.be/1Alczc3hjzY  



UI  
![image](https://github.com/Kai0731200/Particle-Tracker/assets/74250530/109bae0d-84c1-4a99-9ba5-030911e1a848)


# Features

By using Particle Tracker, you can access particle information in particle systems that cannot be accessed directly with the current blender (4.1).
This add-on doesn't just create points at the particle's location; it also registers keyframes and tracks the particle's position and moves the point each frame.
Additionally, since points are created, particle positions can be accessed from geometry nodes, allowing for various applications that are synchronized with particle systems.

This addon creates points and registers keyframes.
It can also stabilize the initial position of points.
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
- **Select Particle System to Track** menu.
A list of particle systems owned by the selected object (active object) will be obtained, so select the particle system you want to track from the pull-down menu..

- **Create Particle Tracker** button will create one object **Particle Tracker** .
The name of the object will be **"Particle System name" _Tracker**. Hereafter it is called **Particle Tracker**.
- The created **Particle Tracker** is an object consisting of (multiple) points, whose number and position correspond to the particles of the particle system.
-Register the position with a key frame at every frame from the particle generation time to the end time set for the particle system in the particle property.
- As you move the frame, the **Particle Tracker** moves to the position registered with keyframe (same position as each particle) and tracks the particles.


**Hint:**
If the particle system name is in Japanese, it will be garbled in the sidebar UI, so please name the particle system in English.

# Explanatory article and Usage example
- Explanatory article  
  ・https://qiita.com/Kai0731200/items/598f356d54b409dca66e  
  ・https://qiita.com/Kai0731200/items/3893be5570275dc096a7  
- Usage example  
  https://www.youtube.com/watch?v=et39FMHpse0&t=5s  

# Author
* Kai0731200
* akanekaiii731@gmail.com
