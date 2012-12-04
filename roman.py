

CHARS = ['I','V','X','L','C','D','M']

def rank(roman_char):
    return CHARS.index(roman_char)


def normalize_roman_char():
    pass


def prep_numeral(numeral):
    out = []
    for n in range(len(numeral)-1):
        diff = rank(numeral[n]) - rank(numeral[n+1])
        assert rank >= -2, 'wtf???'
        if diff <= -1:
            out.extend([numeral[n]] * 4)
        if diff == -2:
            out.append(numeral[n+1])
        if diff >= 0:
            out.append(numeral[n])
    return out
