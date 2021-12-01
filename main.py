#!/usr/bin/env python

import scapy.all as scapy


def scan(ip):
    broadcast_mac = "ff:ff:ff:ff:ff:ff"

    # use scapy to create ARP packet object, represents ARP packet
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst=broadcast_mac)
    arp_request_broadcast = broadcast / arp_request

    # srp = send and receive packets with custom ether part, 1 second timer
    answered_packets, unanswered_packets = scapy.srp(arp_request_broadcast, timeout=1)

    # only print answered packets
    print(answered_packets.summary())


scan("")
