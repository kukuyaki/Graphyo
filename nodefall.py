from manim import *
import numpy as np
from manim.utils.rate_functions import ease_out_bounce
#uv run manim -pql circleanimation.py
class ExampleRotation(Scene):
    def construct(self):
        nodes = {"a":[ 0.29783812, -0.06193126, 0],
                "b":[-0.4016472,   0.53686854, 0],
                "c":[ 1.,         -0.11247366, 0],
                "d":[ 0.26484691, -0.89120213, 0],
                "e":[ 0.64864593,  0.28963108, 0],
                "f":[-0.29803589,  0.57773418, 0],
                "g":[-0.25969054,  0.47125744, 0],
                "h":[-0.57637058, -0.37010745, 0],
                "i":[-0.67558674, -0.43977673, 0]}
        edges = [["a","b",20],
                ["a","c",20],
                ["a","d",20],
                ["a","e",20],
                ["a","f",20],
                ["a","g",20],
                ["a","h",20],
                ["i","h",20]]
        g_nodes = []
        target_positions=[]
        scale = int(config.frame_height/2)
        
        for i in nodes.values():
            i = [j*scale for j in i]
            start_pos = np.array([i[0],scale+5 , 0])
            i = np.array([i[0],i[1] , 0])
            target_positions.append(i)
            m1 = Circle(radius=0.1, color=BLUE).move_to(start_pos).set_fill(YELLOW, opacity=1.0).set_stroke(RED)
            g_nodes.append(m1)
        
        line_ground = [i[:2].copy for i in edges]
        #change "a" to [ 0.29783812, -0.06193126, 0]
        for i,j in enumerate(line_ground):
            line_ground[i][0] = nodes[line_ground[i][0]]
            line_ground[i][1] = nodes[line_ground[i][1]]

        dot1 = line_ground[0][0]*scale 
        dot2 = line_ground[0][1]*scale 
        line = Line(dot1,dot2).set_color(WHITE)

        self.add(line)
        self.add(*g_nodes)
        drop_animations = []
        for node, target in zip(g_nodes, target_positions):
            drop_animations.append(node.animate.move_to(target))
            
        # 一口氣同時降落
        self.play(*drop_animations, run_time=1.2,rate_func=ease_out_bounce)
        self.wait()

