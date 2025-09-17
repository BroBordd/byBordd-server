# Copyright 2025 - Solely by BrotherBoard
# Bug? Feedback? Telegram >> @BroBordd

"""
Custom Hooks v1.0 - From the game

For byBordd-server
"""

from babase import Plugin
from bascenev1 import (
    broadcastmessage as push,
    chatmessage as say
)

def filter_chat_message(m,i):
    push(m)
    say(f"lmfao {i} is funny")
    return m

# ba_meta require api 9
# ba_meta export babase.Plugin
class byBordd(Plugin): pass
