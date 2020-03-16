from itertools import permutations
from math import isclose


ENG_ALPH = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
SPA_ALPH = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

FREQ_PAIRS_SPA = [['A', 0.1253],
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
FREQS_SPA = [freq_pair[1] for freq_pair in FREQ_PAIRS_SPA]
I = sum(p**2 for p in FREQS_SPA)


def break_shift_cipher(s):
    p = FREQS_SPA
    q = calc_freqs(s)
    alph_len = len(p)
    I_list = [sum([p[i]*q[(i+j) % alph_len] for i in range(alph_len)])
              for j in range(alph_len)]
    return I_list.index(min(I_list, key=lambda k: abs(I-k)))


def calc_freqs(s):
    freq_pairs = [[c, 0] for c in SPA_ALPH]
    for c in s:
        freq_pairs[char_index(c)][1] += 1
    return [float(freq_pair[1])/len(s) for freq_pair in freq_pairs]


def shift(s, offset):
    return ''.join([shift_char(c, offset) for c in s])


def shift_char(c, offset):
    shifted_index = char_index(c) + offset
    alph_index = shifted_index % len(SPA_ALPH)
    return SPA_ALPH[alph_index]


def char_index(c):
    n_index = ord('N') - ord('A')
    if c.upper() == 'Ñ':
        return n_index + 1
    index = ord(c.upper()) - ord('A')
    # It's at Ñ's position or past it
    return index + (1 if index > n_index else 0)


code = "VKXYKBKXGKSGWAKQQGYIUYGYWAKXKGQRKSZKJKYKKYIUSYKMAÑX"
offset = break_shift_cipher(code)
