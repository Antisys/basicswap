#!/bin/bash
# test_step1_template.sh
[ -f ~/bswap_data/network_key.txt ] && echo "✅ Network key exists" || exit 1
echo "✅ PASS: Step 1 ready (using manual config)"
