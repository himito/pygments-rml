# pygments-rml
A custom ReactiveML-lexer for [Pygments](http://pygments.org/), for extra
keyword highlighting when using the package
[minted](https://github.com/gpoore/minted) in LaTeX.

## Installation

    $ git clone https://github.com/himito/pygments-rml.git
    $ cd pygments-rml
    $ (sudo) python setup.py install

### Verify

Verify that the package installed correctly by looking for the lexer "rml"

    $ pygmentize -L lexers | grep rml

## Using the lexer in latex

Just use the **rml** "language". In LaTeX this means something like this

    \begin{minted}{rml}
    let process main = print_endline "Hello World!"
    let () = run main
    \end{minted}

See the minted package at https://github.com/gpoore/minted for more information.
