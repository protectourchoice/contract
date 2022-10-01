#!/usr/bin/python3

import pytest
from brownie import Contract
import time

@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    # perform a chain rewind after completing each test, to ensure proper isolation
    # https://eth-brownie.readthedocs.io/en/v1.10.3/tests-pytest-intro.html#isolation-fixtures
    pass


@pytest.fixture(scope="module")
def token(Token, accounts):
    return Token.deploy("Test Token", "TST", 6, 10e6, {'from': accounts[0]})

@pytest.fixture(scope="module")
def uniswap_router():
    yield Contract.from_explorer("0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D")

# @pytest.fixture(scope="module")
# def addLiquidity(token, accounts):
#     uniswap_router.addLiquidityETH(
#         token.address,
#         "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
#         token.totalSupply() / 2,
#         1,
#         0,
#         0,
#         accounts[0],
#         (int(time.time()) + 100000),
#         {
#             'from': accounts[0],
#             'gas': 500000,
#         }
#     )
