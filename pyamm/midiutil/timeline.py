from pyamm.midiutil.MidiFile import MIDIFile

class MidiTimeline(object):
    """
        Represents a midi timeline
        BPM basicly just means Quarter notes per mininute
    """
    def __init__(self, midi_track_name, tempo=160):
        self.time = 0 # keeps track of where the timeline is.
        self.midifile = MIDIFile(1)
        self.track = 0
        self.channel = 0
        self.midifile.addTrackName(self.track, self.time, midi_track_name)
        self.midifile.addTempo(self.track, self.time, 160)
        self.notes = []

    def add_note(self, note, pitch=60, volume=100):
        """ add a note to the timeline
            valid notes are 4, 2, 1, .5, .25, .125
            start_time is deterimined by self.time
            duration is deterimined by note type
        """
        duration = note
        self.midifile.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.notes.append(note)
        # move the timeline along based on duration
        self.time += duration

    def export_midi_file(self, file_name):
        binfile = open(file_name, 'wb')
        self.midifile.writeFile(binfile)
        binfile.close()

