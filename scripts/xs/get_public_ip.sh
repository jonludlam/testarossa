#!/bin/bash

. /etc/xensource-inventory

echo -n $INSTALLATION_UUID,
sudo xe pif-list device=eth1 host-uuid=$INSTALLATION_UUID params=IP --minimal

