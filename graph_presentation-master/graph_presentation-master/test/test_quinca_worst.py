import os
import sys

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from graph.Graph import Graph
from algorithms.quinca import *
from algorithms.floyd_warshall import *

graph = Graph.creategraph(100, .8)
result_before_dist = np.array(Floyd_Warshall(graph))

graph.insert_worst_edge()

result_after_dist = np.array(Floyd_Warshall(graph))

def test_quinca_worst():
    dist_quinca = Quinca(graph, result_before_dist)
    np.testing.assert_array_equal(dist_quinca, result_after_dist)
