#  Anyting related to time in music
class TimeSignature(object):
    """
    Represents Time signatures
    Keywargs:
        beats -- how many beats in bar
        count -- What we are counting in  (4, 2 ,1, .5, .25)

        For reference:
            4 = whole note
            2 = halfnote
            1 = quater note
            .5 or 1/2 = eighth note
            .25 or 1/4 = sixteenth

    """
    def __init__(self, beats, count):

        valid_counts = [4, 2, 1, .5, .25]
        self.beats = beats
        self.count = count
        # lets check for a valid count
        if count not in valid_counts:
            raise ValueError('%s is not a valid count' % count)

        # if we dived beats/counts we get the type of note we can use
        self.note_type = beats/count
        print self.note_type

    def __str__(self):
        return '%s/%s' % (self.beats, self.count)
