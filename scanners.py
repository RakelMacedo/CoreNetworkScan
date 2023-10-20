import socket
import struct


def PING():
    pass

def UDP():
    pass


def Ethernet():
    
    # Mapeia valores hexadecimais para nomes de protocolos
    ethertype_dict = {
        0x0800: 'IPv4',
        0x0806: 'ARP',
        0x86DD: 'IPv6',
    }

    try:

        while True:
            raw_socket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

            # Capture um pacote Ethernet
            packet, addr = raw_socket.recvfrom(65535)

            # Analise o cabeçalho Ethernet
            eth_header = packet[:14]
            eth_payload = packet[14:]

            eth_dest_mac, eth_src_mac, eth_type = struct.unpack("!6s6sH", eth_header)

            header_ethernet = "\nCabeçalho Ethernet:"
            mac_destino = ':'.join('%02x' % b for b in eth_dest_mac)
            mac_origem = ':'.join('%02x' % b for b in eth_src_mac)

            if eth_type in ethertype_dict:
                eth_type_str = ethertype_dict[eth_type]
            else:
                eth_type_str = hex(eth_type)
                print(f"Desconhecido: {eth_type_str}")
            
            tipo = eth_type_str

            payload_hexadecimal = "\nPayload:"
            eth_payload_str = ':'.join(f'{b:02x}' for b in eth_payload)

            separador = "\n" + "-" * 112

            print(header_ethernet)
            print(f"MAC de destino: {mac_destino}")
            print(f"MAC de origem: {mac_origem}")
            print(f"Tipo: {tipo}")
            print(payload_hexadecimal)
            print(eth_payload_str)
            print(separador)

    except KeyboardInterrupt:
        print("Captura de pacotes encerrada.")

    finally:
        raw_socket.close()


def TCP():
    
    try:
        raw_socket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

        while True:
            
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
                    tcp_header = eth_payload[ihl:ihl+20]  # O cabeçalho TCP segue o cabeçalho IP
                    tcp_src_port, tcp_dst_port, tcp_seq, tcp_ack, tcp_offset_reserved, tcp_flags, tcp_window, tcp_checksum, tcp_urg_ptr = struct.unpack("!HHLLBBHHH", tcp_header)

                    print("\nCabeçalho TCP:")
                    print(f"Porta de origem: {tcp_src_port}")
                    print(f"Porta de destino: {tcp_dst_port}")
                    print(f"Número de sequência: {tcp_seq}")
                    print(f"Número de reconhecimento: {tcp_ack}")
                    print(f"Flags: {hex(tcp_flags)}")
                    print(f"Tamanho da janela: {tcp_window}")
                    print(f"Checksum: {hex(tcp_checksum)}")
                    print(f"Ponteiro urgente: {tcp_urg_ptr}")

                    print("\n" + "-" * 112)

    except KeyboardInterrupt:
        print("Captura de pacotes encerrada.")

    finally:
        raw_socket.close()


TCP()