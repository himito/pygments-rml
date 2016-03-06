from setuptools import setup, find_packages

setup(
    name='ReactiveML Pygments Lexer',
    version='0.0.1',
    packages=find_packages(),
    install_requires=['pygments'],
    entry_points="""
    [pygments.lexers]
    rmllexer = rml_lexer.lexer:RmlLexer
    """
)
