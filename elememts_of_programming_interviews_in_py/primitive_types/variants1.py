# Compute x modulo a power of 2 

def mod(x, p):
    return x & (p - 1)

print(mod(77,64))