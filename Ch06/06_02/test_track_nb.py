import json
from os import environ
from pathlib import Path
from subprocess import run
from sys import executable

import numpy as np

here = Path(__file__).absolute().parent


def test_track_nb(tmp_path):
    csv_file = here / 'track.csv'
    nb_file = here / 'track.ipynb'
    out_file = tmp_path / 'output.json'

    cmd = [
        executable, '-m', 'jupyter', 'nbconvert',
        '--execute',
        '--stdout',
        '--to', 'notebook',
        nb_file,
    ]
    env = environ.copy()
    env['CSV_FILE'] = csv_file
    env['OUT_FILE'] = out_file
    run(cmd, env=env, check=True)

    with out_file.open() as fp:
        output = json.load(fp)

    assert np.allclose(9.580444, output['mean_speed'])
