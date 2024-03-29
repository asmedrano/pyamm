"""
Run tests like so:
    python -m unittest discover
Make sure its from the main module directory!
SEE: http://docs.python.org/library/unittest.html#test-discovery
"""
from unittest import TestCase, main
from pyamm.midi import notes

class MidiTest(TestCase):

    def test_midi_note(self):
        c = notes.C()
        self.assertEqual(c.m_note(1), 12)


if __name__ == '__main__':
    main()
