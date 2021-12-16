from dataclasses import dataclass
from io import StringIO
from typing import List, Union

import aoc

input_data = aoc.get_input()


@dataclass
class Packet:
    version: int
    type_id: int


@dataclass
class LiteralPacket(Packet):
    value: int


@dataclass
class OperatorPacket(Packet):
    mode: int
    packets: List[Union['LiteralPacket', 'OperatorPacket']]

    @property
    def value(self):
        if self.type_id == 0:  # sum
            return sum(p.value for p in self.packets)
        elif self.type_id == 1:  # product
            res = self.packets[0].value
            for p in self.packets[1:]:
                res *= p.value

            return res
        elif self.type_id == 2:  # min
            return min(p.value for p in self.packets)
        elif self.type_id == 3:  # max
            return max(p.value for p in self.packets)
        elif self.type_id == 5:  # gt
            return 1 if self.packets[0].value > self.packets[1].value else 0
        elif self.type_id == 6:  # st
            return 1 if self.packets[0].value < self.packets[1].value else 0
        elif self.type_id == 7:  # eq
            return 1 if self.packets[0].value == self.packets[1].value else 0


def _conv_hex(hex_str: str):
    bit_length = len(hex_str) * 4
    bits = bin(int(hex_str, 16))[2:].zfill(bit_length)
    bits.rstrip('0')
    return StringIO(bits)


def _parse_packet(buf: StringIO):
    version = buf.read(3)
    type_id = buf.read(3)
    if not (version and type_id):  # buf empty
        return

    version = int(version, 2)
    type_id = int(type_id, 2)

    ret_packet = None

    if type_id == 4:  # literal
        literal_bits = ''
        keep_reading = True
        while keep_reading:
            prefix = buf.read(1)
            literal_bits += buf.read(4)
            if prefix == '0':
                break

        ret_packet = LiteralPacket(version, type_id, int(literal_bits, 2))
    else:  # operator packet
        mode = buf.read(1)
        if mode == '0':  # total length mode
            length = int(buf.read(15), 2)
            sub_buf = StringIO(buf.read(length))

            # discover sub-packets
            sub_packets = []
            packet = _parse_packet(sub_buf)
            while packet:
                sub_packets.append(packet)
                packet = _parse_packet(sub_buf)

            ret_packet = OperatorPacket(version, type_id, int(mode), sub_packets)
        elif mode == '1':  # packet count mode
            packet_count = int(buf.read(11), 2)

            sub_packets = []
            for _ in range(packet_count):
                packet = _parse_packet(buf)
                sub_packets.append(packet)

            ret_packet = OperatorPacket(version, type_id, int(mode), sub_packets)

    return ret_packet


def _count_versions(packet: Packet):
    res = 0
    if isinstance(packet, OperatorPacket):
        for p in packet.packets:
            res += _count_versions(p)

    return packet.version + res


def challenge1():
    for line in input_data:  # allows multiple examples
        buf = _conv_hex(line)
        parsed = _parse_packet(buf)
        print(_count_versions(parsed))


def challenge2():
    for line in input_data:
        buf = _conv_hex(line)
        parsed = _parse_packet(buf)
        print(parsed.value)


aoc.run(challenge1)
aoc.run(challenge2)
