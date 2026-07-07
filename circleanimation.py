from manim import *
import numpy as np

class ExampleRotation(Scene):
    def construct(self):
        nodes = [[ 0.29783812, -0.06193126, 0],
                [-0.4016472,   0.53686854, 0],
                [ 1.,         -0.11247366, 0],
                [ 0.26484691, -0.89120213, 0],
                [ 0.64864593,  0.28963108, 0],
                [-0.29803589,  0.57773418, 0],
                [-0.25969054,  0.47125744, 0],
                [-0.57637058, -0.37010745, 0],
                [-0.67558674, -0.43977673, 0]]
            
        g_nodes = []
        target_positions=[]
        for i in nodes:
            i = [j*config.frame_height/2 for j in i]
            start_pos = np.array([i[0],config.frame_height/2+5 , 0])
            i = np.array([i[0],i[1] , 0])
            target_positions.append(i)
            m1 = Circle(radius=0.1, color=BLUE).move_to(start_pos).set_fill(YELLOW, opacity=1.0).set_stroke(RED)
            g_nodes.append(m1)
            
        self.add(*g_nodes)
        drop_animations = []
        for node, target in zip(g_nodes, target_positions):
            drop_animations.append(node.animate().move_to(target))
            
        # 一口氣同時降落
        self.play(*drop_animations, run_time=1.2)
        self.wait()