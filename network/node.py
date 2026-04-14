class Node:
    def __init__(self, name: str):
        self.name = name
        self.links = []

    def add_link(self, link):
        self.links.append(link)

    def active_neighbors(self):
        return [link for link in self.links if link.status]

    def __repr__(self):
        return f"Node({self.name})"
