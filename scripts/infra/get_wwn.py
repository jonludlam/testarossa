#!/usr/bin/env python

import rtslib
import sys

i = rtslib.FabricModule("iscsi")
targets = list(i.targets)
t = targets[0]
print t.wwn
