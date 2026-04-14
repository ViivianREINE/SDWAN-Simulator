import random
import os
import sys

import matplotlib.pyplot as plt
import streamlit as st

# Add the parent directory to sys.path to allow imports from the root
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from main import build_sample_topology
from controller.routing import send_traffic
from controller.failover import fail_link
from visualization.graph import draw_network


def build_topology():
    return build_sample_topology()


def make_metric(result):
    packet_loss = random.uniform(0.0, 0.1) * 100
    latency = result["cost"] + random.uniform(0.0, 1.0)
    return {
        "latency": round(latency, 2),
        "packet_loss": round(packet_loss, 2),
        "cost": round(result["cost"], 2),
        "path": " -> ".join(result["path"]) if result["path"] else "no path",
    }


def display_result(result):
    if not result["path"]:
        st.write("**No available path.**")
        return
    st.write(f"**Source:** {result['source']}")
    st.write(f"**Destination:** {result['destination']}")
    st.write(f"**Traffic:** {result['traffic_description']}")
    st.write(f"**Path:** {' -> '.join(result['path'])}")
    st.write(f"**Path cost:** {result['cost']:.2f}")
    st.write(f"**Delivered:** {result['delivered']}")


def render_link_status(topology):
    lines = ["| Link | Latency (ms) | Utilization | Status |", "|---|---|---|---|"]
    for link in topology.links:
        lines.append(
            f"| {link.node1.name}-{link.node2.name} | {link.latency} | {link.utilization_percent}% | {'active' if link.status else 'failed'} |"
        )
    st.markdown("\n".join(lines))


def render_metrics_chart(history):
    if not history:
        st.info("Run traffic to populate the metrics dashboard.")
        return

    latency_series = [item["latency"] for item in history]
    packet_loss_series = [item["packet_loss"] for item in history]
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(latency_series, marker="o", label="Latency (ms)")
    ax.plot(packet_loss_series, marker="o", label="Packet loss (%)")
    ax.set_xlabel("Simulation step")
    ax.set_ylabel("Value")
    ax.set_title("Metrics history")
    ax.grid(True, linestyle="--", alpha=0.4)
    ax.legend()
    st.pyplot(fig)


def main():
    st.set_page_config(page_title="SD-WAN Dashboard", layout="wide")
    st.title("🌐 Mini SD-WAN Control Dashboard")
    st.markdown(
        "Visualize SD-WAN routing decisions, active paths, and failover behavior in a simulated network topology."
    )

    if "failed_links" not in st.session_state:
        st.session_state.failed_links = []
    if "last_result" not in st.session_state:
        st.session_state.last_result = None
    if "history" not in st.session_state:
        st.session_state.history = []
    if "last_reroute" not in st.session_state:
        st.session_state.last_reroute = None

    with st.sidebar:
        st.header("Controls")
        source = st.selectbox("Source", sorted(["A", "B", "C", "D", "E"]))
        destination = st.selectbox("Destination", sorted(["A", "B", "C", "D", "E"]))
        traffic_type = st.selectbox("Traffic Type", ["voice", "video", "data"])
        available_links = [f"{link.node1.name}-{link.node2.name}" for link in build_topology().links]
        selected_link = st.selectbox("Link to fail/recover", available_links)
        st.write("---")
        run_button = st.button("Send Traffic")
        fail_button = st.button("Fail Selected Link")
        recover_button = st.button("Recover Selected Link")
        reset_button = st.button("Reset Topology")

    topology = build_topology()
    for failed in st.session_state.failed_links:
        try:
            fail_link(topology, *failed.split("-"))
        except ValueError:
            pass

    if reset_button:
        st.session_state.failed_links = []
        st.session_state.last_result = None
        st.session_state.last_reroute = None
        st.session_state.history = []
        topology = build_topology()
        st.success("Topology reset to healthy state.")

    if run_button:
        result = send_traffic(topology, source, destination, traffic_type)
        st.session_state.last_result = result
        st.session_state.history.append(make_metric(result))
        if result["delivered"]:
            st.success("Traffic delivered successfully.")
        else:
            st.error("No available path for this traffic flow.")

    if fail_button:
        if selected_link not in st.session_state.failed_links:
            st.session_state.failed_links.append(selected_link)
            topology = build_topology()
            for failed in st.session_state.failed_links:
                fail_link(topology, *failed.split("-"))
            st.warning(f"Link {selected_link} failed. Triggering failover...")
            before = send_traffic(build_topology(), source, destination, traffic_type)
            after = send_traffic(topology, source, destination, traffic_type)
            st.info("Old path:")
            display_result(before)
            st.info("Rerouted path:")
            display_result(after)
            st.session_state.last_result = after
            st.session_state.last_reroute = after
            st.session_state.history.append(make_metric(after))
        else:
            st.info(f"Link {selected_link} is already failed.")

    if recover_button:
        if selected_link in st.session_state.failed_links:
            st.session_state.failed_links.remove(selected_link)
            topology = build_topology()
            for failed in st.session_state.failed_links:
                fail_link(topology, *failed.split("-"))
            st.success(f"Link {selected_link} recovered.")
            result = send_traffic(topology, source, destination, traffic_type)
            st.session_state.last_result = result
            st.session_state.history.append(make_metric(result))
        else:
            st.info(f"Link {selected_link} is not currently failed.")

    st.markdown("## Network Topology")
    active_path = (
        st.session_state.last_reroute["path"]
        if st.session_state.last_reroute
        else (st.session_state.last_result["path"] if st.session_state.last_result else None)
    )
    fig = draw_network(topology, active_path)
    st.pyplot(fig)

    st.markdown("## Traffic Summary")
    if st.session_state.last_result:
        display_result(st.session_state.last_result)
    else:
        st.info("Use the controls to send traffic or fail a link.")

    st.markdown("## Link Status")
    render_link_status(topology)

    st.markdown("## Metrics History")
    render_metrics_chart(st.session_state.history)


if __name__ == "__main__":
    main()
