import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from JackTokenizer import JackTokenizer
from parser import Parser


def test_constructor_aloca_memoria_e_retorna_this(tmp_path):
    input_code = """
    class Point {
        field int x, y;

        constructor Point new(int ax, int ay) {
            let x = ax;
            let y = ay;
            return this;
        }
    }
    """

    arquivo = tmp_path / "Point.jack"
    arquivo.write_text(input_code)

    tokenizer = JackTokenizer(str(arquivo.with_suffix("")))
    parser = Parser(tokenizer.tokens)
    parser.parse_class()

    actual = parser.get_vm_output().strip()

    expected = """
function Point.new 0
push constant 2
call Memory.alloc 1
pop pointer 0
push argument 0
pop this 0
push argument 1
pop this 1
push pointer 0
return
""".strip()

    assert actual == expected