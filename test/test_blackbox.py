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
        "F": "comparti",
        "S": "{^mente}",

        F/S  " compartimente"
        '''
