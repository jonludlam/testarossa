#!/usr/bin/env python

import rtslib
import sys

i = rtslib.FabricModule("iscsi")
targets = list(i.targets)
t = targets[0]
tpg = list(t.tpgs)[0]
lun = list(tpg.luns)[0]
nodeacl = rtslib.NodeACL(tpg, sys.argv[1])
mlun = rtslib.MappedLUN(nodeacl, 0, lun)
