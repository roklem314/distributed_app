
from application import app
import random
import string
import os
import binascii

def generator2():
    gener_key = binascii.b2a_hex(os.urandom(32))
    key = binascii.unhexlify((gener_key))
    return key

def byte_to_binary(n):
    return ''.join(str((n & (1 << i)) and 1) for i in reversed(range(8)))
def hex_to_binary(h):
    return ''.join(byte_to_binary(ord(b)) for b in binascii.unhexlify(h))