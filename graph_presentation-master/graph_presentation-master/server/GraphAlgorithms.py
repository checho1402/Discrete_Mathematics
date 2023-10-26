from graph.Graph import Graph
from server.Services import Services
from algorithms.floyd_warshall import *
from algorithms.dijkstra import *
from algorithms.knnb import *
from algorithms.rr import *
from algorithms.eg import *
from algorithms.quinca import *
from algorithms.abm import *
from algorithms.forest import *
from time import time


class GraphAlgorithms(Services):
    def __init__(self):
        Services.__init__(self)

    def run_algorithm_floyd_warshall(self, values):
        graph = Graph.import_values(values)
        t = time()
        dist = Floyd_Warshall(graph)
        time_seconds = time() - t

        return self.export_algorithm(dist, time_seconds)

    def run_algorithm_dijkstra(self, values, source):
        graph = Graph.import_values(values)
        t = time()
        dist = Dijkstra(int(source), graph)
        time_seconds = time() - t

        return self.export_algorithm([dist], time_seconds)

    def run_algorithm_dijkstra_apsp(self, values):
        graph = Graph.import_values(values)
        t = time()
        dist = Dijkstra_apsp(graph)
        time_seconds = time() - t

        return self.export_algorithm(np.array(dist), time_seconds)

    def run_algorithm_rr_bfs_truncated(self, values, dist):
        graph = Graph.import_values(values)
        matrix_distances = self.import_matrix(dist)

        t = time()
        dist = Bfs_Truncated_With_Sources(graph, np.array(matrix_distances))
        time_seconds = time() - t

        return self.export_algorithm(dist, time_seconds)

    def run_algorithm_knnb_node_incremental(self, values, dist):
        graph = Graph.import_values(values)
        matrix_distances = self.import_matrix(dist)

        t = time()
        dist = KNNB_Node_Incremental(graph, np.array(matrix_distances))
        time_seconds = time() - t

        return self.export_algorithm(dist, time_seconds)

    def run_algorithm_eg(self, values, dist):
        graph = Graph.import_values(values)
        matrix_distances = self.import_matrix(dist)

        t = time()
        dist = Even_Gazit(graph, np.array(matrix_distances))
        time_seconds = time() - t

        return self.export_algorithm(dist, time_seconds)

    def run_algorithm_quinca(self, values, dist):
        graph = Graph.import_values(values)
        matrix_distances = self.import_matrix(dist)

        t = time()
        dist = Quinca(graph, np.array(matrix_distances))
        time_seconds = time() - t
        print("TIME QUINCA: ", time_seconds * 1000)

        return self.export_algorithm(dist, time_seconds)

    def run_algorithm_abm(self, values, dist):
        graph = Graph.import_values(values)
        matrix_distances = self.import_matrix(dist)

        t = time()
        dist = ABM_Update(graph, np.array(matrix_distances))
        time_seconds = time() - t
        print("TIME ABM: ", time_seconds * 1000)

        return self.export_algorithm(dist, time_seconds)

    def run_algorithm_forest(self, values, dist):
        graph = Graph.import_values(values)
        matrix_distances = self.import_matrix(dist)

        t = time()
        dist = Forest_apsp(graph, np.array(matrix_distances))
        time_seconds = time() - t

        return self.export_algorithm(dist, time_seconds)
