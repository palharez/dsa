n1 = 23477
n2 = 31213

print(bin(n1)) # In this way we can prints the binary value of this variable
print(bin(n2))

# AND 1 AND 1 = 1 evertyhing else is 0
n3 = n1 & n2
# print(bin(n3)) # 0b101100110100101

# OR 0 OR 0 = 0 everything else is 1
n4 = n1 | n2
# print(bin(n4)) # 0b111101111111101


# XOR This means either OR
# 1 XOR 0 = 1
# 0 XOR 1 = 1
# Everything else is 0
n5 = n1 ^ n2
# print(bin(n5)) # 0b10001001011000

# NOT
# print(bin(~n1))

# SHIFTS
number = 20 
print(bin(number))
number <<= 1 # This shift all the bits to the left on the binary table
print(bin(number))
number >>= 2 # This shift all the bits to right on the binary table
print(bin(number))


# Ever or Odd
somenumber = 3472348

if somenumber & 1 == 0:
  print("even")
else:
  print("odd")

# Read, Write, Execute, Change
person1 = 0b1000
person2 = 0b1001
person3 = 0b1100
person4 = 0b1111

together1 = person1 & person2 & person3 & person4 # Which flag is the same
together2 = person1 | person2 | person3 | person4 # Which flasg they together have

print(together1)
print(together2)

# XOR Variable SWAP
a = 10 # 01010
b = 20 # 10100

a ^= b # 11110
b ^= a # 01010
a ^= b # 10100

print(a)
print(b)