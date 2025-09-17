# Copyright 2025 - Solely by BrotherBoard
# Bug? Feedback? Telegram >> @BroBordd

"""
Ear v1.0 - Chat listener

For byBordd-server
"""

from babase import Plugin
from bascenev1 import broadcastmessage as push

def ear(t,i):
    if t.startswith('.'):
        push(f'yes {i}',clients=[i])
        return
    return t

# ba_meta require api 9
# ba_meta export babase.Plugin
class byBordd(Plugin):
    def __init__(s):
        __import__('bascenev1')._hooks.filter_chat_message = ear
