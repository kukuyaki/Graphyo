import json
import networkx as nx
from collections import deque

# ------------------------------------------------------------------
# 注意：變數 'graph_input_json' 會由網頁 JS 從階段 1 的輸出中自動注入！
# ------------------------------------------------------------------

def run_bfs_and_record(input_json_str):
    # 1. 載入並解析階段 1 產生的圖形結構
    graph_data = json.loads(input_json_str)
    
    G = nx.Graph()
    # 根據階段 1 的結構在記憶體中重建圖形
    for node in graph_data["nodes"]:
        G.add_node(int(node["id"]))
    for edge in graph_data["edges"]:
        G.add_edge(int(edge["from"]), int(edge["to"]))

    print("\n--- [階段 2] 演算法步驟錄製 ---")
    print("已成功重建 NetworkX 圖形結構。準備執行 BFS 演算法。")

    # 2. 執行 BFS 演算法並錄製步驟
    start_node = 1
    queue = deque([start_node])
    visited = set()
    queued = {start_node}
    bfs_tree_edges = set()  # 用來記錄已經探索過且屬於 BFS 樹的邊
    
    steps = []

    def record_step(message, active_node=None, active_edge=None):
        """記錄當前狀態的快照"""
        node_states = {}
        for n in G.nodes():
            n_str = str(n)
            if n == active_node:
                node_states[n_str] = "active"
            elif n in queue:
                node_states[n_str] = "queued"
            elif n in visited:
                node_states[n_str] = "visited"
            else:
                node_states[n_str] = "unvisited"

        edge_states = {}
        for u, v in G.edges():
            edge_id = f"{min(u, v)}-{max(u, v)}"
            if active_edge and edge_id == f"{min(active_edge)}-{max(active_edge)}":
                edge_states[edge_id] = "active"
            elif edge_id in bfs_tree_edges:
                edge_states[edge_id] = "tree"
            else:
                edge_states[edge_id] = "normal"

        steps.append({
            "step_index": len(steps),
            "message": message,
            "queue": [str(x) for x in queue],
            "visited": [str(x) for x in visited],
            "node_states": node_states,
            "edge_states": edge_states
        })

    # 【步驟 0】：初始狀態
    record_step(f"BFS 演算法初始化。將起點 [{start_node}] 加入排隊佇列中。")

    while queue:
        current = queue.popleft()
        queued.discard(current)
        visited.add(current)
        
        # 【步驟 1】：取出當前節點
        record_step(f"從佇列取出節點 [{current}]，標記為「處理中」。準備探索其鄰居節點。", active_node=current)

        # 為了確保每次遍歷順序一致，鄰居由小到大排序
        neighbors = sorted(list(G.neighbors(current)))
        
        for neighbor in neighbors:
            edge_id = f"{min(current, neighbor)}-{max(current, neighbor)}"
            
            if neighbor not in visited and neighbor not in queued:
                # 【步驟 2】：發現新鄰居，進行邊的探索與節點入隊
                record_step(
                    f"探索邊 {current}-{neighbor}。發現未造訪鄰居 [{neighbor}]！",
                    active_node=current,
                    active_edge=(current, neighbor)
                )
                
                queue.append(neighbor)
                queued.add(neighbor)
                bfs_tree_edges.add(edge_id)
                
                record_step(
                    f"已將鄰居 [{neighbor}] 加入排隊佇列，並將連線納入 BFS 搜尋樹中。",
                    active_node=current
                )
            else:
                # 【步驟 3】：遇到已經排隊或造訪過的節點
                record_step(
                    f"探索邊 {current}-{neighbor}。鄰居 [{neighbor}] 先前已被造訪過或已在佇列中，跳過此邊。",
                    active_node=current,
                    active_edge=(current, neighbor)
                )

        # 【步驟 4】：當前節點探索完畢
        record_step(f"節點 [{current}] 的所有鄰居探索完畢。將 [{current}] 標記為「已造訪（結案）」。")

    # 【步驟 5】：演算法完成
    record_step("🎉 BFS 演算法執行完畢！所有與起點相通的節點皆已探索完成。")

    # 輸出步驟 JSON 給前端 JS 渲染
    return json.dumps(steps)

# 執行演算法並傳入注入的全域變數
run_bfs_and_record(graph_input_json)
