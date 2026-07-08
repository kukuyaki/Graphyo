import json
import networkx as nx
from collections import deque
from random import sample,choice
def random_graph_generator(node_c=20, edge_c=19):
    nodes = [i+1 for i in range(node_c)]
    
    min_edges = node_c - 1
    max_edges = node_c * (node_c - 1) // 2
    
    if edge_c < min_edges:
        print(f"⚠️ [提示]: 連通 {node_c} 個節點至少需要 {min_edges} 條邊。已自動將 edge_c 修正為 {min_edges}。")
        edge_c = min_edges
    elif edge_c > max_edges:
        print(f"⚠️ [提示]: {node_c} 個節點的最大邊數為 {max_edges}。已自動將 edge_c 修正為 {max_edges}。")
        edge_c = max_edges

    edges = set()
    unvisited = set(nodes)
    visited = set()
    
    start_node = sample(nodes, 1)[0]
    visited.add(start_node)
    unvisited.remove(start_node)
    
    while unvisited:
        u = choice(list(visited))
        v = choice(list(unvisited))
        
        edge = (min(u, v), max(u, v))
        edges.add(edge)
        
        visited.add(v)
        unvisited.remove(v)

    all_possible_edges = []
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            candidate = (nodes[i], nodes[j])
            if candidate not in edges:
                all_possible_edges.append(candidate)
                
    remaining_edges_needed = edge_c - len(edges)
    
    if remaining_edges_needed > 0 and all_possible_edges:
        additional_edges = sample(all_possible_edges, remaining_edges_needed)
        edges.update(additional_edges)

    return nodes, list(edges)
def generate_graph_data(node_c=20, edge_c=19):
    # 建立指定的圖形結構
    G = nx.Graph()
    nodes,edges = random_graph_generator(node_c, edge_c)
    
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)

    print("--- [階段 1] 圖形初始化 ---")
    print(f"成功定義節點: {nodes}")
    print(f"成功定義連線: {edges}")

    # 計算靜態座標 (避免畫面亂飄)
    pos = nx.spring_layout(G, seed=42)
    
    graph_data = {
        "nodes": [
            {
                "id": str(n), 
                "label": f"Node {n}",
                "x": float(pos[n][0]) * 500,
                "y": float(pos[n][1]) * 500
            } for n in G.nodes()
        ],
        "edges": [
            {
                "id": f"{min(u, v)}-{max(u, v)}",  # 統一用小到大排序作為 Edge ID
                "from": str(u), 
                "to": str(v)
            } for u, v in G.edges()
        ]
    }
    
    # 導出 JSON 字串，以傳送給階段 2
    return json.dumps(graph_data)

generate_graph_data(30,30)
