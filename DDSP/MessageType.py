# Enumerate the Type of message.

class MessageType:
    """docstring for MessageType"""
    discovery = 0x00
    advertisement = 0x01
    withdraw = 0x02
    query = 0x10
    offer = 0x11
    ack = 0x12
    nack = 0x13
    undefined = 0xff