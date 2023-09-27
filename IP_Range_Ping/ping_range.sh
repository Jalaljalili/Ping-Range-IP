#!/bin/bash

# Get IP range from user input
echo "Enter IP range to scan (e.g. 172.16.96.1-254): "
read ip_range

# Extract first and last IP address from range
first_ip=$(echo $ip_range | cut -d'-' -f1)
last_ip=$(echo $ip_range | cut -d'-' -f2)

# Ping each IP address in the range and write results to CSV file
echo "IP Address,Status" > ping_results.csv
for ((i=$first_ip;i<=$last_ip;i++)); do
    {
        if ping -c 1 -w 1 $i >/dev/null; then
            echo "$i,Success" >> ping_results.csv
        else
            echo "$i,Failed" >> ping_results.csv
        fi
    } &
done
wait

echo "Ping results written to ping_results.csv"
