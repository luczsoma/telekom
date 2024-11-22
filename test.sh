target=$1
sudo /usr/local/bin/mtr --report-cycles 10 --show-ips --aslookup --report --csv $target >> $target.csv
