#!/usr/bin/env python

import rtslib

iscsi = rtslib.FabricModule("iscsi")
f = rtslib.FileIOStorageObject("test1", "/tmp/test.img", 100000000)
f2 = rtslib.FileIOStorageObject("test2", "/tmp/test2.img", 100000000)
target = rtslib.Target(iscsi)
tpg = rtslib.TPG(target,1)
tpg.enable = True
tpg.set_attribute("authentication",False)
portal = rtslib.NetworkPortal(tpg, "0.0.0.0", 3260)
lun = rtslib.LUN(tpg, 0, f)
lun2 = rtslib.LUN(tpg, 1, f2)
print target.wwn
