# FSCZPNRXIUuieanpzcsf
KEYS = (
    'F-', 'S-', 'C-', 'Z-', 'P-', 'N-', 'R-', 'X-', 'I-', 'U-',
    '-u', '-i', '-e', '-a', '-n', '-p', '-z', '-c', '-s', '-f',
)

IMPLICIT_HYPHEN_KEYS = KEYS

SUFFIX_KEYS = ()

NUMBER_KEY = None

NUMBERS = {}

UNDO_STROKE_STENO = 'U'

ORTHOGRAPHY_RULES = []

ORTHOGRAPHY_RULES_ALIASES = {}

ORTHOGRAPHY_WORDLIST = None

KEYMAPS = {
    'Michela Keyboard (MIDI, 2 octaves)': {
        'F-': 'C2',
        'S-': 'C#2',
        'C-': 'D2',
        'Z-': 'D#2',
        'P-': 'E2',
        'N-': 'F2',
        'R-': 'F#2',
        'X-': 'G2',
        'I-': 'G#2',
        'U-': 'A2',
        '-u': 'D#3',
        '-i': 'E3',
        '-e': 'F3',
        '-a': 'F#3',
        '-n': 'G3',
        '-p': 'G#3',
        '-z': 'A3',
        '-c': 'A#3',
        '-s': 'B3',
        '-f': 'C4',
    },
    "Michela Keyboard (MIDI, 3+ octaves)": {
        'F-': 'D#2',
        'S-': 'E2',
        'C-': 'F2',
        'Z-': 'F#2',
        'P-': 'G2',
        'N-': 'G#2',
        'R-': 'A2',
        'X-': 'A#2',
        'I-': 'B2',
        'U-': 'C3',
        '-u': 'E3',
        '-i': 'F3',
        '-e': 'F#3',
        '-a': 'G3',
        '-n': 'G#3',
        '-p': 'A3',
        '-z': 'A#3',
        '-c': 'B3',
        '-s': 'C4',
        '-f': 'C#4',
    },
    'Keyboard': {
        'F-': 'q',
        'S-': 'a',
        'C-': 's',
        'Z-': 'w',
        'P-': 'd',
        'N-': 'e',
        'R-': 'f',
        'X-': 'r',
        'I-': 'c',
        'U-': 'v',
        '-u': 'n',
        '-i': 'm',
        '-e': 'u',
        '-a': 'j',
        '-n': 'i',
        '-p': 'k',
        '-z': 'o',
        '-c': 'l',
        '-s': ';',
        '-f': 'p',
        'arpeggiate': 'space',
        # Suppress adjacent keys to prevent miss-strokes.
        'no-op': ('z', 'x', 'b', ',', '.', '/', '[', '\''),
    },
}

DICTIONARIES_ROOT = 'asset:plover_michela:assets'

DEFAULT_DICTIONARIES = (
    'michela_utente.json',
    'michela_punteggiaturacomandi.json',
    'michela_numeri.json',
    'michela_sillabico.json',
    'michela_principale.json',
)
