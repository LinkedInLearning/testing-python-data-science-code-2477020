from pathlib import Path

import pytest
import yaml

import splitter

here = Path(__file__).absolute().parent


def load_split_cases():
    cases_file = here / 'split_cases.yml'
    with cases_file.open() as fp:
        data = yaml.safe_load(fp)

    for tc in data:
        yield tc['size'], tc['chunk_size'], tc['chunks']


@pytest.mark.parametrize('size, chunk_size, expected', load_split_cases())
def test_split_to_chunks(size, chunk_size, expected):
    chunks = splitter.split_to_chunks(size, chunk_size)
    # split_to_chunks returns tuples generator, test case has lists
    chunks = [list(c) for c in chunks]
    assert chunks == expected
