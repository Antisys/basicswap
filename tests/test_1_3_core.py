#!/usr/bin/env python3
# test_1_3_core.py

import sys

sys.path.insert(0, "/tmp/opencode/basicswap")

from basicswap.interface.btcblake2b.core import (
    deserialize_header_v2,
    deserialize_header_legacy,
    hash_header_blake2b,
)

print("=== Test 1.3: Core (Header-Parsing) ===")

# Test 1: Legacy Header (80 bytes)
legacy_header = bytes.fromhex(
    "01000000"  # version
    + "00" * 32  # prev block
    + "00" * 32  # merkle root
    + "00000000"  # time
    + "ffff001d"  # bits
    + "12345678"  # nonce
)
assert len(legacy_header) == 80, "❌ Test-Header falsch"

parsed_legacy = deserialize_header_legacy(legacy_header)
assert parsed_legacy["version"] == 1, f"❌ Version falsch: {parsed_legacy['version']}"
assert parsed_legacy["header_type"] == "sha256_legacy", "❌ Header-Type falsch"
assert parsed_legacy["nNonce"] == 0x78563412, (
    f"❌ Nonce falsch: {hex(parsed_legacy['nNonce'])}"
)
print("✅ Legacy Header-Parsing OK")

# Test 2: Blake2b v2 Header (164 bytes)
v2_header = bytes.fromhex(
    "000000a0"  # version (0xa0000000)
    + "00" * 32  # prev block
    + "00" * 32  # merkle root
    + "00000000"  # time
    + "ffff001d"  # bits
    + "12345678"  # nonce
    + "ab" * 84  # nNonce256
)
assert len(v2_header) == 164, f"❌ V2-Header falsch: {len(v2_header)}"

parsed_v2 = deserialize_header_v2(v2_header)
assert parsed_v2["version"] == 0xA0000000, (
    f"❌ V2 Version falsch: {hex(parsed_v2['version'])}"
)
assert parsed_v2["header_type"] == "blake2b_v2", "❌ V2 Header-Type falsch"
assert len(parsed_v2["nNonce256"]) == 168, (
    f"❌ nNonce256 falsch: {len(parsed_v2['nNonce256'])}"
)  # 84 bytes = 168 hex chars
print("✅ Blake2b v2 Header-Parsing OK")

# Test 3: Auto-Detect (deserialize_header_v2 sollte beide können)
auto_legacy = deserialize_header_v2(legacy_header)
assert auto_legacy["header_type"] == "sha256_legacy", "❌ Auto-Detect legacy failed"
print("✅ Auto-Detect Legacy OK")

auto_v2 = deserialize_header_v2(v2_header)
assert auto_v2["header_type"] == "blake2b_v2", "❌ Auto-Detect v2 failed"
print("✅ Auto-Detect Blake2b OK")

# Test 4: Hashing
hash_legacy = hash_header_blake2b(legacy_header)
assert len(hash_legacy) == 32, f"❌ Hash-Länge falsch: {len(hash_legacy)}"
print(f"✅ Legacy Hash: {hash_legacy.hex()[:16]}...")

hash_v2 = hash_header_blake2b(v2_header)
assert len(hash_v2) == 32, f"❌ V2 Hash-Länge falsch: {len(hash_v2)}"
print(f"✅ Blake2b Hash: {hash_v2.hex()[:16]}...")

# Test 5: Invalid sizes
try:
    deserialize_header_v2(b"x" * 100)
    print("❌ FAIL: Invalid size nicht abgefangen")
    sys.exit(1)
except ValueError:
    print("✅ Invalid size korrekt rejected")

print("✅ PASS: Core-Modul funktioniert")
