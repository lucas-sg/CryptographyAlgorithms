import pytest
from src.shift_cipher import *


ENG_ALPH = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
SPA_ALPH = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"


# TODO: Test for English alphabet as well
@pytest.mark.parametrize(('c, index'), [('A', 0), ('Ñ', 14), ('Z', 26),
                                        ('a', 0), ('ñ', 14), ('z', 26)])
def test_char_index_spa(c, index):
    assert(char_index(c) == index)


# TODO: Test for English alphabet as well
@pytest.mark.parametrize(('c, offset, shifted'), [('A', 1, 'B'),
                                                  ('a', -1, 'Z'),
                                                  ('a', 27, 'A'),
                                                  ('A', 14, 'Ñ')])
def test_shift_char_spa(c, offset, shifted):
    assert(shift_char(c, offset) == shifted)


# TODO: Test for English alphabet as well
def test_shift_spa():
    assert(shift('hola', 14) == 'UCYÑ')
    assert(shift('hola', 27) == 'HOLA')
    assert(shift('hola', -1) == 'GÑKZ')


def test_calc_freqs():
    assert(calc_freqs('aacccdddde') == [0.2, 0.0, 0.3, 0.4, 0.1] + [0.0]*22)


def test_break_shift_cipher():
    code = 'VKXYKBKXGKSGWAKQQGYIUYGYWAKXKGQRKSZKJKYKKYIUSYKMAÑX'
    assert(break_shift_cipher(code) == 6)
