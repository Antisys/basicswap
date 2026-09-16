#!/bin/bash
# run_all_tests.sh — BasicSwap BTCblake2b Full Test Suite

echo "=== BasicSwap BTCblake2b — Full Test Suite ==="
echo

PYTHON="/tmp/opencode/bswap_venv/bin/python3"
FAILED=0
PASSED=0
SKIPPED=0

run_test() {
    local test_file=$1
    local test_name=$(basename $test_file .py .sh)
    
    echo "▶ Running: $test_name"
    
    if [[ $test_file == *.sh ]]; then
        bash $test_file
    else
        $PYTHON $test_file
    fi
    
    if [ $? -eq 0 ]; then
        PASSED=$((PASSED + 1))
        echo "✅ PASS: $test_name"
    else
        FAILED=$((FAILED + 1))
        echo "❌ FAIL: $test_name"
    fi
    echo
}

# Phase 0
echo "=== Phase 0: Setup ==="
run_test tests/test_0_1_setup.sh
# test_0_2 überspringen (Node reindext)

# Phase 1
echo "=== Phase 1: Coin-Integration ==="
run_test tests/test_1_1_chainparams.py
run_test tests/test_1_2_coin_enum.py
run_test tests/test_1_3_core.py

# Phase 2
echo "=== Phase 2: Interface ==="
run_test tests/test_2_1_interface_basic.py

# Phase 3
echo "=== Phase 3: HTLC-Scripts ==="
run_test tests/test_3_htlc_scripts.py

# Phase 4
echo "=== Phase 4: Security ==="
run_test tests/test_4_security_coin_loss.py

# Summary
echo "=== TEST SUMMARY ==="
echo "✅ PASSED: $PASSED"
echo "❌ FAILED: $FAILED"
echo "⏸️  SKIPPED: 1 (Blake2b Node reindexing)"
echo

if [ $FAILED -eq 0 ]; then
    echo "🎉 ALL TESTS PASSED"
    echo
    echo "Next Steps:"
    echo "1. Wait for Blake2b node to finish reindexing"
    echo "2. Run: python3 tests/test_0_2_blake2b_node.py"
    echo "3. Integration-Test mit echter Node"
    exit 0
else
    echo "❌ SOME TESTS FAILED"
    exit 1
fi
