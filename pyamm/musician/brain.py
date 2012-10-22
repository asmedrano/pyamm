# stuff that happens in the musicians brain
import random
from pyamm.musician.theory import *

def ideate(num_chords, scale='maj', stout=False):
    """
    Returns a list of potential chord/Note combinations
    Keywargs:
        num_chords -- How many chords to string together
        scale -- 'maj' or 'min' Defaul maj
        stout -- print to stout?
    """
    if scale == 'maj':
        degree = MAJOR_SCALE
    elif scale == 'min':
        degree = MINOR_SCALE
    else:
        raise ValueError('%s not supported' % scale)

    iterations = 10000
    combos = []

    for cand in _candidater(num_chords, combos, iterations, degree):
        combos.append(cand)

    if stout:
        _print_results(combos)

    return combos

def _candidater(num_chords, combos, iterations, degree):
    for i in range(iterations):
        #pick root notes
        candidate = random.sample(degree, num_chords)
        if candidate not in combos:
            yield candidate

def _print_results(combos):
    print "Potential combinations: %s" % (len(combos))
    # sort in some order
    combos.sort()
    for c in combos:
        print ",".join(c)
