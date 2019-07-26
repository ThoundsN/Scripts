function massdns_one 
	set help " usage: path of wordlist; type of output : S - simple, F - full, other - json, one or list of domains splited by space"

	if begin test "$argv[1]" = "-h"; or test "$argv[1]"= "--help";  end
		echo $help	
		return 
	end
	set time  (date +'%Y-%m-%d-%H-%M')
	set textname $time'_massdns' 
	if test "$argv[2]" = "S"
		set textname $textname'_simple.txt'
	else if test "$argv[2]" = "F"
		set textname $textname'_full.txt'
	else 
		set textname $textname'_json.txt'
	end

	if test (count $argv) -le 3
		mkdir -p  ~/output/massdns/$argv[3]/
		touch ~/output/massdns/$argv[3]/$textname
		subbrute.py $argv[1] $argv[3] | massdns -r ~/recon_tools/massdns/lists/resolvers.txt -t A -o $argv[2] --outfile  ~/output/massdns/$argv[3]/$textname
	else 
		echo $help 
	end
end
