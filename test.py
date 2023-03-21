from graph import create_graph
from greedy_edge_color import greedy_edge_coloring
from visualize import visualize_edge_coloring
from get_input import input_int, input_int_in_range
import networkx as nx

def test_greedy_edge_coloring():
    # Test case with a graph with no edges
    G = nx.Graph()
    assert greedy_edge_coloring(G) == ({}, 0)
    visualize_edge_coloring(G, {}, 0)

    # Test case with a graph with one edge
    G = nx.Graph([(1, 2)])
    assert greedy_edge_coloring(G) == ({(1, 2): 1}, 1)
    visualize_edge_coloring(G, {(1, 2): 1}, 1)

    # Test case with a graph with two edges
    G = nx.Graph([(1, 2), (2, 3)])
    assert greedy_edge_coloring(G) == ({(1, 2): 1, (2, 3): 2}, 2)
    visualize_edge_coloring(G, {(1, 2): 1, (2, 3): 2}, 2)

    # Test case with a graph with three edges
    G = nx.Graph([(1, 2), (2, 3), (3, 1)])
    assert greedy_edge_coloring(G) == ({(1, 2): 1, (1, 3): 2, (2, 3): 3}, 3)
    visualize_edge_coloring(G, {(1, 2): 1, (1, 3): 2, (2, 3): 3}, 3)

    # Test case with a graph with four edges
    G = nx.Graph([(1, 2), (2, 3), (3, 1), (1, 4)])
    assert greedy_edge_coloring(G) == ({(1, 2): 1, (1, 3): 2, (1, 4): 3, (2, 3): 3}, 3)
    visualize_edge_coloring(G, {(1, 2): 1, (1, 3): 2, (1, 4): 3, (2, 3): 3}, 3)

    # Test case with a graph with five edges
    G = nx.Graph([(1, 2), (2, 3), (3, 1), (1, 4), (4, 5)])
    assert greedy_edge_coloring(G) == ({(1, 2): 1, (1, 3): 2, (1, 4): 3, (2, 3): 3, (4, 5): 1}, 3)
    visualize_edge_coloring(G, {(1, 2): 1, (1, 3): 2, (1, 4): 3, (2, 3): 3, (4, 5): 1}, 3)

    # Test case with a graph with six edges
    G = nx.Graph([(1, 2), (2, 3), (3, 1), (1, 4), (4, 5), (5, 6)])
    assert greedy_edge_coloring(G) == ({(1, 2): 1, (1, 3): 2, (1, 4): 3, (2, 3): 3, (4, 5): 1, (5, 6): 2}, 3)
    visualize_edge_coloring(G, {(1, 2): 1, (1, 3): 2, (1, 4): 3, (2, 3): 3, (4, 5): 1, (5, 6): 2}, 3)


if __name__ == "__main__":
    test_greedy_edge_coloring()