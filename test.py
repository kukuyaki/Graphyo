from random import sample
#this is a python file that generate 2 json file(graph.json and steps.json)
#run_bfs_and_export() will return and save 2 json file 

def random_graph_generator(node_c=20,edge_c=10):
    nodes = [i+1 for i in range(node_c)]
    edges = [tuple(sample(nodes,2)) for i in range(edge_c)]
    return nodes,edges

z = random_graph_generator()
print(z)

演算法步驟錄製失敗！Traceback (most recent call last):
  File "/lib/python312.zip/_pyodide/_base.py", line 597, in eval_code_async
    await CodeRunner(
          ^^^^^^^^^^^
  File "/lib/python312.zip/_pyodide/_base.py", line 285, in __init__
    self.ast = next(self._gen)
               ^^^^^^^^^^^^^^^
  File "/lib/python312.zip/_pyodide/_base.py", line 149, in _parse_and_compile_gen
    mod = compile(source, filename, mode, flags | ast.PyCF_ONLY_AST)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<exec>", line 19
    print("
          ^
SyntaxError: unterminated string literal (detected at line 19)