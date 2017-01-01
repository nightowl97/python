import math

flag = "XXXXXXXXXXXXXXX"

def encrypt_(plaintext):
    nums = map(ord, flag)
    diffs = [nums[0]] + [b-a for a,b in zip(nums[:-1], nums[1:])]

    return ''.join([('-' if x < 0 else '+')*abs(x)+'.' for x in diffs])

def encode_hex(value):
    return value.encode('hex')

## JUST FUCKING RETURN 36 HOLY SHIT!
def make_key(x,y,z):
    s = lambda x, y, z: x % 7 ** y << z
    return s(x,y,z)
    
key = make_key(9,5,2)

def unicoded(val):
    cipher2 = ""
    for i in val:
        cipher2 += chr(ord(i)+key)
        
    return cipher2    

ciphertext = unicoded(encode_hex(encrypt_(flag)))        

with open("encrypt_key2.txt","wb") as f:
    
    f.write(ciphertext)
    f.close()
    print ciphertext 
