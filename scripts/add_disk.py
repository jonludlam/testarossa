#!/usr/bin/python

import xmlrpclib
import os

host="host1"

def get_host_vm_ref(host):
    fname = ".vagrant/machines/%s/xenserver/id" % host
    with open(fname, 'r') as f:
        vm = f.read()
    return vm

def add_vbd(s,sess,host,vdi):
    vm=get_host_vm_ref(host)
    vbd=s.VBD.create(sess,{"VM":vm,"VDI":vdi,"userdevice":"2","bootable":False,"mode":"RW","type":"Disk","unpluggable":False,"empty":False,"other_config":{"owner":""},"qos_algorithm_type":"","qos_algorithm_params":{}})['Value']
    print "Created VBD: %s" % s.VBD.get_uuid(sess,vbd)['Value']

def get_host_vm_uuid(s,sess,host):
    vm=get_host_vm_ref(host)
    return s.VM.get_uuid(sess,vm)['Value']

def create_shared_disk(s,sess):
    pools = s.pool.get_all(sess)['Value']
    pool = pools[0]
    default_sr = s.pool.get_default_SR(sess,pool)['Value']
    vdi = s.VDI.create(sess,{"name_label":"shared ocfs2 vdi", "name_description":"", "SR":default_sr, "virtual_size":"%Ld" % (10*1024*1024*1024),
                             "type":"user","sharable":True,"read_only":False,"other_config":{},"xenstore_data":{},"sm_config":{},"tags":[]})['Value']
    uuid = s.VDI.get_uuid(sess,vdi)['Value']
    print "Created VDI: %s" % uuid
    return vdi

def find_hosts():
    poss=os.listdir(".vagrant/machines")
    return filter(lambda d: os.path.exists(".vagrant/machines/%s/xenserver/id" % d), poss)

def main():
    s=xmlrpclib.Server("https://gandalf.uk.xensource.com/")
    sess=s.session.login_with_password("root","xenroot")['Value']
    print "sess=%s" % sess
    vdi = create_shared_disk(s,sess)
    print "vdi=%s uuid=%s" % (vdi,s.VDI.get_uuid(sess,vdi)['Value'])
    for host in find_hosts(): 
        uuid=get_host_vm_uuid(s,sess,host)
        add_vbd(s,sess,host,vdi)
        print uuid

main()

