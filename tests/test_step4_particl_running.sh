#!/bin/bash
# test_step4_particl_running.sh

PARTICL_CLI=~/bswap_data/bin/particl/particl-27.2.4.0_nousb/bin/particl-cli

# Check RPC
if $PARTICL_CLI -datadir=~/bswap_data/particl getblockchaininfo 2>/dev/null | grep -q "chain"; then
    echo "✅ Particl RPC OK"
else
    echo "❌ RPC failed"
    exit 1
fi

echo "✅ PASS: Particl running"
