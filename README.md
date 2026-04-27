# Network-Topology-Exploration
CSC 2770 Honors Project on Network Topologies

## Author:

- Simon Glashauser - [Github](https://github.com/sglasha)

## Topologies:

- Point-To-Point: Two devices connected to eachother.
- Daisy-Chain: A Chain of Point-To-Point Topologies.
- bus: Similar to Daisy-Chain, but slightly more fault tolerant because it doesn't require each end device to function properly.
- Ring: A Daisy-Chain Topology that is connected to form a ring. For the sake of this project it will be a directional relation instead of bidirectional.
- Star: Each end device is connected to a center device. Typically a Switch.
- Mesh: Each device is connected to every other device.

## What the Program Does:

The program procederally generates a graph of x end devices, where x is changeable at the `num_end_devices` variable. It then uses Breadth First Search (BFS) to analyze the generated graph and shows what devices can reach other devices, which devices are damaged, and each connection, sorted by if it is damaged or not. It then damages a number of random devices 

## How to Run the Program:

The Project can be fully ran from [main.py](./Code/main.py). You can change the `num_end_devices` variable on line 6 to simulate larger or smaller networks, but it may be hard to see the results when analyzing a network that is to large since it will print out every connection and device accessable by every device. The `damages` variable on line 7 can also be changed to alter how many devices or connections are simulated as damaged.
