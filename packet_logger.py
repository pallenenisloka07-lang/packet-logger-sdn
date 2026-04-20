from pox.core import core
import pox.openflow.libopenflow_01 as of

from pox.lib.packet import ethernet, ipv4, arp, tcp, udp, icmp
from pox.lib.util import dpid_to_str

log = core.getLogger()


def _handle_PacketIn(event):
    packet = event.parsed

    if not packet.parsed:
        log.warning("Incomplete packet")
        return

    log.info("---- Packet Received ----")
    log.info("Switch: %s", dpid_to_str(event.dpid))
    log.info("Source MAC: %s", packet.src)
    log.info("Destination MAC: %s", packet.dst)

    # Protocol detection
    if isinstance(packet.next, arp):
        log.info("Protocol: ARP")

    elif isinstance(packet.next, ipv4):
        ip_packet = packet.next
        log.info("Protocol: IPv4")
        log.info("Source IP: %s", ip_packet.srcip)
        log.info("Destination IP: %s", ip_packet.dstip)

        # Transport layer
        if isinstance(ip_packet.next, tcp):
            log.info("Transport: TCP")
            log.info("Src Port: %s", ip_packet.next.srcport)
            log.info("Dst Port: %s", ip_packet.next.dstport)

        elif isinstance(ip_packet.next, udp):
            log.info("Transport: UDP")

        elif isinstance(ip_packet.next, icmp):
            log.info("Transport: ICMP")

    log.info("--------------------------\n")

    # 🔥 VERY IMPORTANT → FORWARD PACKET
    msg = of.ofp_packet_out()
    msg.data = event.ofp
    msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
    event.connection.send(msg)


def _handle_ConnectionUp(event):
    log.info("Switch connected: %s", dpid_to_str(event.dpid))


def launch():
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
    core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)
