#!/usr/bin/env python
def convert(Dec):
    binary = 'b'
    while Dec != 0:
        rem = Dec%2
        Dec = Dec//2
        
        if rem == 0:
            binary += str(0)
        
        else:
            binary += str(1)
    
    binary = binary[1:]
    binary = binary[::-1]
    return binary 


Dec = int(input("Enter a decimal: "))



print("You entered: {}".format(Dec))

binary = convert(Dec)

print(binary)


