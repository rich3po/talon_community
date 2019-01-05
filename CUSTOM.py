from talon.voice import Word, Context, Key, Rep, Str, press
import logging

ctx = Context('CUSTOM')
ctx.keymap({
    "flip": Key("cmd-tab"),
    "copy": Key("cmd-c"),
    "cut": Key("cmd-x"),
    "paste": Key("cmd-v"),
    "undo": Key("cmd-z"),
    "redo": Key("cmd-shift-z"),
    "copy line": [
        Key("cmd-left"),
        Key("cmd-shift-right"),
        Key("cmd-c"),
    ],
    "my email address": "rich.3po@gmail.com",
    "el bracket": "(",
    "ah bracket": ")",
})
