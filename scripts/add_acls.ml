#!/usr/bin/env ocamlscript
Ocaml.packs := ["lwt"; "xen-api-client.lwt"; "re"]
Ocaml.sources := ["../scripts/yorick.ml"]
--
open Lwt
open Xen_api
open Xen_api_lwt_unix

let uri = ref "http://gandalf.uk.xensource.com"
let username = ref "root"
let password = ref "xenroot"

let main


open Cmdliner

let name_arg =
  let doc = "Name of the Vagrant VM for whom the ACL is required" in
  Arg.(value & pos 0 string "" & info [] ~docv:"NAME" ~doc)
    
let main_t = Term.(pure main $ name_arg)

let info =
  let doc = "Add the host IQN of the specified host to the iscsi server on then infrastructure VM" in
  let man = [ `S "BUGS"; `P "Report bug on the github issue tracker" ] in
  Term.info "add_acls" ~version:"1.0" ~doc ~man
    
let () = match Term.eval (main_t, info) with `Error _ -> exit 1 | _ -> exit 0
