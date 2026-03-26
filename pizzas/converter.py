from pizzas.utilities import get_next_filename
from music21 import converter, meter, tempo
import os

def converter_():
    # Load recorded MIDI
    score = converter.parse('midfile.mid')

    score.insert(0, tempo.MetronomeMark(number=120))  # Set tempo
    score.insert(0, meter.TimeSignature('4/4'))  # Set time signature

    # Improve notation
    # score = score.makeMeasures()
    # score = score.makeTies()
    # score = score.makeBeams()
    score = score.quantize(quarterLengthDivisors=[1,2,4,8,16])

    # Export

    output_path = get_next_filename('recordings', '.xml')
    score.write('musicxml', output_path)
    absolute_path_of_score = f"{os.getcwd()}/{output_path}"

    score = converter.parse(absolute_path_of_score)
    print(score)
    print(f"Saved as {output_path}")