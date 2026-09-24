#!/usr/bin/env python3
"""Replay NovaMart firewall events to a Splunk UDP input (Lab 2, Part E).

Usage:  python3 send_syslog.py [splunk_host] [port]
        python3 send_syslog.py 127.0.0.1 5514

Each line of firewall.log is re-stamped with the CURRENT local time, including
its UTC offset (ISO 8601), so the events appear correctly in 'Last 15 minutes'
searches whatever time zone the Splunk server runs in.
"""
import socket, sys, time, datetime, re, os

host = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
port = int(sys.argv[2]) if len(sys.argv) > 2 else 5514
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "firewall.log")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sent = 0
with open(path) as f:
    for line in f:
        now = datetime.datetime.now().astimezone().isoformat(timespec="milliseconds")
        line = re.sub(r"^<(\d+)>\S+", r"<\1>" + now, line.strip())
        sock.sendto(line.encode(), (host, port))
        sent += 1
        time.sleep(0.02)
print(f"Sent {sent} events to udp://{host}:{port}")
