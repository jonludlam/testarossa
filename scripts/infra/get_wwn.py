#!/usr/bin/env python

import rtslib_fb
import sys

i = rtslib_fb.FabricModule("iscsi")
targets = list(i.targets)
t = targets[0]
print t.wwn
