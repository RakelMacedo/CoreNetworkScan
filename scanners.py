import socket
import struct
import time
from mongodb import Insert_MongoDB


def Ethernet():
    
    # Mapeia valores hexadecimais para nomes de protocolos
    ethertype_dict = {
        0x0800: 'IPv4',
        0x0806: 'ARP',
        0x86DD: 'IPv6',
    }

    try:
        start_time = time.time()  # Marca o tempo de início

        while time.time() - start_time < 10:  # Roda por 10 segundos

            raw_socket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

            # Capture um pacote Ethernet
            packet, addr = raw_socket.recvfrom(65535)

            # Analise o cabeçalho Ethernet
            eth_header = packet[:14]
            eth_payload = packet[14:]

            eth_dest_mac, eth_src_mac, eth_type = struct.unpack("!6s6sH", eth_header)

            mac_destino = ':'.join('%02x' % b for b in eth_dest_mac)
            mac_origem = ':'.join('%02x' % b for b in eth_src_mac)

            if eth_type in ethertype_dict:
                eth_type_str = ethertype_dict[eth_type]
            else:
                eth_type_str = hex(eth_type)
            
            tipo = eth_type_str

            eth_payload_str = ':'.join(f'{b:02x}' for b in eth_payload)

            ethernet_dict = {
                "MAC de destino": mac_destino,
                "MAC de origem": mac_origem,
                "Tipo": tipo,
                "Payload Hexadecimal": eth_payload_str,
            }

        Insert_MongoDB(ethernet_dict, 'ETHERNET')

        print("Captura de pacotes encerrada após 10 segundos.")

    except KeyboardInterrupt:
        print("Captura de pacotes encerrada.")

    finally:
        raw_socket.close()

    return ethernet_dict


def TCP():
    try:
        raw_socket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
        start_time = time.time()  # Marca o tempo de início

        while time.time() - start_time < 5:  # Roda por 10 segundos
            # Capture um pacote Ethernet
            packet, addr = raw_socket.recvfrom(65535)

            # Analise o cabeçalho Ethernet
            eth_header = packet[:14]
            eth_payload = packet[14:]

            eth_dest_mac, eth_src_mac, eth_type = struct.unpack("!6s6sH", eth_header)

            if eth_type == 0x0800:  # Se for um pacote IPv4
                # Analise o payload IP e verifique se é um pacote TCP
                ip_header = eth_payload[:20]
                ip_version_ihl, ip_tos, ip_total_length, ip_id, ip_flags_frag_offset, ip_ttl, ip_protocol, ip_checksum, ip_src, ip_dst = struct.unpack("!BBHHHBBH4s4s", ip_header)

                ihl = (ip_version_ihl & 0xF) * 4  # O tamanho do cabeçalho IP (IHL) é o valor mais baixo de 4 bits

                if ip_protocol == 6:  # Se for um pacote TCP
                    tcp_header = eth_payload[ihl:ihl + 20]  # O cabeçalho TCP segue o cabeçalho IP
                    tcp_src_port, tcp_dst_port, tcp_seq, tcp_ack, tcp_offset_reserved, tcp_flags, tcp_window, tcp_checksum, tcp_urg_ptr = struct.unpack("!HHLLBBHHH", tcp_header)

                    # Crie um dicionário com as informações do cabeçalho TCP
                    tcp_dict = {
                        "Porta de origem": tcp_src_port,
                        "Porta de destino": tcp_dst_port,
                        "Numero de sequencia": tcp_seq,
                        "Numero de reconhecimento": tcp_ack,
                        "Flags": hex(tcp_flags),
                        "Tamanho da janela": tcp_window,
                        "Checksum": hex(tcp_checksum),
                        "Ponteiro urgente": tcp_urg_ptr
                    }

                    Insert_MongoDB(tcp_dict, 'TCP')
                    
        print("Captura de pacotes encerrada após 10 segundos.")
        
    except KeyboardInterrupt:
        print("Captura de pacotes encerrada manualmente.")
    
    except Exception as e:
        print("Erro durante a captura de pacotes:", str(e))
    
    finally:
        raw_socket.close()

    return tcp_dict


