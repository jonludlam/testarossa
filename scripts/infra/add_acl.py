#!/usr/bin/env python

import rtslib_fb
import sys

i = rtslib_fb.FabricModule("iscsi")
targets = list(i.targets)
t = targets[0]
tpg = list(t.tpgs)[0]
lun = list(tpg.luns)[0]
nodeacl = rtslib_fb.NodeACL(tpg, sys.argv[1])
mlun = rtslib_fb.MappedLUN(nodeacl, 0, lun)
