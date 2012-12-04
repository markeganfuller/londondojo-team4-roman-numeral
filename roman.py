

CHARS = ['I','V','X','L','C','D','M']

def rank(roman_char):
    return CHARS.index(roman_char)


def prep_numeral(numeral):
    out = []
    n = 0
    while n < len(numeral):
        rank_of_current_char = rank(numeral[n])
        if n == (len(numeral) - 1):
            out.append(numeral[n])
        else:
            diff = rank(numeral[n]) - rank(numeral[n+1])
            assert diff >= -2, 'wtf???'
            if diff <= -1:
                out.extend([numeral[n]] * 4)
                n += 1
            if diff == -2:
                out.append(CHARS[rank_of_current_char+1])
            if diff >= 0:
                out.append(numeral[n])
        n += 1
    return out



def sort_numeral(numeral):
    return sorted(numeral, key=rank, reverse=True)
