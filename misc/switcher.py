from talon.voice import Word, Context, Key, Rep, Str, press
from talon import ui
import time
import os
import logging

running = {}
launch = {}

def switch_app(m, name=None):
    if name is None:
        name = str(m['switcher.running'][0])

    full = running.get(name)
    if not full: return
    for app in ui.apps():
        if app.name == full:
            app.focus()
            # TODO: replace sleep with a check to see when it is in foreground
            time.sleep(0.25)
            break

def switch_to_canary():
    for app in ui.apps():
        if app.bundle == 'com.google.Chrome.canary':
            app.focus()
            # TODO: replace sleep with a check to see when it is in foreground
            time.sleep(0.25)
            break

def launch_app(m, name=None):
    if name is None:
        name = str(m['switcher.running'][0])
        
    path = launch.get(name)
    if path:
        ui.launch(path=path)

ctx = Context('switcher')
ctx.keymap({
    'oh {switcher.running}': switch_app,
    'launch {switcher.launch}': launch_app,
    # custom switchers here
    # "madam": lambda x: switch_app(x, "Atom"),
    # "focus outlook": lambda x: switch_app(x, "Outlook"),
    # "focus slack": lambda x: switch_app(x, "Slack"),
    # "focus skype": lambda x: switch_app(x, "Skype for Business"),
    # "focus signal": lambda x: switch_app(x, "Signal"),
    # my custom
    "oh chrome": lambda x: switch_app(x, "Google Chrome"),
    "oh canary": lambda x: switch_to_canary(),
    "oh storm": lambda x: switch_app(x, "PhpStorm"),
    "launch storm": lambda x: launch_app(x, "PhpStorm"),
    "oh shell": lambda x: switch_app(x, "iTerm2"),
    "oh sublime": lambda x: switch_app(x, "Sublime Text"),
    "oh sequel": lambda x: switch_app(x, "Sequel Pro"),
    "oh prefs": lambda x: switch_app(x, "System Preferences"),
    "oh cal": lambda x: switch_app(x, "Calendar"),
    "oh notes": lambda x: switch_app(x, "Evernote"),
    "oh duck": lambda x: switch_app(x, "Cyberduck"),
})

def update_lists():
    global running
    global launch
    new = {}
    for app in ui.apps():
        if app.background and not app.windows():
            continue
        words = app.name.split(' ')
        for word in words:
            if word and not word in new:
                new[word] = app.name
        new[app.name] = app.name
    running = new
    ctx.set_list('running', running.keys())

    new = {}
    for base in '/Applications', '/Applications/Utilities':
        for name in os.listdir(base):
            path = os.path.join(base, name)
            name = name.rsplit('.', 1)[0]
            new[name] = path
            words = name.split(' ')
            for word in words:
                if word and word not in new:
                    if len(name) > 6 and len(word) < 3:
                        continue
                    new[word] = path
    launch = new
    ctx.set_list('launch', launch.keys())

def ui_event(event, arg):
    if event in ('app_activate', 'app_launch', 'app_close', 'win_open', 'win_close'):
        update_lists()

ui.register('', ui_event)
update_lists()
