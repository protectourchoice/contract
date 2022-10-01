#!/usr/bin/python3
import brownie
import pytest


@pytest.fixture(scope='module', autouse=True)
def can_trade(token):
    return token.canTrade()

@pytest.fixture(scope='module', autouse=True)
def set_taxes(token):
    return token.setTaxes(1, 1)

def test_to_balance_decreases_tax(accounts, token):
    sender_balance = token.balanceOf(accounts[0])
    amount_send = sender_balance * 2 / 100
    taxed_amount_end = amount_send * ((100 - token.sellTax()) / 100)
    token.approve(accounts[1], amount_send, {'from': accounts[0]})
    token.transferFrom(accounts[0], accounts[2], amount_send, {'from': accounts[1]})
    print(f'Sender Balance: {sender_balance / (10 ** token.decimals())}')
    print(f'Send Amount: {amount_send / (10 ** token.decimals())}')
    print(f'Balance account 0: {token.balanceOf(accounts[0]) / (10 ** token.decimals())}')
    print(f'Balance account 2: {token.balanceOf(accounts[2]) / (10 ** token.decimals())}')
    print(f'Contract Balance: {token.balanceOf(token) / (10 ** token.decimals())}')

    assert token.balanceOf(token) == amount_send - taxed_amount_end
    assert token.balanceOf(accounts[0]) == sender_balance - amount_send