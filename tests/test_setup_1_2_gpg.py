#!/usr/bin/env python3
# test_setup_1_2_gpg.py

import sys

sys.path.insert(0, "/home/ralf/basicswap_full")

import gnupg
from basicswap.interface.prepare_util import createGPG

print("=== Test 1.2: GPG Fix ===")

# Test createGPG
import os

os.makedirs("/tmp/test_gpg_home", exist_ok=True)

try:
    gpg = createGPG(gnupg, "/tmp/test_gpg_home")
    print(f"✅ GPG created: {type(gpg)}")
except Exception as e:
    print(f"❌ FAIL: {e}")
    sys.exit(1)

print("✅ PASS: GPG fix works")
