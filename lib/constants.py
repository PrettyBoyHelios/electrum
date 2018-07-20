# -*- coding: utf-8 -*-
#
# Electrum - lightweight Bitcoin client
# Copyright (C) 2018 The Electrum developers
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import json
def read_json(filename, default):
    path = os.path.join(os.path.dirname(__file__), filename)
    try:
        with open(path, 'r') as f:
            r = json.loads(f.read())
    except:
        r = default
    return r


class BitcoinMainnet:

    TESTNET = False
    WIF_PREFIX = 0x80
    ADDRTYPE_P2PKH = 0
    ADDRTYPE_P2SH = 5
    SEGWIT_HRP = "bc"
    GENESIS = "000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f"
    DEFAULT_PORTS = {'t': '50001', 's': '50002'}
    DEFAULT_SERVERS = read_json('servers-btc.json', {})
    CHECKPOINTS = read_json('checkpoints-btc.json', [])

    XPRV_HEADERS = {
        'standard':    0x0488ade4,  # xprv
        'p2wpkh-p2sh': 0x049d7878,  # yprv
        'p2wsh-p2sh':  0x0295b005,  # Yprv
        'p2wpkh':      0x04b2430c,  # zprv
        'p2wsh':       0x02aa7a99,  # Zprv
    }
    XPUB_HEADERS = {
        'standard':    0x0488b21e,  # xpub
        'p2wpkh-p2sh': 0x049d7cb2,  # ypub
        'p2wsh-p2sh':  0x0295b43f,  # Ypub
        'p2wpkh':      0x04b24746,  # zpub
        'p2wsh':       0x02aa7ed3,  # Zpub
    }
    BIP44_COIN_TYPE = 0

class CrypoData:
    def __init__(self):
        self.supported_cryptos = ['btc', 'bch', 'polis', 'dash', 'colx', 'xmcc', 'gbx', 'ltc']



class PolisMainnet:

    TESTNET = False
    WIF_PREFIX = 0x3C
    ADDRTYPE_P2PKH = 0x37
    ADDRTYPE_P2SH = 0x38
    POW_TARGET_SPACING = 2
    POW_DGW3_HEIGHT = 551
    GENESIS = "000009701eb781a8113b1af1d814e2f060f6408a2c990db291bc5108a1345c1e"
    DEFAULT_PORTS = {'s': '50002'}
    DEFAULT_SERVERS = read_json('servers-polis.json', {})
    CHECKPOINTS = read_json('checkpoints-polis.json', [])

    XPRV_HEADERS = {
        'standard':    0x03E25D7E,  # pprv
    }
    XPUB_HEADERS = {
        'standard':    0x03E25945,  # ppub
    }
    BIP44_COIN_TYPE = 0

class LitecoinMainnet:
    TESTNET = False
    WIF_PREFIX = 0x80
    ADDRTYPE_P2PKH = 48
    ADDRTYPE_P2SH = 50
    SEGWIT_HRP = "ltc"
    GENESIS = "12a765e31ffd4059bada1e25190f6e98c99d9714d334efa41a195a7e7e04bfe2"
    DEFAULT_PORTS = {'t': '50001', 's': '50002'}
    DEFAULT_SERVERS = read_json('servers-ltc.json', {})
    CHECKPOINTS = read_json('checkpoints-ltc.json', [])

    XPRV_HEADERS = {
       'standard': 0x0488ade4,  # xprv
       'p2wpkh-p2sh': 0x049d7878,  # yprv
       'p2wsh-p2sh': 0x0295b005,  # Yprv
       'p2wpkh': 0x04b2430c,  # zprv
       'p2wsh': 0x02aa7a99,  # Zprv
    }
    XPUB_HEADERS = {
       'standard': 0x0488b21e,  # xpub
       'p2wpkh-p2sh': 0x049d7cb2,  # ypub
       'p2wsh-p2sh': 0x0295b43f,  # Ypub
       'p2wpkh': 0x04b24746,  # zpub
       'p2wsh': 0x02aa7ed3,  # Zpub
    }
    BIP44_COIN_TYPE = 2



class DashMainnet:

    TESTNET = False
    WIF_PREFIX = 204
    ADDRTYPE_P2PKH = 76
    ADDRTYPE_P2SH = 16
    POW_TARGET_SPACING = 2.5 * 60
    POW_DGW3_HEIGHT = 68589
    GENESIS = "00000ffd590b1485b3caadc19b22e6379c733355108f107a430458cdf3407ab6"
    DEFAULT_PORTS = {'t': '50001', 's': '50002'}
    DEFAULT_SERVERS = read_json('servers-dash.json', {})
    CHECKPOINTS = read_json('checkpoints-dash.json', [])

    XPRV_HEADERS = {
        'standard':    0x02fe52f8,
    }
    XPUB_HEADERS = {
        'standard':    0x02fe52cc,
    }
    BIP44_COIN_TYPE = 0

class BitcoinCashMainnet:

    TESTNET = False
    WIF_PREFIX = 0x80
    ADDRTYPE_P2PKH = 0
    ADDRTYPE_P2PKH_BITPAY = 28
    ADDRTYPE_P2SH = 5
    CASHADDR_PREFIX = "bitcoincash"
    ADDRTYPE_P2SH_BITPAY = 40
    GENESIS = "000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f"
    DEFAULT_PORTS = {'t': '50001', 's': '50002'}
    DEFAULT_SERVERS = read_json('servers-bch.json', {})
    CHECKPOINTS = read_json('checkpoints-bch.json', [])

    XPRV_HEADERS = {
        'standard':    0x0488ade4,
    }
    XPUB_HEADERS = {
        'standard':    0x0488b21e,
    }
    BIP44_COIN_TYPE = 0

net = PolisMainnet

def set_btcmainnet():
    global net
    net = BitcoinMainnet

def set_polismainnet():
    global net
    net = PolisMainnet

def set_bitcoincashmainnet():
    global net
    net = BitcoinCashMainnet

def set_dashmainnet():
    global net
    net = DashMainnet