
def cabecalhoudp(protocolo):    print(f"""
       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       |        Porta origem:{protocolo.sport}  | Porta destino: {protocolo.dport}     |
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
        |        Tamanho:{protocolo.size}        |  {protocolo.chksum}(?)           |
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+""")

def cabecalhotcp(protocolo):

    print(f"""
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          |             Porta origem: {protocolo.sport} | Porta destino: {protocolo.dport}          | 
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          | Núumero sequência: {protocolo.seq}                                 |
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          | Número de ACK: {protocolo.ack}                                     |
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          | Offset: protocolo.offset {flag(protocolo.flags)} Janela: {protocolo.window}       |
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          | Checksum: {protocolo.chksum} (?)                              |
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+""")
    

def flag(flag):
    lista_flags = ["U", "A", "P", "R", "S", "F"] 
    linha = "|"
    for f in lista_flags:
        if f in flag:
            linha += f + "|"   
        else:
            linha += " |"     
    return linha



