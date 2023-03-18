# IP Range Pinger

This is a Python script that allows you to ping a range of IP addresses and write the results to a CSV file.

## Usage

1. Clone the repository or download the `ip_range_pinger.py` file.

2. Install the required packages using the following command:

```bash
pip install ping3
```

3. Run the script using the following command:

```bash
python ip_range_pinger.py
```

4. Enter the IP range to scan in the format `xxx.xxx.xxx.xxx/xx` when prompted.

5. The script will ping all of the IP addresses in the specified range and write the results to a CSV file named `ping_results.csv`.

## Example

Suppose you want to scan the IP range `172.16.96.1` to `172.16.96.254`, with a subnet mask of `255.255.255.0`. You would enter the following when prompted:

Enter IP range to scan (e.g. 172.16.96.1/24): 172.16.96.1/24

The script will then ping all of the IP addresses in the range and write the results to a CSV file named `ping_results.csv`. The file will be located in the same directory as the script.

## Example Output

| IP Address   | Result   |
|--------------|----------|
| 172.16.96.1   | Success  |
| 172.16.96.2   | Failure  |
| 172.16.96.3   | Success  |
| 172.16.96.4   | Failure  |
| 172.16.96.5   | Success  |
| 172.16.96.6   | Success  |
| 172.16.96.7   | Failure  |
| ...          | ...      |

## Limitations

The script currently only supports IPv4 addresses. IPv6 addresses are not supported.


# Bash script for pinging IP addresses in a range
This bash script allows you to ping all the IP addresses in a specified range and writes the results to a CSV file.

## Usage

To use the script, simply run it from the command line:

```bash
./ping_range.sh
```
You will be prompted to enter the IP range you wish to scan. The range should be entered in the format <first_ip>-<last_ip>. For example, to scan the range 192.168.1.1 to 192.168.1.254, you would enter:
```bash
192.168.1.1-254
```
The script will then ping each IP address in the range and write the results to a CSV file named ping_results.csv.

## Improvements

In this updated version of the script, each ping command is run in the background using {} and &, which allows all the pings to be run simultaneously. This makes the script much faster than the previous version, which ran each ping command sequentially.


