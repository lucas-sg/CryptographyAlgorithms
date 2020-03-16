import pytest
from src.shift_cipher import *


ENG_ALPH = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
SPA_ALPH = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"


# TODO: Test for English alphabet as well
def test_char_index_uppercase():
    assert(char_index('A') == 0)
    assert(char_index('Ñ') == 14)
    assert(char_index('Z') == 26)


def test_char_index_lowercase():
    assert(char_index('a') == 0)
    assert(char_index('ñ') == 14)
    assert(char_index('z') == 26)


def test_shift_char():
    assert(shift_char('A', 1) == 'B')
    assert(shift_char('A', -1) == 'Z')
    assert(shift_char('A', 27) == 'A')
    assert(shift_char('A', 14) == 'Ñ')


def test_shift():
    assert(shift('hola', 14) == 'UCYÑ')
    assert(shift('hola', 27) == 'HOLA')
    assert(shift('hola', -1) == 'GÑKZ')


def test_calc_freqs():
    assert(calc_freqs('aacccdddde') == [0.2, 0.0, 0.3, 0.4, 0.1] + [0.0]*22)
    

def test_break_shift_cipher():
    code = 'VKXYKBKXGKSGWAKQQGYIUYGYWAKXKGQRKSZKJKYKKYIUSYKMAÑX'
    assert(break_shift_cipher(code) == 6)
