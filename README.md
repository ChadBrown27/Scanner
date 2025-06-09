## Description
A command-line port scanning tool written in Python. This script allows a user to identify open TCP ports on a target host, which is a fundamental step in network reconnaissance and the initial phase of a penetration test.

## Features
* Scans a user-defined range of ports on a given target.
* Accepts a hostname or an IP address as a command-line argument.
* Reports in real-time which ports are found to be open.
* Includes Service Version Detection through Banner Grabbing
* Includes basic error handling for invalid hostnames and graceful exit.

## How to Use
1.  Clone the repository: `git clone [your-repo-link-here]`
2.  Navigate to the directory: `cd [your-repo-directory]`
3.  Run the script with a target: `python3 scanner.py <hostname_or_ip>`

    Example: `python3 scanner.py scanme.nmap.org`

## Skills Demonstrated
* **Programming:** Python Scripting
* **Networking:** Socket Programming, TCP/IP Fundamentals
* **Cybersecurity:** Network Reconnaissance, Port Scanning Principles

## Future Improvements
* [ ] Implement multi-threading to speed up scans.
* [ ] Allow users to specify a list or range of ports to scan.
* [ ] Add service version detection to identify what's running on open ports.
