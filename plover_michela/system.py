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
    # == +cela, +cele, +celi, +celo ==
    #: fare + cela = farcela
    #: portare + cele = portarcele
    #: vedere + celi = vederceli
    #: sentire + celo = sentircelo
    #: comporre + cela = comporcela
    #: produrre + cele = producele
    #: sottrarre + celi = sottrarceli
    #: sottoporre + celo = sottoporcelo
    #: scrivete + cel[aeio] = scrivetecel[aeio]
    #: indicato + cel[aeio] = indicatecel[aeio]
    (r'^(.*[aeiou])r?re \^ cel([aeio])$', r'\1rcel\2'),
    (r'^(.*). \^ cel([aeio])$', r'\1ecel\2'),

    # == +cene ==
    #: fare + cene = farcene
    #: liberare + cene = liberarcene
    #: produrre + cene = produrcene
    #: portato + cene = portatecene
    #: scrivete + cene = scrivetecene
    (r'^(.*[aeiou])r?re \^ cene$', r'\1rcene'),
    (r'^(.*). \^ cene$', r'\1ecene'),

    # == +ci ==
    #: fare + ci = farci
    #: credere + ci = crederci
    #: indurre + ci = indurci
    (r'^(.*[aeiou])r?re \^ ci$', r'\1rci'),

    # == +esco ==
    #: mano + esco = manesco
    #: libro + esco = libresco
    #: arabo + esco = arabesco
    (r'^(.*). \^ esco$', r'\1esco'),

    # == +esimo ==
    #: undici + esimo = undicesimo
    #: diciasette + esimo = diciasettesimo
    #: ventitré + esimo = ventitreesimo
    #: monaco + esimo = monachesimo
    (r'^(.*[aeiou])tré \^ esimo$', r'\1treesimo'),
    (r'^(.*[aeiou])co \^ esimo$', r'\1chesimo'),
    (r'^(.*). \^ esimo$', r'\1esimo'),

    # == +ismo ==
    #: abolizione + ismo = abolizionismo
    #: abusivo + ismo = abusivismo
    #: centro + ismo = centrismo
    (r'^(.*). \^ ismo$', r'\1ismo'),

    # == +ità ==
    #: vasto + ità = vastità
    #: utile + ità = utilità
    #: unico + ità = unicità
    (r'^(.*). \^ ità$', r'\1ità'),

    # == +età ==
    #: vario + età = varietà
    #: socio + età = società
    #: sobrio + età = sobrietà
    (r'^(.*). \^ età$', r'\1età'),

    # == +gli ==
    #: dire + gli = dirgli
    #: proporre + gli = proporgli
    (r'^(.*[aeiou])r?re \^ gli$', r'\1rgli'),

    # == +gliela, +gliele, +glieli, +glielo ==
    #: fare + gliela = fargliela
    #: portare + gliele = portargliele
    #: vedere + glieli = vederglieli
    #: sentire + glielo = sentirglielo
    #: tradurre + gliela = tradurgliela
    #: estrarre + gliele = estrargliele
    #: sottrarre + glieli = sottrarglieli
    #: sottoporre + glielo = sottoporglielo
    #: scrivete + gliel[aeio] = scrivetegliel[aeio]
    #: indicato + gliel[aeio] = indicategliel[aeio]
    (r'^(.*[aeiou])r?re \^ gliel([aeio])$', r'\1rgliel\2'),
    (r'^(.*). \^ gliel([aeio])$', r'\1egliel\2'),

    # == +gliene ==
    #: fare + gliene = fargliene
    #: portare + gliene = portargliene
    #: sottoporre + gliene = sottoporgliene
    (r'^(.*[aeiou])r?re \^ gliene$', r'\1rgliene'),
    (r'^(.*). \^ gliene$', r'\1egliene'),

    # == +issima, +issime, +issimi, +issimo,==
    #: felice + issim[aeio] = felicissim[aeio]
    #: secco + issim[aeio] = secchissim[aeio]
    #: abile + issim[aeio] = abilissim[aeio]
    (r'^(.*[aeiou])cco \^ issim([aeio])$', r'\1cchissim\2'),
    (r'^(.*). \^ issim([aeio])$', r'\1issim\2'),

    # == +la, +le, +li, +lo ==
    #: dire + la = dirla
    #: fare + le = farle
    #: cambiare + li = cambiarli
    #: vedere + lo = vederlo
    #: proporre + la = proporla
    #: condurre + le = condurle
    #: indurre + li = indurli
    #: ridurre + lo = ridurlo
    (r'^(.*[aeiou])r?re \^ l([aeio])$', r'\1rl\2'),

    # == +mela, +mele, +meli, +melo ==
    #: fare + mela = farmela
    #: portare + mele = portarmele
    #: vedere + meli = vedermeli
    #: sentire + melo = sentirmelo
    #: tradurre + mela = tradurmela
    #: estrarre + mele = estrarmele
    #: sottrarre + meli = sottrarmeli
    #: sottoporre + melo = sottopormelo
    #: scrivete + mel[aeio] = scrivetemel[aeio]
    #: indicato + mel[aeio] = indicatemel[aeio]
    (r'^(.*[aeiou])r?re \^ mel([aeio])$', r'\1rmel\2'),
    (r'^(.*). \^ mel([eio])$', r'\1emel\2'),

    # == +mene ==
    #: fare + mene = farmene
    #: liberare + mene = liberarmene
    #: estrarre + mene = estrarmene
    #: scrivete + mene = scrivetemene
    #: indicato + mene = indicatemene
    (r'^(.*[aeiou])r?re \^ mene$', r'\1rmene'),
    (r'^(.*). \^ mene$', r'\1emene'),

    # == +mente ==
    #: abile + mente = abilmente
    #: folle + mente = follemente
    #: familiare + mente = familiarmente
    #: puro + mente = puramente
    #: retto + mente = rettamente
    #: espresso + mente = espressamente
    #: distinto + mente = distintamente
    (r'^(.*[aeiou])l?le \^ mente$', r'\1lmente'),
    (r'^(.*[aeiou])re \^ mente$', r'\1rmente'),
    (r'^(.*[aeiou])ro \^ mente$', r'\1ramente'),
    (r'^(.*[aeiou])tto \^ mente$', r'\1tamente'),
    (r'^(.*[aeiou])sso \^ mente$', r'\1ssamente'),
    (r'^(.*[aeiou])nto \^ mente$', r'\1ntamente'),

    # == +mi ==
    #: fare + mi = farmi
    #: sentire + mi = sentirmi
    #: indurre + mi = indurmi
    (r'^(.*[aeiou])r?re \^ mi$', r'\1rmi'),

    # == +ne ==
    #: sentire + ne = sentirne
    #: ridurre + ne = ridurne
    (r'^(.*[aeiou])r?re \^ ne$', r'\1rne'),

    # == +sela, +sele, +seli, +selo ==
    #: fare + sela = farsela
    #: portare + sele = portarsele
    #: vedere + seli = vederseli
    #: sentire + selo = sentirselo
    #: detrarre + sela = detrarsela
    #: estrarre + sele = estrarsele
    #: comporre + seli = comporseli
    #: tradurre + selo = tradurselo
    (r'^(.*[aeiou])r?re \^ sel([aeio])$', r'\1rsel\2'),

    # == +si ==
    #: dire + si = dirsi
    #: sentire + si = sentirsi
    #: porre + si = porsi
    (r'^(.*[aeiou])r?re \^ si$', r'\1rsi'),

    #== +teci ==
    #: portato + teci = portateci
    #: scrivete + teci = scriveteci
    (r'^(.*[aeiou])t[oe] \^ teci$', r'\1teci'),

    # == +tegli ==
    #: convertito + tegli = convertitegli
    #: scrivete + tegli = scrivetegli
    (r'^(.*[aeiou])t[oe] \^ tegli$', r'\1tegli'),

    # == +tela, +tele, +teli, +telo ==
    #: cambiare + tela = cambiartela
    #: portare + tele = portartele
    #: vedere + teli = vederteli
    #: sentire + telo = sentirtelo
    #: estrarre + tela = estrartela
    #: detrarre + tele = detrartele
    #: scomporre + teli = scomporteli
    #: produrre + telo = produrtelo
    (r'^(.*[aeiou])r?re \^ tel([aeio])$', r'\1rtel\2'),

    #== +temi ==
    #: convertito + temi = convertitemi
    #: scrivete + temi = scrivetemi
    (r'^(.*[aeiou])t[oe] \^ temi$', r'\1temi'),

    #== +tevi ==
    #: convertito + tevi = convertitevi
    #: scrivete + tevi = scrivetevi
    (r'^(.*[aeiou])t[oe] \^ tevi$', r'\1tevi'),

    # == +ti ==
    #: dire + ti = dirti
    #: sentire + ti = sentirti
    #: porre + ti = porti
    (r'^(.*[aeiou])r?re \^ ti$', r'\1rti'),

    # == +vela, +vele, +veli, +velo ==
    #: cambiare + vela = cambiarvela
    #: portare + vele = portarvele
    #: vedere + veli = vederveli
    #: sentire + velo = sentirvelo
    #: estrarre + vela = estrarvela
    #: comporre + vele = comporvele
    #: tradurre + veli = tradurveli
    #: produrre + velo = produrvelo
    #: portato + vela = portatevela
    #: scrivete + vela = scrivetevela
    #: portato + vele = portatevele
    #: scrivete + vele = scrivetevele
    #: portato + veli = portateveli
    #: scrivete + veli = scriveteveli
    #: portato + velo = portatevelo
    #: scrivete + velo = scrivetevelo
    (r'^(.*[aeiou])r?re \^ vel([aeio])$', r'\1rvel\2'),
    (r'^(.*). \^ vel([aeio])$', r'\1evel\2'),

    # == +vene ==
    #: fare + vene = farvene
    #: liberare + vene = liberarvene
    #: estrarre + vene = estrarvene
    #: scrivete + vene = scrivetevene
    #: indicato + vene = indicatevene
    (r'^(.*[aeiou])r?re \^ vene$', r'\1rvene'),
    (r'^(.*). \^ vene$', r'\1evene'),

    # == +vi ==
    #: dire + vi = dirvi
    #: sentire + vi = sentirvi
    #: apporre + vi = apporvi
    (r'^(.*[aeiou])r?re \^ vi$', r'\1rvi'),

    # == +zata +zate +zati +zato ==
    #: parziale + zat[aeio] = parzializzat[aeio]
    #: disavanzo + zat[aeio] = disavanzat[aeio]
    #: battezzo + izzat[aeio] = battezzat[aeio]
    (r'^(.*[aeiou])zzo \^ zat([aeio])$', r'\1zzat\2'),
    (r'^(.*[ln])zo \^ zat([aeio])$', r'\1zat\2'),
    (r'^(.*). \^ zat([aeio])$', r'\1izzat\2'),

    # == +a, +e, +i, +o,==
    # these suffixes are used to change the gender and the number of words
    #: vivo + a = viva
    #: contratto + e = contratte
    #: legame + i = legami
    #: chiede + o = chiedo
    #: secco + [ei] = secch[ei]
    #: reco + i = rechi
    #: legge + i = leggi
    #: lego + [ei] = legh[ei]
    (r'^(.*[aeiou])co \^ e$', r'\1che'),
    (r'^(.*[aeiou])gge \^ e$', r'\1ggi'),
    (r'^(.*[aeiou])go \^ e$', r'\1ghe'),
    (r'^(.*). \^ ([aeio])$', r'\1\2'),
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
