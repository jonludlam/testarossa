#!/bin/bash

sudo yum clean all
sudo yum install -y targetcli python-rtslib
sudo modprobe target_core_mod
sudo modprobe iscsi_target_mod
sudo mkdir -p /var/target/pr/
sudo /scripts/add_lun.py
sudo /scripts/unset_acls.py

