import random
import window
import pygame

import socket


from scapy.all import Ether, IP, TCP, sendp,Raw



class computer(window.window):
    
    def __init__(self):
        packets = self.createPacketList()
        packet = self.create_fake_packet("Hello, the secret code is 300!","148.88.247.82")
        
        packets[43] = packet

        print(packets)
        
        


    def display(self,screen):
        pass
        

    def create_fake_packet(self,data,src_ip = None):
            # Create a fake Ethernet frame
            eth = Ether()
            # Create an IP packet
            dst_ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
            if src_ip is None:
                src_ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))

            
            dst_mac =   ":".join(map(lambda x: "%02x" % x, (random.randint(0, 255) for _ in range(6))))
            #if src_mac is None: 
            src_mac =  ":".join(map(lambda x: "%02x" % x, (random.randint(0, 255) for _ in range(6))))

            
            dst_port = random.randint(1024, 65535)
            #if src_port is None:
            src_port = random.randint(1024, 65535)
            # Create a TCP segment
            eth = Ether(src=src_mac, dst=dst_mac)
            ip = IP(src=src_ip, dst=dst_ip)
            tcp = TCP(sport=src_port, dport=dst_port)
            payload = Raw(load=data)
            # Stack the layers and the payload
            packet = eth / ip / tcp / payload
            return f"{packet[Ether].src} {packet[IP].src} {packet[TCP].sport} {packet[Raw].load}"
    
    def createPacketList(self):
        pleasantries = []

        with open('pleasantries.csv', 'r') as file:
            # Read the entire file content
            content = file.read()

            # Split the content by comma and strip extra spaces and quotes
            pleasantries = [item.strip().strip('"') for item in content.split(',')]

        packets = []
        for  pleasantry in pleasantries:
            packets.append(self.create_fake_packet(pleasantry))
            
        return(packets)

    
computer()