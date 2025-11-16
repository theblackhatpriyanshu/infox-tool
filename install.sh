#!/bin/bash

pkg install python -y
pip install requests

cd $HOME
git clone https://github.com/your-username/infox-tool
cd infox-tool

python infox.py
