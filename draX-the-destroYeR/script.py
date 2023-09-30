import pwn

with open('ciphertext', 'r') as handle:
    encoded = handle.read()
    cipher = encoded.decode('base64')
    for i in range(256):
        plain = pwn.xor(cipher,i)
        print(plain)




