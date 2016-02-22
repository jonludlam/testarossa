#!/bin/bash

sudo rpm -ivh --force --nodeps /rpms/*.rpm || true

rm /etc/sysconfig/network-scripts/ifcfg-eth0

service forkexecd start
chkconfig forkexecd on
service xcp-networkd start
chkconfig xcp-networkd on
service genptoken start
chkconfig genptoken on
service squeezed start
chkconfig squeezed on
service xcp-rrdd start
chkconfig xcp-rrdd on
service xenopsd-xc start
chkconfig xenopsd-xc on
service xapi start
chkconfig xapi on

sleep 30

service xcp-rrdd-plugins start
chkconfig xcp-rrdd-plugins on
service xs-firstboot start
#service perfmon start
#chkconfig perfmon on

. /etc/xensource-inventory
xe pif-scan host-uuid=${INSTALLATION_UUID}
PIF=$(xe pif-list device=eth0 params=uuid --minimal)
xe pif-reconfigure-ip uuid=${PIF} mode=dhcp
xe pif-plug uuid=${PIF}
pif=`sudo xe pif-list device=eth1 --minimal`
sudo xe pif-reconfigure-ip uuid=$pif mode=dhcp
sudo xe pif-param-set uuid=$pif other-config:defaultroute=true other-config:peerdns=true
sudo xe pif-unplug uuid=$pif
sudo xe pif-plug uuid=$pif
sudo chmod 777 /var/lib/xcp/xapi
host=`sudo xe host-list --minimal`
sudo xe host-param-set uuid=$host other-config:multipathing=true other-config:multipathhandle=dmp

