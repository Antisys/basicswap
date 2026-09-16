#!/usr/bin/env python3
# test_step2_config.py

import json

with open("/home/ralf/bswap_data/basicswap.json") as f:
    cfg = json.load(f)

required = ["network_key", "zmqhost", "zmqport", "chainclients"]
for key in required:
    assert key in cfg, f"❌ Missing: {key}"
    print(f"✅ {key}")

assert "particl" in cfg["chainclients"], "❌ No particl"
print("✅ PASS: Config complete")
