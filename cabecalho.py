import scapy.all as scapy
from scapy.compat import raw

def checksum_udp(pkt):
    try:
        pkt_copia = pkt.copy()
        pkt_copia.chksum = None
        recalculado = scapy.UDP(raw(pkt_copia)).chksum
        if recalculado == pkt.chksum:
            return "OK"  
        else:
            return "ERRO"
    except Exception:
        return "Indefinido"


def checksum_tcp(pkt_tcp, pkt_ip):
    try:
        pkt_temp = scapy.IP(src=pkt_ip.src, dst=pkt_ip.dst) / pkt_tcp.copy()
        pkt_temp[scapy.TCP].chksum = None
        recalculado = scapy.raw(pkt_temp[scapy.TCP])
        recalculado = scapy.TCP(recalculado).chksum

        original = pkt_tcp.chksum
        
        if recalculado == original:
            return "OK"  
        else:
            return "ERRO"
        
    except Exception:
        return "Indefinido"


def cabecalhoudp(protocolo):
    checksum_status = checksum_udp(protocolo)
    print(f"""
       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       | Porta origem: {protocolo.sport:<8} | Porta destino: {protocolo.dport:<14} |
       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       | Tamanho: {protocolo.len:<13} | Checksum: {protocolo.chksum:<6} ({checksum_status})         |
       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    """)


def cabecalhotcp(protocolo, ip_pkt):
    checksum_status = checksum_tcp(protocolo, ip_pkt)
    print(f"""
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          | Porta origem: {protocolo.sport:<16} | Porta destino: {protocolo.dport:<13} |
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          | Número de sequência: {protocolo.seq:<40} |
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          | Número de ACK: {protocolo.ack:<45}  |
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          | Offset: {protocolo.dataofs:<10} {flag(protocolo.flags):<3} Janela: {protocolo.window:<20} |
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          | Checksum: {protocolo.chksum:<6} ({checksum_status})                                         |
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    """)


def flag(flag):
    lista_flags = ["U", "A", "P", "R", "S", "F"]
    linha = "|"
    for f in lista_flags:
        linha += f + "|" if f in flag else " |"
    return linha
