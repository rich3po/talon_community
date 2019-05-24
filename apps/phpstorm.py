from talon.voice import Word, Context, Key, Rep, RepPhrase, Str, press


ctx = Context("phpstorm", bundle="com.jetbrains.PhpStorm")

ctx.keymap(
    {
        # shortcuts
        "go line": Key("cmd-l"),
        "drill": Key("cmd-b"),
        "disable": Key("cmd-/"),
        "debug": Key("ctrl-l"),
        "reformat code": Key("cmd-alt-l"),
        "explore": [Key("shift"), Key("shift")],
        "(next tab | goneck)": Key("cmd-shift-]"),
        "((last | previous | preev) tab | gopreev)": Key("cmd-shift-["),
        "clone": Key("cmd-d"),
        "grab": Key("alt-up"),
        "rename": Key("shift-f6"),

        # PHP
        "block": [" {", Key("enter")],
        "function block": [Key("enter"), "{", Key("enter")],
        "static": "static ",
        "protected": "protected ",
        "public": "public ",
        "private": "private ",
        "abstract": "abstract ",
        "extends": "extends ",
        "implements": "implements ",
        "function": "function ",
        "create if": ["if () {", Key("enter"), Key("up"), Key("right"), Key("right")],
        "create for each": ["foreach () {", Key("enter"), Key("up"), Key("right"), Key("right"), Key("right"), Key("right"), Key("right")],
        #"equals": " = ",
        "rocket": " => ",
        "identical": " == ",
        "not identical": " !== ",
        "plus equals": " += ",  
        "bracket": "[",  
        "return": "return ",
        "null": "null",
        "onset": "unset",
        # "this": "this",
        # "var": (True, lambda i, word, _: word if i == 0 else word.capitalize()),
    }
)