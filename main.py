import argparse
import scanner 
import results

# command line arguments
parser = argparse.ArgumentParser(description='A port scanner')
parser.add_argument('target', help='IP address or hostname to scan')
parser.add_argument('-p', '--ports', default='1-1024', help='Ports to scan (default 1-1024)')
parser.add_argument('-t', '--timeout', type=float, default=1.0, help='Timeout in seconds (default: 1.0)')
args = parser.parse_args()

# initializing scanner
scan = scanner.PortScanner(args.target, args.ports, args.timeout)

# performing scan
scan_results = scan.scan()

# print the results to the console
results = results.ResultsProcessor(scan_results)
print(results.scan_result())
