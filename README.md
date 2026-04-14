# Mini SD-WAN Simulator

This project simulates a simplified Software-Defined WAN (SD-WAN) environment using Python. It models network nodes, link latency, dynamic routing, and automatic failover behavior.

## Features

- Dynamic path selection using Dijkstra-based routing
- Automatic failover when links fail
- Traffic type awareness (VoIP, video, data) with priority-based routing
- Load-aware routing using simulated link utilization
- Interactive Streamlit dashboard for topology, failover, and metrics
- Simple packet loss and latency reporting
- CLI interface for simulation control
- Modular network and controller architecture

## Architecture

```
sdwan-simulator/
│── main.py
│── dashboard/
│     └── app.py
│── visualization/
│     ├── __init__.py
│     └── graph.py
│── network/
│     ├── node.py
│     ├── link.py
│     ├── topology.py
│── controller/
│     ├── routing.py
│     ├── failover.py
│── utils/
│     ├── logger.py
│── README.md
```

## Getting Started

1. Open a terminal in the `sdwan-simulator` folder.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the simulator:

```bash
python main.py
```

### Interactive Dashboard

```bash
streamlit run dashboard/app.py
```

### Example CLI

```bash
python main.py --source A --destination E --traffic voice --fail B-C
```

## Sample Output

```
2026-04-14 12:00:00 INFO Starting SD-WAN simulation
2026-04-14 12:00:00 INFO Link A-B utilization: 72%
2026-04-14 12:00:00 INFO Link B-C utilization: 35%
2026-04-14 12:00:00 INFO Link A-C utilization: 45%
2026-04-14 12:00:00 INFO Link C-D utilization: 25%
2026-04-14 12:00:00 INFO Link B-D utilization: 80%
2026-04-14 12:00:00 INFO Link D-E utilization: 65%
2026-04-14 12:00:00 INFO Traffic sent via: A -> B -> D -> E | Type: VoIP (priority routing applied) | Cost: 7.50 | Packet loss: 4.23%
2026-04-14 12:00:00 INFO Link B-D failed. Triggering failover...
2026-04-14 12:00:00 INFO Rerouted traffic after failure:
2026-04-14 12:00:00 INFO Traffic sent via: A -> C -> D -> E | Type: VoIP (priority routing applied) | Cost: 5.41 | Packet loss: 2.12%
2026-04-14 12:00:00 INFO Simulation complete
```

## Resume-Worthy Highlights

- Implemented Dijkstra-based dynamic path selection
- Simulated real-time link failure and recovery
- Designed modular SD-WAN controller logic in Python
- Added traffic-type-aware routing and resilience metrics

## Future Enhancements

- Add load balancing across multiple paths
- Animate rerouting transitions on the dashboard
- Add richer QoS behavior and per-flow metrics
- Add unit tests and topology import/export
