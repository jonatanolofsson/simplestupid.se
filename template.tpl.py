def header(environ, fmt):
    return """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
<title>{title}</title>
</head>
<body>
""".format(**fmt)

def footer(environ, fmt = {}):
    return """
</body>
</html>
""".format(**fmt)
