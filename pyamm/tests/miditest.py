############################################################################
# A sample program to create a single-track MIDI file, add a note,
# and write to disk.
############################################################################

#Import the library
from pyamm.midiutil.MidiFile import MIDIFile

# Create the MIDIFile Object
MyMIDI = MIDIFile(1)

# Add track name and tempo. The first argument to addTrackName and
# addTempo is the time to write the event.
track = 0
time=0
MyMIDI.addTrackName(track, time, "Sample Track")
MyMIDI.addTempo(track, time, 160)
channel = 0
volume = 100
notes = [4, 2, 1, .5, .25, .125]
#notes = [4,2]
#notes = [2,2]
#notes = [1,1]
time=0
pitch = 60

# Each note is a bar in this scenario
for i in range(len(notes)):
    # we need to do something per note in notes list
    note = notes[i]
    print "-----------------------------------------"
    print 'note: ',note
    print "-----------------------------------------"
    notes_per_bar = int(4/note) # how many of this note type it takes to make 1 whole note
    duration = note
    if i == 0: # we need to check if this is the first note in the timeline
        for n in range(notes_per_bar):
            fill_notes = note
            if n == 0:
                MyMIDI.addNote(track, channel, pitch, time, duration, volume)
                time += duration
                print time
            else:
                time += fill_notes
                MyMIDI.addNote(track, channel, pitch, time, duration, volume)

    else:
        for n in range(notes_per_bar):
            fill_notes = note
            if n !=0:
                time += fill_notes
            print 'time: ' , time
            MyMIDI.addNote(track, channel, pitch, time, duration, volume)

#for i in range(1): # 1 bar
    # Add a note. addNote expects the following information:
#    pitch = 60 + i # step up
    #duration = TIME_SIG[1]/TIME_SIG[1] # quarter note  or 1
    #duration = 0.125
    #time = i # when the note happens should be sequential
    # Now add the note.
    #MyMIDI.addNote(track, channel, pitch, time, duration, volume)

# And write it to disk.

binfile = open("output.mid", 'wb')
MyMIDI.writeFile(binfile)
binfile.close()
