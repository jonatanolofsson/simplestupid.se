def header(environ, fmt):
    return """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
<link rel="stylesheet" type="text/css" href="/style.css">
<title>{title}</title>
</head>
<body>
<div class="header"><span class="keepit">Keep It</span><span class="simplestupid">Simple Stupid</span></div>
<div class="menu">{menu}</div>
<div class="body">
""".format(**fmt)

def footer(environ, fmt = {}):
    return """
</div>
</body>
</html>
""".format(**fmt)
