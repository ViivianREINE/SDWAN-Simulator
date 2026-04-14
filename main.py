import argparse
import random

from network.topology import NetworkTopology
from controller.routing import send_traffic
from controller.failover import fail_link, recover_link
from utils.logger import configure_logger
from visualization.graph import draw_network


logger = configure_logger()


def build_sample_topology() -> NetworkTopology:
    topology = NetworkTopology()
    for node_name in ["A", "B", "C", "D", "E"]:
        topology.add_node(node_name)

    topology.connect("A", "B", 1, utilization=0.72)
    topology.connect("B", "C", 2, utilization=0.35)
    topology.connect("A", "C", 4, utilization=0.45)
    topology.connect("C", "D", 1, utilization=0.25)
    topology.connect("B", "D", 3, utilization=0.80)
    topology.connect("D", "E", 2, utilization=0.65)
    return topology


def simulate_packet_delivery(result):
    if not result["delivered"]:
        logger.warning("No available path from %s to %s", result["source"], result["destination"])
        return

    packet_loss = random.uniform(0.0, 0.1)
    latency_report = result["cost"] + random.uniform(0.0, 1.0)
    logger.info(
        "Traffic sent via: %s | Type: %s | Cost: %.2f | Packet loss: %.2f%%",
        " -> ".join(result["path"]),
        result["traffic_description"],
        latency_report,
        packet_loss * 100,
    )


def display_link_utilization(topology: NetworkTopology):
    for link in topology.links:
        logger.info(
            "Link %s-%s utilization: %d%%",
            link.node1.name,
            link.node2.name,
            link.utilization_percent,
        )


def run_simulation(source: str, destination: str, traffic_type: str, fail: str = None, recover: str = None, show_graph: bool = False):
    topology = build_sample_topology()
    logger.info("Starting SD-WAN simulation")
    display_link_utilization(topology)

    baseline = send_traffic(topology, source, destination, traffic_type)
    simulate_packet_delivery(baseline)
    if show_graph and baseline["delivered"]:
        fig = draw_network(topology, baseline["path"], title="Baseline Route")
        fig.show()

    if fail:
        node1, node2 = fail.split("-")
        logger.info("Link %s-%s failed. Triggering failover...", node1, node2)
        fail_link(topology, node1, node2)
        rerouted = send_traffic(topology, source, destination, traffic_type)
        logger.info("Rerouted traffic after failure:")
        simulate_packet_delivery(rerouted)
        if show_graph and rerouted["delivered"]:
            fig = draw_network(topology, rerouted["path"], title="Rerouted Path")
            fig.show()

    if recover:
        node1, node2 = recover.split("-")
        recover_data = recover_link(topology, node1, node2)
        logger.info(recover_data["message"])
        recovered = send_traffic(topology, source, destination, traffic_type)
        simulate_packet_delivery(recovered)
        if show_graph and recovered["delivered"]:
            fig = draw_network(topology, recovered["path"], title="Recovered Route")
            fig.show()

    logger.info("Simulation complete")


def parse_args():
    parser = argparse.ArgumentParser(description="Mini SD-WAN Simulator")
    parser.add_argument("--source", default="A", help="Source node")
    parser.add_argument("--destination", default="E", help="Destination node")
    parser.add_argument("--traffic", default="data", choices=["voice", "video", "data"], help="Traffic type")
    parser.add_argument("--fail", help="Fail a link, format NODE1-NODE2")
    parser.add_argument("--recover", help="Recover a failed link, format NODE1-NODE2")
    parser.add_argument("--show-graph", action="store_true", help="Show network graph views for baseline and rerouted paths")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    run_simulation(args.source, args.destination, args.traffic, args.fail, args.recover, args.show_graph)
