#!/usr/bin/python3
import brownie

def check_run(token):
    should_run = token.isTrading()
    return should_run

def test_enable_trading(token):
    token.canTrade()

    assert token.isTrading() == True

def test_enable_trading_not_owner_revert(token, accounts):
    with brownie.reverts():
        token.canTrade({'from': accounts[1]})

def test_isOwner_internal(token, accounts):
    with brownie.reverts():
        token.pauseTrading({'from': accounts[1]})

def test_sellTax_init(token):
    assert token.sellTax() == 0

def test_buyTax_init(token):
    assert token.buyTax() == 0

def test_set_taxes(token):
    token.setTaxes(1, 1)

    assert token.buyTax() == 1
    assert token.sellTax() == 1

def test_set_taxes_not_owner(token, accounts):
    with brownie.reverts():
        token.setTaxes(1, 1, {'from': accounts[1]})

def test_set_taxes_over_threshold(token):
    with brownie.reverts():
        token.setTaxes(13, 13)

def test_set_taxes_threshold_equal_25(token):
    token.setTaxes(10, 15)
    
    assert token.buyTax() == 10
    assert token.sellTax() == 15

def test_has_paused_init(token):
    hasPaused = token.hasPaused()

    assert hasPaused == False

def test_pauseTrading(token):
    token.pauseTrading()

    assert token.isTrading() == False
    assert token.hasPaused() == True

def test_pauseTrading_not_owner(token, accounts):
    with brownie.reverts():
        token.pauseTrading({'from': accounts[1]})

def test_botVestedAmount_init(token):
    assert token.botVestedAmount() == 0

def test_swapThreshol_init(token):
    assert token.swapThreshold() == 0

def test_set_swapThreshold(token):
    amount = 9
    print(f'Total Supply: {token.totalSupply()}')
    token.setSwapThreshold(amount)

    assert token.swapThreshold() == token.totalSupply() * amount / 1000

def test_tx_limit(token):
    assert token.txLimit() == 200000 * 10 ** token.decimals()

def test_set_devWallet(token, accounts):
    token.setDevWallet(accounts[2])
    
    assert token.devWallet() == accounts[2]

def test_set_router(token):
    uniswap_router = "0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D"
    token.setRouter(uniswap_router)

    assert token.routerAddress() == uniswap_router
