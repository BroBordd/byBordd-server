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
    chatmessage as say
)
from bubble import Bubble

def ear(m,i):
    p = i2p(i)
    if m.startswith('.'):
        return
    Bubble(
        node=p.actor.node,
        text=m,
        time=max(3,min(6,len(m)/60)),
        color=p.actor.node.color
    )
    return m

def i2p(i):
    a = ga()
    for j,p in enumerate(a.players):
        if p.sessionplayer.inputdevice.client_id == i:
            return a.players[j]

# ba_meta require api 9
# ba_meta export babase.Plugin
class byBordd(Plugin): pass
