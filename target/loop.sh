#!/bin/sh

FILE="t.txt"
# echo "------------------------------"
# echo "target:" $TARGETEXE
# ${TARGETEXE}
while [ -e $FILE ]
do
  /usr/local/gnupg-1.4.13/bin/gpg -o file_dec -r yukitam ../target/file
  rm file_dec
done

wait $!
# touch t.txt
echo "loop.sh end"
