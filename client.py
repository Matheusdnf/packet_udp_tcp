from cabecalho import cabecalhotcp, cabecalhoudp
import scapy.all as scapy

print("Iniciando a captura de pacotes. Aperte Ctrl+C para interromper.")

# capturando pacotes
packets = scapy.sniff()

# print(f"aq pai {packets}\n\n\n")
 # sumario de todos pacotes capturados
# packets.summary()
 # looping em todos os pacotes capturados
cabecalho_udp=0
cabecalho_tcp=0
for packet in packets:
    # verificando um cabeçalho
    if packet.haslayer("UDP"):
        cabecalho_udp+=1
        cabecalhoudp(packet["UDP"])
        
     # packet.show()
    elif packet.haslayer("TCP"):
        cabecalho_tcp+=1
        #print(packet["TCP"].flags)


        cabecalhotcp(packet["TCP"])
    else:
        #exibir os restos dos pacotes, a quantidade e qual foi 
        # print("oi", packets.summary())
        print(packet.haslayer())
        
print(f"\n\nTotal de pacotes UDP: {cabecalho_udp}")
print(f"Total de pacotes TCP: {cabecalho_tcp}")