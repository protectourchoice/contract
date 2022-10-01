import pytest
from brownie import Contract, Wei
import brownie
import time

@pytest.fixture(scope="session")
def uniswap_router():
    yield Contract.from_explorer("0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D")

@pytest.fixture(scope="module", autouse=True)
def add_liq_contract_function(token, accounts):
    token.canTrade()
    token.setRouter("0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D")

    token.addLiquidity({"value": "5 ether", "from": accounts[0]})

def test_swap_for_choice_from_eth(token, accounts, uniswap_router):
    token.canTrade()
    token.setTaxes(1, 5)
    
    uniswap_router.swapExactETHForTokens(
        0,
        ["0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",token.address],
        accounts[1],
        (int(time.time()) + 100000),
        {
            'from': accounts[1],
            'value': Wei(".5 ether"),
            'gas': 500000,
        }
    )
    print(token.balanceOf(token))


def test_swap_to_tax_swap(token, accounts, uniswap_router):
    token.canTrade()
    token.setTaxes(10, 1)
    token.setSwapThreshold(1)
    token.setDevWallet(accounts[5])
    print(token.devWallet())
    with brownie.reverts():
        print(accounts[5].balance())
        uniswap_router.swapExactETHForTokens(
            0,
            ["0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",token.address],
            accounts[1],
            (int(time.time()) + 100000),
            {
                'from': accounts[1],
                'value': Wei("1 ether"),
                'gas': 500000,
            }
        )
        print(token.balanceOf(token))
        token.manualSwapBack()
        print(token.balanceOf(token))
        print(accounts[5].balance())