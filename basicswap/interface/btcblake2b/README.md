# BasicSwap Bitcoin Blake2b Module

✅ **Status:** Ready for Regtest Testing  
⚠️ **Testnet4:** Needs Peers  
❌ **Mainnet:** Blocked (RC-Build)

---

## Features

- ✅ HTLC Atomic Swaps (BTC ↔ BTCblake2b)
- ✅ SegWit Support
- ✅ Blake2b v2 Header-Parsing (164 bytes)
- ✅ Legacy SHA256 Header-Support (80 bytes)
- ✅ Full RPC-Kompatibilität
- ✅ Coin-Loss-Protection (Refund-Paths)

---

## Installation

### 1. Blake2b-Node Setup

**Option A: Deine bestehende Node (192.168.1.125)**
```bash
# Warte bis Reindex fertig
# Dann RPC-Credentials in BasicSwap-Config eintragen
```

**Option B: Lokale Regtest-Node**
```bash
# Bitcoin Knots Blake2b herunterladen
git clone https://github.com/paulscode/knots-blake2b-startos.git

# Regtest-Config
mkdir -p ~/.bitcoin_blake2b
cat > ~/.bitcoin_blake2b/bitcoin.conf <<EOF
regtest=1
server=1
rpcuser=test
rpcpassword=test
rpcport=18543
blake2b_headline=TestHeadline
testactivationheight=blake2b@1
EOF

# Start
bitcoind -datadir=~/.bitcoin_blake2b
```

### 2. BasicSwap-Integration

```bash
# BasicSwap mit Dependencies
cd /tmp/opencode/basicswap
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Tests ausführen
./run_all_tests.sh
```

**Manuelle BasicSwap-Config** (für echte Nutzung):
```json
{
  "chains": {
    "btcblake2b": {
      "connection_type": "rpc",
      "rpchost": "192.168.1.125",
      "rpcport": 8332,
      "rpcuser": "your_user",
      "rpcpassword": "your_password",
      "use_segwit": true,
      "blocks_confirmed": 20,
      "conf_target": 2
    }
  }
}
```

---

## Tests

Alle Tests in `/tests/`:

```bash
# Einzelne Tests
python3 tests/test_1_1_chainparams.py
python3 tests/test_1_2_coin_enum.py
python3 tests/test_1_3_core.py
python3 tests/test_2_1_interface_basic.py
python3 tests/test_3_htlc_scripts.py
python3 tests/test_4_security_coin_loss.py

# Alle Tests
bash run_all_tests.sh
```

**Test-Status:**
- ✅ Chainparams
- ✅ Coin-Enum
- ✅ Core (Header-Parsing)
- ✅ Interface
- ✅ HTLC-Scripts
- ✅ Security (Coin-Loss)

---

## Sicherheit

### Confirmations

| Network | Empfohlen | Warum |
|---------|-----------|-------|
| Regtest | 1-6 | Kontrollierte Umgebung |
| Testnet4 | 20+ | Niedriges Hash-Power → Reorg-Risiko |
| Mainnet | N/A | Gesperrt (RC-Build) |

### Lock-Times

**Standard-Werte:**
- **Initiate-TX:** 48 Stunden (172.800 Sekunden)
- **Participate-TX:** 24 Stunden (86.400 Sekunden)
- **Puffer:** 24h zwischen PTX-Refund und ITX-Redeem

**Konfigurierbar** bei Offer-Erstellung.

### Risiko-Mitigation

| Risiko | Wahrscheinlichkeit | Schutz |
|--------|-------------------|--------|
| Software-Bug | Niedrig | Code-Reviews + Tests |
| Timing-Attack | Sehr niedrig | Lange Lock-Times (48h+) |
| Testnet-Reorg | Mittel | 20+ Confirmations |
| Wrong Secret | Unmöglich | Hash-Verifikation in Script |
| Timeout | Kein Risiko | Refund-Path vorhanden |

---

## Technische Details

### Header-Format

**Legacy (vor Blake2b-Aktivierung):**
- 80 bytes
- SHA256d Hashing

**Blake2b v2 (nach Aktivierung):**
- 164 bytes
- Version: `0xa0000000`
- Zusätzlich: 84-byte `nNonce256` Feld
- Double-Blake2b Hashing

**Auto-Detection:** Modul erkennt automatisch Format (80 vs 164 bytes).

### HTLC-Scripts

**Wichtig:** HTLC-Scripts sind **identisch** zu BTC!
- Secret-Hash nutzt **SHA256** (nicht Blake2b)
- Blake2b = nur PoW-Algo, nicht Script-Hash
- 100% kompatibel ohne Code-Änderung

**Script-Struktur:**
```
OP_IF
  <secret_hash> OP_SHA256 OP_EQUALVERIFY  # Redeem-Path
  <pkh_redeem> OP_CHECKSIG
OP_ELSE
  <lock_value> OP_CHECKSEQUENCEVERIFY     # Refund-Path
  <pkh_refund> OP_CHECKSIG
OP_ENDIF
```

---

## Bekannte Einschränkungen

1. **Mainnet gesperrt** (Bitcoin Knots RC-Build)
2. **Testnet4-Peers fehlen** (Manual Peer-Setup nötig)
3. **Reorg-Risiko auf Testnet** (wenig Hash-Power)

---

## Nächste Schritte

### Für Entwickler:
1. ✅ Unit-Tests vollständig
2. ⏳ Integration-Test mit echter Node (warte auf Reindex)
3. ⏳ Testnet4-Swap (needs Peers)

### Für Produktion:
1. Warte auf stabilen Mainnet-Release
2. Setup Mining-Pool (Hash-Power sichern)
3. Monitoring-Scripts deployen

---

## Support

- **Code:** `/tmp/opencode/basicswap/basicswap/interface/btcblake2b/`
- **Tests:** `/tmp/opencode/basicswap/tests/test_*`
- **Upstream:** [paulscode/knots-blake2b-startos](https://github.com/paulscode/knots-blake2b-startos)
- **BasicSwap:** [basicswap/basicswap](https://github.com/basicswap/basicswap)

---

## Lizenz

MIT (wie BasicSwap)
