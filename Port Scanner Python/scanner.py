import nmap
import ipaddress
import re
import eel
import os

port_range_pattern = re.compile("([0-9]+)-([0-9]+)")

port_min = 0
port_max = 65535

eel.init(f'{os.path.dirname(os.path.realpath(__file__))}/web')

@eel.expose
def scan_ports(ip_add_entered, port_range):
    try:
        ip_address_obj = ipaddress.ip_address(ip_add_entered)
        print("You entered a valid ip address.")
    except:
        print("You entered an invalid ip address")
        return "Error ! "

    port_range_valid = port_range_pattern.search(port_range.replace(" ",""))
    if port_range_valid:
        port_min = int(port_range_valid.group(1))
        port_max = int(port_range_valid.group(2))
    else:
        return "Error !"

    nm = nmap.PortScanner()
    results = []
    

    for port in range(port_min, port_max + 1):
        try:
            result = nm.scan(ip_add_entered, str(port))
            port_status = result['scan'][ip_add_entered]['tcp'][port]['state']
            results.append(f"Port {port} is {port_status}")
        except:
            results.append(f"Cannot scan port {port}.")

    return results

eel.start('index.html',  size=(1200,1000))