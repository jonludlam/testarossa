# Testarossa

Testarossa is a small system-level test framework using Xen-on-Xen with the
Xenserver provider for Vagrant.

## Dependencies

Get vagrant from https://www.vagrantup.com/downloads.html

```sh
$ vagrant plugin install vagrant-xenserver
$ opam remote add xapi-project git://github.com/xapi-project/opam-repo-dev
$ DEPS='ocamlscript xen-api-client ezxmlm'
$ opam depext $DEPS
$ opam install $DEPS
```

You'll also want to create a stanza in your `~/.vagrant.d/Vagrantfile` for the
XenServer provider configuration:

```ruby
Vagrant.configure("2") do |config|
  config.vm.provider :xenserver do |xs|
    xs.xs_host = "<host>
    xs.xs_username = "root"
    xs.xs_password = "<password>"
  end
end
```

## Usage

The tests are written using OCamlscript so they are just run like any
executable script. For example, to run quicktest on a host use

```sh
$ tests/test_quicktest
```

This will update the Vagrant box to the latest build, install a CentOS
infrastructure VM to expose an iSCSI target, spin up a XenServer VM, create an
iSCSI SR and run `quicktest`.

## Extension
New tests welcome under the `tests/` directory.
