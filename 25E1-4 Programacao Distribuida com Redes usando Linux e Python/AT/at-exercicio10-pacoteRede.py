from scapy.all import *
host = "45.33.32.156"
for i in range(1, 20):
    packet = IP(dst=host, ttl=i) / UDP(dport=33434)
    reply = sr1(packet, verbose=0,timeout=1)
    if reply is None:
        pass
    elif reply.type == 3:
        print("Done!", reply.src)
        break
    else:
        print("%d hops away: " % i , reply.src)