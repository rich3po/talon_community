from talon.voice import Word, Context, Key, Rep, RepPhrase, Str, press


ctx = Context("phpstorm", bundle="com.jetbrains.PhpStorm")

ctx.keymap(
    {
        "go line": Key("cmd-l"),
        "search all": Key("shift shift"),
        "(next tab | goneck)": Key("cmd-shift-]"),
        "((last | previous | preev) tab | gopreev)": Key("cmd-shift-["),

        # PHP
        "block": [" {", Key("enter")],
        "function block": [Key("enter"), "{", Key("enter")],
        "static": "static ",
        "protected": "protected ",
        "public": "public ",
        "private": "private ",
        "abstract": "abstract ",
        "function": "function ",
        "if": ["if () {", Key("enter"), Key("up")],
        "equals": " = ",
        "plus equals": " += ",
        # "var": (True, lambda i, word, _: word if i == 0 else word.capitalize()),
    }
)