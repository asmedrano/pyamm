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


class Csh(Note):
    def __init__(self):
        midi_notes = [1, 13, 25, 37, 49, 61, 73, 85, 97, 109, 121]
        Note.__init__(self, 'C#', midi_notes)


class D(Note):
    def __init__(self):
        midi_notes = [2, 14, 26, 38, 50, 62, 74, 86, 98, 110, 122]
        Note.__init__(self, 'D', midi_notes)


class Dsh(Note):
    def __init__(self):
        midi_notes = [3, 15, 27, 39, 51, 63, 75, 87, 99, 111, 123]
        Note.__init__(self, 'D#', midi_notes)


class E(Note):
    def __init__(self):
        midi_notes = [4, 16, 28, 40, 52, 64, 76, 88, 100, 112, 124]
        Note.__init__(self, 'E', midi_notes)


class F(Note):
    def __init__(self):
        midi_notes = [5, 17, 29, 41, 53, 65, 77, 89, 101, 113, 125]
        Note.__init__(self, 'F', midi_notes)


class Fsh(Note):
    def __init__(self):
        midi_notes = [6, 18, 30, 42, 54, 66, 78, 90, 102, 114, 126]
        Note.__init__(self, 'F#', midi_notes)


class G(Note):
    def __init__(self):
        midi_notes = [7, 19, 31, 43, 55, 67, 79, 91, 103, 115, 127]
        Note.__init__(self, 'G', midi_notes)


class Gsh(Note):
    def __init__(self):
        midi_notes = [8, 20, 32, 44, 56, 68, 80, 92, 104, 116, 128]
        Note.__init__(self, 'G#', midi_notes)


class A(Note):
    def __init__(self):
        midi_notes = [9, 21, 33, 45, 57, 69, 81, 93, 105, 117, 129]
        Note.__init__(self, 'A', midi_notes)


class Ash(Note):
    def __init__(self):
        midi_notes = [10, 22, 34, 46, 58, 70, 82, 94, 106, 118, 130]
        Note.__init__(self, 'A#', midi_notes)


class B(Note):
    def __init__(self):
        midi_notes = [11, 23, 35, 47, 59, 71, 83, 95, 107, 119, 131]
        Note.__init__(self, 'B', midi_notes)
