import pytest
from src.gpt import gpt, generate

def test_gpt():
    input = [1,0,2,4,6]
    actual_output = gpt(input)
    expected_output = [
        [0.75,0.1,0.0,0.15,0.0,0.0,0.0],
        [0.0,0.0,0.8,0.1,0.0,0.1],
        [0.0,0.0,0.0,0.1,0.0,0.05,0.85]]
    assert expected_output == actual_output


def test_generate():
    input_ids = [1,0]
    ntokens_to_generate = 3
    actual_output = generate(input_ids, ntokens_to_generate)
    except_output = [6,6,6]
    assert except_output == actual_output