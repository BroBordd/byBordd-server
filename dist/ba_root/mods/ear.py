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

def ear(m,i):
    if m.startswith('.'):
        p = i2p(i)
        push(f'{p}',clients=[i])
        return
    return m

def i2p(i):
    a = ga()
    k = None
    for j,p in a.players:
        if j.sessionplayer.inputdevice.client_id == i:
            k = j
    return k if k is None else a.players[k]

# ba_meta require api 9
# ba_meta export babase.Plugin
class byBordd(Plugin): pass
