#!/usr/bin/env python
# this script is used to run our experiments multiple times

import os

for i in range(1,15):
    for j in [10,20]:
        for k in [100,200]:
            os.system('ns exp3.tcl %i %i %i' % (i, j, k))