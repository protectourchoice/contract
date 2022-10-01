#!/usr/bin/python3
import brownie

def check_run(token):
    should_run = token.isTrading()
    return should_run

