import ipaddress

def count_ip_addresses(file_path):
    total_count = 0

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            try:
                network = ipaddress.ip_network(line, strict=False)
                total_count += network.num_addresses
            except ValueError:
                print(f"Invalid CIDR format: {line}")

    return total_count
