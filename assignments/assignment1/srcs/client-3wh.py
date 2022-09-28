#!/usr/bin/env python

'''
 * client-3wh.py
 * Name: Deepak Maurya
 * PUID: 0030191785
'''

from scapy.all import *
import threading
import pdb 

SEND_PACKET_SIZE = 1000  # should be less than max packet size of 1500 bytes

# A client class for implementing TCP's three-way-handshake connection establishment and closing protocol,
# along with data transmission.


class Client3WH:

    def __init__(self, dip, dport):
        """Initializing variables"""
        self.dip = dip
        self.dport = dport
        # selecting a source port at random
        self.sport = random.randrange(0, 2**16)

        self.next_seq = 0                       # TCP's next sequence number
        self.next_ack = 0                       # TCP's next acknowledgement number

        self.ip = IP(dst=self.dip)              # IP header

        self.connected = False
        self.timeout = 3

    def _start_sniffer(self):
        t = threading.Thread(target=self._sniffer)
        t.start()

    def _filter(self, pkt):
        if (IP in pkt) and (TCP in pkt):  # capture only IP and TCP packets
            return True
        return False

    def _sniffer(self):
        while self.connected:
            sniff(prn=lambda x: self._handle_packet(
                x), lfilter=lambda x: self._filter(x), count=1, timeout=self.timeout)

    def _handle_packet(self, pkt):
        """TODO(1): Handle incoming packets from the server and acknowledge them accordingly. Here are some pointers on
           what you need to do:
           1. If the incoming packet has data (or payload), send an acknowledgement (TCP) packet with correct 
              `sequence` and `acknowledgement` numbers.
           2. If the incoming packet is a FIN (or FINACK) packet, send an appropriate acknowledgement or FINACK packet
              to the server with correct `sequence` and `acknowledgement` numbers.
        """

        ### BEGIN: ADD YOUR CODE HERE ... ###
        print('I am here in handle packet')
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        ### END: ADD YOUR CODE HERE ... #####

    def connect(self):
        """TODO(2): Implement TCP's three-way-handshake protocol for establishing a connection. Here are some
           pointers on what you need to do:
           1. Handle SYN -> SYNACK -> ACK packets.
           2. Make sure to update the `sequence` and `acknowledgement` numbers correctly, along with the 
              TCP `flags`.
        """

        ### BEGIN: ADD YOUR CODE HERE ... ###
        print('inside the connect function 1');
        TCP_SYN = TCP(sport = self.sport, dport = self.dport, flags = "S", seq = self.next_seq); 
        print('TCP_SYN[TCP].sport: ', TCP_SYN[TCP].sport,' TCP_SYN[TCP].dport: ', TCP_SYN[TCP].dport, '\n')
        print('TCP_SYN[TCP].flags: ', TCP_SYN[TCP].flags,' TCP_SYN[TCP].seq: ', TCP_SYN[TCP].seq, ' TCP_SYN[TCP].ack: ', TCP_SYN[TCP].ack, '\n')
        
        #pdb.set_trace()
        TCP_SYNACK = sr1(self.ip/TCP_SYN) #  iface = 'br0'
        #TCP_SYNACK.show()
        self.next_seq +=1

        assert TCP_SYNACK.haslayer(TCP) , 'TCP layer missing'
        assert TCP_SYNACK[TCP].flags & 0x12 == 0x12 , 'No SYN/ACK flags'
        assert TCP_SYNACK[TCP].ack == self.next_seq , 'Acknowledgment number error'

        print('TCP_SYNACK[TCP].sport: ', TCP_SYNACK[TCP].sport,' TCP_SYNACK[TCP].dport: ', TCP_SYNACK[TCP].dport, '\n')
        print('TCP_SYNACK[TCP].flags: ', TCP_SYNACK[TCP].flags,' TCP_SYNACK[TCP].seq: ', TCP_SYNACK[TCP].seq, ' TCP_SYNACK[TCP].ack: ', TCP_SYNACK[TCP].ack, '\n')
        	
        print('inside the connect function 2');
        self.next_ack = TCP_SYNACK.seq + 1
        #self.next_seq = TCP_SYNACK.ack
        TCP_ACK = TCP(sport = self.sport, dport = self.dport, flags = "A", seq = self.next_seq, ack = self.next_ack);
        TCP_ACK.show()
        print('TCP_ACK[TCP].sport: ', TCP_ACK[TCP].sport,' TCP_ACK[TCP].dport: ', TCP_ACK[TCP].dport, '\n')
        print('TCP_ACK[TCP].flags: ', TCP_ACK[TCP].flags,' TCP_ACK[TCP].seq: ', TCP_ACK[TCP].seq, ' TCP_ACK[TCP].ack: ', TCP_ACK[TCP].ack, '\n')
        send(self.ip/TCP_ACK) 
        

        ### END: ADD YOUR CODE HERE ... #####

        self.connected = True
        # self.close() 
        #self._start_sniffer()
        print('Connection Established')

    def close(self):
        """TODO(3): Implement TCP's three-way-handshake protocol for closing a connection. Here are some
           pointers on what you need to do:
           1. Handle FIN -> FINACK -> ACK packets.
           2. Make sure to update the `sequence` and `acknowledgement` numbers correctly, along with the 
              TCP `flags`.
        """

        ### BEGIN: ADD YOUR CODE HERE ... ###
        print('I am here in close')

        fin = self.ip/TCP(sport=self.sport, dport=self.dport, flags='FA', seq=self.next_seq, ack=self.next_ack)
        fin_ack = sr1(fin, timeout = self.timeout)
        self.next_seq +=1
        print('fin[TCP].sport: ', fin_ack[TCP].sport,' TCP_SYN[TCP].dport: ', fin_ack[TCP].dport, '\n')
        print('TCP_SYN[TCP].flags: ', fin_ack[TCP].flags,' TCP_SYN[TCP].seq: ', fin_ack[TCP].seq, ' TCP_SYN[TCP].ack: ', fin_ack[TCP].ack, '\n')
        
        assert fin_ack.haslayer(TCP), 'TCP layer missing'
        assert fin_ack[TCP].flags & 0x11 == 0x11 , 'No FIN/ACK flags'
        assert fin_ack[TCP].ack == self.next_seq , 'Acknowledgment number error'

        self.ack = fin_ack[TCP].seq + 1
        ack = self.ip/TCP(sport=self.sport, dport=self.dport, flags='A', seq=self.seq,  ack=self.ack)
        send(ack)
        

        ### END: ADD YOUR CODE HERE ... #####

        self.connected = False
        print('Connection Closed')

    def send(self, payload):
        """TODO(4): Create and send TCP's data packets for sharing the given message (or file):
           1. Make sure to update the `sequence` and `acknowledgement` numbers correctly, along with the 
              TCP `flags`.
        """

        ### BEGIN: ADD YOUR CODE HERE ... ###
        TCP_PUSH = TCP(sport = self.sport, dport = self.dport, flags = "PA", seq = self.next_seq, ack = self.next_ack)/payload
        self.next_seq += len(TCP_PUSH[Raw])
        ack = sr1(TCP_PUSH, timeout = self.timeout)

        assert ack.haslayer(TCP), 'TCP layer missing'
        assert ack[TCP].flags & 0x10 == 0x10, 'No ACK flag'
        assert ack[TCP].ack == self.seq , 'Acknowledgment number error'
        
        
        
        
        
        
        
        

        ### END: ADD YOUR CODE HERE ... #####


def main():
    """Parse command-line arguments and call client function """
    print("Length of inputs ", len(sys.argv),"\n")
    print("sys.argv[0] ", sys.argv[0],"\n")
    print("sys.argv[1] ", sys.argv[1],"\n")
    print("sys.argv[2] ", sys.argv[2],"\n")
    print("sys.argv[3] ", sys.argv[3],"\n")
    # TODO: Change the sys.argv to 3 later on.
    if len(sys.argv) != 4:
        sys.exit(
            "Usage: ./client-3wh.py [Server IP] [Server Port] < [message]")
    server_ip = sys.argv[1]
    server_port = int(sys.argv[2])

    client = Client3WH(server_ip, server_port)
    client.connect()

    message = sys.stdin.read(SEND_PACKET_SIZE)
    while message:
        client.send(message)
        message = sys.stdin.read(SEND_PACKET_SIZE)

    client.close()


if __name__ == "__main__":
    main()

