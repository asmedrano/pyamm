# Midi Notes and Numbers maps

class Note(object):

    def __init__(self, name, midi_notes):
        self.octaves = [0,1,2,3,4,5,6,7,8,9,10]
        self.name = name
        self.midi_map = dict(zip(self.octaves, midi_notes))

    def m_note(self, octave):
        """
        Returns midi note value
        Keywargs:
        octave -- int, the octave
        """
        if octave not in self.octaves:
            return ValueError('%s not supported' % str(octave))
        return self.midi_map[octave]


## Real notes begin here
class C(Note):
    def __init__(self):
        midi_notes = [0, 12, 24, 36, 48, 60, 72, 84, 96, 108, 120]
        Note.__init__(self, 'C', midi_notes)


