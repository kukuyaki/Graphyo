import networkx as nx
import matplotlib.pyplot as plt

# 創建一個無向圖
G = nx.Graph()  # DiGraph為有向圖, Graph為無向

# 加入名稱為1, 2, 3的三個節點（字串或數字節可當作節點名稱）
G.add_nodes_from([1, 2, 3])

# 加入節點1 節點2，以及節點2節點3的線
G.add_edges_from([(1, 2), (2, 3)])

# 繪製圖形
nx.draw(G, with_labels=True, font_weight='bold')
plt.show()