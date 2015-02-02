#!/bin/bash
curl https://raw.githubusercontent.com/mitsuhiko/pipsi/master/get-pipsi.py | python
echo "export PATH=~/.local/bin:$PATH" >> $HOME/.bashrc 
$HOME/.local/bin/pipsi install for-beginner-piano
~/.local/venvs/for-beginner-piano/bin/pip install -U setuptools
