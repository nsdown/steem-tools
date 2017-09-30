#!/usr/bin/python
# -*- coding: utf-8 -*-

from steem import Steem
from steem.account import Account
from config import Key
from log import Log

user = Key['user_name']
account = Account(user)
logger = Log()

wif = {
    "posting": Key['posting_key']
}

try:
    steem = Steem(keys=wif)

    sbd = account.balances["rewards"]["SBD"]
    st = account.balances["rewards"]["STEEM"]
    vests = account.balances["rewards"]["VESTS"]

    if sbd > 0 or st > 0 or vests > 0:
        logger.info('Claiming rewards ... ')
        steem.claim_reward_balance(account=user)
    else:
        logger.info('Nothing to claim')
except:
    logger.warning('Oops, something not right.')
