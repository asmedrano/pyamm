import random

OCTAVES = [1,2,3,4,5,6,7] # based on piano
MAJOR_SCALE=['I','ii','iii','IV','V','vi','vii']
ms = MAJOR_SCALE # save typing :D
# 1 1/2 1/4 1/8 1/16 Note types
# start with 1 Bar of 4/4 Time Sig
iterations = 100000
num_beats = 4
combos = []

def candidater():
    for i in range(iterations):
        #pick root notes
        root_notes = random.sample(ms, num_beats)
        # pick octave for each note
        candidate = map(lambda note: note + str(random.choice(OCTAVES)) , root_notes)
        if candidate not in combos:
            yield candidate

def main():
    for cand in candidater():
        combos.append(cand)

    print_results()


def print_results():
    print "Total Iterations: %s \n Potential combinations: %s" % (iterations, len(combos))
    # sort in some order
    combos.sort()
    for c in combos:
        print ",".join(c)

if __name__ == '__main__':
    main()
