import random
from device import Device
from connection import Connection
import msvcrt #imported to clear out input buffering keystrokes: # Source - https://stackoverflow.com/a/38993222 # Posted by kollery, modified by community. See post 'Timeline' for change history # License - CC BY-SA 3.0

num_end_devices = 5
damages = 3

# Prints out every accessible device from each device. Also Prints out which devices and connections are damaged or undamaged
# Uses BFS to check every possible undamaged connection
def display_connections(topology_array):
    undamaged_connections = set()
    damaged_connections = set()
    for device in topology_array:
        print(f"Devices Accessible by {device}:")
        if device.get_is_damaged():
            print(f"Device: {device} is damaged")
            print()
            continue

        accessed_devices = set()
        accessed_devices.add(device)
        queue = [device] # queue used to iterate using BFS

        while queue: # runs while queue is not empty
            current_device = queue.pop(0) # current device represents BFS node
            for connection in current_device.get_connections():
                if connection.get_is_damaged():
                    damaged_connections.add(connection)
                    continue
                else:
                    undamaged_connections.add(connection)

                connected_device = connection.get_other_device(current_device)

                if connected_device not in accessed_devices: # Prevents infinite loops caused by repeatedly accessing the same two elements
                    if not connected_device.get_is_damaged():
                        queue.append(connected_device)
                        print(connected_device)
                accessed_devices.add(connected_device) # places any device accessed into the accessed_device set to prevent trying to access it again

        print()

    if len(undamaged_connections) != 0:
        print("Undamaged Connections:")
        for undamaged in undamaged_connections:
            print(undamaged)

        print()

    if len(damaged_connections) != 0:
        print("Damaged Connections:")
        for damaged in damaged_connections:
            print(damaged)

        print()

    unaccessed_connections = set() # ensures that if both devices surround a connection that those connections are still displayed
    for device in topology_array:
        for connection in device.get_connections():
            if connection not in undamaged_connections and connection not in damaged_connections:
                unaccessed_connections.add(connection)

    if len(unaccessed_connections) != 0:
        print("Unaccessible Connections:")
        for unaccessed in unaccessed_connections:
            print(unaccessed)

    while msvcrt.kbhit(): # clear input buffering: # Source - https://stackoverflow.com/a/38993222 # Posted by kollery, modified by community. See post 'Timeline' for change history # License - CC BY-SA 3.0
        msvcrt.getch()
    input("Press enter to continue: ")
    print()

def damage_random(topology_array, damages):
    damages_list = []
    for i in range(damages):
        while len(damages_list) < damages: # loops through and ensures that damages devices or connections are damaged
            damage_type = random.randint(0,1)
            access = random.randint(0, len(topology_array) - 1)
            if damage_type == 0:
                damage = topology_array[access]
                if damage not in damages_list:
                    damage.damage()
                    damages_list.append(damage)
            if damage_type == 1:
                damage = topology_array[access].get_connections()[random.randint(0, len(topology_array[access].get_connections()) - 1)]
                if damage not in damages_list:
                    damage.damage()
                    damages_list.append(damage)

"""
    --------------------
    Daisy Chain Topology
    --------------------
"""
daisy_chain = []
for i in range(num_end_devices):
    daisy_chain.append(Device(f"Computer_{i + 1}"))
    if i != 0:
        connection = Connection(daisy_chain[i - 1], daisy_chain[i])
        daisy_chain[i - 1].add_connection(connection)
        daisy_chain[i].add_connection(connection)

# Undamaged Topology Search:
print("--------------------------------\n"
      "Daisy-Chain Topology:"
      "\n--------------------------------")
display_connections(daisy_chain)

# Partially Damaged Topology Search:
print("--------------------------------\n"
      "Damaged Daisy-Chain Topology: Random"
      "\n--------------------------------")
damage_random(daisy_chain, damages)
display_connections(daisy_chain)

"""
    ------------
    Bus Topology
    ------------
"""
bus = []
for i in range(num_end_devices):
    bus.append(Device(f"Computer_{i + 1}"))
    bus.append(Device(f"Bus_Connection_{i + 1}"))
    connection = Connection(bus[i * 2], bus[i * 2 + 1])
    bus[i * 2].add_connection(connection)
    bus[i * 2 + 1].add_connection(connection)

    if i != 0:
        connection = Connection(bus[i * 2 - 1], bus[i * 2 + 1])
        bus[i * 2 - 1].add_connection(connection)
        bus[i * 2 + 1].add_connection(connection)


# Undamaged Topology Search:
print("--------------------------------\n"
      "Bus Topology:"
      "\n--------------------------------")
display_connections(bus)

# Partially Damaged Topology Search:
print("--------------------------------\n"
      "Damaged Bus Topology: Random"
      "\n--------------------------------")
damage_random(bus, damages)
display_connections(bus)

"""
    -------------
    Ring Topology
    -------------
"""
ring = []
for i in range(num_end_devices):
    ring.append(Device(f"Computer_{i + 1}"))
    if i != 0:
        connection = Connection(ring[i - 1], ring[i])
        ring[i - 1].add_connection(connection)
ring[-1].add_connection(Connection(ring[0], ring[-1])) # Completes Ring

# Undamaged Topology Search:
print("--------------------------------\n"
      "Ring Topology:"
      "\n--------------------------------")
display_connections(ring)

# Partially Damaged Topology Search:
print("--------------------------------\n"
      "Damaged Ring Topology: Random"
      "\n--------------------------------")
damage_random(ring, damages)
display_connections(ring)

"""
    -------------
    Star Topology
    -------------
"""
star = [Device("Switch")]
for i in range(num_end_devices):
    star.append(Device(f"Computer_{i + 1}"))
    # Add connection between switch and computer
    connection = Connection(star[0], star[i + 1])
    star[0].add_connection(connection)
    star[i + 1].add_connection(connection)

# Undamaged Topology Search:
print("--------------------------------\n"
      "Star Topology:"
      "\n--------------------------------")
display_connections(star)

# Partially Damaged Topology Search:
print("--------------------------------\n"
      "Damaged Star Topology: Switch"
      "\n--------------------------------")
star[0].damage()
display_connections(star)
star[0].fix()

print("--------------------------------\n"
      "Damaged Star Topology: Random"
      "\n--------------------------------")
damage_random(star, damages)
display_connections(star)

"""
    -------------
    Mesh Topology
    -------------
"""
mesh = []
for i in range(num_end_devices):
    mesh.append(Device(f"Computer_{i + 1}"))
    if i != 0:
        for j in range(i):
            connection = Connection(mesh[j], mesh[i])
            mesh[j].add_connection(connection)
            mesh[i].add_connection(connection)


# Undamaged Topology Search:
print("--------------------------------\n"
      "Mesh Topology:"
      "\n--------------------------------")
display_connections(mesh)

# Partially Damaged Topology Search:
print("--------------------------------\n"
      "Damaged Mesh Topology: Random"
      "\n--------------------------------")
damage_random(mesh, damages)
display_connections(mesh)
