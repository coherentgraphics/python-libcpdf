(* AUTO for libpycdf.c *)
open Pdfutil

let contents_of_file filename =
  let ch = open_in_bin filename in
  let s = really_input_string ch (in_channel_length ch) in
    close_in ch;
    s

let contents_to_file filename contents =
  let ch = open_out_bin filename in
    output_string ch contents;
    close_out ch

let lines contents =
  map implode (split_around (eq '\n') (explode contents))

(*

/* __AUTO int fromFile(char *filename, char *userpw) */

...becomes...

int pycpdf_fromFile(char *filename, char *userpw) {
  return cpdf_fromFile(filename, userpw);
}

*)

(*
1. Extract type name (first thing, ends with space)
2. Extract function name (second thing, ends with '(' )
3. Extract parameter names (have space before them and end with a non-alphabetic character)
4. Generate output
*)

let spliton c s =
  let a, b = cleavewhile (neq c) (explode s) in
    String.trim (implode a), String.trim (implode b)

let getmany l =
  let r = ref [] in
  let l = ref (explode l) in
  while !l <> ['*'; '/'] do
      let x, y = cleavewhile (fun x -> x <> ' ' && x <> ',' && x <> ')')  !l in
        (*Printf.printf "x = |%S|, y = |%S|\n%!" (implode x) (implode y);*)
        l := if y <> [] then explode (String.trim (implode (tl y))) else !l;
        r =| x
    done;
    rev (map String.trim (map implode !r))

let mkauto l =
  let l = String.sub l 10 (String.length l - 10) in
  let type_name, l = spliton ' ' l in
  let function_name, l = spliton '(' l in
  let param_types_and_names = getmany l in
  let types, names = really_drop_evens param_types_and_names, drop_odds param_types_and_names in
  (*Printf.printf "%i types, %i names\n" (length types) (length names);*)
  let cparams =
    if length types > length names then "" else
      implode (tl (rev (tl (tl (rev (explode (fold_left ( ^ ) "" (map2 (fun t n -> t ^ " " ^ n ^ ", ") types names))))))))
  in
  let trim_star s = match explode s with '*'::t -> implode t | _ -> s in
  Printf.sprintf "%s pycpdf_%s(%s) {\n  return cpdf_%s(%s);\n}\n"
    type_name function_name cparams function_name
    (fold_left (fun a b -> if a = "" then b else a ^ ", " ^ b) "" (map trim_star (drop_odds param_types_and_names)))

let rec process a = function
  | [] -> rev (map (fun x -> x ^ "\n") a)
  | h::t ->
      if starts_with "/* __AUTO" h then process (mkauto h::a) t else process (h::a) t

let go infile outfile =
  let indata = lines (contents_of_file infile) in
  let processed = process [] indata in
    contents_to_file outfile (fold_left ( ^ ) "" processed)

let () = go "../libpycpdf.auto.c" "../libpycpdf.c"
