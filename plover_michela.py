# vim: set fileencoding=utf-8 :

# #SPCTHVRIAEOcsthpr*ieao
KEYS = (
    'F-', 'S-', 'C-', 'Z-', 'P-', 'N-', 'R-', 'X-', 'I-', 'U-',
    '-u', '-i', '-e', '-a', '-n', '-p', '-z', '-c', '-s', '-f',
)

IMPLICIT_HYPHEN_KEYS = KEYS

SUFFIX_KEYS = ()

NUMBER_KEY = None

NUMBERS = {}

UNDO_STROKE_STENO = 'X'

ORTHOGRAPHY_RULES = []

ORTHOGRAPHY_RULES_ALIASES = {}

ORTHOGRAPHY_WORDLIST = None

KEYMAPS = {
    'Michela Keyboard': {
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

DICTIONARIES_ROOT = 'asset:plover:assets'
DEFAULT_DICTIONARIES = ()
