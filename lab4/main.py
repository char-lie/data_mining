from graph_tool.all import *
from words import data as words
from bigrams import data as bigrams
from trigrams import data as trigrams
from math import log10


def get_vertex(g, name, word, vertices):
    # If we already have this vertex, just use it from cache
    if name in vertices:
        return vertices[name]
    # Otherwise we have to create new one
    a = g.add_vertex()
    word[a] = name
    # Add the vertex to cache
    vertices[name] = a
    return a


def build_graph(g, entries, containers, weight, word, color, vertices,
                treshold=.1, last_word=-1,
                entry_color='red', container_color='red'):
    def add_to_container(entry, container):
        a = get_vertex(g, entry, word, vertices)
        color[a] = entry_color
        b = get_vertex(g, container, word, vertices)
        color[b] = container_color
        e = g.add_edge(a, b)
        # Set weight for new edge (tf-idf)
        # Just empirical formula, which gives edges with 1 <= width < 30
        weight[e] = log10(containers[container])+4
    for entry in entries:
        if entries[entry] < treshold:
            continue
        for container in containers:
            if container.find(entry) < 0:
                continue
            add_to_container(entry, container)
    return


def init_graph():
    # Create directed graph
    g = Graph(directed=True)
    # Create 'weight' property for edge: will contain tf-idf
    weight = g.new_edge_property('float')
    # Create 'word' property for vertex: will contain string with current word
    word = g.new_vertex_property('string')
    color = g.new_vertex_property('string')
    return g, weight, word, color, {}


if __name__ == '__main__':
    g, weight, word, color, vertices = init_graph()
    # Dictionary with existent vertices (cache)
    build_graph(g, entries=words, containers=bigrams, color=color,
                weight=weight, word=word, vertices=vertices,
                entry_color='red', container_color='blue')
    build_graph(g, entries=bigrams, containers=trigrams, color=color,
                weight=weight, word=word, vertices=vertices,
                entry_color='blue', container_color='purple')
    # Draw the graph;
    # Weight is responsible for edges widths
    # Word contains labels for vertices
    graph_draw(g, vertex_font_size=12, edge_pen_width=weight, vertex_text=word,
               vertex_fill_color=color,
               output='words.png', output_size=(2000, 2000))
    # Alternative
    # graph_draw(g, edge_pen_width=weight, vertex_text=word, node_first=True,
    #            vertex_text_position=0, vertex_size=20, vertex_shape='double_square')
    # Or even
    # state=minimize_nested_blockmodel_dl(g)
    # draw_hierarchy(state, vertex_text=word, vertex_text_position=0)

