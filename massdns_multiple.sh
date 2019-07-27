#!/bin/bash

usage(){
    echo " usage: -w    path of wordlist; -t    type of output : S - simple, F - full, J - json , -d    domainlist" 1>&2;
    exit 1
}



while getopts  "w:t:d:" option;
do
    case $option in
        w)  wordlist=$OPTARG
            ;;
        d) domainlist=$OPTARG
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

sed 's/[[:blank:]]*$//' $domainlist


while read line ;
do
   echo  "$line"
   massdns_one -w $wordlist -t $type -d $line
done < "$domainlist"
