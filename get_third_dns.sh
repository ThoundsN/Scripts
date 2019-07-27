#!/bin/bash
cnamerootpath="~/OneDrive/output/cname"

parse_dns_dir(){
  echo

  dir=$1
  parsedfile=$(ls -t $1/parsed* | head -1 )
  echo "debug:  parsed_file    $parsedfile"

}


for dir in $cnamerootpath/*; do
  if [ -d "$dir" ];then
     echo "debug: dir  $dir"
     parse_dns_dir $dir
  fi
done
