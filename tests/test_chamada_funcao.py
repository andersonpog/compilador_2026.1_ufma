import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from JackTokenizer import JackTokenizer
from parser import Parser


def test_chamada_de_funcao(tmp_path):
    input_code = """
    class Main {
        function int soma(int x, int y) {
            return x + y;
        }

        function void main() {
            var int d;
            let d = Main.soma(4, 5);
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
function Main.soma 0
push argument 0
push argument 1
add
return
function Main.main 1
push constant 4
push constant 5
call Main.soma 2
pop local 0
push constant 0
return
""".strip()

    assert actual == expected