#!/bin/bash

sudo yum install -y targetcli python-rtsli
sudo modprobe target_core_mod
sudo modprobe iscsi_target_mod
sudo /scripts/add_lun.py
