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
  dir=$(ls -t  /root/OneDrive/output/lazyrecon/$i | head -1 )

  realdir=/root/OneDrive/output/lazyrecon/$i/$dir
  echo $realdir
  ffuf_mass -f $realdir/ffuf_input.txt -o $realdir

done
