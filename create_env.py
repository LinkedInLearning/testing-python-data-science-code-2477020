#!/usr/bin/env python3

from subprocess import run
from sys import executable, platform


def call(cmd):
    print(' '.join(cmd))
    run(cmd, check=True)


venv = '.venv'
call([executable, '-m', 'venv', venv])
if platform == 'win32':
    py = f'{venv}/Scripts/python.exe'
else:
    py = f'{venv}/bin/python'
call([py, '-m', 'pip', 'install', '--upgrade', 'pip'])
call([py, '-m', 'pip', 'install', '-r', 'requirements.txt'])
