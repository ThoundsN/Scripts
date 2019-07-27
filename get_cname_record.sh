#!/bin/bash
basepath="/root/OneDrive/output"

grepcname(){
      dir=$1
      echo "debug: dir      $1"
      mkdir -p "$basepath/cname/$(basename $dir)"
      latestname=$(ls -t $1/*simple* | head -1 )
      latestfile="$1/$latestname"
      echo "debug:   $latestname "
      echo "debug:    $latestfile"
      newfile="$basepath/cname/cname_$(basename $dir)/"
      newfileparsed="""$basepath/cname/parsed_cname_$(basename $dir)/"
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
    while read p ; do
        echo "debug: $basepath/massdns/$p"
        grepcname "$basepath/massdns/$p"
    done < "$domainlist"
fi
