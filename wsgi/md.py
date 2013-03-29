#-*- coding: utf-8 -*-
import os, markdown2, imp
siteroot = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
htdocs = os.path.join(siteroot, 'htdocs')
tplname = 'template.tpl.py'

def wsgi_app(environ, start_response):
    output = ""
    mdfile = os.path.join(htdocs, environ['REDIRECT_URL'].lstrip('/'))
    tpldir = os.path.dirname(mdfile)
    while not os.path.exists(os.path.join(tpldir, tplname)) and not (os.path.realpath(tpldir) == os.path.realpath(siteroot)):
        tpldir = os.path.dirname(tpldir)
    
    tpl = os.path.join(tpldir, tplname)
    template = {}
    if os.path.exists(tpl):
        template = imp.load_source('template', tpl)

    if "header" in dir(template):
        output += template.header(environ, {'title': mdfile})
       
    with open(mdfile) as f:
        output +=  markdown2.markdown(f.read())

    if "footer" in dir(template):
        output += template.footer(environ)

    # send first header and status
    status = '200 OK'
    headers = [('Content-type', 'text/html'),
		('Content-Length', str(len(output)))]
    start_response(status, headers)

    # wsgi apps should return and iterable, the following is acceptable too :
    # return [output]
    yield output

# mod_wsgi need the *application* variable to serve our small app
application = wsgi_app
