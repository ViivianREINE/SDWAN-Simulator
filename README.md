<div align="center">

# 🌐 𝐌𝐢𝐧𝐢 𝐒𝐃-𝐖𝐀𝐍 𝐒𝐢𝐦𝐮𝐥𝐚𝐭𝐨𝐫

### <em>Dynamic Routing • Traffic-Aware Path Selection • Automatic Failover</em>

<p>
  <strong>A lightweight Python simulation of SD-WAN routing intelligence in a dynamic network topology.</strong>
</p>

<br>

[![Python](https://img.shields.io/badge/Python-3.x-5A3E36?style=for-the-badge&logo=python&logoColor=FFF7F3)](https://www.python.org/)
[![NetworkX](https://img.shields.io/badge/NetworkX-Graph%20Routing-B76E79?style=for-the-badge)](https://networkx.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-C98F95?style=for-the-badge&logo=streamlit&logoColor=FFF7F3)](https://streamlit.io/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-C9A79A?style=for-the-badge)](https://matplotlib.org/)

<br>

🌸 **Route intelligently. Survive failures. Visualize everything.**

</div>

---

<div align="center">

> ♡ **Mini SD-WAN Simulator** models how a software-defined network can dynamically select paths,
> react to link failures, and reroute traffic according to traffic-specific routing preferences.

</div>

---

## 🎀 Table of Contents

- [About](#-about)
- [What This Project Simulates](#-what-this-project-simulates)
- [Core Features](#-core-features)
- [Architecture](#-architecture)
- [How Routing Works](#-how-routing-works)
- [Traffic Profiles](#-traffic-profiles)
- [Failover Mechanism](#-failover-mechanism)
- [Network Topology](#-network-topology)
- [Interactive Dashboard](#-interactive-dashboard)
- [CLI Usage](#-cli-usage)
- [Installation](#-installation)
- [Running the Simulator](#-running-the-simulator)
- [Project Structure](#-project-structure)
- [Example Simulation](#-example-simulation)
- [Visualization](#-visualization)
- [Technology Stack](#-technology-stack)
- [Design Highlights](#-design-highlights)
- [Limitations](#-limitations)
- [Future Scope](#-future-scope)
- [Author](#-author)
- [License](#-license)

---

## 🌷 About

**Mini SD-WAN Simulator** is a modular Python project that demonstrates the core ideas behind dynamic software-defined wide-area networking through simulation.

The system represents a network as a collection of:

- **Nodes**
- **Links**
- **Latency**
- **Utilization**
- **Link availability**
- **Traffic profiles**

A routing controller evaluates available paths between a source and destination and calculates a path cost based on both **link latency** and **link utilization**.

When a selected link fails, the simulator removes that link from active routing and calculates a new path automatically.

The project also includes an interactive **Streamlit dashboard** for exploring topology, traffic flows, failures, rerouting, link status, and simulated metrics.

---

## ✦ What This Project Simulates

The simulator focuses on four fundamental SD-WAN concepts:

```text
                    🌐 NETWORK TOPOLOGY
                           │
                           ▼
                  ┌──────────────────┐
                  │  Traffic Request │
                  └────────┬─────────┘
                           │
                           ▼
                  ┌──────────────────┐
                  │ Dynamic Routing  │
                  │                  │
                  │ Latency + Load   │
                  └────────┬─────────┘
                           │
                           ▼
                  ┌──────────────────┐
                  │ Selected Path    │
                  └────────┬─────────┘
                           │
                 ┌─────────┴─────────┐
                 │                   │
                 ▼                   ▼
           Link Healthy          Link Failure
                 │                   │
                 ▼                   ▼
           Deliver Traffic      Trigger Failover
                                     │
                                     ▼
                              Recalculate Path
                                     │
                                     ▼
                               Reroute Traffic
````

---

## 💗 Core Features

<table>
<tr>
<td width="50%">

### 🧭 Dynamic Routing

Uses a Dijkstra-style shortest-path search with a custom cost function rather than simply selecting the path with the fewest hops.

</td>

<td width="50%">

### ⚡ Automatic Failover

When a link is marked as failed, the routing system ignores it and searches for an alternative active path.

</td>
</tr>

<tr>
<td>

### 🎧 Traffic Awareness

Different traffic classes use different weighting factors for latency and utilization.

</td>

<td>

### 📊 Load-Aware Routing

Link utilization contributes to routing cost, allowing congested paths to become less attractive.

</td>
</tr>

<tr>
<td>

### 🖥️ Interactive Dashboard

Streamlit provides controls for source, destination, traffic type, link failures, recovery, topology reset, and metrics.

</td>

<td>

### 📈 Network Visualization

NetworkX and Matplotlib visualize nodes, active paths, failed links, latency, and utilization.

</td>
</tr>

<tr>
<td>

### 💌 CLI Interface

Run simulations directly from a terminal with configurable source, destination, traffic type, failure, recovery, and graph display options.

</td>

<td>

### 🧩 Modular Architecture

Network, controller, visualization, dashboard, and utility logic are separated into dedicated modules.

</td>
</tr>
</table>

---

## 🪞 Architecture

```text
                         ┌──────────────────────┐
                         │       main.py        │
                         │   Simulation Entry   │
                         └──────────┬───────────┘
                                    │
                ┌───────────────────┼───────────────────┐
                │                   │                   │
                ▼                   ▼                   ▼
      ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
      │     network/    │  │   controller/   │  │ visualization/  │
      │                 │  │                 │  │                 │
      │ node.py         │  │ routing.py      │  │ graph.py        │
      │ link.py         │  │ failover.py     │  │                 │
      │ topology.py     │  │                 │  │                 │
      └────────┬────────┘  └────────┬────────┘  └────────┬────────┘
               │                    │                    │
               └────────────────────┼────────────────────┘
                                    │
                                    ▼
                          ┌─────────────────────┐
                          │ Simulation Results  │
                          │                     │
                          │ Path                 │
                          │ Cost                 │
                          │ Delivery             │
                          │ Latency              │
                          │ Packet Loss          │
                          └──────────┬──────────┘
                                     │
                                     ▼
                          ┌─────────────────────┐
                          │ dashboard/app.py    │
                          │     Streamlit UI    │
                          └─────────────────────┘
```

---

## 🧠 How Routing Works

Routing is implemented in:

```text
controller/routing.py
```

The routing engine uses a priority queue and a Dijkstra-style traversal.

Instead of considering latency alone, each active link contributes:

```text
Effective Link Cost
=
Latency × Latency Weight
+
Utilization × Utilization Weight × 10
```

Therefore, the selected route depends on the **traffic profile**.

### Conceptual calculation

```text
             ┌──────────── Latency
             │
             │       ┌──── Traffic-specific weight
             ▼       ▼
       latency × latency_weight

                       +

             ┌──────────── Utilization
             │
             │       ┌──── Traffic-specific weight
             ▼       ▼
       utilization × utilization_weight × 10

                       ↓

                 Effective Cost
                       ↓
                Route Selection
```

This makes the simulation more expressive than a basic shortest-hop algorithm.

---

## 🎧 Traffic Profiles

The routing controller defines three traffic classes.

| Traffic Type | Description                     | Latency Weight | Utilization Weight |
| ------------ | ------------------------------- | -------------: | -----------------: |
| `voice`      | VoIP / priority routing         |          `0.8` |              `0.2` |
| `video`      | Video / bandwidth-aware routing |          `1.0` |              `0.5` |
| `data`       | Normal data routing             |          `1.2` |              `0.8` |

### Voice

```text
VoIP
↓
Lower latency weighting
↓
Latency-sensitive path selection
```

### Video

```text
Video
↓
Balanced latency + utilization sensitivity
↓
Bandwidth-aware path selection
```

### Data

```text
Data
↓
Higher latency + utilization weighting
↓
Normal routing behavior
```

These profiles influence how link costs are calculated.

---

## 🧯 Failover Mechanism

The simulator can dynamically fail and recover individual links.

Implemented in:

```text
controller/failover.py
network/topology.py
```

### Failure lifecycle

```text
             Link ACTIVE
                  │
                  ▼
           Failure Triggered
                  │
                  ▼
           Link.status = False
                  │
                  ▼
        Routing ignores failed link
                  │
                  ▼
          Alternative path search
                  │
                  ▼
          Traffic is rerouted
```

### Recovery lifecycle

```text
             Link FAILED
                  │
                  ▼
          Recovery Triggered
                  │
                  ▼
           Link.status = True
                  │
                  ▼
        Link becomes routable
                  │
                  ▼
          Route recalculated
```

This provides a simple demonstration of **network resilience and path recovery**.

---

## 🌐 Network Topology

The sample topology contains five nodes:

```text
A
B
C
D
E
```

with links:

| Link  | Latency | Utilization |
| ----- | ------: | ----------: |
| `A-B` |       1 |         72% |
| `B-C` |       2 |         35% |
| `A-C` |       4 |         45% |
| `C-D` |       1 |         25% |
| `B-D` |       3 |         80% |
| `D-E` |       2 |         65% |

The network is created inside:

```text
main.py
```

through:

```python
build_sample_topology()
```

---

## 🖥️ Interactive Dashboard

The project includes a **Streamlit dashboard** in:

```text
dashboard/app.py
```

Launch it with:

```bash
streamlit run dashboard/app.py
```

### Dashboard Controls

The interface provides controls for:

| Control               | Purpose                      |
| --------------------- | ---------------------------- |
| Source                | Choose source node           |
| Destination           | Choose destination node      |
| Traffic Type          | Select voice, video, or data |
| Link to fail/recover  | Select a network link        |
| Send Traffic          | Run a traffic simulation     |
| Fail Selected Link    | Simulate link failure        |
| Recover Selected Link | Restore a link               |
| Reset Topology        | Return to healthy topology   |

### Dashboard Views

The interface presents:

```text
🌐 Network Topology
        ↓
📦 Traffic Summary
        ↓
🔗 Link Status
        ↓
📈 Metrics History
```

The topology visualization highlights the current active path and visually distinguishes failed links.

---

## 📊 Simulated Metrics

Each traffic event generates simulated:

* Path cost
* Latency
* Packet loss

The simulator calculates latency using the selected route cost plus a small random component.

Packet loss is also simulated randomly for demonstration purposes.

The dashboard records these values over multiple simulation steps and plots their history.

> These metrics are simulated values intended for experimentation and visualization; they are not measurements from real network hardware.

---

## 💻 CLI Usage

The main entry point is:

```text
main.py
```

Basic execution:

```bash
python main.py
```

### Specify Source & Destination

```bash
python main.py --source A --destination E
```

### Select Traffic Type

```bash
python main.py --source A --destination E --traffic voice
```

Supported traffic types:

```text
voice
video
data
```

### Simulate Link Failure

```bash
python main.py --source A --destination E --traffic voice --fail B-D
```

### Simulate Recovery

```bash
python main.py --source A --destination E --traffic voice --fail B-D --recover B-D
```

### Display Network Graph

```bash
python main.py --source A --destination E --traffic voice --show-graph
```

### Full Example

```bash
python main.py \
  --source A \
  --destination E \
  --traffic voice \
  --fail B-D \
  --recover B-D \
  --show-graph
```

---

## 🤍 Installation

### 1. Clone the repository

```bash
git clone https://github.com/ViivianREINE/SDWAN-Simulator.git
cd SDWAN-Simulator
```

### 2. Create a virtual environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

Current dependencies are:

```text
streamlit
networkx
matplotlib
```

---

## 🚀 Running the Simulator

### Terminal Simulation

```bash
python main.py
```

### Interactive Dashboard

```bash
streamlit run dashboard/app.py
```

Once launched, Streamlit will provide a local browser interface for interacting with the simulated network.

---

## ✨ Example Simulation

A representative simulation flow is:

```text
🌐 Starting SD-WAN simulation

Link A-B utilization: 72%
Link B-C utilization: 35%
Link A-C utilization: 45%
Link C-D utilization: 25%
Link B-D utilization: 80%
Link D-E utilization: 65%

        ↓

Traffic request:
A → E

Traffic:
VoIP

        ↓

Selected route:
A → B → D → E

        ↓

Link B-D fails

        ↓

FAILOVER TRIGGERED

        ↓

New route:
A → C → D → E

        ↓

Traffic continues through
an alternative active path

        ↓

Simulation complete
```

The exact resulting metrics can vary because packet loss and part of the reported latency are simulated using random values.

---

## 🎨 Visualization

Network visualization is implemented in:

```text
visualization/graph.py
```

The graph is built using:

```text
NetworkX + Matplotlib
```

### Visual Semantics

```text
🟢 Active selected route
⚪ Available non-selected link
🔴 Failed link
🔵 Network node
```

Each link displays:

```text
Latency / Utilization
```

For example:

```text
2ms / 65%
```

The network layout uses a seeded spring layout so that the simulated topology remains visually consistent.

---

## 🧩 Project Structure

```text
SDWAN-Simulator/
│
├── 🌐 main.py
│   └── CLI entry point & simulation orchestration
│
├── 📂 network/
│   ├── __init__.py
│   ├── node.py
│   ├── link.py
│   └── topology.py
│
├── 🎛️ controller/
│   ├── __init__.py
│   ├── routing.py
│   └── failover.py
│
├── 🖥️ dashboard/
│   └── app.py
│
├── 📊 visualization/
│   ├── __init__.py
│   └── graph.py
│
├── 🛠️ utils/
│   ├── __init__.py
│   └── logger.py
│
├── 📦 requirements.txt
├── 📝 README.md
└── ⚙️ .gitignore
```

---

## 🏗️ Module Responsibilities

### `network/node.py`

Defines the `Node` object.

Responsibilities:

```text
• Store node name
• Store attached links
• Return active neighboring links
```

---

### `network/link.py`

Defines the `Link` object.

Each link stores:

```text
• Endpoint nodes
• Latency
• Utilization
• Availability status
```

It also supports:

```text
fail()
recover()
```

---

### `network/topology.py`

Manages the overall network.

Responsibilities include:

```text
• Add nodes
• Connect nodes
• Find links
• Fail links
• Recover links
• Return active links
```

---

### `controller/routing.py`

Contains the routing intelligence.

Responsibilities:

```text
• Traffic profiles
• Path calculation
• Cost computation
• Dynamic route selection
• Traffic delivery decisions
```

---

### `controller/failover.py`

Provides the controller-level failure and recovery operations.

```text
fail_link(...)
recover_link(...)
```

---

### `visualization/graph.py`

Converts the topology into a NetworkX graph and visualizes:

```text
• Nodes
• Links
• Active route
• Failed links
• Latency
• Utilization
```

---

### `dashboard/app.py`

Provides an interactive Streamlit interface over the simulation engine.

---

### `utils/logger.py`

Provides logging configuration for simulation output.

---

## 🌸 Design Highlights

<table>
<tr>
<td>

### 🧩 Modular

Network modeling, routing, failover, visualization, and dashboard logic are separated into independent modules.

</td>
<td>

### 🧠 Algorithmic

The routing engine implements a priority-queue-based Dijkstra-style traversal with custom weighted link costs.

</td>
</tr>

<tr>
<td>

### ⚡ Resilient

Failed links are excluded from path selection and traffic can be rerouted through remaining active links.

</td>
<td>

### 🎧 Traffic-Aware

Routing behavior changes according to whether traffic is classified as voice, video, or data.

</td>
</tr>

<tr>
<td>

### 📊 Observable

Link status, paths, latency, packet loss, and simulation history can be inspected through the dashboard.

</td>
<td>

### 🪶 Lightweight

The project uses a small Python dependency footprint and is designed for experimentation and learning.

</td>
</tr>
</table>

---

## 🌱 Limitations

This repository is intentionally a **simplified SD-WAN simulation**.

It does not currently implement:

```text
✦ Real WAN hardware integration
✦ Real packet forwarding
✦ Real routing protocols
✦ SD-WAN vendor controllers
✦ BGP / OSPF integration
✦ Real telemetry streams
✦ Encryption / tunnels
✦ Authentication or authorization
✦ Production-grade QoS enforcement
✦ Real packet-loss measurements
✦ Distributed controller deployment
```

Packet loss and part of the latency reporting are simulated using random values.

The project should therefore be viewed as an educational / experimental simulation of routing and failover behavior rather than a production networking platform.

---

## 🌺 Future Scope

Potential extensions include:

```text
✧ Multi-path load balancing
✧ Real-time traffic generation
✧ More detailed QoS policies
✧ Dynamic bandwidth modeling
✧ Additional routing algorithms
✧ Link health scoring
✧ Automated congestion detection
✧ Animated failover visualization
✧ Network topology import/export
✧ Unit and integration testing
✧ Historical simulation replay
✧ Real telemetry integration
✧ More detailed per-flow metrics
✧ Containerized deployment
```

---

## 🧪 Suggested Experiment Scenarios

The simulator can be used to explore scenarios such as:

### Scenario 01 — Healthy Network

```bash
python main.py --source A --destination E --traffic data
```

### Scenario 02 — Voice Traffic

```bash
python main.py --source A --destination E --traffic voice
```

### Scenario 03 — Video Traffic

```bash
python main.py --source A --destination E --traffic video
```

### Scenario 04 — Link Failure

```bash
python main.py --source A --destination E --traffic voice --fail B-D
```

### Scenario 05 — Failure + Recovery

```bash
python main.py \
  --source A \
  --destination E \
  --traffic voice \
  --fail B-D \
  --recover B-D
```

These scenarios make it possible to observe how traffic classes and topology changes affect route selection.

---

## 🛠️ Technology Stack

<div align="center">

| Technology               | Purpose                                        |
| ------------------------ | ---------------------------------------------- |
| 🐍 Python                | Core simulation logic                          |
| 🕸️ NetworkX             | Graph representation and network visualization |
| 📊 Matplotlib            | Network and metric visualization               |
| 🖥️ Streamlit            | Interactive dashboard                          |
| 🧭 Dijkstra-style Search | Dynamic route selection                        |
| 📝 Python Logging        | Simulation event reporting                     |
| ⚙️ argparse              | CLI configuration                              |

</div>

---

## 🌷 Project Philosophy

```text
             ┌─────────────────────────┐
             │    Observe the Network  │
             └────────────┬────────────┘
                          ↓
             ┌─────────────────────────┐
             │     Understand Traffic  │
             └────────────┬────────────┘
                          ↓
             ┌─────────────────────────┐
             │      Select a Path      │
             └────────────┬────────────┘
                          ↓
             ┌─────────────────────────┐
             │   Detect Link Failure   │
             └────────────┬────────────┘
                          ↓
             ┌─────────────────────────┐
             │      Reroute Traffic    │
             └────────────┬────────────┘
                          ↓
             ┌─────────────────────────┐
             │      Keep Flow Moving   │
             └─────────────────────────┘
```

The purpose of this project is to make dynamic routing and failover behavior easier to understand, experiment with, and visualize.

---

## 👩🏻‍💻 Author

<div align="center">

### **Priyam Parashar**

AI • Data Science • Software Engineering

<a href="https://github.com/ViivianREINE">
<img src="https://img.shields.io/badge/GitHub-ViivianREINE-5A3E36?style=for-the-badge&logo=github&logoColor=FFF7F3">
</a>

</div>

---

## 📜 License

This project is distributed according to the license information included in the repository.

Please review the repository's license before using, modifying, or redistributing the project.

---

<div align="center">

### 🌸 𝐌𝐢𝐧𝐢 𝐒𝐃-𝐖𝐀𝐍 𝐒𝐢𝐦𝐮𝐥𝐚𝐭𝐨𝐫

<em>Dynamic paths · intelligent routing · resilient networks</em>

♡ ───────────────────────────── ♡

</div>
```

