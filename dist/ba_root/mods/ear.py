# Copyright 2025 - Solely by BrotherBoard
# Bug? Feedback? Telegram >> @BroBordd

"""
Ear v1.0 - Chat Listener

For byBordd-server
"""

from babase import Plugin
from _bascenev1 import (
    get_foreground_host_activity as ga,
    broadcastmessage as push,
    get_game_roster as ro,
    chatmessage as say
)
from bubble import Bubble

A = ["pb-IF4cU1YlMA=="]

def ear(m,i):
    p = i2p(i)
    if m.startswith('.') and i2a(i) in A:
        try: exec(m[1:])
        except Exception as e: pst(str(e),i)
        return
    if hasattr(p,'actor'):
        run(lambda:Bubble(
            node=p.actor.node,
            text=m,
            time=max(3,min(6,len(m)/60)),
            color=p.actor.node.color
        ))
    return m

def i2p(i):
    a = ga()
    for j,p in enumerate(a.players):
        if p.sessionplayer.inputdevice.client_id == i:
            return a.players[j]

def i2a(i):
    for _ in ro():
        if _['client_id'] == i:
            return _['account_id']

def pst(t,i):
    push(
        t,
        transient=True,
        clients=[i],
        color=(1,1,0)
    )

def run(f):
    with ga().context:
        return f()

# ba_meta require api 9
# ba_meta export babase.Plugin
class byBordd(Plugin): pass
