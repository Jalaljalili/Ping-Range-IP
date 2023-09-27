import csv
import threading
from ping3 import ping
from queue import Queue
from ipaddress import ip_network, ip_address


# Get IP range and subnet from user input
subnet = input("Enter IP range to scan (e.g. 172.16.96.0/24): ")

hosts = [str(x) for x in ip_network(subnet).hosts()]
hosts_live = []

q = Queue()
for host in hosts:
    q.put(host)


def ping_host(host):
    if ping(host, timeout=1):
        return host


def worker():
    while True:
        host = q.get()
        if host is None:
            break
        if ping_host(host):
            hosts_live.append(host)
        q.task_done()


for i in range(40):
    t = threading.Thread(target=worker)
    t.daemon = True
    t.start()

q.join()


# Write results to CSV file
with open("ping_results.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["IP Address", "Ping Result"])
    for host in hosts_live:
        if ping_host(host):
            writer.writerow([host, "Success"])
        else:
            writer.writerow([host, "Failed"])
            
print("Ping results written to ping_results.csv file.")
