#!/usr/bin/env python
# this script is used to run our experiments multiple times

import os

for i in range(1,15):
    for tup in [(10,200), (20,200), (30,400), (40,400)]:
        os.system('ns exp2.tcl %i %i %i' % (i, tup[0], tup[1]))