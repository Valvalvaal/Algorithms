# Primitive types

def bitwise_or(n1, n2):
    "| returns 1 if at least one of the bits compared is 1"
    print(f"{n1}: {bin(n1)}\n{n2}: {bin(n2)}")
    result = n1 | n2
    print(bin(result))
    print(result)

def bitwise_and(n1, n2):
    "& returns 1 when both of the bits compared are 1"
    print(f"{n1}: {bin(n1)}\n{n2}: {bin(n2)}")
    result = n1 & n2
    print(bin(result))
    print(result)

def bitwise_xor(n1, n2):
    "& returns 1 when ONLY ONE of the bits compared are 1"
    print(f"{n1}: {bin(n1)}\n{n2}: {bin(n2)}")
    result = n1 ^ n2
    print(bin(result))
    print(result)

def bitwise_not(n):
    "& returns 1 when ONLY ONE of the bits compared is 1"
    print(f"{n}: {bin(n)}")
    result = ~ n
    print(bin(result))
    print(result)

def bitwise_right_shift(n, shift):
    "Right shift operator shifts bits, it's the same as dividing n by 2^shift (//)"
    print(f"{n}: {bin(n)}")
    result = n >> shift
    print(bin(result))
    print(result)




bitwise_or(5,10)
bitwise_and(5,10)
bitwise_xor(5,10)
bitwise_not(10)
bitwise_right_shift(12,3)

