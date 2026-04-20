import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from JackTokenizer import JackTokenizer
from parser import Parser

def test_parse_term_integer():
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "term_test")

    tokenizer = JackTokenizer(file_path)
    tokens = tokenizer.tokens

    parser = Parser(tokens)
    parser.parse_term()
    xml = parser.get_xml()

    assert "<term>" in xml
    assert "<integerConstant> 10 </integerConstant>" in xml


# Colocando o teste para expressões conforme aula
def test_parse_expression():
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "expression_test")

    tokenizer = JackTokenizer(file_path)
    tokens = tokenizer.tokens

    parser = Parser(tokens)
    parser.parse_expression()
    xml = parser.get_xml()

    assert "<expression>" in xml
    assert "<symbol> + </symbol>" in xml