import rtmidi
import mido
from mido import MidiFile, MidiTrack, Message
import music21
import time
import os





def get_input():

    score = music21.stream.Stream()
    
    active_notes = {}

    start_time = time.time()

    instruments = mido.get_input_names() #get the names of the midi instruments in an list

    # Create MIDI file + track
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)

    port_name = instruments[0]

    last_time = time.time()

    try:
        print(f"Listening ... Press Ctrl+C to stop.")
        with mido.open_input(port_name) as inport:
            for msg in inport:
                now = time.time()
                delta = now - last_time
                last_time = now

                # Convert seconds → MIDI ticks
                ticks = int(mido.second2tick(delta, mid.ticks_per_beat, 500000))

                msg.time = ticks
                track.append(msg)

                print(msg)

    except KeyboardInterrupt:
        print("\nRecording stopped.")

    # Save file
    mid.save('midfile.mid')
    print(f"Saved recording to {'midfile'}")


