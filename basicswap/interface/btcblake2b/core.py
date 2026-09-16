# -*- coding: utf-8 -*-
# Copyright (c) 2026 The Basicswap developers
# Distributed under the MIT software license

"""
Blake2b-spezifische Core-Funktionen
Hauptsächlich Header-Parsing (164 bytes statt 80)
"""

import struct
import hashlib


def deserialize_header_v2(header_bytes: bytes) -> dict:
    """
    Parse Blake2b v2 Header (164 bytes) oder Legacy (80 bytes)

    Blake2b Format (post-activation):
    - 4 bytes: version (0xa0000000 für Blake2b)
    - 32 bytes: hashPrevBlock
    - 32 bytes: hashMerkleRoot
    - 4 bytes: nTime
    - 4 bytes: nBits
    - 4 bytes: nNonce
    - 84 bytes: nNonce256 (zusätzliche Nonce-Daten für Blake2b)

    Total: 164 bytes
    """
    if len(header_bytes) == 80:
        # Legacy SHA256 Header (vor Blake2b-Aktivierung)
        return deserialize_header_legacy(header_bytes)

    if len(header_bytes) != 164:
        raise ValueError(
            f"Invalid Blake2b header size: {len(header_bytes)} (expected 164 or 80)"
        )

    offset = 0
    version = struct.unpack("<I", header_bytes[offset : offset + 4])[0]
    offset += 4

    hashPrevBlock = header_bytes[offset : offset + 32][::-1].hex()  # Little-endian
    offset += 32

    hashMerkleRoot = header_bytes[offset : offset + 32][::-1].hex()
    offset += 32

    nTime = struct.unpack("<I", header_bytes[offset : offset + 4])[0]
    offset += 4

    nBits = struct.unpack("<I", header_bytes[offset : offset + 4])[0]
    offset += 4

    nNonce = struct.unpack("<I", header_bytes[offset : offset + 4])[0]
    offset += 4

    nNonce256 = header_bytes[offset : offset + 84].hex()

    return {
        "version": version,
        "hashPrevBlock": hashPrevBlock,
        "hashMerkleRoot": hashMerkleRoot,
        "nTime": nTime,
        "nBits": nBits,
        "nNonce": nNonce,
        "nNonce256": nNonce256,
        "header_type": "blake2b_v2",
    }


def deserialize_header_legacy(header_bytes: bytes) -> dict:
    """Parse legacy 80-byte SHA256 header"""
    if len(header_bytes) != 80:
        raise ValueError(f"Invalid legacy header size: {len(header_bytes)}")

    offset = 0
    version = struct.unpack("<I", header_bytes[offset : offset + 4])[0]
    offset += 4

    hashPrevBlock = header_bytes[offset : offset + 32][::-1].hex()
    offset += 32

    hashMerkleRoot = header_bytes[offset : offset + 32][::-1].hex()
    offset += 32

    nTime = struct.unpack("<I", header_bytes[offset : offset + 4])[0]
    offset += 4

    nBits = struct.unpack("<I", header_bytes[offset : offset + 4])[0]
    offset += 4

    nNonce = struct.unpack("<I", header_bytes[offset : offset + 4])[0]

    return {
        "version": version,
        "hashPrevBlock": hashPrevBlock,
        "hashMerkleRoot": hashMerkleRoot,
        "nTime": nTime,
        "nBits": nBits,
        "nNonce": nNonce,
        "header_type": "sha256_legacy",
    }


def hash_header_blake2b(header_bytes: bytes) -> bytes:
    """
    Hash Blake2b v2 header (double Blake2b) oder Legacy (double SHA256)
    Returns 32-byte hash
    """
    if len(header_bytes) == 164:
        # Blake2b hashing (double Blake2b wie Bitcoin's double SHA256)
        h1 = hashlib.blake2b(header_bytes, digest_size=32).digest()
        h2 = hashlib.blake2b(h1, digest_size=32).digest()
        return h2
    elif len(header_bytes) == 80:
        # Legacy SHA256d
        h1 = hashlib.sha256(header_bytes).digest()
        h2 = hashlib.sha256(h1).digest()
        return h2
    else:
        raise ValueError(f"Invalid header size: {len(header_bytes)}")
