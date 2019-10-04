#!/usr/bin/env bash

declare -a domains=("news.yahoo.com"
"stock.yahoo.com "
"builtbygirls.com"
"buildseries.com"
"makers.com"
"finance.yahoo.com"
"gemini.yahoo.com"
"huffpost.net"
"huffpost.kr"
"huffpost.com"
"yahoo.com")

for i in "${domains[@]}"
do
  cd /root/OneDrive/output/lazyrecon/$i
  dir=$(ls -t  | head -1 )
  cd $dir
  realdir=$(realpath $dir)
  if [ ! -f ffuf_output.txt ]; then
    echo "File not found!"
    ffuf_mass -f $realdir/ffuf_input.txt -o $realdir
  fi
done
