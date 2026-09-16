#!/bin/bash
# test_step3_particl_conf.sh

grep -q "zmqpubhashblock" ~/bswap_data/particl/particl.conf && echo "✅ ZMQ configured" || exit 1
grep -q "deprecatedrpc=create_bdb" ~/bswap_data/particl/particl.conf && echo "✅ BDB enabled" || exit 1
echo "✅ PASS: Particl config OK"
