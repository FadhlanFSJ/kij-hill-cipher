import numpy as np

plain = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"
key = "test"

plain = plain.lower().replace(" ", "")
eam = {chr(i):i-97 for i in range(97, 97+26)}
eam_rev = {i-97:chr(i) for i in range(97, 97+26)}

if len(plain) % 2 == 1:
    plain = plain + 'x'
plain_number = np.array([eam[i] for i in plain])
key_number = np.array([eam[i] for i in key])
bl = len(key_number)//2

key_matrix = np.array(key_number).reshape(bl,bl)
plain_array = np.array(plain_number)
plain_block = np.split(plain_array, len(plain_array)/bl)
ct_block = [np.matmul(plain_block[i], key_matrix) % 26 for i in range(len(plain_block))]

ct_array = np.concatenate(ct_block)
ct = [eam_rev[ct_array[i]] for i in range(len(ct_array))]
ct = ''.join(ct)
print(ct)
