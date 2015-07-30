#!/usr/bin/python
# XenRT: Test harness for Xen and the XenServer product family
#
# Disk patterns helper script
#
# Copyright (c) 2007 XenSource, Inc. All use and distribution of this
# copyrighted material is governed by and subject to terms and
# conditions as licensed by XenSource, Inc. All other rights reserved.
#

import sys,struct


# We will be given three arguments, a file/device name, a size (in bytes), and
# an action, which is either "write" or "read"
# There may also be a fourth argument, which specifies the type of pattern
# An optional fifth argument varies the pattern it should be an integer

if len(sys.argv) < 4 or len(sys.argv) > 6:
    sys.stderr.write("Invalid number of arguments\n")
    sys.exit(1)

filename = sys.argv[1]
size = int(sys.argv[2]) # in bytes
action = sys.argv[3]

if len(sys.argv) >= 5:
    pattern = int(sys.argv[4])
else:
    pattern = 0

if len(sys.argv) >= 6:
    rotate = int(sys.argv[5])
else:
    rotate = 0

# Defined patterns
# numbers are written as 4 byte values (TODO: Test on a 64 bit system)
# 0 = write a number every 4MB
# 1 = write a 1KB block of numbers every 4MB
# 2 = write a 1MB block of numbers in the last 1MB of the file
# 3 = write a number every 2MB

def makePattern(index):
    global rotate
    index = index + rotate
    index = index & 0xffffffff
    return struct.pack("I", index)

def checkPattern(pattern, index):
    global rotate
    index = index + rotate
    index = index & 0xffffffff
    return struct.unpack("I", pattern)[0] == index

print "Filename: %s" % (filename)

if action == "write":
    print "Writing file"

    f = file(filename, "w")
    if pattern == 0:
        num_writes = size / (4096*1024)
        for i in range(num_writes):
            f.seek(i*4096*1024)
            f.write(makePattern(i))
    elif pattern == 1:
        num_writes = size / (4096*1024)
        for i in range(num_writes):
            f.seek(i*4096*1024)
            for j in range(1024/4):
                f.write(makePattern(j))
    elif pattern == 2:
        f.seek(size - (1024*1024))
        for i in range(1024*1024/4):
            f.write(makePattern(i))
    elif pattern == 3:
        num_writes = size / (2048*1024)
        for i in range(num_writes):
            f.seek(i*2048*1024)
            f.write(makePattern(i))
    else:
        sys.stderr.write("Unknown pattern %d\n" % (pattern))
        sys.exit(1)
    f.close()
    print "File written"
elif action == "read":
    print "Reading file"
    f = file(filename, "r")
    if pattern == 0:
        num_writes = size / (4096*1024)
        for i in range(num_writes):
            try:
                f.seek(i*4096*1024)
                d = f.read(4)
                if not checkPattern(d, i):
                    sys.stderr.write("Inconsistency at byte position %X\n" % (f.tell()-4))
                    sys.exit(1)
            except Exception, e:
                sys.stderr.write("Exception while reading file: %s\n" % (str(e)))
                sys.exit(1)
    elif pattern == 1:
        num_writes = size / (4096*1024)
        for i in range(num_writes):
            try:
                f.seek(i*4096*1024)
                for j in range(1024/4):
                    d = f.read(4)
                    if not checkPattern(d, j):
                        sys.stderr.write("Inconsistency at byte position %X\n" % (f.tell()-4))
                        sys.exit(1)
            except Exception, e:
                sys.stderr.write("Exception while reading file: %s\n" % (str(e)))
                sys.exit(1)
    elif pattern == 2:
        try:
            f.seek(size - (1024*1024))
            for i in range(1024*1024/4):
                d = f.read(4)
                if not checkPattern(d, i):
                    sys.stderr.write("Inconsistency at byte position %X\n" % (f.tell()-4))
                    sys.exit(1)
        except Exception, e:
            sys.stderr.write("Exception while reading file: %s\n" % (str(e)))
            sys.exit(1)
    elif pattern == 3:
        num_writes = size / (2048*1024)
        for i in range(num_writes):
            try:
                f.seek(i*2048*1024)
                d = f.read(4)
                if not checkPattern(d, i):
                    sys.stderr.write("Inconsistency at byte position %X\n" % (f.tell()-4))
                    sys.exit(1)
            except Exception, e:
                sys.stderr.write("Exception while reading file: %s\n" % (str(e)))
                sys.exit(1)
    else:
        sys.stderr.write("Unknown pattern %d\n" % (pattern))
        sys.exit(1)
    print "File is as expected"
    f.close()
    sys.exit(0)
else:
    sys.stderr.write("Invalid action\n")
    sys.exit(1)
