import pytest
from brownie import Contract
import brownie
import time

@pytest.fixture(scope="session")
def dai():
    yield Contract.from_explorer("0x6B175474E89094C44Da98b954EedeAC495271d0F")

@pytest.fixture(scope="session")
def uniswap_router():
    yield Contract.from_explorer("0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D")

@pytest.fixture(scope="module", autouse=True)
def buy_dai(accounts, dai, uniswap_router):
    uniswap_router.swapExactETHForTokens(
        0,
        ["0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2","0x6B175474E89094C44Da98b954EedeAC495271d0F"],
        accounts[0],
        (int(time.time()) + 100000),
        {
            'from': accounts[0],
            'value': 1,
            'gas': 500000,
        }
    )

def test_buy_dai(accounts, dai):
    assert dai.balanceOf(accounts[0]) > 0

def test_add_liquidity(token, accounts, uniswap_router):
    token.canTrade()
    token.approve("0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D", token.totalSupply() / 2)

    uniswap_router.addLiquidityETH(
        token.address,
        token.totalSupply() / 2,
        token.totalSupply() / 2,
        0,
        accounts[0],
        (int(time.time()) + 100000),
        {
            'from': accounts[0],
            "value": 1
        }
    )

def test_add_liq_contract_function(token, accounts):
    token.canTrade()
    token.setRouter("0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D")

    token.addLiquidity({"value": 1*10**18, "from": accounts[0]})

def test_add_liq_contract_not_owner_revert(token, accounts):
    token.canTrade()
    token.setRouter("0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D")
    with brownie.reverts():
        token.addLiquidity({"value": 1*10**18, "from": accounts[1]})
