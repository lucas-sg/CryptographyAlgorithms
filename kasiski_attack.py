import numpy as np
from math import gcd
from functools import reduce

from shift_cipher import break_shift_cipher, shift, shift_char


ENG_ALPH = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
SPA_ALPH = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"


def kasiski_decipher(s):
    for keys in calc_keys(s):
        msg = [shift_char(s[i], -keys[i % len(keys)]) for i in range(len(s))]
        print('\n' + str(keys) + ': ' + ''.join(msg))


def calc_keys(s):
    keys = []
    for key_length in calc_key_lengths(s):
        k_cols = calc_k_cols_for_key_length(s, key_length)
        possible_keys = [break_shift_cipher(col.rstrip()) for col in k_cols]
        keys.append(possible_keys)
    return keys


def calc_k_cols_for_key_length(s, key_length):
    n_grams = calc_n_grams(s, key_length)
    k_cols = [[row[i] for row in n_grams] for i in range(key_length)]
    return [''.join(s) for s in k_cols]


def calc_n_grams(s, n):
    rmdr = len(s) % n
    mult = len(s)-rmdr    # Multiple of n
    n_grams = [s[i:i+n] for i in range(0, mult, n)]
    add_padding(s, rmdr, n_grams, n)
    return n_grams


def add_padding(s, rmdr, n_grams, n):
    tail = s[:rmdr]
    if tail:
        n_grams.append((tail).ljust(len(tail)+n-rmdr))
    return


def calc_key_lengths(s):
    lengths = []
    for n in np.arange(3, int(len(s)/2)):
        all_offsets = offsets_for_n_grams(s, n)
        if all_offsets:
            mcd = reduce(gcd, all_offsets)
            if mcd > 1:
                lengths.append(mcd)
    return lengths


def offsets_for_n_grams(s, n):
    seen_n_grams = []
    all_offsets = []
    for i in np.arange(0, len(s)-n):
        n_gram = s[i:i+n]
        if n_gram not in seen_n_grams:
            all_offsets.append(offsets_between_repetitions(s, n_gram))
        seen_n_grams.append(n_gram)
    return flatten([offsets for offsets in all_offsets if offsets])


# Example:  aasdfkjXXXksajkljXXXooieruXXXppperXXX  should return 3 ints for XXX
# And something such as:   wiulnsXXXuioop   should return an empty list
def offsets_between_repetitions(s, subs):
    if s.count(subs) <= 1:
        return []
    inter_strings = (s.split(subs))[1:]
    offsets = [len(inter_s) + len(subs) for inter_s in inter_strings]
    if not s.endswith(subs):
        offsets.pop()
    return offsets


def flatten(list):
    return [y for x in list for y in x]


C1 = "PBVRQVICADSKAÑSDETSJPSIEDBGGMPSLRPWRÑPWYEDSDEÑDRDPCRCPQMNPWKUBZVSFNVRDMTIPWUEQVVCBOVNUEDIFQLONMWNUVRSEIKAZYEACEYEDSETFPHLBHGUÑESOMEHLBXVAEEPUÑELISEVEFWHUNMCLPQPMBRRNBPVIÑMTIBVVEÑIDANSJAMTJOKMDODSELPWIUFOZMQMVNFOHASESRJWRSFQCOTWVMBJGRPWVSUEXINQRSJEUEMGGRBDGNNILAGSJIDSVSUEEINTGRUEETFGGMPORDFOGTSSTOSEQOÑTGRRYVLPWJIFWXOTGGRPQRRJSKETXRNBLZETGGNEMUOTXJATORVJHRSFHVNUEJIBCHASEHEUEUOTIEFFGYATGGMPIKTBWUEÑENIEEU"
C2 = "JGAZNWINHYLZDYVBBJLCQHTNKUDQXMOXJNOZMUSPNONYJMTEJHQHQFOOPUPBCYAÑJONCNNQHNMONDHKUTJMQCMOPNFAOXNTNLOAZMJDQYMOZCJRNBAOQTUIENFAIXTLXJGAZMJAXJVAZMUDNMYLNLJMUMUYHVUMHTÑIGDXDQUCLSJPIBCUSFNUGXXGEEXKAEJMESJÑENASLHLBAEYJROJXACQTCNMYPUCUNMJWOYNHZNKUOGAJDUJXENRYTENJSCNMONTYJNMJYFXFIGJMIBUUSNTFAPNFAFKUROJNYCTUYNBYSGJVACAUCGQWAZMJJHJHSNTPAPXMGNECOGJUTENCNGJGEGAJSPNULGDMAÑJDOFDNPUNNPNTGENMJSNTTOFDKIOXSSQNNFBATOCXMMNVÑEZNMEZBOSNTUSQBUDBTJRBBUYPQZIOQFTBANIBVMEDDYRUMUPNAULBOMAEDHVHNFOCJOSNMJ"
kasiski_decipher(C1)
