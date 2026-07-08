import json
import networkx as nx

# ------------------------------------------------------------------
# 注意：變數 'graph_input_json' 會由網頁 JS 從階段 1 的輸出中自動注入！
# ------------------------------------------------------------------

def run_dfs_and_record(input_json_str):
    # 1. 載入並解析階段 1 產生的圖形結構
    graph_data = json.loads(input_json_str)
    
    G = nx.Graph()
    # 根據階段 1 的結構在記憶體中重建圖形
    for node in graph_data["nodes"]:
        G.add_node(int(node["id"]))
    for edge in graph_data["edges"]:
        G.add_edge(int(edge["from"]), int(edge["to"]))

    print("\n--- [階段 2] 演算法步驟錄製 (DFS 深度優先) ---")
    print("已成功重建 NetworkX 圖形結構。準備執行 DFS 遞迴演算法。")

    # 2. 確保起點存在（優先選擇節點 1，若無則選擇編號最小的點）
    start_node = 1 if 1 in G.nodes() else sorted(list(G.nodes()))[0]
    
    visited = set()
    call_stack = []          # 模擬遞迴呼叫堆疊，對應前端播放器的佇列 (Queue) 顯示
    dfs_tree_edges = set()   # 記錄 DFS 搜尋樹中實際走過的邊
    steps = []

    def record_step(message, active_node=None, active_edge=None):
        """記錄當前 DFS 狀態的快照"""
        node_states = {}
        for n in G.nodes():
            n_str = str(n)
            if n == active_node:
                node_states[n_str] = "active"
            elif n in call_stack:
                # 在遞迴路徑中的點，我們標記為 "queued" (在前端會呈現黃色)
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
            elif edge_id in dfs_tree_edges:
                edge_states[edge_id] = "tree"
            else:
                edge_states[edge_id] = "normal"

        # 將呼叫堆疊 (call_stack) 的內容當作 queue 輸出給前端渲染
        steps.append({
            "step_index": len(steps),
            "message": message,
            "queue": [str(x) for x in call_stack],
            "visited": [str(x) for x in visited],
            "node_states": node_states,
            "edge_states": edge_states
        })

    # 3. 遞迴 DFS 主體演算法
    def dfs_visit(node, parent=None):
        # 進入節點，壓入呼叫堆疊
        call_stack.append(node)
        
        # 【步驟 1】：進入節點的瞬間
        edge_msg = f" 經由邊 {parent}-{node}" if parent else ""
        record_step(
            f"📥 遞迴進入節點 [{node}]{edge_msg}，將其壓入呼叫堆疊（Call Stack）。\n目前堆疊路徑: {' -> '.join(map(str, call_stack))}",
            active_node=node,
            active_edge=(parent, node) if parent else None
        )

        visited.add(node)
        
        # 【步驟 2】：標記為已造訪，準備探索鄰居
        record_step(
            f"將節點 [{node}] 標記為「已造訪（處理中）」。開始依序檢查其鄰居節點...",
            active_node=node
        )

        # 為了確保走訪順序固定且好觀察，鄰居由小到大排序
        neighbors = sorted(list(G.neighbors(node)))
        
        for neighbor in neighbors:
            edge_id = f"{min(node, neighbor)}-{max(node, neighbor)}"
            
            if neighbor not in visited:
                # 【步驟 3】：發現未造訪鄰居，準備深入探索
                record_step(
                    f"🔍 探索邊 {node}-{neighbor}。發現未造訪鄰居 [{neighbor}]，準備深入遞迴！",
                    active_node=node,
                    active_edge=(node, neighbor)
                )
                
                # 將此邊加入 DFS 搜尋樹中
                dfs_tree_edges.add(edge_id)
                
                # 遞迴深入
                dfs_visit(neighbor, node)
                
                # 【步驟 4】：從遞迴子程序返回
                record_step(
                    f"↩️ 從節點 [{neighbor}] 遞迴返回至 [{node}]。繼續檢查 [{node}] 的其餘鄰居。\n目前堆疊路徑: {' -> '.join(map(str, call_stack))}",
                    active_node=node
                )
            else:
                # 【步驟 5】：遇到已經造訪過的鄰居，跳過此邊
                # 若這條邊是剛剛進入時的父節點邊，就不用特別說明（或簡單跳過）
                if neighbor != parent:
                    record_step(
                        f"探索邊 {node}-{neighbor}。鄰居 [{neighbor}] 先前已被造訪過，跳過此邊（不進行遞迴）。",
                        active_node=node,
                        active_edge=(node, neighbor)
                    )

        # 【步驟 6】：離開節點，自呼叫堆疊彈出
        call_stack.pop()
        record_step(
            f"📤 節點 [{node}] 的所有鄰居已探索完畢。自呼叫堆疊（Call Stack）彈出，回溯回上一層。",
            active_node=node
        )

    # 【步驟 0】：演算法初始化
    record_step(f"DFS 深度優先搜尋演算法初始化。準備從起點 [{start_node}] 開始深入探索。")
    
    # 開始進行 DFS 走訪
    dfs_visit(start_node)

    # 【步驟 7】：演算法完成
    record_step("🎉 DFS 演算法執行完畢！所有與起點相連的路徑皆已深度探索完成。")

    # 輸出步驟 JSON 給前端播放器
    return json.dumps(steps)

# 執行 DFS 演算法並傳入注入的全域變數
run_dfs_and_record(graph_input_json)
