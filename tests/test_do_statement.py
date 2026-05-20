import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from JackTokenizer import JackTokenizer
from parser import Parser


def test_do_statement_descarta_retorno_da_chamada(tmp_path):
    input_code = """
    class Main {
        function void main() {
            var int x;
            let x = 10;
            do Output.printInt(x);
            return;
        }
    }
    """

    arquivo = tmp_path / "Main.jack"
    arquivo.write_text(input_code)

    tokenizer = JackTokenizer(str(arquivo.with_suffix("")))
    parser = Parser(tokenizer.tokens)
    parser.parse_class()

    actual = parser.get_vm_output().strip()

    expected = """
function Main.main 1
push constant 10
pop local 0
push local 0
call Output.printInt 1
pop temp 0
push constant 0
return
""".strip()

    assert actual == expected