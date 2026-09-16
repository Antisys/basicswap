#!/usr/bin/env python3
# test_2_1_interface_basic.py

import sys
import logging

sys.path.insert(0, "/tmp/opencode/basicswap")

from basicswap.interface.btcblake2b.btcblake2b import BTCBlake2bInterface
from basicswap.chainparams import Coins

logging.basicConfig(level=logging.WARNING)  # Less noise

print("=== Test 2.1: Interface Basis ===")

# Mock coin_settings
coin_settings = {
    "connection_type": "rpc",
    "manage_daemon": False,
    "rpchost": "127.0.0.1",
    "rpcport": 18543,
    "rpcuser": "test",
    "rpcpassword": "test",
    "rpcauth": "test:test",
    "use_segwit": True,
    "blocks_confirmed": 6,
    "conf_target": 2,
    "fee_priority": 0,
}

# Init Interface
try:
    ci = BTCBlake2bInterface(coin_settings, "regtest")
    print("✅ Interface erstellt")
except Exception as e:
    print(f"❌ FAIL: {e}")
    import traceback

    traceback.print_exc()
    sys.exit(1)

# Check: Methoden existieren
assert hasattr(ci, "coin_type"), "❌ coin_type fehlt"
assert hasattr(ci, "coin_name"), "❌ coin_name fehlt"
assert hasattr(ci, "ticker"), "❌ ticker fehlt"
assert hasattr(ci, "testDaemonRPC"), "❌ testDaemonRPC fehlt"
print("✅ Alle Interface-Methoden vorhanden")

# Check: Coin-Typ
assert ci.coin_type() == Coins.BTCBLAKE2B, f"❌ Coin-Type falsch: {ci.coin_type()}"
print(f"✅ Coin-Type: {ci.coin_type()}")

# Check: Namen
assert ci.coin_name() == "Bitcoin Blake2b", f"❌ Name falsch: {ci.coin_name()}"
assert ci.ticker() == "BTCb2", f"❌ Ticker falsch: {ci.ticker()}"
print(f"✅ Name: {ci.coin_name()}, Ticker: {ci.ticker()}")

print("✅ PASS: Interface-Basis OK")
