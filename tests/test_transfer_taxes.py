#!/usr/bin/python3
import brownie
import pytest


@pytest.fixture(scope='module', autouse=True)
def can_trade(token):
    return token.canTrade()

def test_transfer_tax(token, accounts):
    token.setTaxes(1, 1)
    sender_balance = token.balanceOf(accounts[0])
    amount_send = sender_balance * 2 / 100
    taxed_amount_end = amount_send * ((100 - token.buyTax()) / 100)
    token.transfer(accounts[1], amount_send, {'from': accounts[0]})
    
    assert token.balanceOf(token) == amount_send - taxed_amount_end
    assert token.balanceOf(accounts[1]) == taxed_amount_end