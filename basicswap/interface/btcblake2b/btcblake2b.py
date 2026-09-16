# -*- coding: utf-8 -*-
# Copyright (c) 2026 The Basicswap developers
# Distributed under the MIT software license

"""
BTCBlake2b Interface — Atomic Swap Support für Bitcoin Blake2b
Basiert auf BTC-Interface mit Blake2b-Header-Support
"""

import logging
from typing import Optional

from basicswap.interface.btc.btc import BTCInterface
from basicswap.chainparams import Coins
from .core import deserialize_header_v2, hash_header_blake2b


class BTCBlake2bInterface(BTCInterface):
    """
    Bitcoin Blake2b Interface

    Erbt von BTCInterface (meiste Funktionen identisch)
    Überschreibt nur Header-spezifische Methoden
    """

    @staticmethod
    def coin_type():
        return Coins.BTCBLAKE2B

    def __init__(self, coin_settings, network, swap_client=None):
        super().__init__(coin_settings, network, swap_client)
        self._log = logging.getLogger(f"BTCBlake2b-{network}")
        self._log.info("BTCBlake2b Interface initialized")

    def coin_name(self) -> str:
        return "Bitcoin Blake2b"

    def ticker(self) -> str:
        return "BTCb2"

    def testDaemonRPC(self, with_wallet: bool = True) -> None:
        """
        Test RPC-Verbindung zur Blake2b-Node

        Erweitert Parent-Methode um Blake2b-spezifische Checks
        """
        self._log.info("Testing Blake2b RPC connection...")

        # Basis-RPC-Test
        super().testDaemonRPC(with_wallet)

        # Blake2b-spezifischer Check (best effort, nicht fatal)
        try:
            deployment_info = self.rpc("getdeploymentinfo")
            deployments = deployment_info.get("deployments", {})
            if "blake2b" in deployments:
                b = deployments["blake2b"]
                self._log.info(f"Blake2b deployment: {b}")
            else:
                self._log.debug(
                    "Kein 'blake2b' deployment im getdeploymentinfo (Stand-in-Node?)"
                )
        except Exception as e:
            self._log.debug(f"Blake2b deployment check übersprungen: {e}")

        self._log.info("Blake2b RPC OK")
