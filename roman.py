

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


def compress_numeral(numeral):
    numeral = ''.join(numeral)
    while True:
        l = len(numeral)

        numeral = numeral.replace('CCCCC', 'D')
        numeral = numeral.replace('XXXXX', 'L')
        numeral = numeral.replace('IIIII', 'V')

        numeral = numeral.replace('CCCC', 'CD')
        numeral = numeral.replace('IIII', 'IV')
        numeral = numeral.replace('XXXX', 'XL')

        numeral = numeral.replace('DD', 'M')
        numeral = numeral.replace('LL', 'C')
        numeral = numeral.replace('VV', 'X')

        if len(numeral) == l:
            return numeral



def add_numeral(n1, n2):
    n1 = prep_numeral(n1)
    n2 = prep_numeral(n2)

    combined = n1 + n2
    sorted_ = sort_numeral(combined)
    out = compress_numeral(sorted_)
    return out


if __name__ == '__main__':
    import sys
    n1, n2 = sys.argv[1:]
    print 'in:', n1, n2
    print 'out', add_numeral(n1, n2)
