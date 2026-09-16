#!/bin/bash
# test_setup_1_1_venv.sh

source ~/basicswap_full/.venv/bin/activate

# Check: Python version
python3 --version | grep "3.1" || exit 1
echo "✅ Python OK"

# Check: Key packages
python3 -c "import coincurve; import gnupg; import sqlalchemy" || exit 1
echo "✅ Dependencies OK"

echo "✅ PASS: venv ready"
