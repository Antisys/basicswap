# -*- coding: utf-8 -*-
# Copyright (c) 2026 The Basicswap developers
# Distributed under the MIT software license

# Bitcoin Knots carrying the BLAKE2b proof-of-work change
# (bitcoinknots/bitcoin PR #359, pinned tag v29.4.1.knots20260508rc3).
#
# The fork shares Bitcoin's genesis, address encoding, magic bytes and default
# ports on every network; only the PoW hash changes after the activation height
# (mainnet 961640, testnet4 150027, regtest via -testactivationheight=blake2b@N).
# Address params below are therefore identical to Bitcoin's. Only the default
# rpcport values differ, as a convenience for running a Blake2b node alongside a
# normal Bitcoin node on the same host; the actual port always comes from the
# chainclients entry in basicswap.json.

from basicswap.util import COIN

params = {
    "name": "bitcoin_blake2b",
    "display_name": "Bitcoin Blake2b",
    "ticker": "BTCb2",
    "message_magic": "Bitcoin Signed Message:\n",
    "blocks_target": 60 * 10,
    "decimal_places": 8,
    "has_segwit": True,
    "mainnet": {
        "rpcport": 8432,
        "pubkey_address": 0,
        "script_address": 5,
        "key_prefix": 128,
        "hrp": "bc",
        "bip44": 0,
        "min_amount": 100000,
        "max_amount": 10000000 * COIN,
        "ext_public_key_prefix": 0x0488B21E,
        "ext_secret_key_prefix": 0x0488ADE4,
    },
    "testnet": {
        "rpcport": 18432,
        "pubkey_address": 111,
        "script_address": 196,
        "key_prefix": 239,
        "hrp": "tb",
        "bip44": 1,
        "min_amount": 100000,
        "max_amount": 10000000 * COIN,
        "name": "testnet4",
        "ext_public_key_prefix": 0x043587CF,
        "ext_secret_key_prefix": 0x04358394,
    },
    "regtest": {
        "rpcport": 18543,
        "pubkey_address": 111,
        "script_address": 196,
        "key_prefix": 239,
        "hrp": "bcrt",
        "bip44": 1,
        "min_amount": 100000,
        "max_amount": 10000000 * COIN,
        "ext_public_key_prefix": 0x043587CF,
        "ext_secret_key_prefix": 0x04358394,
    },
}
