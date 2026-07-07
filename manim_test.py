from manim import *

class GenerateGraphImage(Scene):
    def construct(self):
        # 1. 你的原始輸入資料：[起點, 終點, 權重]
        input_data = [
            ["A", "B", 3],
            ["C", "B", 5],
            ["B", "D", 2],
            ["A", "C", 1],
            ["D", "A", 7]
        ]
        
        # 2. 解析資料，分離出「節點清單」與「邊清單」
        vertices = list(set([item[0] for item in input_data] + [item[1] for item in input_data]))
        edges = [(item[0], item[1]) for item in input_data]
     
        # 3. 建立節點內部的純文字標籤（完全不使用 LaTeX）
        vertex_labels = {v: Text(v, color=WHITE).scale(0.6) for v in vertices}

        # 4. 在 Manim 建立有向圖物件
        graph = DiGraph(
            vertices,
            edges,
            layout="spring",          # 彈簧力導向佈局，自動散開節點
            layout_scale=3.0,         # 放大圖形範圍，避免擠在一起
            labels=vertex_labels,     # 帶入我們自己建立的純文字標籤
            edge_config={
                "stroke_width": 4,    # 線條粗細
                "color": WHITE,       # 線條顏色
                "tip_length": 0.25     # 🔥 新版 Manim 修正：直接控制箭頭的絕對長度
            },
            vertex_config={
                "radius": 0.4,        # 圓圈大小
                "color": BLUE,        # 圓圈顏色
                "fill_opacity": 0.8   # 圓圈不透明度
            },
        )
        
        # 5. 直接將圖形繪製在畫面上
        self.add(graph)