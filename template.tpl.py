def header(environ, fmt):
    return """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
<link rel="stylesheet" type="text/css" href="/style.css">
<link href="http://kevinburke.bitbucket.org/markdowncss/markdown.css" rel="stylesheet"></link>
<script type="text/x-mathjax-config">
MathJax.Hub.Config({{tex2jax: {{inlineMath: [['$','$'], ['\\(','\\)']]}}}});
</script>
<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
<title>{title}</title>
</head>
<body>
<div id="wrapper">
<div id="header"><span id="keepit">Keep It</span><span id="simplestupid">Simple, Stupid!</span></div>
<div id="menuwrapper">{menu}</div>
<div id="content">
""".format(**fmt)

def footer(environ, fmt = {}):
    return """
<hr class="footerrule" />
<div id="footerinfo">
This is the website of Jonatan Olofsson.
</div>
</div>
</div>
</body>
</html>
""".format(**fmt)
