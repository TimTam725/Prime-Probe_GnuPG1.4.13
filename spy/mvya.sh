#!/bin/sh

# scp tamura@172.20.24.61:~/gnu18/data/scan-gpg18_set22_4000.tar.gz yuki@172.20.24.40:~/gnu18/data
scp yamaarashi:~/gnu18/data/scan-gpg18_set26_4000.tar ~/elgamal/gnu13/data
# $wait
scp ../data/scan-gpg18_set26_4000.tar alice:~/gnu13/data
echo "send scan"
