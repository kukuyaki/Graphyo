import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from manim import *
import numpy as np
from manim.utils.rate_functions import ease_out_bounce
from early_work.show_single_graph import pos_f

# uv run manim -pql nodefall.py

class ExampleRotation(Scene):
    def construct(self):
        # nodes = {'A': [ 0.2665238 , -0.10578828,0],
        #         'B': [-0.14934043,  0.81921045,0],
        #         'C': [ 1.        , -0.03582265,0],
        #         'D': [ 0.27444849, -0.90221614,0],
        #         'E': [ 0.0462308 , -0.68244947,0],
        #         'F': [0.07354898, 0.79703234,0],
        #         'G': [-0.07677974,  0.50718285,0],
        #         'H': [-0.65935248, -0.01766415,0],
        #         'I': [-0.7752794 , -0.37948494,0]}
        # edges = [['A', 'A', 3], 
        #         ['A', 'B', 3], 
        #         ['A', 'C', 3], 
        #         ['A', 'D', 3], 
        #         ['A', 'E', 3], 
        #         ['F', 'B', 3], 
        #         ['G', 'B', 3], 
        #         ['H', 'I', 10]]
        nodes,edges = pos_f()
        g_nodes = []
        target_positions=[]
        scale1 = int(0.9*config.frame_width/2)
        scale2 = int(0.9*config.frame_height/2)
        scale = int(0.9*config.frame_height/2)
        
        for d,i in zip(nodes.keys(),nodes.values()):
            ii = [i[0]*scale1, i[1]*scale2]
            start_pos = np.array([ii[0],scale+5 , 0])
            ii = np.array([ii[0],ii[1] , 0])
            target_positions.append(ii)
            m1 = Circle(radius=0.1, color=BLUE).move_to(start_pos).set_fill(YELLOW, opacity=1.0).set_stroke(RED)
            label_t = Text(d, color=BLACK).scale(0.3).move_to(start_pos)
            m1 = VGroup(m1,label_t)
            g_nodes.append(m1)

        self.add(*g_nodes)
        drop_animations = []
        for node, target in zip(g_nodes, target_positions):
            drop_animations.append(node.animate.move_to(target))
            
        line_ground = [i[:2].copy() for i in edges]
        #change "a" to [ 0.29783812, -0.06193126, 0]
        for i,j in enumerate(line_ground):
            line_ground[i][0] = nodes[line_ground[i][0]]
            line_ground[i][1] = nodes[line_ground[i][1]]
            
        line_animations = []
        label_t_group = []
        for num in range(len(line_ground)):
            dot1 = [line_ground[num][0][0]*scale1,line_ground[num][0][1]*scale2,0]
            dot2 = [line_ground[num][1][0]*scale1,line_ground[num][1][1]*scale2,0]
            line = Line(dot1,dot2).set_color(WHITE).set_z_index(-1)
            
            # --- 以下為新增的文字旋轉與偏移邏輯 ---
            # 1. 計算兩點中心點
            posx = (dot1[0] + dot2[0]) / 2
            posy = (dot1[1] + dot2[1]) / 2
            midpoint = np.array([posx, posy, 0])
            
            # 2. 計算線段方向與角度
            dx = dot2[0] - dot1[0]
            dy = dot2[1] - dot1[1]
            angle = np.arctan2(dy, dx)
            
            # 3. 計算垂直的法向量並單位化
            normal_vec = np.array([-dy, dx, 0])
            norm = np.linalg.norm(normal_vec)
            if norm > 0:
                normal_vec = normal_vec / norm
                
            # 4. 防止文字上下顛倒（當線段往左畫時修正角度與法向量）
            if dx < 0:
                angle += np.pi
                normal_vec = -normal_vec
                
            # 5. 計算最終偏移位置（0.25 是文字與線的視覺間距，可依喜好微調）
            offset_distance = 0.25
            text_pos = midpoint + normal_vec * offset_distance
            
            # 6. 建立文字、旋轉，並移動到法向量位置
            label_t = Text(str(edges[num][2]), color=WHITE).scale(0.3)
            label_t.rotate(angle)
            label_t.move_to(text_pos)
            # -------------------------------------
            
            label_t_group.append(FadeIn(label_t))
            line_animations.append(Create(line))
        
        # 一口氣同時降落
        self.play(*drop_animations, run_time=1.2, rate_func=ease_out_bounce)
        self.wait(0.1)
        self.play(*line_animations, run_time=4, rate_func=smooth)
        self.play(*label_t_group, run_time=4, rate_func=smooth)
        self.wait()