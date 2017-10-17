#!/usr/bin/env python
# this script is used to run our experiments multiple times

import os

for i in range(1,10):
	for k in range(1,5):
		os.system('ns exp1.tcl %i %i' % (i,k))