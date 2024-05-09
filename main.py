import math, queue
from collections import Counter

####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'), ('relev--ant','-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    # TO DO - modify to account for insertions, deletions and substitutions
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    else:
        if (S[0] == T[0]):
            return(MED(S[1:], T[1:]))
        else:
            return(1 + min(MED(S, T[1:]), MED(S[1:], T)))


def fast_MED(S, T, MED={}):
    if (S, T) in MED:
        return MED[(S, T)]
    if not S:
        return len(T)
    elif not T:
        return len(S)
    elif S[0] == T[0]:
        MED[(S, T)] = fast_MED(S[1:], T[1:], MED)
    else:
        MED[(S, T)] = 1 + min(fast_MED(S, T[1:], MED), fast_MED(S[1:], T, MED), fast_MED(S[1:], T[1:], MED))
    return MED[(S, T)]

def fast_align_MED(S, T, MED={}):
    if (S, T) in MED:
        return MED[(S, T)]
    if not S:
        return ('-' * len(T), T)
    elif not T:
        return (S, '-' * len(S))
    elif S[0] == T[0]:
        aligned_S, aligned_T = fast_align_MED(S[1:], T[1:], MED)
        MED[(S, T)] = (S[0] + aligned_S, T[0] + aligned_T)
    else:
        options = [
            (1 + fast_MED(S, T[1:], MED), '-' + T[0] + fast_align_MED(S, T[1:], MED)[1]),
            (1 + fast_MED(S[1:], T, MED), S[0] + '-' + fast_align_MED(S[1:], T, MED)[1]),
            (1 + fast_MED(S[1:], T[1:], MED), S[0] + T[0] + fast_align_MED(S[1:], T[1:], MED)[1])
        ]
        MED[(S, T)] = min(options, key=lambda x: x[0])
    return MED[(S, T)]

