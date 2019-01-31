from talon.voice import Context, Key, press
from talon import ctrl
import logging

# Note: These keyboard shortcuts won't work unless keyboard shortcuts are turned on.
# See https://support.google.com/mail/answer/6594?hl=en-GB

ctx = Context(
    "google_mail",
    func=lambda app, win: "- Gmail" in win.title or "CarePlanner Mail" in win.title
)
ctx.keymap(
    {
        "inbox": Key("g i"),
        "starred": Key("g s"),
        "open": Key("o"),
        "archive": Key("e"),
        "newer": Key("k"),
        "older": Key("j"),
        "compose": Key("c"),
        "mark unread": Key("shift-u"),
        "end": Key("cmd-right"),
        "start": Key("cmd-left"),
    }
)
