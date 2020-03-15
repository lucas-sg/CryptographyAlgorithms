from itertools import permutations
from math import isclose


ENG_ALPH = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
SPA_ALPH = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

FREQS_SPA = [['A', 0.1253],
             ['B', 0.0142],
             ['C', 0.0468],
             ['D', 0.0586],
             ['E', 0.1368],
             ['F', 0.0069],
             ['G', 0.0101],
             ['H', 0.0070],
             ['I', 0.0625],
             ['J', 0.0044],
             ['K', 0.0002],
             ['L', 0.0497],
             ['M', 0.0315],
             ['N', 0.0671],
             ['Ñ', 0.0031],
             ['O', 0.0868],
             ['P', 0.0251],
             ['Q', 0.0088],
             ['R', 0.0687],
             ['S', 0.0798],
             ['T', 0.0463],
             ['U', 0.0393],
             ['V', 0.0090],
             ['W', 0.0001],
             ['X', 0.0022],
             ['Y', 0.0090],
             ['Z', 0.0052]]
I = sum(p**2 for p in [freq[1] for freq in FREQS_SPA])

def break_shift_cipher(s):
    p = [freq[1] for freq in FREQS_SPA]
    q = [freq[1] for freq in calc_freqs(s)]
    alph_len = len(p)
    I_list = [sum([p[i]*q[(i + j)%alph_len] for i in range(alph_len)]) 
                                            for j in range(alph_len)]
    I_list = [abs(I-i) for i in I_list]
    return [I_list.index(k) for k in sorted(I_list)][0]


def calc_offset_between(c1, c2):
    offset = char_index(c1) - char_index(c2)
    return offset + (len(SPA_ALPH) if offset < 0 else 0)


def calc_freqs(s):
    freq_pairs = [[c,0] for c in SPA_ALPH]
    
    for c in s:
        freq_pairs[char_index(c)][1] += 1

    # freq_pairs = sorted(freq_pairs, key=lambda pair: pair[1], reverse=True)
    return [[p[0], float(p[1])/len(s)] for p in freq_pairs]
        

def shift(s, offset):
    return ''.join([shift_char(c, offset) for c in s])


def shift_char(c, offset):
    shifted_index = char_index(c) + offset    
    alph_index = shifted_index%len(SPA_ALPH)
    return SPA_ALPH[alph_index]


def char_index(c):
    n_index = ord('N') - ord('A')
    
    if c.upper() == 'Ñ':
        return n_index + 1
    
    index = ord(c.upper()) - ord('A') 
    return index + (1 if index > n_index else 0) # It's at Ñ's position or past it


def flatten(list):
    return [y for x in list for y in x]



code = "VKXYKBKXGKSGWAKQQGYIUYGYWAKXKGQRKSZKJKYKKYIUSYKMAÑX"
offset = break_shift_cipher(code)
# print(shift(code, -offset))