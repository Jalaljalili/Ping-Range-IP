# IP Address Counter

This Python script is designed to count the total number of IP addresses represented by CIDR notation in a text file. It parses each line in the file, extracts the CIDR notation, calculates the number of IP addresses within each network, and sums them up to provide a total count.

## Usage

1. Create a text file (`temp.txt` in this example) with one CIDR notation per line. For example:

```
192.168.0.0/24
10.0.0.0/8
172.16.0.0/16
```

2. Modify the `file_path` variable in the script to point to your input file.

3. Run the script using the following command:

```bash
python main.py
```
The script will read the input file, calculate the total number of IP addresses, and display the result.

## Example

For the provided example usage and input file, the script will produce the following output:

Total number of IP addresses: 16777216

## Handling Invalid Input

If the input file contains lines with invalid CIDR notation, the script will print an error message indicating the line with the invalid format. It will continue processing other lines in the file.
