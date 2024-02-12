'''
Name: <Gloria Castorena>
Student ID: 1221643982
Course: IFT 101
Priblem Set: PS4
Problem: P3
Date:<02-02-2024>
'''

# List: Device IP addresses
print("List of IP Addresses:")
device_ip = ['192.168.1.1', '192.168.1.2', '192.168.1.3', '192.168.1.4', '192.168.1.5', '192.168.1.6', '192.168.1.7', '192.168.1.8' ]
for ip in device_ip:
    print(ip)
print()
# Tuple: Device MAC addresses
print("Tuple od MAC Addresses:")
device_mac = (
    '00:14:22:01:23:45', '00:14:22:01:23:46', '00:14:22:01:23:47',
    '00:14:22:01:23:48', '00:14:22:01:23:49', '00:14:22:01:23:50', '00:14:22:01:23:51', '00:14:22:01:23:52'
)
for mac in device_mac:
    print(mac)
print()
# Set: Device types
print("Set of Device Types:")
device_type = {'printer', 'mobile device', 'switch', 'router', 'server', 'workstation'}
for dev_type in device_type:
    print(dev_type)
print()
# List and Dictionary: Device types and Network Inventory
print("Network Inventory:")
device_types = ['router', 'switch', 'server', 'workstation', 'printer', 'mobile device']

network_inventory = {}
for ip in device_ip:
    if ip == '192.168.1.1':
        network_inventory.update({ip: device_types[0]})
    elif ip == '192.168.1.2':
        network_inventory.update({ip: device_types[1]})
    elif ip == '192.168.1.3':
        network_inventory.update({ip: device_types[1]})
    elif ip == '192.168.1.4' or ip == '192.168.1.5':
        network_inventory.update({ip: device_types[2]})
    elif ip == '192.168.1.6':
        network_inventory.update({ip: device_types[3]})
    elif ip == '192.168.1.7':
        network_inventory.update({ip: device_types[4]})
    elif ip == '192.168.1.8':
        network_inventory.update({ip: device_types[5]})
i = 0
for x, y in network_inventory.items():
    print("IP: "+x+", MAC: " +device_mac[i] + " Type: " + y)
    i+=1
# Ensure that the router type is assigned to the device with IP '192.168.1.1'




