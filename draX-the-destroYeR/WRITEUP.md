### chalenge description: 
decipher the mysterious Minecraft glyphs, and unveil the strings they guard.

---
### solution

In this challenge, participants are provided with ciphertext and tasked with encoding it. Looking at the ciphertext which looks like its base64 encoded message. 
and the name of the challenge indicates that it’s xor encoded as well
  
so we start by writing a simple python code to decode the message.
First we decode the base64 message then we try to brute force the xor encryption key as there is only 255 possible keys

```
import pwn

with open('ciphertext', 'r') as handle:
    encoded = handle.read()
    cipher = encoded.decode('base64')
    for i in range(256):
        plain = pwn.xor(cipher,i)
        if 'PlaygroundsCTF{' in plain:
            print(plain)
```

Running this script showed us nothing. let’s read the description again and see if we can find something that helps.
“decipher the mysterious Minecraft glyphs, and unveil the strings they guard.” This sentence caught my attention “unveil the STRINGS”. Weird way to describe the message or the flag.
Let’s try to put the output in a file then use strings as there might be unprintable chars in the message which would explain why we got nothing running our original script. 
I removed the if statement from my original code and redirected the output to a file.

```
import pwn

with open('ciphertext', 'r') as handle:
    encoded = handle.read()
    cipher = encoded.decode('base64')
    for i in range(256):
        plain = pwn.xor(cipher,i)
        print(plain)
```

then in the terminal using
```
python script.py > output
strings output
```

**FLAG**
```PlaygroundsCTF{XoR_enCrYpt!on_M@st3r}```
