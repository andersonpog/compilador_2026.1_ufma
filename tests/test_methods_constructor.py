import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from JackTokenizer import JackTokenizer
from parser import Parser


def test_declaracao_de_metodos_e_constructor(tmp_path):
    input_code = """
    class Point {
        field int x, y;

        method int getX() {
            return x;
        }

        method int getY() {
            return y;
        }

        method void print() {
            do Output.printInt(getX());
            do Output.printInt(getY());
            return;
        }

        constructor Point new(int Ax, int Ay) {
            var int w;
            let x = Ax;
            let y = Ay;
            let w = 42;
            let x = w;
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
function Point.getX 0
push argument 0
pop pointer 0
push this 0
return
function Point.getY 0
push argument 0
pop pointer 0
push this 1
return
function Point.print 0
push argument 0
pop pointer 0
push pointer 0
call Point.getX 1
call Output.printInt 1
pop temp 0
push pointer 0
call Point.getY 1
call Output.printInt 1
pop temp 0
push constant 0
return
function Point.new 1
push constant 2
call Memory.alloc 1
pop pointer 0
push argument 0
pop this 0
push argument 1
pop this 1
push constant 42
pop local 0
push local 0
pop this 0
push pointer 0
return
""".strip()

    assert actual == expected