"""
Knowledge Graph Service

Creates a graph from extracted entities.
"""

import networkx as nx


graph = nx.Graph()


def build_graph(entities):
    """
    Build graph using extracted entities.
    """

    graph.clear()

    for entity in entities:

        name = entity["Entity"]
        entity_type = entity["Type"]

        # Add entity node
        graph.add_node(
            name,
            entity_type=entity_type
        )

        # Connect entity to its type
        graph.add_node(entity_type)

        graph.add_edge(
            name,
            entity_type
        )

    print(f"Knowledge Graph Created")

    print(f"Nodes : {graph.number_of_nodes()}")
    print(f"Edges : {graph.number_of_edges()}")

    return graph


def get_graph():

    return graph