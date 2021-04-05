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

ORTHOGRAPHY_RULES = [
    (r'^(.*). \^ cela$', r'\1cela'),
    (r'^(.*). \^ cele$', r'\1cele'),
    (r'^(.*). \^ celi$', r'\1celi'),
    (r'^(.*). \^ celo$', r'\1celo'),

    (r'^(.*). \^ cene$', r'\1cene'),

    (r'^(.*). \^ ci$', r'\1ci'),

    (r'^(.*). \^ dola$', r'\1dola'),
    (r'^(.*). \^ dole$', r'\1dole'),
    (r'^(.*). \^ doli$', r'\1doli'),
    (r'^(.*). \^ dolo$', r'\1dolo'),

    (r'^(.*). \^ done$', r'\1done'),

    (r'^(.*). \^ gli$', r'\1gli'),

    (r'^(.*). \^ la$', r'\1la'),
    (r'^(.*). \^ le$', r'\1le'),
    (r'^(.*). \^ li$', r'\1li'),
    (r'^(.*). \^ lo$', r'\1lo'),

    (r'^(.*). \^ mela$', r'\1mela'),
    (r'^(.*). \^ mele$', r'\1mele'),
    (r'^(.*). \^ meli$', r'\1meli'),
    (r'^(.*). \^ melo$', r'\1melo'),

    (r'^(.*). \^ mene$', r'\1mene'),
    (r'^(.*). \^ mente$', r'\1mente'),
    (r'^(.*). \^ mente$', r'\1amente'),

    (r'^(.*). \^ mi$', r'\1mi'),

    (r'^(.*). \^ ne$', r'\1ne'),

    (r'^(.*). \^ sela$', r'\1sela'),
    (r'^(.*). \^ sele$', r'\1sele'),
    (r'^(.*). \^ seli$', r'\1seli'),
    (r'^(.*). \^ selo$', r'\1selo'),

    (r'^(.*). \^ si$', r'\1si'),

    (r'^(.*). \^ tela$', r'\1tela'),
    (r'^(.*). \^ tele$', r'\1tele'),
    (r'^(.*). \^ teli$', r'\1teli'),
    (r'^(.*). \^ telo$', r'\1telo'),

    (r'^(.*). \^ ti$', r'\1ti'),

    (r'^(.*). \^ vela$', r'\1vela'),
    (r'^(.*). \^ vele$', r'\1vele'),
    (r'^(.*). \^ veli$', r'\1veli'),
    (r'^(.*). \^ velo$', r'\1velo'),

    (r'^(.*). \^ vi$', r'\1vi'),

    (r'^(.*). \^ issima$', r'\1issima'),
    (r'^(.*). \^ issime$', r'\1issime'),
    (r'^(.*). \^ issimi$', r'\1issimi'),
    (r'^(.*). \^ issimo$', r'\1issimo'),

    (r'^(.*). \^ i$', r'\1i'),
]

ORTHOGRAPHY_RULES_ALIASES = {}

ORTHOGRAPHY_WORDLIST = 'italian_words.txt'

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
