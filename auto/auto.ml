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

let rec process a = function
  | [] -> rev (map (fun x -> x ^ "\n") a)
  | h::t ->
      if starts_with "/* __AUTO" h then
        begin
          Printf.printf "found auto\n";
          process a t
        end
      else
        process (h::a) t

let go infile outfile =
  let indata = lines (contents_of_file infile) in
  let processed = process [] indata in
    contents_to_file outfile (fold_left ( ^ ) "" processed)

let () = go "../libpycpdf.auto.c" "../libpycpdf.c"
