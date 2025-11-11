from cabecalho import cabecalhotcp, cabecalhoudp
import scapy.all as scapy

print("Iniciando a captura de pacotes. Aperte Ctrl+C para interromper.")

# capturando pacotes
packets = scapy.sniff()

print(f"aq pai {packets}\n\n\n")
 # sumario de todos pacotes capturados
# packets.summary()
 # looping em todos os pacotes capturados
for packet in packets:
    # verificando um cabeçalho
    if packet.haslayer("UDP"):
        cabecalhoudp(packet["UDP"])
        # packet.show()
    elif packet.haslayer("TCP"):
        cabecalhotcp(packet["TCP"])
    else:
        #exibir os restos dos pacotes, a quantidade e qual foi 
        print("oi", packets.summary())