from plover import log, system
from plover.registry import registry
from plover_build_utils.testing import blackbox_test


log.set_level(log.DEBUG)


@blackbox_test
class TestsBlackbox:

    @classmethod
    def setup_class(cls):
        registry.update()
        system.setup('Michela')

    def test_orthography_1(self):
        r'''
        "F": "fare",
        "S": "{^lo}",

        F/S  " farlo"
        '''

    def test_orthography_2(self):
        r'''
        "F": "vera",
        "S": "{^mente}",

        F/S  " veramente"
        '''

    def test_orthography_3(self):
        r'''
        "F": "chiude",
        "S": "{^dola}",

        F/S  " chiudendola"
        '''

    def test_orthography_4(self):
        r'''
        "F": "elimina",
        "S": "{^dola}",

        F/S  " eliminandola"
        '''

    def test_orthography_5(self):
        r'''
        "F": "enogastronomia",
        "S": "{^ci}",

        F/S  " enogastronomici"
        '''
