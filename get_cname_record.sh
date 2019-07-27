#!/bin/bash
basepath="/root/OneDrive/output"

grepcname(){
      echo
      echo
      echo 

      dir=$1
      echo "debug: dir      $1"
      mkdir -p "$basepath/cname/$(basename $dir)"
      latestfile=$(ls -t $1/*simple* | head -1 )
      echo "debug:  latestfile    $latestfile"
      newfile="$basepath/cname/$(basename $dir)/cname_$(basename $latestfile)"
      newfileparsed="$basepath/cname/$(basename $dir)/parsed_cname_$(basename $latestfile)"
      echo "debug: $newfile"
      echo "debug: $newfileparsed"
      touch "$newfile"
      touch "$newfileparsed"
      grep -i cname $latestfile > $newfile
      awk 'BEGIN {OFS='\n'} {print $1,$3}' $newfile  > $newfileparsed
}

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
            exit 1
            ;;
    esac
done
shift $((OPTIND-1))


if [[ $default == 1 ]];
then
     for dir in  $basepath/massdns/* ; do
         if [ -d "$dir" ];then
            echo "debug: $dir"
             grepcname "$dir"
         fi
     done
 else
    sed 's/[[:blank:]]*$//' $domainlist
    while read p ; do
        echo "debug: $basepath/massdns/$p"
        grepcname "$basepath/massdns/$p"
    done < "$domainlist"
fi
