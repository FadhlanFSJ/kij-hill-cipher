import numpy as np

ct = "tbaieykqnpmgzrezlaevwadepnxabsxkxsit"
key = "test"

ct = ct.lower().replace(" ","")
eam = {chr(i):i-97 for i in range(97, 97+26)}
eam_rev = {i-97:chr(i) for i in range(97, 97+26)}

if len(ct) % 2 == 1:
    ct+='x'
ct_number = np.array([eam[i] for i in ct])
key_number = np.array([eam[i] for i in key])
bl = len(key_number) // 2

key_matrix = np.array(key_number).reshape(bl,bl)
ct_array = np.array(ct_number)
adj_key_matrix = np.linalg.inv(key_matrix) * round(np.linalg.det(key_matrix))
key_inverse = (9 * adj_key_matrix) % 26

ct_blocks = np.split(ct_array, len(ct_number)/bl)
pt_block = [np.matmul(ct_blocks[i], key_inverse) % 26 for i in range(len(ct_blocks))]
pt_array = np.concatenate(pt_block)
pt = [eam_rev[round(i)] for i in pt_array]
pt = ''.join(pt)
print(pt)
