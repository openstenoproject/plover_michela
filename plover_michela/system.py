# -*- coding: utf-8 -*-

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
    #: produrre + cele = produrcele
    #: sottrarre + celi = sottrarceli
    #: sottoporre + celo = sottoporcelo
    #: scrivete + cel[aeio] = scrivetecel[aeio]
    #: indicato + cel[aeio] = indicatecel[aeio]
    #: porto + cel[aeio] = portacel[aeio]
    #: scrivo + cel[aeio] = scrivicel[aeio]
    (r'^(.*[aeiou])r?re \^ cel([aeio])$', r'\1rcel\2'),
    (r'^(.*[aeiou])t[oe] \^ cel([aeio])$', r'\1tecel\2'),
    (r'^(.*)o \^ cel([aeio])$', r'\1acel\2'),
    (r'^(.*)[oe] \^ cel([aeio])$', r'\1icel\2'),

    # == +cene ==
    #: fare + cene = farcene
    #: liberare + cene = liberarcene
    #: produrre + cene = produrcene
    #: portato + cene = portatecene
    #: scrivete + cene = scrivetecene
    #: porto + cene = portacene
    #: scrivo + cene = scrivicene
    (r'^(.*[aeiou])r?re \^ cene$', r'\1rcene'),
    (r'^(.*)t[oe] \^ cene$', r'\1tecene'),
    (r'^(.*)o \^ cene$', r'\1acene'),
    (r'^(.*)o \^ cene$', r'\1icene'),

    # == +ci ==
    #: fare + ci = farci
    #: credere + ci = crederci
    #: indurre + ci = indurci
    (r'^(.*[aeiou])r?re \^ ci$', r'\1rci'),

    # == +esco +eschi ==
    #: mano + esco = manesco
    #: libro + esco = libresco
    #: arabo + esco = arabesco
    #: mano + eschi = maneschi
    #: libro + eschi = libreschi
    #: arabo + eschi = arabeschi
    (r'^(.*). \^ esco$', r'\1esco'),
    (r'^(.*). \^ eschi$', r'\1eschi'),

    # == +esimo, +esimo,==
    #: undici + esim[oi] = undicesim[oi]
    #: diciasette + esim[oi] = diciasettesim[oi]
    #: ventitré + esim[oi] = ventitreesim[oi]
    #: monaco + esim[oi] = monachesim[oi]
    (r'^(.*[aeiou])tré \^ esim([oi])$', r'\1treesim\2'),
    (r'^(.*[aeiou])co \^ esim([oi])$', r'\1chesim\2'),
    (r'^(.*). \^ esim([oi])$', r'\1esim\2'),

    # == +ismo, +ismi ==
    #: abolizione + ism[oi] = abolizionism[oi]
    #: abusivo + ism[oi] = abusivism[oi]
    #: centro + ism[oi] = centrism[oi]
    (r'^(.*). \^ ism([oi])$', r'\1ism\2'),

    # == +ista, +iste, +isti ==
    #: abolizione + ist[aei] = abolizionist[aei]
    #: negazione + ist[aei] = negazionist[aei]
    #: centro + ist[aei] = centrist[aei]
    (r'^(.*). \^ ist([aei])$', r'\1ist\2'),

    # == +ità ==
    #: vasto + ità = vastità
    #: utile + ità = utilità
    #: unico + ità = unicità
    (r'^(.*). \^ ità$', r'\1ità'),

    # == +ietà ==
    #: terzo + ietà = terzietà
    #: vario + ietà = varietà
    (r'^(.*)io \^ ietà$', r'\1ietà'),
    (r'^(.*)o \^ ietà$', r'\1ietà'),

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
    #: porto + gliel[aeio] = portagliel[aeio]
    #: scrivo + gliel[aeio] = scrivigliel[aeio]
    (r'^(.*[aeiou])r?re \^ gliel([aeio])$', r'\1rgliel\2'),
    (r'^(.*)t[oe] \^ gliel([aeio])e$', r'\1tegliel\2'),
    (r'^(.*)o \^ gliel([aeio])$', r'\1agliel\2'),
    (r'^(.*)o \^ gliel([aeio])$', r'\1igliel\2'),

    # == +gliene ==
    #: fare + gliene = fargliene
    #: portare + gliene = portargliene
    #: sottoporre + gliene = sottoporgliene
    #: portato + gliene = portategliene
    #: scrivete + gliene = scrivetegliene
    #: porto + gliene = portagliene
    #: scrivo + gliene = scrivigliene
    (r'^(.*[aeiou])r?re \^ gliene$', r'\1rgliene'),
    (r'^(.*)t[oe] \^ gliene$', r'\1tegliene'),
    (r'^(.*)o \^ gliene$', r'\1agliene'),
    (r'^(.*)o \^ gliene$', r'\1igliene'),

    # == +issima, +issime, +issimi, +issimo,==
    #: felice + issim[aeio] = felicissim[aeio]
    #: secco + issim[aeio] = secchissim[aeio]
    #: abile + issim[aeio] = abilissim[aeio]
    (r'^(.*[aeiou])cco \^ issim([aeio])$', r'\1cchissim\2'),
    (r'^(.*). \^ issim([aeio])$', r'\1issim\2'),

    # == +la, +le, +li, +lo ==
    #: dire + l[aeio] = dirl[aeio]
    #: fare + l[aeio]= farl[aeio]
    #: proporre + l[aeio] = proporl[aeio]
    #: condurre + l[aeio] = condurl[aeio]
    (r'^(.*[aeiou])r?re \^ l([aeio])$', r'\1rl\2'),

    # == +mela, +mele, +meli, +melo ==
    #: fare + mel[aeio] = farmel[aeio]
    #: portare + mel[aeio]= portarmel[aeio]
    #: sottrarre + mel[aeio] = sottrarmel[aeio]
    #: sottoporre + mel[aeio]= sottopormel[aeio]
    #: scrivete + mel[aeio] = scrivetemel[aeio]
    #: indicato + mel[aeio] = indicatemel[aeio]
    #: porto + mele = portamele
    #: scrivo + mele = scrivimele
    (r'^(.*[aeiou])r?re \^ mel([aeio])$', r'\1rmel\2'),
    (r'^(.*)t[oe] \^ mel([aeio])$', r'\1temel\2'),
    (r'^(.*)o \^ mel([aeio])$', r'\1amel\2'),
    (r'^(.*)o \^ mel([aeio])$', r'\1imel\2'),

    # == +mene ==
    #: fare + mene = farmene
    #: liberare + mene = liberarmene
    #: estrarre + mene = estrarmene
    #: scrivete + mene = scrivetemene
    #: indicato + mene = indicatemene
    #: porto + mene = portamene
    #: scrivo + mene = scrivimene
    (r'^(.*[aeiou])r?re \^ mene$', r'\1rmene'),
    (r'^(.*)t[oe] \^ mene$', r'\1temene'),
    (r'^(.*)o \^ mene$', r'\1amene'),
    (r'^(.*)o \^ mene$', r'\1imene'),

    # == +mente ==
    #: abile + mente = abilmente
    #: familiare + mente = familiarmente
    #: puro + mente = puramente
    #: retto + mente = rettamente
    #: espresso + mente = espressamente
    #: distinto + mente = distintamente
    (r'^(.*[aeiou])le \^ mente$', r'\1lmente'),
    (r'^(.*[aeiou])re \^ mente$', r'\1rmente'),
    (r'^(.*[aeiou])ro \^ mente$', r'\1ramente'),
    (r'^(.*[aeiou])tto \^ mente$', r'\1tamente'),
    (r'^(.*[aeiou])sso \^ mente$', r'\1ssamente'),
    (r'^(.*[aeiou])vo \^ mente$', r'\1vamente'),
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
    #: porto + teci = portateci
    #: scrivo + mene = scriveteci
    (r'^(.*[aeiou])t[oe] \^ teci$', r'\1teci'),
    (r'^(.*)o \^ teci$', r'\1ateci'),
    (r'^(.*)o \^ teci$', r'\1eteci'),

    # == +tegli ==
    #: convertito + tegli = convertitegli
    #: scrivete + tegli = scrivetegli
    #: porto + tegli = portategli
    #: scrivo + tegli = scrivetegli
    (r'^(.*[aeiou])t[oe] \^ tegli$', r'\1tegli'),
    (r'^(.*)o \^ tegli$', r'\1ategli'),
    (r'^(.*)o \^ tegli$', r'\1etegli'),

    # == +tela, +tele, +teli, +telo
    #: cambiare + tel[aeio] = cambiartel[aeio]
    #: portare + tel[aeio] = portartel[aeio]
    #: estrarre + tel[aeio] = estrartel[aeio]
    #: detrarre + tel[aeio]= detrartel[aeio]
    #: porto + tel[aeio] = portatel[aeio]
    #: scrivo + tel[aeio] = scrivetel[aeio]
    (r'^(.*[aeiou])r?re \^ tel([aeio])$', r'\1rtel\2'),
    (r'^(.*)o \^ tel([aeio])$', r'\1atel\2'),
    (r'^(.*)o \^ tel([aeio])$', r'\1etel\2'),
    (r'^(.*)o \^ tel([aeio])$', r'\1itel\2'),

    #== +temi ==
    #: convertito + temi = convertitemi
    #: seguo + temi = seguitemi
    #: porto + temi = portatemi
    #: scrivo + temi = scrivetemi
    (r'^(.*[aeiou])t[oe] \^ temi$', r'\1temi'),
    (r'^(.*)o \^ temi$', r'\1atemi'),
    (r'^(.*)o \^ temi$', r'\1etemi'),
    (r'^(.*)o \^ temi$', r'\1itemi'),

    #== +tene ==
    #: convertito + tene = convertitene
    #: seguo + tene = seguitene
    #: porto + tene = portatene
    #: scrivo + tene = scrivetene
    (r'^(.*[aeiou])t[oe] \^ tene$', r'\1tene'),
    (r'^(.*)o \^ tene$', r'\1atene'),
    (r'^(.*)o \^ tene$', r'\1etene'),
    (r'^(.*)o \^ tene$', r'\1itene'),

    #== +tevi ==
    #: convertito + tevi = convertitevi
    #: seguo + tevi = seguitevi
    #: porto + tevi = portatevi
    #: scrivo + tevi = scrivetevi
    (r'^(.*[aeiou])t[oe] \^ tevi$', r'\1tevi'),
    (r'^(.*)o \^ tevi$', r'\1atevi'),
    (r'^(.*)o \^ tevi$', r'\1etevi'),
    (r'^(.*)o \^ tevi$', r'\1itevi'),

    # == +ti ==
    #: dire + ti = dirti
    #: sentire + ti = sentirti
    #: porre + ti = porti
    (r'^(.*[aeiou])r?re \^ ti$', r'\1rti'),

    # == +vela, +vele, +veli, +velo ==
    #: cambiare + vel[aeio] = cambiarvel[aeio]
    #: portare + vel[aeio] = portarvel[aeio]
    #: estrarre + vel[aeio] = estrarvel[aeio]
    #: comporre + vel[aeio] = comporvel[aeio]
    #: portato + vel[aeio] = portatevel[aeio]
    #: scrivete + vel[aeio]= scrivetevel[aeio]
    (r'^(.*[aeiou])r?re \^ vel([aeio])$', r'\1rvel\2'),
    (r'^(.*[aeiou])t[oe] \^ vel([aeio])$', r'\1tevel\2'),

    # == +vene ==
    #: fare + vene = farvene
    #: liberare + vene = liberarvene
    #: estrarre + vene = estrarvene
    #: scrivete + vene = scrivetevene
    #: portato + vene = portatevene
   (r'^(.*[aeiou])r?re \^ vene$', r'\1rvene'),
   (r'^(.*[aeiou])t[oe] \^ vene$', r'\1tevene'),

    # == +vi ==
    #: dire + vi = dirvi
    #: sentire + vi = sentirvi
    #: apporre + vi = apporvi
    (r'^(.*[aeiou])r?re \^ vi$', r'\1rvi'),

    # == +zata +zate +zati +zato ==
    #: parziale + zat[aeio] = parzializzat[aeio]
    #: avanzo + zat[aeio] = avanzat[aeio]
    #: battezzo + zat[aeio] = battezzat[aeio]
    (r'^(.*[aeiou])zzo \^ zat([aeio])$', r'\1zzat\2'),
    (r'^(.*[n])zo \^ zat([aeio])$', r'\1zat\2'),
    (r'^(.*). \^ zat([aeio])$', r'\1izzat\2'),

    # == +a, +e, +i, +o,==
    # these suffixes are used to change the gender and the number of any words
    #: vivo + a = viva
    #: contratto + e = contratte
    #: legame + i = legami
    #: chiede + o = chiedo
    #: secco + [ei] = secch[ei]
    #: reco + i = rechi
    #: legge + i = leggi
    #: lego + [ei] = legh[ei]
    (r'^(.*[aeiou])ch?[aeio] \^ a$', r'\1ca'),
    (r'^(.*[aeiou])cch?[aeio] \^ a$', r'\1cca'),
    (r'^(.*[aeiou])ch?[aeio] \^ e$', r'\1che'),
    (r'^(.*[aeiou])cch?[aeio] \^ e$', r'\1cche'),
    (r'^(.*[aeiou])ch?[aeio] \^ i$', r'\1chi'),
    (r'^(.*[aeiou])cch?[aeio] \^ i$', r'\1cchi'),
    (r'^(.*[aeiou])ch?[aeio] \^ o$', r'\1co'),
    (r'^(.*[aeiou])cch?[aeio] \^ o$', r'\1cco'),
    (r'^(.*[aeiou])gh?[aeio] \^ a$', r'\1ga'),
    (r'^(.*[aeiou])gg[aeio] \^ a$', r'\1gga'),
    (r'^(.*[aeiou])gh?[aeio] \^ e$', r'\1ghe'),
    (r'^(.*[aeiou])gg[aeio] \^ e$', r'\1gge'),
    (r'^(.*[aeiou])gh?[aeio] \^ i$', r'\1ghi'),
    (r'^(.*[aeiou])gg[aeio] \^ i$', r'\1ggi'),
    (r'^(.*[aeiou])gh?[aeio] \^ o$', r'\1go'),
    (r'^(.*[aeiou])gg[aeio] \^ o$', r'\1ggo'),
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

# vim: spell spelllang=it
