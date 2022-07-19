#!/usr/bin/env python3

from subprocess import run
from sys import executable


def call(cmd):
    print(' '.join(cmd))
    run(cmd, check=True)


venv = '.venv'
call([executable, '-m', 'venv', venv])
py = f'{venv}/bin/python'
call([py, '-m', 'pip', 'install', '--upgrade', 'pip'])
call([py, '-m', 'pip', 'install', '-r', 'requirements.txt'])
