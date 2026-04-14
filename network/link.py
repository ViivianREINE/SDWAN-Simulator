class Link:
    def __init__(self, node1, node2, latency: float, utilization: float = 0.0, status: bool = True):
        self.node1 = node1
        self.node2 = node2
        self.latency = latency
        self.utilization = max(0.0, min(utilization, 1.0))
        self.status = status

    @property
    def endpoints(self):
        return (self.node1.name, self.node2.name)

    @property
    def utilization_percent(self):
        return int(self.utilization * 100)

    def other_end(self, node_name: str):
        return self.node2 if self.node1.name == node_name else self.node1

    def fail(self):
        self.status = False

    def recover(self):
        self.status = True

    def __repr__(self):
        state = "ACTIVE" if self.status else "FAILED"
        return (
            f"Link({self.node1.name}-{self.node2.name}, latency={self.latency}, "
            f"utilization={self.utilization_percent}%, {state})"
        )
