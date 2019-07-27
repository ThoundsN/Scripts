#!/bin/bash
rootpath="/root/OneDrive/output"
usage(){
    echo " usage: -d  specify target direcotries  -s target file containing specific string for httprobe to check  " 1>&2;
    exit 1
}

while getopts ":d:s:" o;
do
    case "${o}" in
        w)
            direcotry=${OPTARG}
            ;;
        s)
            keyword=${OPTARG}
            ;;
        *)
            usage
            exit 1
            ;;
    esac
done
shift $((OPTIND-1))

httprobe_dir(){
    echo
    echo

    $dir=$1
    echo "debug: dir      $1"
    mkdir -p "$rootpath/httprobe/$(basename $dir)"
    fileinput=$(ls -t $dir/*$keyword* | head -1 )
    echo "debug:  fileinput    $fileinput"
    newfile="$rootpath/httprobe/$(basename $dir)/httprobe_$(basename $fileinput)"
    echo "debug:  newfile    $newfile"
    touch $newfile
    cat $fileinput| httprobe -c 50 > $newfile

}



for dir in $rootpath/$direcotry/* ; do
  if [ -d "$dir" ];then
     echo "debug: $dir"
      httprobe_dir  "$dir"
fi
done
