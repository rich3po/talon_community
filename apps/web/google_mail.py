from talon.voice import Context, Key, press
from talon import ctrl
import logging

ctx = Context(
    "google_mail",
    func=lambda app, win: "- Gmail" in win.title or "- Edo Mail" in win.title
)
ctx.keymap(
    {
        "inbox": Key("g i"),
        "starred": Key("g s"),
        "open": Key("o"),
        "archive": Key("e"),
        "newer": Key("k"),
        "older": Key("j"),
    }
)
