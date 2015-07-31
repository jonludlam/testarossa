#!/bin/bash

sudo rpm -ivh --force --nodeps /xs/*.rpm || true
sudo cp /xs/xapi /opt/xensource/bin/ || true
sudo vagrant-xenserver-scripts/start.sh
pif=`sudo xe pif-list device=eth1 --minimal`
sudo xe pif-reconfigure-ip uuid=$pif mode=dhcp
sudo xe pif-param-set uuid=$pif other-config:defaultroute=true
sudo xe pif-unplug uuid=$pif
sudo xe pif-plug uuid=$pif
sudo mkdir -p /var/lib/xenvmd
sudo chmod 777 /var/lib/xcp/xapi

