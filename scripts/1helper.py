#!/usr/bin/env python
# this script is used to run our experiments multiple times

import os

for i in range(1,15):
	for k in [10, 20, 30, 40]:
		os.system('ns exp1.tcl %i %i' % (i,k))