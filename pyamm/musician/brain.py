# stuff that happens in the musicians brain
import random
from pyamm.theory import roman

def ideate(num_chords, scale='maj', limit=None, stout=False):
    """
    Returns a list of potential chord/Note combinations
    Keywargs:
        num_chords -- How many chords to string together
        scale -- 'maj' or 'min' Defaul maj
        limit -- amount of ideas to return
        stout -- print to stout?
    """
    if scale == 'maj':
        degree = roman.MAJOR_SCALE
    elif scale == 'min':
        degree = roman.MINOR_SCALE
    else:
        raise ValueError('%s not supported' % scale)

    iterations = 10000
    combos = []

    for cand in _candidater(num_chords, combos, iterations, degree):
        combos.append(cand)

    if limit:
        combos = random.sample(combos, limit)

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
