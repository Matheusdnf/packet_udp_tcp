import scapy.all as scapy

print("Iniciando a captura de pacotes. Aperte Ctrl+C para interromper.")

# capturando pacotes
packets = scapy.sniff()
 # sumario de todos pacotes capturados
 # packets.summary()
 # looping em todos os pacotes capturados
for packet in packets:
    # verificando um cabeçalho
    if packet.haslayer("UDP"):
        # packet.show()
        print(f"Porta de origem: {packet['UDP'].sport}")
        print(f"Porta de destino: {packet['UDP'].dport}")