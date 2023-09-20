import numpy as np

#crc_bits = np.zeros((num_users, len_data+len_crc), dtype=np.int8)
#h = np.zeros(num_users, dtype=np.complex64)

def run(h_re, h_im):
    print(h_re, h_im)
    c = np.array(np.vectorize(complex)(h_re, h_im))
    print(c)
    input()

h_re = [i for i in range (16)]
h_im = np.zeros(16)
print(h_re, h_im)
run(h_re, h_im)
