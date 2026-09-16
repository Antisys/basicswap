#!/usr/bin/env python3
# test_1_1_chainparams.py

import sys

sys.path.insert(0, "/tmp/opencode/basicswap")

print("=== Test 1.1: Chainparams ===")

# Import testen
try:
    from basicswap.interface.btcblake2b.chainparams import params as blake2b_params

    print("✅ Import erfolgreich")
except ImportError as e:
    print(f"❌ FAIL: {e}")
    sys.exit(1)

# Struktur validieren
required_keys = ["name", "ticker", "message_magic", "blocks_target", "decimal_places"]
for key in required_keys:
    assert key in blake2b_params, f"❌ FAIL: {key} fehlt"
print(f"✅ Top-level keys OK")

# Network-Params validieren
for network in ["mainnet", "testnet", "regtest"]:
    assert network in blake2b_params, f"❌ {network} fehlt"
    net_params = blake2b_params[network]

    required_net_keys = [
        "rpcport",
        "pubkey_address",
        "script_address",
        "hrp",
        "min_amount",
        "max_amount",
    ]
    for key in required_net_keys:
        assert key in net_params, f"❌ {network}.{key} fehlt"

    print(f"✅ {network} params OK (rpcport={net_params['rpcport']})")

# Regtest-spezifisch
assert blake2b_params["regtest"]["rpcport"] == 18543, "❌ Falscher regtest RPC-Port"
assert blake2b_params["ticker"] == "BTCb2", "❌ Falscher Ticker"

print("✅ PASS: Chainparams korrekt")
