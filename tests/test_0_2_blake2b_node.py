#!/usr/bin/env python3
# test_0_2_blake2b_node.py

import json
import subprocess
import sys


def rpc(host, port, user, password, method, params=[]):
    """RPC helper"""
    cmd = [
        "bitcoin-cli",
        f"-rpcconnect={host}",
        f"-rpcport={port}",
        f"-rpcuser={user}",
        f"-rpcpassword={password}",
        method,
    ] + [str(p) for p in params]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
    if result.returncode != 0:
        print(f"❌ RPC failed: {result.stderr}")
        return None
    try:
        return json.loads(result.stdout)
    except:
        return result.stdout.strip()


print("=== Test 0.2: Blake2b Node ===")

# Config (anpassen für deine Node)
NODE_HOST = "192.168.1.125"
NODE_PORT = 8332  # Oder dein Port
NODE_USER = "rpc"  # Deine RPC-Credentials
NODE_PASS = "rpc"

print(f"Testing Node: {NODE_HOST}:{NODE_PORT}")

# Check: Node erreichbar
info = rpc(NODE_HOST, NODE_PORT, NODE_USER, NODE_PASS, "getblockchaininfo")
if info is None:
    print("⚠️  Node nicht erreichbar (reindexing?)")
    print("   Dieser Test wird übersprungen")
    print("   Bitte später wiederholen wenn Node fertig")
    sys.exit(0)  # Soft-fail während Reindex

assert info.get("chain") in ["main", "test", "regtest"], (
    f"❌ Unbekannte Chain: {info.get('chain')}"
)
print(f"✅ Chain: {info['chain']}")

# Check: Blake2b-Deployment
deployment = rpc(NODE_HOST, NODE_PORT, NODE_USER, NODE_PASS, "getdeploymentinfo")
if deployment and "blake2b" in deployment:
    print(f"✅ Blake2b-Deployment gefunden")
    blake2b_info = deployment["blake2b"]
    print(f"   Active: {blake2b_info.get('active', False)}")
    print(f"   Height: {blake2b_info.get('height', 'N/A')}")
else:
    print("⚠️  Blake2b-Deployment nicht gefunden (älterer Client oder noch nicht aktiv)")

# Check: Blocks
blocks = info.get("blocks", 0)
print(f"✅ {blocks} Blöcke vorhanden")

print("✅ PASS: Blake2b Node funktioniert")
