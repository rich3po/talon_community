from talon.voice import Word, Context, Key, Rep, RepPhrase, Str, press


ctx = Context("sequel_pro", bundle="com.sequelpro.SequelPro")

ctx.keymap(
    {
        "reload": Key("cmd-r"),
        "new tab": Key("cmd-t"),
        "close tab": Key("cmd-w"),
    }
)