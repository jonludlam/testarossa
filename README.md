# testarossa

## Dependencies

Get vagrant from https://www.vagrantup.com/downloads.html

```
vagrant plugin install vagrant-xenserver
opam remote add xapi-project git://github.com/xapi-project/opam-repo-dev
DEPS='ocamlscript xen-api-client ezxmlm'
opam depext $DEPS
opam install $DEPS
```
