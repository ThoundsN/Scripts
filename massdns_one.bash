#!/bin/bash

usage(){
    echo "usage: path of wordlist; type of output : S - simple, F - full, other - json, one or list of domains splited by space" 1>&2;
    exit 1
}

mode=S

while getopts  "w:f:d:" option
do 
    case $option in 
        w)  wordlist=$OPTARG
            ;;
        d) domain=$OPTARG
            ;;
        f)mode=$OPTARG
            ;;
        *) usage
            ;;
    esac
done
shift $((OPTIND-1))





time=$(date +'%Y-%m-%d-%H-%M')
textname="$time_massdns"

if [[ $mode == "S"]]; then
    textname="$textname_simple.txt"
elif [[ $mode == "F"  ]]; then
    textname="$textname_full.txt"
else
    textname="$textname_json.txt"

fi


mkdir -p ~/OneDrive/output/massdns/$domain/
touch ~/OneDrive/output/massdns/$domain/$textname
subbrute.py $wordlist $domain | massdns -r 
