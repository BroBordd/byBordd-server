# Copyright 2025 - Solely by BrotherBoard
# Bug? Feedback? Telegram >> @BroBordd

"""
Ear v1.0 - Chat Listener

For byBordd-server
"""

from babase import Plugin
from bascenev1 import (
    screenmessage as push,
    chatmessage as say
)

def ear(m,i):
    push(m)
    say(f"lmfao {i} is funny")
    return m

# ba_meta require api 9
# ba_meta export babase.Plugin
class byBordd(Plugin): pass
