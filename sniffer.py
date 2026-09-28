from scapy.all import sniff, IP, TCP, UDP, ICMP


packet_count = 0


def packet_callback(packet):
    global packet_count

    if IP in packet:
        packet_count += 1

        source = packet[IP].src
        destination = packet[IP].dst

        # Find protocol and ports
        if TCP in packet:
            protocol = "TCP"
            source_port = packet[TCP].sport
            destination_port = packet[TCP].dport

        elif  UDP in packet:
            protocol = "UDP"
            source_port = packet[UDP].sport
            destination_port = packet[UDP].dport

        elif ICMP in packet:
            protocol = "ICMP"
            source_port = "-"
            destination_port = "-"

        else:
            protocol = "Other"
            source_port = "-"
            destination_port = "-"

        # Payload size only
        if packet.haslayer("Raw"):
            payload_size = len(packet["Raw"].load)
        else:
            payload_size = 0

        print("=" * 50)
        print("Packet", packet_count)
        print("Source IP        :", source)
        print("Destination IP   :", destination)
        print("Protocol         :", protocol)
        print("Source Port      :", source_port)
        print("Destination Port :", destination_port)
        print("Payload Size     :", payload_size, "bytes")


print("Starting Network Sniffer...")
print("Capturing packets...")

# Capture 10 packets
sniff(prn=packet_callback, count=10)

print("\nPacket capture completed.")