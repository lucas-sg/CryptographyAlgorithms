import numpy as np
from math import gcd
from functools import reduce

from frequency_analysis import freq_analysis


ENG_ALPH = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
SPA_ALPH = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"


def calc_keys(c):
    key_lengths = calc_key_lengths(c)
    keys = []
    
    for key_length in key_lengths:
        k_cols = calc_k_cols_for_key_length(c, key_length)
#        keys.append([freq_analysis(col) for col in k_cols])
        
    return [shift_with_key(c, key) for key in keys]


def shift_with_key(s, k):    
    return "".join([shift_char(s[i], k[i%len(k)]) for i in range(len(s))])


def shift_char(c, offset):
    shifted_index = char_index(c) + offset    
    alph_index = shifted_index%len(SPA_ALPH)
    return SPA_ALPH[alph_index]


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
key_lengths = calc_key_lengths(C1)
print(key_lengths)
# print(shift_with_key("PARAQUELACOSANOME", [0,1,4,18]))
# print("PBVRQVICADSKAÑSDE")