target=$1
mtr=/usr/local/bin/mtr
sudo $mtr --report-cycles 10 --show-ips --aslookup --report --csv $target >> $target.csv
