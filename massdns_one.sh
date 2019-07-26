#!/bin/bash

usage(){
    echo "usage: -w path of wordlist;-t  type of output : S - simple, F - full, other - json, -d domain " 1>&2;
    exit 1
}

type=S

while getopts  "w:m:d:" option ;
do
    case $option in
        w)  wordlist=$OPTARG
            ;;
        d) domain=$OPTARG
            ;;
        m) type=$OPTARG
            ;;
        *) usage
            ;;
    esac
done
shift $((OPTIND-1))

if [[ ! $type =~ ^(S|F|J)$  ]]; then
    usage
fi


time=$(date +'%Y-%m-%d-%H-%M')
textname="$time_massdns"

if [[ $type = "S"]]; then
    textname="$textname_simple.txt"
elif [[ $type = "F"  ]]; then
    textname="$textname_full.txt"
else
    textname="$textname_json.txt"
fi


mkdir -p ~/OneDrive/output/massdns/$domain/
touch  ~/OneDrive/output/massdns/$domain/$textname
subbrute.py $wordlist $domain |massdns -r ~/recon_tools/massdns/lists/resolvers.txt -t A -o $type --outfile  ~/OneDrive/output/massdns/$domain/$textname
