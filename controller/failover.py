def fail_link(topology, node1: str, node2: str) -> dict:
    link = topology.fail_link(node1, node2)
    return {
        "failed_link": (node1, node2),
        "status": link.status,
        "message": f"Link between {node1} and {node2} FAILED",
    }


def recover_link(topology, node1: str, node2: str) -> dict:
    link = topology.recover_link(node1, node2)
    return {
        "recovered_link": (node1, node2),
        "status": link.status,
        "message": f"Link between {node1} and {node2} RECOVERED",
    }
