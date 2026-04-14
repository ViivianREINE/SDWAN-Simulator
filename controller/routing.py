import heapq
from typing import Dict, List, Tuple

TRAFFIC_PROFILES = {
    "voice": {
        "label": "VoIP (priority routing applied)",
        "latency_weight": 0.8,
        "utilization_weight": 0.2,
    },
    "video": {
        "label": "Video (bandwidth-aware routing)",
        "latency_weight": 1.0,
        "utilization_weight": 0.5,
    },
    "data": {
        "label": "Data (normal routing)",
        "latency_weight": 1.2,
        "utilization_weight": 0.8,
    },
}


def shortest_path(topology, start: str, end: str, traffic_type: str = "data") -> Tuple[List[str], float]:
    if start not in topology.nodes or end not in topology.nodes:
        raise ValueError("Start and end nodes must exist in the topology.")

    profile = TRAFFIC_PROFILES.get(traffic_type, TRAFFIC_PROFILES["data"])
    queue = [(0.0, start, [])]
    visited = set()

    while queue:
        cost, current, path = heapq.heappop(queue)
        if current in visited:
            continue

        path = path + [current]
        visited.add(current)

        if current == end:
            return path, cost

        for link in topology.nodes[current].links:
            if not link.status:
                continue

            neighbor = link.node2.name if link.node1.name == current else link.node1.name
            if neighbor in visited:
                continue

            effective_cost = (
                cost
                + link.latency * profile["latency_weight"]
                + link.utilization * profile["utilization_weight"] * 10
            )
            heapq.heappush(queue, (effective_cost, neighbor, path))

    return [], float("inf")


def send_traffic(topology, source: str, destination: str, traffic_type: str = "data") -> Dict[str, object]:
    profile = TRAFFIC_PROFILES.get(traffic_type, TRAFFIC_PROFILES["data"])
    path, cost = shortest_path(topology, source, destination, traffic_type)
    result = {
        "source": source,
        "destination": destination,
        "traffic_type": traffic_type,
        "traffic_description": profile["label"],
        "path": path,
        "cost": cost,
        "delivered": bool(path),
    }
    return result
