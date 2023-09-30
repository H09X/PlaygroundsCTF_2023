import math
import random
from Crypto.Util.number import bytes_to_long,long_to_bytes


flag = b"PlaygroundsCTF{************************}"
p = random.getrandbits(128)
q = random.getrandbits(128)
e = 65537
n = 61974480154644117830514010572552673374575128286475822404650429838087711095644
ct = 18228129414403117160958496280719098130343804146611228843689569857092514426177

