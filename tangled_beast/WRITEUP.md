## Challenge - tangled beast [Misc]

### Challenge Description

Assemble the mysterious message hidden within the code.

---

### Solution

We are provided with 1 line of c code

```int main(){  int VWlkfGJ3an;  BrYXZGUUN+(TTUxXVo0dl);  return 0;}int pnYDJxQHda(int Mk1kS1pfbG){  return RhdnF3eA==^5;}```

and the description indicates that there is a hidden message in this code.

Looking at this code. we notice some bizarre strings and they all have 1 thing in common.
The length of all strings is 10, indicating a possibly disassembled message.

let's try to assemble these strings to see what we get:

```VWlkfGJ3anBrYXZGUUN+TTUxXVo0dlpnYDJxQHdaMk1kS1pfbGRhdnF3eA==```

It looks like a base64 to me but let’s try to use a tool like cyberchef to make sure.
Cyberchef confirms it’s a base64 but when we try to decode we get an unreadable text let's look at the code again maybe I missed something.

If we remove the weird strings from the code the only thing remaining is 

```^5```

which indicates that the message is xored with 5 
Let's try to xor the decoded base64 message with 5.

**FLAG**
```PlaygroundsCTF{H04X_1s_be7tEr_7HaN_Ziadstr}```
