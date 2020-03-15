import numpy as np
from math import gcd
from functools import reduce

from shift_cipher import break_shift_cipher, shift, shift_char


ENG_ALPH = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
SPA_ALPH = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"


def kasiski_decipher(s):
    for keys in calc_keys(s):
        m = [shift_char(s[i], -keys[i%len(keys)]) for i in range(len(s))]
        print('\n' + str(keys) + ': ' + ''.join(m))


def calc_keys(s):
    possible_keys = []
    for key_length in calc_key_lengths(s):
        k_cols = calc_k_cols_for_key_length(s, key_length)
        possible_keys.append([break_shift_cipher(col) for col in k_cols])
    return possible_keys


def calc_k_cols_for_key_length(s, key_length):
    groupings = [s[i:i+key_length] for i in range(0, len(s), key_length)]
    k_cols = [[row[i] for row in groupings] for i in range(key_length)]
    return ["".join(s) for s in k_cols]


def calc_key_lengths(s):
    lengths = []
    
    for seq_len in np.arange(3, len(s)):
        seq_pairs = [seq_offset_pair(s, i, seq_len) for i in np.arange(0, len(s)-seq_len)]
        all_offsets = flatten([pair[1] for pair in seq_pairs if pair[1]])
        
        if all_offsets:
            lengths.append(mcd(all_offsets))
        
    return lengths
        

def seq_offset_pair(s, i, seq_len):
    sequence = s[i:i+seq_len]
    offsets = offsets_between_repetitions(s, sequence)
    return [sequence, offsets]


# Example:   aasdfkjXXXksajkljXXXooieruXXXppperXXX  should return 3 ints for XXX
# And something such as:   wiulnsXXXuioop   should return an empty list
def offsets_between_repetitions(s, subs):
    if s.count(subs) <= 1:
        return []
    
    inter_strings = (s.split(subs))[1:]
    offsets = [len(inter_s) + len(subs) for inter_s in inter_strings]
    
    if not s.endswith(subs):
        offsets.pop()

    return offsets


def mcd(list):
    return reduce(gcd, list)


def flatten(list):
    return [y for x in list for y in x]


C1 = "PBVRQVICADSKAÑSDETSJPSIEDBGGMPSLRPWRÑPWYEDSDEÑDRDPCRCPQMNPWKUBZVSFNVRDMTIPWUEQVVCBOVNUEDIFQLONMWNUVRSEIKAZYEACEYEDSETFPHLBHGUÑESOMEHLBXVAEEPUÑELISEVEFWHUNMCLPQPMBRRNBPVIÑMTIBVVEÑIDANSJAMTJOKMDODSELPWIUFOZMQMVNFOHASESRJWRSFQCOTWVMBJGRPWVSUEXINQRSJEUEMGGRBDGNNILAGSJIDSVSUEEINTGRUEETFGGMPORDFOGTSSTOSEQOÑTGRRYVLPWJIFWXOTGGRPQRRJSKETXRNBLZETGGNEMUOTXJATORVJHRSFHVNUEJIBCHASEHEUEUOTIEFFGYATGGMPIKTBWUEÑENIEEU"
C2 = "JGAZNWINHYLZDYVBBJLCQHTNKUDQXMOXJNOZMUSPNONYJMTEJHQHQFOOPUPBCYAÑJONCNNQHNMONDHKUTJMQCMOPNFAOXNTNLOAZMJDQYMOZCJRNBAOQTUIENFAIXTLXJGAZMJAXJVAZMUDNMYLNLJMUMUYHVUMHTÑIGDXDQUCLSJPIBCUSFNUGXXGEEXKAEJMESJÑENASLHLBAEYJROJXACQTCNMYPUCUNMJWOYNHZNKUOGAJDUJXENRYTENJSCNMONTYJNMJYFXFIGJMIBUUSNTFAPNFAFKUROJNYCTUYNBYSGJVACAUCGQWAZMJJHJHSNTPAPXMGNECOGJUTENCNGJGEGAJSPNULGDMAÑJDOFDNPUNNPNTGENMJSNTTOFDKIOXSSQNNFBATOCXMMNVÑEZNMEZBOSNTUSQBUDBTJRBBUYPQZIOQFTBANIBVMEDDYRUMUPNAULBOMAEDHVHNFOCJOSNMJ"
# key_lengths = calc_key_lengths(C1)
# print(key_lengths)
# print(shift_with_key("PARAQUELACOSANOME", [0,1,4,18]))
kasiski_decipher(C1)
