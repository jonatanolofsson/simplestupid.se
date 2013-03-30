def header(environ, fmt):
    return """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
<link rel="stylesheet" type="text/css" href="/style.css">
<title>{title}</title>
</head>
<body>
<div id="wrapper">
<div id="header"><span id="keepit">Keep It</span><span id="simplestupid">Simple Stupid</span></div>
<div id="menu">{menu}</div>
<div id="content">
""".format(**fmt)

def footer(environ, fmt = {}):
    return """
</div>
</div>
</body>
</html>
""".format(**fmt)
