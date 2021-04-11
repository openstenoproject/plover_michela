from collections import namedtuple
from pprint import pformat
import functools
import itertools
import re

import libcst as cst
import pytest

from plover.orthography import add_suffix, make_candidates_from_rules
from plover import system


ORTHOGRAPHIC_RULE_TEST_RX = re.compile(r'^\s+(?P<word>\w+)\s*\+\s*(?P<suffix>\w*(?P<variants>\[\w+\])?)\s*=\s*(?P<expected>\w+(?P=variants)?)(\s*\(\s*(?P<explanation>[^)]+)\s*\))?\s*$')


class OrthographicRuleTest(namedtuple('OrthographicRuleTest', 'location word suffix expected explanation')):

    def format(self, location=True, result=None):
        s = ''
        if location:
            s += '%s:%u:%u: ' % self.location
        s += '%r + %r ' % (self.word, self.suffix)
        if result is not None:
            s += '=> %r !' % result
        s += '= %r' % self.expected
        if self.explanation:
            s += ' (%s)' % self.explanation
        return s


class OrthographicTestsCollector(cst.CSTVisitor):

    METADATA_DEPENDENCIES = (cst.metadata.PositionProvider,)

    def __init__(self, filename):
        self.filename = filename
        self.test_list = []
        self._parse_comments = False

    def visit_Assign(self, node):
        if node.targets[0].target.value == 'ORTHOGRAPHY_RULES':
            self._parse_comments = True

    def visit_Comment(self, node):
        if not self._parse_comments:
            return
        if not node.value.startswith('#:'):
            return
        position = self.get_metadata(cst.metadata.PositionProvider, node).start
        location = (self.filename, position.line, position.column)
        m = ORTHOGRAPHIC_RULE_TEST_RX.match(node.value[2:])
        if m is None or not m.group('suffix'):
            raise ValueError('invalid test definition\n'
                             '%s:%u:%u %s' % (location + (node.value,)))
        test = m.groupdict()
        variants = test.pop('variants')
        if variants is None:
            self.test_list.append(OrthographicRuleTest(location=location, **test))
            return
        suffix = test.pop('suffix')[:-len(variants)]
        suffix_list = list(itertools.product([suffix], variants[1:-1]))
        expected = test.pop('expected')
        if expected.endswith(variants):
            expected = expected[:-len(variants)]
            expected_list = list(itertools.product([expected], variants[1:-1]))
        else:
            expected_list = [expected]
        for suffix, expected in zip(suffix_list, expected_list):
            test['suffix'] = ''.join(suffix)
            test['expected'] = ''.join(expected)
            self.test_list.append(OrthographicRuleTest(location=location, **test))

    def leave_Assign(self, node):
        self._parse_comments = False


def collect_orthographic_rules_tests(source_file):
    with open(source_file, encoding='utf-8') as fp:
        src = fp.read()
    tree = cst.metadata.MetadataWrapper(cst.parse_module(src))
    ortho_collector = OrthographicTestsCollector(source_file)
    tree.visit(ortho_collector)
    return ortho_collector.test_list


def orthographic_rules_report(word, suffix):
    report = {}
    in_wordlist = system.ORTHOGRAPHY_WORDS.__contains__
    rules_alias = system.ORTHOGRAPHY_RULES_ALIASES.get(suffix)
    if rules_alias is not None:
        report['rules alias'] = rules_alias
        report['candidates [alias]'] = make_candidates_from_rules(word, alias, in_wordlist)
    report['simple join in wordlist'] = in_wordlist(word + suffix)
    report['wordlist candidates'] = {
        w: system.ORTHOGRAPHY_WORDS[w] for w in
        make_candidates_from_rules(word, suffix, in_wordlist)
    }
    report['other candidates'] = [
        w
        for w in make_candidates_from_rules(word, suffix)
        if w not in report['wordlist candidates']
    ]
    return report


def orthographic_rules_test(system_source_py):
    test_list = collect_orthographic_rules_tests(system_source_py)
    test_ids = [t.format() for t in test_list]
    def decorator(fn):
        @pytest.mark.parametrize('test', test_list, ids=test_ids)
        @functools.wraps(fn)
        def test_runner(test, *args, **kwargs):
            fn(test, *args, **kwargs)
            result = add_suffix(test.word, test.suffix)
            report = orthographic_rules_report(test.word, test.suffix)
            msg = '%s\n%s' % (
                test.format(location=False, result=result),
                '\n'.join('• %s: %s' % (k, pformat(v)) for k, v in report.items()),
            )
            assert result == test.expected, msg
        return test_runner
    return decorator
