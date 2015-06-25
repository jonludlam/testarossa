# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
# Disable default synced folder
  config.vm.synced_folder ".", "/vagrant", disabled: true

  config.vm.define "infrastructure" do |infra|
    infra.vm.box = "jonludlam/xs-centos-7"
    infra.vm.provision "shell", path: "scripts/infra/vagrant_provision.sh"
    infra.vm.synced_folder "scripts/infra", "/scripts"
  end

  config.vm.define "host1" do |host1|
    host1.vm.box = "jonludlam/xs-thin-lvhd-ring3"
    host1.vm.provision "shell",
      inline: "hostname host1; echo host1 > /etc/hostname"
    host1.vm.synced_folder "xs", "/xs"
    host1.vm.network "forwarded_port", guest: 80, host: 8880
  end

  config.vm.define "host2" do |host2|
    host2.vm.box = "jonludlam/xs-thin-lvhd-ring3"
    host2.vm.provision "shell",
      inline: "hostname host2; echo host2 > /etc/hostname"
    host2.vm.synced_folder "xs", "/xs"
    host2.vm.network "forwarded_port", guest: 80, host: 8881
  end

  config.vm.define "host3" do |host3|
    host3.vm.box = "jonludlam/xs-thin-lvhd-ring3"
    host3.vm.provision "shell",
      inline: "hostname host3; echo host3 > /etc/hostname"
    host3.vm.synced_folder "xs", "/xs"
  end

    config.vm.provider "xenserver" do |xs|
       xs.memory = 4096
    end
end

