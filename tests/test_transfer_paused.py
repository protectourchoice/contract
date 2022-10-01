#!/usr/bin/python3
import brownie
import pytest

def test_paused_transfer_revert(token, accounts):
    sender_balance = token.balanceOf(accounts[0])
    amount = sender_balance // 4
    
    with brownie.reverts():
        token.transfer(accounts[1], amount, {'from': accounts[0]})

def test_is_paused_revert(token):
    assert token.isTrading() == False