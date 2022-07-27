############################  LICENSE  #########################

# Copyright (C) <2013-2021> Crowd Render Pty Limited, Sydney Australia


# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

# You can contact the author at info at
# crowdrender dot com dot au

################################################################


import socket, netifaces


MAC_ADDR_LEN_BYTES = 6

def wol(lunaMacAddress: bytes, broadcast: str):

    # setup an appropriate socket to send the magic packet
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    # construct and send the magic packet to the machine's mac address
    # via the broadcast address of it's network
    magic = b'\xff' * 6 + lunaMacAddress * 16
    s.sendto(magic, (broadcast, 9))

def main()-> None:    
    # pass to wol the mac address of the ethernet port of the appliance to wakeup
    macaddr_input = input("Enter the mac address of the computer to wake, e.g. '12:34:56:78:9a:bc'\n>")

    # make sure the resulting bytes stream is in transmission order, that is lsb to the left.
    #  https://en.wikipedia.org/wiki/MAC_address#Notational_conventions
    macaddr_bytes = int(
        "0x".join(
            [macaddr_input.replace(":", "")]
        ), 16).to_bytes(MAC_ADDR_LEN_BYTES, byteorder='big')

    print(f"Using macaddr {macaddr_input}, which was converted to bytes: {macaddr_bytes}")

    print(f"""Which interface would you like to send the packet to?: 
        {netifaces.interfaces()}
    """)
    interface = input()

    if interface not in netifaces.interfaces():
        raise ValueError(f"{interface} is not valid, please choose from the above.")

    # get the broadcast address of this interface, assuming the last address for this if is the
    # right one
    if_broad_addr = netifaces.ifaddresses(interface)[netifaces.AF_INET][-1]['broadcast']
    print(f"Interface to be used is: {interface}, broadcast addr: {if_broad_addr}")
    
    # send the magic packet to the computer
    wol(macaddr_bytes, if_broad_addr)

if __name__ == '__main__':
    main()