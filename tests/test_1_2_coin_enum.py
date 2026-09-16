#!/usr/bin/env python3
# test_1_2_coin_enum.py

import sys

sys.path.insert(0, "/tmp/opencode/basicswap")

from basicswap.chainparams import Coins, chainparams

print("=== Test 1.2: Coin-Enum ===")

# Check: Enum existiert
assert hasattr(Coins, "BTCBLAKE2B"), "❌ BTCBLAKE2B Enum fehlt"
assert Coins.BTCBLAKE2B == 19, f"❌ Falsche Coin-ID: {Coins.BTCBLAKE2B}"
print(f"✅ Coins.BTCBLAKE2B = {Coins.BTCBLAKE2B}")

# Check: Chainparams registriert
assert Coins.BTCBLAKE2B in chainparams, "❌ Chainparams nicht registriert"
params = chainparams[Coins.BTCBLAKE2B]
assert params["ticker"] == "BTCb2", f"❌ Falscher Ticker: {params['ticker']}"
print(f"✅ Chainparams registriert: {params['name']}")

# Check: Name-Map
from basicswap.chainparams import name_map, ticker_map

assert "bitcoin_blake2b" in name_map, "❌ Name-Map fehlt"
assert name_map["bitcoin_blake2b"] == Coins.BTCBLAKE2B, "❌ Name-Map falsch"
assert "btcb2" in ticker_map, "❌ Ticker-Map fehlt"
assert ticker_map["btcb2"] == Coins.BTCBLAKE2B, "❌ Ticker-Map falsch"
print(f"✅ Name-Map & Ticker-Map OK")

print("✅ PASS: Coin-Enum korrekt registriert")
