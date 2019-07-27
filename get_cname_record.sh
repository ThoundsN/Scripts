#!/bin/bash
basepath="~/OneDrive/output"


usage(){
    echo 'usage: -d default mode - grep all cname records in the latest simple text file of all subdirecotrys in output,
    -w specify list of domain to grep  '
}

while getopts ":w:d" o;
do
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
shift $((OPTIND-1))


if [[ $default == 1 ]];
then
     for dir in  "$basepath/massdns/*" ; do
         if [-d "$dir"];then
            echo "debug: $dir"
             grepcname "$dir"
         fi
     done
 else
    while read p ; do
        echo "debug: $basepath/massdns/$p"
        grepcname "$basepath/massdns/$p"
    done < "$domainlist"
fi



gerpcname(){
      dir=$1
      originalfilepath="$basepath/massdns/$dir"
      echo "$originalfilepath"
      mkdir -p "$basepath/cname/$dir"
      latestname=$(ls -t $originalfilepath/*simple* | head -1 )
      latestfile="$originalfilepath/$latestname"
      newfile="$bashpath/cname/$dir/cname_$latestname"
      newfileparsed="$bashpath/cname/$dir/parsed_cname_$latestname"
      echo "debug: $newfile"
      echo "debug: $newfileparsed"
      touch "$newfile"
      touch "$newfileparsed"
      grep -i cname $latestfile > $newfile
      awk 'BEGIN {OFS='\n'} {print $1,$3}' $newfile  > $newfileparsed
}
