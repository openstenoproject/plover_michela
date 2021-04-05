from plover_midi.machine import MidiStenotype


class MichelaKeyboardMidi2(MidiStenotype):

    '''
    Michela on a 2 octaves MIDI keyboard
    '''

    KEYS_LAYOUT = '''
    C2   D#2  F2  G2          F3  G3  A3     C4
    C#2 D2 E2 F#2 G#2 A2  D#3 E3 F#3 G#3 A#3 B3
    '''


class MichelaKeyboardMidi3p(MidiStenotype):

    '''
    Michela on a 3+ octaves MIDI keyboard
    '''

    KEYS_LAYOUT = '''
    D#2   F#2 G#2 A#2      F#3 G#3 A#3   C#4
    E2  F2  G2 A2 B2 C3  E3 F3 G3 A3  B3  C4
    '''
