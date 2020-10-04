import sys
sys.path.append('/home/aziz/401/data-structures-and-algorithms-python')
import pytest
from data_structures_and_algorithms_python.data_structures.graph.graph import Graph, Node

def test_add_node():

    graph = Graph()

    assert graph.add_node('a').value == 'a'

def test_add_edge():

    graph = Graph()

    end = graph.add_node('banana')

    start = graph.add_node('apple')

    graph.add_edge(start, end)

    assert graph._adjacency_list[start][0] == (end, 1)
    assert graph.get_neighbors(start) == [(end, 1)]
    graph.add_edge(end, start)
    assert graph.get_neighbors(end) == [(start, 1)]

def test_get_nodes():

    g = Graph()

    a = g.add_node('a')
    b = g.add_node('b')
    c = g.add_node('c')

    assert len(g.get_nodes()) == 3

def test_get_neighbors():
    g = Graph()

    a = g.add_node('a')
    b = g.add_node('b')
    c = g.add_node('c')
    
    g.add_edge(a,b,4)
    neighbors = g.get_neighbors(a)
    assert neighbors[0][0].value == 'b'
    assert len(neighbors) == 1
    assert neighbors[0][1] == 4


def test_size():

    g = Graph()

    a = g.add_node('a')
    b = g.add_node('b')
    c = g.add_node('c')

    assert g.size() == 3

def test_get_nodes_no_nodes():
    g = Graph()
    assert len(g.get_nodes())== 0


def test_breadth_first_empty_graph():

    graph = Graph()

    amman = Node("Amman")
    with pytest.raises(ValueError):
        lst = graph.breadth_first(amman)


def test_breadth_first_one_element():

    graph = Graph()

    amman = graph.add_node('Amman')
    lst = graph.breadth_first(amman)
    assert lst == [amman]