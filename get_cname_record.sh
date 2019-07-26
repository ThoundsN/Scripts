#!/bin/bash

usage(){
    echo 'usage: default mode - grep all cname records in the latest simple text file of all subdirecotrys in output,
    -w specify list of domain to grep  '
}

while getopts "wd:" o; do
    case "${o}" in 
        w)
            domainlist=${OPTARG}
            ;;
        d)
            default=1
            ;;
        *)
            usage
            ;;
        
    esac
done

if [$default -eq 1 ]
then
     for dir in  /root/output/massdns/*; do
         if [-d "$dir"];then 
             grepcname "$dir"
         fi
     done
 else
    while read p ; do
        grepcname "$p"
    done < "$domainlist"
fi



gerpcname(){
    
}
