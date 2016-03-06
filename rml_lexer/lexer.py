from pygments.lexers.functional import OcamlLexer
from pygments.token import Name, Keyword


class RmlLexer(OcamlLexer):
    name = "ReactiveML"
    aliases = ['rml']
    filenames = ['*.rml']

    EXTRA_KEYWORDS = set(('process', 'proc', 'run', 'nothing', 'pause', 'halt'))

    def get_tokens_unprocessed(self, text):
        for index, token, value in OcamlLexer.get_tokens_unprocessed(self, text):
            if token in Name and value in self.EXTRA_KEYWORDS:
                yield index, Keyword, value
            else:
                yield index, token, value
