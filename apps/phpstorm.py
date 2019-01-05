from talon.voice import Word, Context, Key, Rep, RepPhrase, Str, press


ctx = Context("phpstorm", bundle="com.jetbrains.PhpStorm")

ctx.keymap(
    {
        "block": [" {", Key("enter")],
        "go line": Key("cmd-l"),
        "static": "static ",
        "protected": "protected ",
        "public": "public ",
        "private": "private ",
        "abstract": "abstract ",
        "equals": " = ",
        "plus equals": " += ",
        # "var": (True, lambda i, word, _: word if i == 0 else word.capitalize()),

    }
)