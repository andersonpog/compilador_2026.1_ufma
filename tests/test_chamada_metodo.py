import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from JackTokenizer import JackTokenizer
from parser import Parser


def test_chamada_de_metodo_em_objeto(tmp_path):
    input_code = """
    class Main {
        function void main() {
            var Point p;
            var int x;
            let p = Point.new(10, 20);
            let x = p.getX();
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
function Main.main 2
push constant 10
push constant 20
call Point.new 2
pop local 0
push local 0
call Point.getX 1
pop local 1
push constant 0
return
""".strip()

    assert actual == expected