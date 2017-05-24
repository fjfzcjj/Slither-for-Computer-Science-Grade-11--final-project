import sys, functools

nl = "\n"

def StreamOut(stream, *s, **kw):
    k = kw.setdefault
    # Process keyword arguments
    sep     = k("sep", "")
    auto_nl = k("auto_nl", True)
    prefix  = k("prefix", "")
    convert = k("convert", str)
    # Convert position arguments to strings
    strings = map(convert, s)
    # Dump them to the stream
    stream.write(prefix + sep.join(strings))
    # Add a newline if desired
    if auto_nl:
        stream.write(nl)

out  = functools.partial(StreamOut, sys.stdout)
outs = functools.partial(StreamOut, sys.stdout, sep=" ")
dbg  = functools.partial(StreamOut, sys.stdout, sep=" ", prefix="+ ")
err  = functools.partial(StreamOut, sys.stderr)

out("Hi there", "how are you?")
outs("Hi there", "how are you?")