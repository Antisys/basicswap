#!/usr/bin/env python3
# step2_create_config.py

import json

NETKEY = open("/home/ralf/bswap_data/network_key.txt").read().strip()

config = {
    "debug": True,
    "chain": "mainnet",
    "network_key": NETKEY,
    "network_pubkey": "",
    "use_tor": False,
    "tor_proxy": "127.0.0.1:9050",
    "check_progress_seconds": 60,
    "check_watched_seconds": 60,
    "check_expired_seconds": 60,
    "check_events_seconds": 10,
    "check_xmr_swaps_seconds": 20,
    "min_delay_event": 10,
    "max_delay_event": 60,
    "min_delay_event_short": 2,
    "max_delay_event_short": 30,
    "html_host": "127.0.0.1",
    "html_port": 12700,
    "allow_cors": False,
    "zmqhost": "tcp://127.0.0.1",
    "zmqport": 20792,
    "smsgaddrindex": True,
    "chainclients": {
        "particl": {
            "connection_type": "rpc",
            "manage_daemon": True,
            "rpcport": 51735,
            "datadir": "/home/ralf/bswap_data/particl",
            "bindir": "/home/ralf/bswap_data/bin/particl/particl-27.2.4.0_nousb/bin",
            "blocks_confirmed": 1,
            "conf_target": 2,
            "anon_tx_ring_size": 12,
        }
    },
}

with open("/home/ralf/bswap_data/basicswap.json", "w") as f:
    json.dump(config, f, indent=2)

print("✅ Config created")
