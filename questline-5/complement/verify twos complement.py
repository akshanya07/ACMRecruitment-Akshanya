n = -42
bits = 8

twos_complement = (1 << bits) + n
binary = format(twos_complement, '08b')

print(binary)