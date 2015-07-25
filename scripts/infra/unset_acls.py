#!/usr/bin/env python

import rtslib
import sys

i = rtslib.FabricModule("iscsi")
targets = list(i.targets)
t = targets[0]
tpg = list(t.tpgs)[0]
tpg.set_attribute("cache_dynamic_acls",1)
tpg.set_attribute("generate_node_acls",1)
