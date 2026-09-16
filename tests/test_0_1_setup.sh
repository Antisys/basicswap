#!/bin/bash
# test_0_1_setup.sh

echo "=== Test 0.1: Setup-Validierung ==="

# Check: BasicSwap-Code vorhanden
if [ ! -f "basicswap/chainparams.py" ]; then
    echo "❌ FAIL: BasicSwap nicht korrekt geklont"
    exit 1
fi
echo "✅ BasicSwap-Code vorhanden"

# Check: Python-Env
python3 -c "import coincurve; print('✅ coincurve OK')" || exit 1

# Check: Test-Dirs
for dir in btc blake2b; do
    if [ ! -d ~/test_nodes/$dir ]; then
        echo "❌ FAIL: ~/test_nodes/$dir fehlt"
        exit 1
    fi
done
echo "✅ Test-Verzeichnisse vorhanden"

echo "✅ PASS: Setup komplett"
