function massdns_multiple
	set help " usage: path of wordlist; type of output : S - simple, F - full, other - json, domainfile"

        if begin test "$argv[1]" = "-h"; or test "$argv[1]"= "--help";  end
                echo $help
                return
        end

	echo $argv
	set wordlist $argv[1]
	set type $argv[2]
	set domainfile $argv[3]

	for line in (cat $domainfile)
		echo $line
		massdns_one $wordlist $type $line
	end
end
