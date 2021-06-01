#!/bin/sh

DR="python3 mk_folder.py"
MKnp1="python3 mknp.py"
MKnp2="python3 mknp_under.py"
DLAY1="python3 mkdelay.py"
CUT="python3 cut_np10.py"


echo "#### START ####"
${DR}
${MKnp1}
${MKnp2}
${DLAY1}
${CUT}
echo "#### finish ALL ####"
