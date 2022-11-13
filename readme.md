# Wake On Lan
A Simple command line utiltiy for waking hosts on a local network. Wakeonlan is written in python and can be installed using pip.

# Installation
First clone the repository, then open a shell terminal and cd to the location of the repository's parent directory, then run...

```bash
python3 -m pip install wakeonlan

```
to install the wakeonlan command. 

# Usage
```bash
$ wol
Enter the mac address of the computer to wake, e.g. '12:34:56:78:9a:bc'
> '<enter mac address of the host here>

Using macaddr 12:34:56:78:9a:bc, which was converted to bytes: b'\x124Vx\x9a\xbc'
Which interface would you like to send the packet to?: 
            ['lo0', 'gif0', 'stf0', 'en0', 'en1', 'en2', 'bridge0', 'p2p0', 'awdl0', 'llw0', 'utun0', 'utun1']
    
en0

Interface to be used is: en0, broadcast addr: 192.168.1.255

```
The utiltity will first ask you for the MAC address of the host. Whichever machine you are on that is running the utility needs to be connected 
to the same network as the host you want to wake. Use the MAC address on the host that maps to that network if it has more than one netowrk connection. 

The utilitiy will then ask you for the netowrk interface you want to use. As demonstrated above, your machine may have several. Make sure you 
know which one you are connected to the host on.

# Caveats

## Setting up your network isn't optional!
To successfully send a WOL packet (also known as a magic packet) to the correct host, you need to ensure that;
1. The host has been configured to listen and act on WOL packets, out of the box nearly all hosts require changes to BIOS settings to enable this.
2. The host will be powered down, so pretty much any router/switch equipment will not send any packets to it as hosts only get an IP if they are up.
    the way around this is to give the node a static IP. Most router/switches allow you to create a mapping between the host's MAC address and a preferred IP address.
    NOTE: You do not have to input this address when using wakeonlan, as the utility will send a WOL packet to the broadcast address, all hosts will get it, but only 
    the host with the MAC address you provide will react to it.

## Think about security
Though its convenient to be able to power on hosts remotely, you might want to read this if you plan on using this on sensitive netowrks - https://en.wikipedia.org/wiki/Wake-on-LAN#Security_considerations

# Further Reading
MAC Addressess are usually in transmission order, that is how this utiltity expects them, read more here - https://en.wikipedia.org/wiki/MAC_address#Notational_conventions
For a more complete introduction, including security considerations, read more here - https://en.wikipedia.org/wiki/Wake-on-LAN
