#!/bin/sh

time pip install -e . "numpy>1.18"
time pip install -r <(echo "-e .\nnumpy>1.18")
