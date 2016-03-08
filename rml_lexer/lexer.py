from pygments.lexers.functional import OcamlLexer
from pygments.token import Name, Keyword


class RmlLexer(OcamlLexer):
    name = "ReactiveML"
    aliases = ['rml']
    filenames = ['*.rml']

    EXTRA_KEYWORDS = ['process', 'proc', 'run', 'nothing', 'pause', 'halt',
                      'emit', 'signal', 'until', 'loop', 'await', 'immediate',
                      'one', 'print_endline', 'string_of_int', 'int_of_string',
                      'float_of_string', 'ref' ]

    def get_tokens_unprocessed(self, text):
        for index, token, value in OcamlLexer.get_tokens_unprocessed(self, text):
            if token in Name and value in self.EXTRA_KEYWORDS:
                yield index, Keyword, value
            else:
                yield index, token, value
