import matplotlib.pyplot as plt
import networkx as nx


def draw_network(topology, active_path=None, title="SD-WAN Network Topology"):
    G = nx.Graph()
    active_edges = set(zip(active_path, active_path[1:])) if active_path else set()

    for node_name in topology.nodes:
        G.add_node(node_name)

    edge_colors = []
    edge_labels = {}
    for link in topology.links:
        n1 = link.node1.name
        n2 = link.node2.name
        G.add_edge(n1, n2)
        edge_labels[(n1, n2)] = f"{link.latency}ms / {link.utilization_percent}%"

        if not link.status:
            edge_colors.append("red")
        elif (n1, n2) in active_edges or (n2, n1) in active_edges:
            edge_colors.append("green")
        else:
            edge_colors.append("gray")

    pos = nx.spring_layout(G, seed=42)
    fig, ax = plt.subplots(figsize=(8, 5))
    nx.draw_networkx_nodes(G, pos, ax=ax, node_size=1400, node_color="#89CFF0")
    nx.draw_networkx_labels(G, pos, ax=ax, font_weight="bold")
    nx.draw_networkx_edges(G, pos, ax=ax, edge_color=edge_colors, width=3)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color="black", ax=ax)
    ax.set_title(title)
    ax.axis("off")
    plt.tight_layout()
    return fig
