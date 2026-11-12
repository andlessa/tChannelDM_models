#!/bin/bash

currentDIR="$( pwd )"
collierDIR=$currentDIR/MG5/HEPTools/collier
lhapdfDIR=$currentDIR/MG5/HEPTools/lhapdf6_py3
ninjaDIR=$currentDIR/MG5/HEPTools/ninja
export LD_LIBRARY_PATH=$collierDIR:$lhapdfDIR/lib:$ninjaDIR/lib:$LD_LIBRARY_PATH
export PYTHONPATH=$currentDIR/MG5/HEPTools/lhapdf6_py3/local/lib/python3.12/dist-packages:$PYTHONPATH
