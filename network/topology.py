import random

from .node import Node
from .link import Link

class NetworkTopology:
    def __init__(self):
        self.nodes = {}
        self.links = []

    def add_node(self, name: str):
        if name not in self.nodes:
            self.nodes[name] = Node(name)

    def connect(self, n1: str, n2: str, latency: float, utilization: float = None):
        if n1 not in self.nodes or n2 not in self.nodes:
            raise ValueError("Both nodes must exist before connecting them.")

        if utilization is None:
            utilization = random.uniform(0.25, 0.85)

        link = Link(self.nodes[n1], self.nodes[n2], latency, utilization=utilization)
        self.links.append(link)
        self.nodes[n1].add_link(link)
        self.nodes[n2].add_link(link)
        return link

    def find_link(self, n1: str, n2: str):
        for link in self.links:
            endpoints = {link.node1.name, link.node2.name}
            if {n1, n2} == endpoints:
                return link
        return None

    def fail_link(self, n1: str, n2: str):
        link = self.find_link(n1, n2)
        if link:
            link.fail()
            return link
        raise ValueError(f"Link {n1}-{n2} not found.")

    def recover_link(self, n1: str, n2: str):
        link = self.find_link(n1, n2)
        if link:
            link.recover()
            return link
        raise ValueError(f"Link {n1}-{n2} not found.")

    def active_links(self):
        return [link for link in self.links if link.status]

    def __repr__(self):
        nodes = ", ".join(self.nodes)
        links = ", ".join(str(link) for link in self.links)
        return f"Topology(nodes=[{nodes}], links=[{links}])"
