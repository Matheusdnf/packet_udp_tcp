import scapy.all as scapy

print("Iniciando a captura de pacotes. Aperte Ctrl+C para interromper.")

# capturando pacotes
packets = scapy.sniff()

print(f"aq pai {packets}\n\n\n")
 # sumario de todos pacotes capturados
packets.summary()
 # looping em todos os pacotes capturados
for packet in packets:
    # verificando um cabeçalho
    if packet.haslayer("UDP"):
        # packet.show()
        print(f"Porta de origem: {packet['UDP'].sport}")
        print(f"Porta de destino: {packet['UDP'].dport}")
        print(f"Comprimento: {packet['UDP'].len}")
        print(f"Checksum: {packet['UDP'].chksum}")

    elif packet.haslayer("TCP"):
        print(f"Porta de origem: {packet['TCP'].sport}")
        print(f"Porta de destino: {packet['TCP'].dport}")
        print(f"Comprimento: {packet['TCP'].len}")
        print(f"Checksum: {packet['TCP'].chksum}")

    else:
        print(packet.haslayer("ICMP"))