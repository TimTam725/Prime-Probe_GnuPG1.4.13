#!/bin/sh

SPYSCRIPT="./L3-scan"
TARGETEXE="../target/loop.sh"
DPATH="../data/"
# FILE="./only_pow.csv"

set="52"
F1="scan-gpg13_set${set}_4000.csv"
F2="consol_scan-gpg13_set${set}_4000.csv"

FILE="t.txt"

taskset -c 0 ${SPYSCRIPT} "${DPATH}/${F1}" ${set} >> ${F2}&
pid1=$!

# sleep 1.5
taskset -c 1 ${TARGETEXE}&


wait ${pid1}
rm ${FILE}
wait $!
echo "spy.sh end"
