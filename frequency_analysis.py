from itertools import permutations


ENG_ALPH = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
SPA_ALPH = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
# Arbitrary number of most frequent letters to orient a probable shift
# ['E','A','S','O','I','N','R','D','T','C','L','U','M','P','G','B','F','V']
MOST_FREQ_SPA = ['E','A','S']


def freq_analysis(s):
    most_frequent = flatten([p[0] for p in calc_freq_pairs(s)[:len(MOST_FREQ_SPA)]]) 
    offset = -1

    for permutation in permutations(most_frequent):
        if shift_matches(permutation):
            offset = char_index(permutation[0]) - char_index(MOST_FREQ_SPA[0])

    return offset


def shift_matches(permutation):
    if len(permutation) != len(MOST_FREQ_SPA):
        return False
    
    prev_offset = calc_offset_between(permutation[0], MOST_FREQ_SPA[0])

    for i in range(len(MOST_FREQ_SPA)):
        offset = calc_offset_between(permutation[i], MOST_FREQ_SPA[i])
        if offset != prev_offset:
            return False
        prev_offset = offset
        
    return True


def calc_offset_between(c1, c2):
    offset = char_index(c1) - char_index(c2)
    return offset + (len(SPA_ALPH) if offset < 0 else 0)


def calc_freq_pairs(s):
    freq_pairs = [[c,0] for c in SPA_ALPH]
    
    for c in s:
        freq_pairs[char_index(c)][1] += 1

    freq_pairs = sorted(freq_pairs, key=lambda pair: pair[1], reverse=True)
    return [[p[0], float(p[1])/len(s)] for p in freq_pairs]
        

def char_index(c):
    n_index = ord('N') - ord('A')
    
    if c.upper() == 'Ñ':
        return n_index + 1
    
    index = ord(c.upper()) - ord('A') 
    return index + (1 if index > n_index else 0) # It's at Ñ's position or past it


def flatten(list):
    return [y for x in list for y in x]


print(freq_analysis("VKXYKBKXGKSGWAKQQGYIUYGYWAKXKGQRKSZKJKYKKYIUSYKMAÑX"))
# print(shift_matches("FBTPJ"))
