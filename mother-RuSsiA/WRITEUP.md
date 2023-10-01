### Challenge Description:

Russia, the icy wonderland where redstone circuits and secret chambers guard the most precious treasures.
Now, a mysterious small n has been discovered, concealing a hidden message.
Can you mine your way through the cryptographic labyrinth to unearth its secrets

---

### Solution

From the name of the challenge and the script we are provided with we know that it’s a basic rsa challenge with a small n.
Small n in rsa is very dangerous as we can find the factors of n and then find phi and d to decrypt the ciphertext
There are 2 ways to solve the challenge:
1)Find the factors of n (p,q) then calculate phi and d using tools like: http://factordb.com
2)Find phi without needing to find the factors using a tool like: https://www.alpertron.com.ar/ECM.HTM
Personally, I prefer the second as it is faster.
Using the tool we get:

```Phi = 16612382709255864090302277633184939233723254429014068302985001384015822848000```

Then we can find d easily using 

```d = Pow(e,-1,phi)```

now we have everything we need to decrypt the message so we write a python script.

```
import math
import random
from Crypto.Util.number import bytes_to_long,long_to_bytes

e = 65537
n = 61974480154644117830514010572552673374575128286475822404650429838087711095644
ct = 18228129414403117160958496280719098130343804146611228843689569857092514426177

phi = 16612382709255864090302277633184939233723254429014068302985001384015822848000
d = pow(e,-1,phi)
plaintext = pow(ct,d,n)

print(long_to_bytes(plaintext).decode())
```

**FLAG**
```PlaygroundsCTF{cRAFtYFlagHUN73R}```

