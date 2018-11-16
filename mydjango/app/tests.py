# from django.test import TestC
# Create your tests here.
import os

import mnemonic
import binascii
import Crypto.Random
from Crypto.PublicKey import RSA

import hashlib

# mnemonic=mnemonic.Mnemonic('english')
# words=mnemonic.generate(128)
# print(words)
# print(mnemonic.wordlist)
# print(mnemonic.check(words))
# entropy=mnemonic.to_entropy(words)
# print(entropy)
# seed=mnemonic.to_seed(words,passphrase='hello')
# print(seed)
# print(binascii.hexlify(seed).decode())
# str = '人生苦短，我用Python!'
# bytes = bytearray(str.encode())
# print(bytes)
# # bytes = bytearray(b'\xe4\xba\xba\xe7\x94\x9f\xe8\x8b\xa6\xe7\x9f\xad\xef\xbc\x8c\xe6\x88\x91\xe7\x94\xa8Python!')

str="['0_1_2','0_2_3','2_1_3']"
str1=str.strip('[').strip(']')
print(str1)
str2=str1.split(',')

mnemonic=mnemonic.Mnemonic('english')
words=mnemonic.generate(128)
print(words)
print(mnemonic.wordlist)
print(mnemonic.check(words))
entropy=mnemonic.to_entropy(words)
print(entropy)
seed=mnemonic.to_seed(words,passphrase='hello')
print(seed)
print(binascii.hexlify(seed).decode())
str = '人生苦短，我用Python!'
bytes = bytearray(str.encode())
print(bytes)
# bytes = bytearray(b'\xe4\xba\xba\xe7\x94\x9f\xe8\x8b\xa6\xe7\x9f\xad\xef\xbc\x8c\xe6\x88\x91\xe7\x94\xa8Python!')


