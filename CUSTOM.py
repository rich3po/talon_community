from talon.voice import Word, Context, Key, Rep, Str, press
import logging

ctx = Context('CUSTOM')
ctx.keymap({
    "flip": Key("cmd-tab"),
    "switch window": Key("cmd-`"),
    "switch tab": Key("ctrl-tab"),
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
    "personal email": "rich.3po@gmail.com",
    "work email": "rich@care-planner.co.uk",
    "lock screen": Key("cmd-ctrl-q"),
    "el bracket": "(",
    "ah bracket": ")",
    "php": "php",
    "symphony": "symfony ",
    "dock sal": "docksal ",
    "heya": "Hey",
})
